"""Staff-facing serialization for landing content records."""

from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.db.models import Max
from rest_framework import serializers

from landing_copy.models import LandingCopyRevision, LandingPage, Site
from landing_copy.validation import validate_copy


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ("id", "key", "name")
        read_only_fields = ("id",)


class LandingPageSerializer(serializers.ModelSerializer):
    site = serializers.SlugRelatedField(slug_field="key", queryset=Site.objects.all())

    class Meta:
        model = LandingPage
        fields = (
            "id",
            "site",
            "slug",
            "locale",
            "published_revision",
            "published_at",
            "published_by",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "published_revision",
            "published_at",
            "published_by",
            "created_at",
            "updated_at",
        )

    def validate(self, attrs):
        publication_fields = {
            "published_revision",
            "published_at",
            "published_by",
        } & self.initial_data.keys()
        if publication_fields:
            raise serializers.ValidationError(
                {field: "Use the confirmed publication endpoint." for field in publication_fields}
            )
        return attrs


class LandingCopyRevisionSerializer(serializers.ModelSerializer):
    page = serializers.PrimaryKeyRelatedField(queryset=LandingPage.objects.all())

    class Meta:
        model = LandingCopyRevision
        fields = (
            "id",
            "page",
            "version",
            "schema_version",
            "copy",
            "change_summary",
            "created_by",
            "created_at",
        )
        read_only_fields = ("id", "version", "schema_version", "created_by", "created_at")

    def validate_copy(self, value: object) -> object:
        try:
            validate_copy(value)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages) from exc
        return value

    def create(self, validated_data: dict) -> LandingCopyRevision:
        page = validated_data["page"]
        with transaction.atomic():
            page = LandingPage.objects.select_for_update().get(pk=page.pk)
            latest = page.revisions.aggregate(max_version=Max("version"))["max_version"]
            revision = LandingCopyRevision(
                page=page,
                version=(latest or 0) + 1,
                schema_version=1,
                copy=validated_data["copy"],
                change_summary=validated_data["change_summary"],
                created_by=self.context["request"].user,
            )
            try:
                revision.save()
            except DjangoValidationError as exc:
                raise serializers.ValidationError(exc.messages) from exc
        return revision


class RevisionReplacementSerializer(serializers.Serializer):
    """Input for a new immutable version derived from an existing revision."""

    copy = serializers.JSONField()
    change_summary = serializers.CharField(max_length=240)
