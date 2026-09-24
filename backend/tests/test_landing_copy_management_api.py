"""Staff REST model operations and historical-copy boundaries."""

from copy import deepcopy

from django.contrib.auth import get_user_model
from django.test import TestCase

from landing_copy.models import LandingCopyRevision, LandingPage, Site

ROOT = "/api/v1/editor/data/"


class LandingContentManagementTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.staff = get_user_model().objects.create_user(
            username="content-editor", password="test-password", is_staff=True
        )
        cls.regular = get_user_model().objects.create_user(
            username="regular-reader", password="test-password"
        )

    def setUp(self):
        self.page = LandingPage.objects.get(site__key="jung", slug="home", locale="es-CO")
        self.copy = deepcopy(self.page.revisions.get(version=1).copy)

    def test_only_staff_can_access_model_resources(self):
        for resource in ("sites/", "pages/", "revisions/"):
            self.assertEqual(self.client.get(ROOT + resource).status_code, 403)
        self.client.force_login(self.regular)
        self.assertEqual(
            self.client.post(ROOT + "sites/", {"key": "x", "name": "X"}).status_code, 403
        )
        self.client.force_login(self.staff)
        self.assertEqual(self.client.get(ROOT).status_code, 200)
        self.assertEqual(self.client.get(ROOT + "sites/").status_code, 200)

    def test_site_crud_and_nonempty_delete_guard(self):
        self.client.force_login(self.staff)
        created = self.client.post(ROOT + "sites/", {"key": "second", "name": "Second"})
        self.assertEqual(created.status_code, 201)
        detail = ROOT + "sites/" + created.json()["id"] + "/"
        self.assertEqual(
            self.client.put(
                detail, {"key": "second", "name": "Updated"}, content_type="application/json"
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.patch(
                detail, {"name": "Again"}, content_type="application/json"
            ).status_code,
            200,
        )
        self.assertEqual(self.client.get(detail).json()["name"], "Again")
        self.assertEqual(self.client.delete(detail).status_code, 204)
        self.assertFalse(Site.objects.filter(key="second").exists())

        jung = Site.objects.get(key="jung")
        jung_detail = ROOT + "sites/" + str(jung.pk) + "/"
        self.assertEqual(
            self.client.patch(
                jung_detail, {"key": "renamed"}, content_type="application/json"
            ).status_code,
            409,
        )
        self.assertEqual(self.client.delete(jung_detail).status_code, 409)
        self.assertTrue(Site.objects.filter(key="jung").exists())

    def test_page_crud_without_revision_and_identity_guard_after_revision(self):
        self.client.force_login(self.staff)
        created = self.client.post(
            ROOT + "pages/",
            {"site": "jung", "slug": "new", "locale": "es-CO"},
        )
        self.assertEqual(created.status_code, 201)
        detail = ROOT + "pages/" + created.json()["id"] + "/"
        self.assertEqual(
            self.client.put(
                detail,
                {"site": "jung", "slug": "renamed", "locale": "es-CO"},
                content_type="application/json",
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.patch(
                detail, {"locale": "en-US"}, content_type="application/json"
            ).status_code,
            200,
        )
        self.assertEqual(self.client.delete(detail).status_code, 204)

        protected = ROOT + "pages/" + str(self.page.pk) + "/"
        self.assertEqual(
            self.client.patch(
                protected, {"slug": "changed"}, content_type="application/json"
            ).status_code,
            409,
        )
        self.assertEqual(self.client.delete(protected).status_code, 409)
        self.page.refresh_from_db()
        self.assertEqual(self.page.slug, "home")

    def test_new_copy_is_an_unpublished_immutable_revision(self):
        self.client.force_login(self.staff)
        edited = deepcopy(self.copy)
        edited["hero"]["heading_accent"] = "en nuevas citas."
        response = self.client.post(
            ROOT + "revisions/",
            {
                "page": str(self.page.pk),
                "copy": edited,
                "change_summary": "Refine the hero headline",
                "version": 99,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["version"], 2)
        revision = LandingCopyRevision.objects.get(pk=response.json()["id"])
        self.assertEqual(revision.created_by, self.staff)
        self.assertEqual(revision.copy, edited)
        self.assertIsNone(self.page.published_revision_id)
        self.assertEqual(
            self.client.get("/api/v1/sites/jung/pages/home/?locale=es-CO").status_code,
            404,
        )
        detail = ROOT + "revisions/" + str(revision.pk) + "/"
        patched = self.client.patch(
            detail,
            {
                "copy": {"hero": {"heading_accent": "en más ventas."}},
                "change_summary": "Adjust the hero wording",
            },
            content_type="application/json",
        )
        self.assertEqual(patched.status_code, 201)
        self.assertEqual(patched.json()["version"], 3)
        self.assertEqual(patched.json()["copy"]["hero"]["heading_accent"], "en más ventas.")
        self.assertIn(str(patched.json()["id"]), patched["Location"])
        replaced = self.client.put(
            detail,
            {"copy": self.copy, "change_summary": "Restore the original wording"},
            content_type="application/json",
        )
        self.assertEqual(replaced.status_code, 201)
        self.assertEqual(replaced.json()["version"], 4)
        self.assertEqual(replaced.json()["copy"], self.copy)
        self.assertEqual(self.client.delete(detail).status_code, 405)
        revision.refresh_from_db()
        self.assertEqual(revision.copy, edited)
        self.assertEqual(self.page.revisions.count(), 4)
        self.page.refresh_from_db()
        self.assertIsNone(self.page.published_revision_id)

    def test_invalid_copy_is_rejected_without_creating_revision(self):
        self.client.force_login(self.staff)
        invalid = deepcopy(self.copy)
        invalid["hero"]["unknown"] = "No"
        response = self.client.post(
            ROOT + "revisions/",
            {
                "page": str(self.page.pk),
                "copy": invalid,
                "change_summary": "Invalid draft",
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.page.revisions.count(), 1)

    def test_publication_metadata_cannot_be_written_through_page_crud(self):
        self.client.force_login(self.staff)
        revision = self.page.revisions.get(version=1)
        response = self.client.patch(
            ROOT + "pages/" + str(self.page.pk) + "/",
            {"published_revision": str(revision.pk), "published_at": "2026-09-21T00:00:00Z"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("published_revision", response.json())
        self.page.refresh_from_db()
        self.assertIsNone(self.page.published_revision_id)
        self.assertIsNone(self.page.published_at)

    def test_browsable_forms_are_available_for_staff(self):
        self.client.force_login(self.staff)
        response = self.client.get(ROOT + "revisions/", HTTP_ACCEPT="text/html")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        self.assertIn('name="copy"', response.content.decode())
