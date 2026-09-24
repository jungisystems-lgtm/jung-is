"""Behavior checks for localized landing copy and seeded drafts."""

from copy import deepcopy

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from landing_copy.models import LandingCopyRevision, LandingPage, Site


class LandingCopyTests(TestCase):
    def test_seed_has_two_unpublished_valid_locales_without_unverified_claims(self):
        pages = LandingPage.objects.filter(site__key="jung", slug="home")
        self.assertCountEqual(pages.values_list("locale", flat=True), ["es-CO", "en-US"])
        for page in pages:
            self.assertIsNone(page.published_revision_id)
            self.assertEqual(page.revisions.count(), 1)
            revision = page.revisions.get()
            self.assertEqual(revision.version, 1)
            self.assertEqual(revision.schema_version, 1)
            self.assertNotIn("trust", revision.copy)
            self.assertNotIn("results", revision.copy)
            revision.full_clean()

    def test_revision_cannot_be_edited_after_creation(self):
        revision = LandingCopyRevision.objects.get(page__site__key="jung", page__locale="es-CO")
        revision.change_summary = "Changed after creation"
        with self.assertRaises(ValidationError):
            revision.save()

    def test_copy_rejects_unknown_fields_and_markup(self):
        original = LandingCopyRevision.objects.get(page__site__key="jung", page__locale="es-CO")
        invalid = deepcopy(original.copy)
        invalid["hero"]["unexpected"] = "not in v1"
        with self.assertRaises(ValidationError):
            LandingCopyRevision(
                page=original.page,
                version=2,
                copy=invalid,
                change_summary="Invalid copy",
            ).save()

        invalid = deepcopy(original.copy)
        invalid["hero"]["heading_accent"] = "<b>Unsafe</b>"
        with self.assertRaises(ValidationError):
            LandingCopyRevision(
                page=original.page,
                version=2,
                copy=invalid,
                change_summary="Invalid markup",
            ).save()

    def test_page_cannot_publish_revision_from_another_locale(self):
        spanish = LandingPage.objects.get(site__key="jung", locale="es-CO")
        english = LandingPage.objects.get(site__key="jung", locale="en-US")
        spanish.published_revision = english.revisions.get()
        spanish.published_at = timezone.now()
        with self.assertRaises(ValidationError):
            spanish.save()

    def test_publication_requires_a_timestamp(self):
        page = LandingPage.objects.get(site__key="jung", locale="es-CO")
        page.published_revision = page.revisions.get()
        with self.assertRaises(ValidationError):
            page.save()

    def test_site_slug_and_locale_are_unique(self):
        page = LandingPage.objects.get(site__key="jung", locale="es-CO")
        with self.assertRaises(ValidationError):
            LandingPage(site=page.site, slug=page.slug, locale=page.locale).save()

    def test_new_site_can_reuse_home_slug(self):
        site = Site.objects.create(key="another-site", name="Another Site")
        page = LandingPage.objects.create(site=site, slug="home", locale="es-CO")
        self.assertEqual(page.slug, "home")
