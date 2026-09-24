"""Staff-only REST resources for public content and immutable copy revisions."""

import logging
from copy import deepcopy

from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

from landing_copy.models import LandingCopyRevision, LandingPage, Site
from landing_copy.serializers import (
    LandingCopyRevisionSerializer,
    LandingPageSerializer,
    RevisionReplacementSerializer,
    SiteSerializer,
)

logger = logging.getLogger(__name__)


class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "This content has dependent records."
    default_code = "conflict"


class StaffContentViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAdminUser,)
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response["Cache-Control"] = "private, no-store"
        return response


class SiteViewSet(StaffContentViewSet):
    queryset = Site.objects.all().order_by("key")
    serializer_class = SiteSerializer

    def perform_update(self, serializer):
        instance = serializer.instance
        new_key = serializer.validated_data.get("key", instance.key)
        if new_key != instance.key and instance.pages.exists():
            raise Conflict("A site with pages cannot change its key.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.pages.exists():
            raise Conflict("A site with pages cannot be deleted.")
        instance.delete()


class LandingPageViewSet(StaffContentViewSet):
    queryset = LandingPage.objects.select_related("site", "published_revision").order_by(
        "site__key", "slug", "locale"
    )
    serializer_class = LandingPageSerializer

    def perform_update(self, serializer):
        instance = serializer.instance
        identity = ("site", "slug", "locale")
        if instance.revisions.exists() and any(
            serializer.validated_data.get(field, getattr(instance, field))
            != getattr(instance, field)
            for field in identity
        ):
            raise Conflict("A page with revisions cannot change its identity.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.revisions.exists():
            raise Conflict("A page with revisions cannot be deleted.")
        instance.delete()


class LandingCopyRevisionViewSet(StaffContentViewSet):
    queryset = LandingCopyRevision.objects.select_related(
        "page", "page__site", "created_by"
    ).order_by("page__site__key", "page__slug", "page__locale", "version")
    serializer_class = LandingCopyRevisionSerializer
    http_method_names = ("get", "post", "put", "patch", "head", "options")

    def get_serializer_class(self):
        if self.action in {"update", "partial_update"}:
            return RevisionReplacementSerializer
        return super().get_serializer_class()

    def update(self, request, *args, **kwargs):
        source = self.get_object()
        replacement = self.get_serializer(data=request.data)
        replacement.is_valid(raise_exception=True)
        copy = replacement.validated_data["copy"]
        if request.method == "PATCH":
            copy = self._merge_copy(source.copy, copy)
        creation = LandingCopyRevisionSerializer(
            data={
                "page": str(source.page_id),
                "copy": copy,
                "change_summary": replacement.validated_data["change_summary"],
            },
            context={"request": request},
        )
        creation.is_valid(raise_exception=True)
        revision = creation.save()
        self._log_created(revision)
        location = reverse("editor-revision-detail", kwargs={"pk": revision.pk}, request=request)
        return Response(
            LandingCopyRevisionSerializer(revision).data,
            status=status.HTTP_201_CREATED,
            headers={"Location": location},
        )

    @staticmethod
    def _merge_copy(original, changes):
        if not isinstance(original, dict) or not isinstance(changes, dict):
            return changes
        merged = deepcopy(original)
        for key, value in changes.items():
            merged[key] = LandingCopyRevisionViewSet._merge_copy(merged.get(key), value)
        return merged

    def perform_create(self, serializer):
        revision = serializer.save()
        self._log_created(revision)

    def _log_created(self, revision):
        logger.info(
            "landing_copy_revision_created",
            extra={
                "site_key": revision.page.site.key,
                "page_slug": revision.page.slug,
                "locale": revision.page.locale,
                "version": revision.version,
                "user_id": self.request.user.pk,
            },
        )
