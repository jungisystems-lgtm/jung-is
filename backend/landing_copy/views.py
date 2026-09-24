"""Public, read-only access to published landing text."""

import logging
import re

from django.db import transaction
from django.db.models import F
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from landing_copy.models import LandingCopyRevision, LandingPage

KEY_PATTERN = re.compile(r"[a-z0-9][a-z0-9-]*\Z")
LOCALE_PATTERN = re.compile(r"[a-z]{2}-[A-Z]{2}\Z")
logger = logging.getLogger(__name__)


class PublishedLandingCopyView(APIView):
    """Return one complete published revision for an exact locale."""

    authentication_classes = []
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    http_method_names = ["get", "head", "options"]

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if response.status_code != 200:
            response["Cache-Control"] = "no-store"
        return response

    def get(self, request, site_key: str, page_slug: str) -> Response:
        if (
            len(site_key) > 64
            or len(page_slug) > 80
            or not KEY_PATTERN.fullmatch(site_key)
            or not KEY_PATTERN.fullmatch(page_slug)
        ):
            raise ValidationError({"detail": "Invalid site key or page slug."})

        locales = request.query_params.getlist("locale")
        if len(locales) != 1 or not LOCALE_PATTERN.fullmatch(locales[0]):
            raise ValidationError({"locale": "Specify one locale such as es-CO or en-US."})

        locale = locales[0]
        revision = (
            LandingCopyRevision.objects.select_related("page", "page__site")
            .filter(
                page__site__key=site_key,
                page__slug=page_slug,
                page__locale=locale,
                page__published_at__isnull=False,
                id=F("page__published_revision_id"),
            )
            .first()
        )
        if revision is None:
            raise NotFound("Published page not found.")

        response = Response(
            {
                "schema_version": revision.schema_version,
                "site_key": revision.page.site.key,
                "page_slug": revision.page.slug,
                "locale": revision.page.locale,
                "revision": revision.version,
                "published_at": revision.page.published_at,
                "copy": revision.copy,
            }
        )
        response["Cache-Control"] = "public, max-age=60"
        return response


class PublishRevisionSerializer(serializers.Serializer):
    version = serializers.IntegerField(min_value=1, max_value=2_147_483_647)
    confirm_publish = serializers.BooleanField(required=True)

    def validate_confirm_publish(self, value: bool) -> bool:
        if not value:
            raise serializers.ValidationError("Confirm that a human reviewed this revision.")
        return value


class LandingCopyEditorView(GenericAPIView):
    """Review localized drafts and publish an approved revision."""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = PublishRevisionSerializer
    http_method_names = ["get", "post", "head", "options"]

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response["Cache-Control"] = "private, no-store"
        return response

    def _get_page(self, request, site_key: str, page_slug: str) -> LandingPage:
        if (
            len(site_key) > 64
            or len(page_slug) > 80
            or not KEY_PATTERN.fullmatch(site_key)
            or not KEY_PATTERN.fullmatch(page_slug)
        ):
            raise ValidationError({"detail": "Invalid site key or page slug."})
        locales = request.query_params.getlist("locale")
        if len(locales) != 1 or not LOCALE_PATTERN.fullmatch(locales[0]):
            raise ValidationError({"locale": "Specify one locale such as es-CO or en-US."})
        page = LandingPage.objects.filter(
            site__key=site_key, slug=page_slug, locale=locales[0]
        ).first()
        if page is None:
            raise NotFound("Page not found.")
        return page

    def get(self, request, site_key: str, page_slug: str) -> Response:
        page = self._get_page(request, site_key, page_slug)
        return Response(
            {
                "site_key": site_key,
                "page_slug": page_slug,
                "locale": page.locale,
                "published_revision": (
                    page.published_revision.version if page.published_revision_id else None
                ),
                "revisions": [
                    {
                        "version": revision.version,
                        "schema_version": revision.schema_version,
                        "change_summary": revision.change_summary,
                        "created_at": revision.created_at,
                        "copy": revision.copy,
                    }
                    for revision in page.revisions.order_by("version")
                ],
            }
        )

    def post(self, request, site_key: str, page_slug: str) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            page = self._get_page(request, site_key, page_slug)
            page = LandingPage.objects.select_for_update().get(pk=page.pk)
            revision = page.revisions.filter(version=serializer.validated_data["version"]).first()
            if revision is None:
                logger.warning(
                    "landing_copy_publication_rejected",
                    extra={
                        "site_key": site_key,
                        "page_slug": page_slug,
                        "locale": page.locale,
                        "revision": serializer.validated_data["version"],
                        "user_id": request.user.pk,
                    },
                )
                raise NotFound("Revision not found for this page.")
            changed = page.published_revision_id != revision.pk
            if changed:
                page.published_revision = revision
                page.published_at = timezone.now()
                page.published_by = request.user
                page.save(
                    update_fields=[
                        "published_revision",
                        "published_at",
                        "published_by",
                        "updated_at",
                    ]
                )
        if changed:
            logger.info(
                "landing_copy_published",
                extra={
                    "site_key": site_key,
                    "page_slug": page_slug,
                    "locale": page.locale,
                    "revision": revision.version,
                    "user_id": request.user.pk,
                },
            )
        return Response(
            {
                "site_key": site_key,
                "page_slug": page_slug,
                "locale": page.locale,
                "published_revision": revision.version,
                "published_at": page.published_at,
            }
        )
