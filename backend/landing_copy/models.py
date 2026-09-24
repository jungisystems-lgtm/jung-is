"""Landing copy models and publication metadata."""

import uuid

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from landing_copy.validation import validate_copy

key_validator = RegexValidator(
    regex=r"^[a-z0-9][a-z0-9-]*$",
    message="Use lowercase letters, digits, and hyphens.",
)
locale_validator = RegexValidator(
    regex=r"^[a-z]{2}-[A-Z]{2}$",
    message="Use a locale such as es-CO or en-US.",
)


class Site(models.Model):
    """A public content namespace, not a tenant security boundary."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=64, unique=True, validators=[key_validator])
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.key


class LandingPage(models.Model):
    """One page in one locale, with a pointer to its public revision."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="pages")
    slug = models.CharField(max_length=80, validators=[key_validator])
    locale = models.CharField(max_length=5, validators=[locale_validator])
    published_revision = models.ForeignKey(
        "LandingCopyRevision",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    published_at = models.DateTimeField(null=True, blank=True)
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="published_landing_pages",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["site", "slug", "locale"],
                name="unique_landing_page_locale",
            )
        ]

    def clean(self) -> None:
        super().clean()
        if self.published_revision_id:
            revision_page_id = (
                LandingCopyRevision.objects.filter(pk=self.published_revision_id)
                .values_list("page_id", flat=True)
                .first()
            )
            if revision_page_id != self.pk:
                raise ValidationError(
                    {"published_revision": "The published revision must belong to this page."}
                )
        if self.published_revision_id is None and (
            self.published_at is not None or self.published_by_id is not None
        ):
            raise ValidationError(
                {"published_revision": "Publication metadata requires a published revision."}
            )
        if self.published_revision_id is not None and self.published_at is None:
            raise ValidationError(
                {"published_at": "A published revision requires a publication timestamp."}
            )

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.site.key}/{self.slug} ({self.locale})"


class LandingCopyRevision(models.Model):
    """A complete, immutable text snapshot for one localized page."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(LandingPage, on_delete=models.CASCADE, related_name="revisions")
    version = models.PositiveIntegerField()
    schema_version = models.PositiveSmallIntegerField(default=1)
    copy = models.JSONField()
    change_summary = models.CharField(max_length=240)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_landing_revisions",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["page", "version"],
                name="unique_landing_copy_version",
            ),
            models.CheckConstraint(
                condition=models.Q(version__gte=1),
                name="landing_copy_version_positive",
            ),
        ]

    def clean(self) -> None:
        super().clean()
        if self.schema_version != 1:
            raise ValidationError({"schema_version": "Unsupported copy schema version."})
        validate_copy(self.copy)

    def save(self, *args, **kwargs) -> None:
        if not self._state.adding or type(self).objects.filter(pk=self.pk).exists():
            raise ValidationError("Landing copy revisions are immutable; create a new revision.")
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.page} v{self.version}"
