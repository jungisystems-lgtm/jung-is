"""Browsable landing copy review and publication tests."""

from copy import deepcopy

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.utils import timezone

from landing_copy.models import LandingCopyRevision, LandingPage

EDITOR_URL = "/api/v1/editor/sites/jung/pages/home/?locale=es-CO"
PUBLIC_URL = "/api/v1/sites/jung/pages/home/?locale=es-CO"


class LandingCopyEditorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        cls.staff = user_model.objects.create_user(
            username="editor", password="test-password", is_staff=True
        )
        cls.regular = user_model.objects.create_user(username="reader", password="test-password")

    def test_public_route_renders_browsable_api_in_browser(self):
        response = self.client.get(PUBLIC_URL, HTTP_ACCEPT="text/html")
        self.assertEqual(response.status_code, 404)
        self.assertIn("text/html", response["Content-Type"])
        self.assertNotIn("Convierte conversaciones", response.content.decode())

    def test_drf_login_page_is_available(self):
        response = self.client.get("/api-auth/login/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])

    def test_browser_login_opens_staff_editor(self):
        client = Client(enforce_csrf_checks=True)
        login = client.get("/api-auth/login/")
        self.assertEqual(login.status_code, 200)
        token = client.cookies["csrftoken"].value
        response = client.post(
            "/api-auth/login/",
            {"username": "editor", "password": "test-password"},
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, 302)
        editor = client.get(EDITOR_URL, HTTP_ACCEPT="text/html")
        self.assertEqual(editor.status_code, 200)
        self.assertIn('name="confirm_publish"', editor.content.decode())

    def test_only_staff_can_review_drafts(self):
        self.assertEqual(self.client.get(EDITOR_URL).status_code, 403)
        self.client.force_login(self.regular)
        self.assertEqual(self.client.get(EDITOR_URL).status_code, 403)
        self.assertEqual(
            self.client.post(EDITOR_URL, {"version": 1, "confirm_publish": "true"}).status_code,
            403,
        )
        self.client.force_login(self.staff)
        response = self.client.get(EDITOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        self.assertEqual(response.json()["revisions"][0]["version"], 1)
        self.assertIn("hero", response.json()["revisions"][0]["copy"])

    def test_staff_get_has_browsable_publish_form(self):
        self.client.force_login(self.staff)
        response = self.client.get(EDITOR_URL, HTTP_ACCEPT="text/html")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response["Content-Type"])
        html = response.content.decode()
        self.assertIn('name="version"', html)
        self.assertIn('name="confirm_publish"', html)
        self.assertIn("locale=es-CO", html)

    def test_publication_requires_explicit_confirmation_and_staff(self):
        self.client.force_login(self.staff)
        no_confirmation = self.client.post(EDITOR_URL, {"version": 1})
        self.assertEqual(no_confirmation.status_code, 400)
        false_confirmation = self.client.post(
            EDITOR_URL, {"version": 1, "confirm_publish": "false"}
        )
        self.assertEqual(false_confirmation.status_code, 400)
        missing = self.client.post(EDITOR_URL, {"version": 999, "confirm_publish": "true"})
        self.assertEqual(missing.status_code, 404)
        self.assertEqual(self.client.get(PUBLIC_URL).status_code, 404)

    def test_staff_can_publish_reviewed_version(self):
        self.client.force_login(self.staff)
        response = self.client.post(EDITOR_URL, {"version": 1, "confirm_publish": "true"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Cache-Control"], "private, no-store")
        page = LandingPage.objects.get(site__key="jung", slug="home", locale="es-CO")
        self.assertEqual(page.published_revision.version, 1)
        self.assertEqual(page.published_by, self.staff)
        self.assertLessEqual(page.published_at, timezone.now())
        self.assertEqual(self.client.get(PUBLIC_URL).status_code, 200)

    def test_staff_can_restore_an_earlier_revision(self):
        page = LandingPage.objects.get(site__key="jung", slug="home", locale="es-CO")
        newer_copy = deepcopy(page.revisions.get(version=1).copy)
        newer_copy["hero"]["heading_accent"] = "en nuevas citas."
        LandingCopyRevision.objects.create(
            page=page,
            version=2,
            copy=newer_copy,
            change_summary="Try revised heading",
            created_by=self.staff,
        )
        self.client.force_login(self.staff)
        self.assertEqual(
            self.client.post(EDITOR_URL, {"version": 2, "confirm_publish": "true"}).status_code,
            200,
        )
        self.assertEqual(self.client.get(PUBLIC_URL).json()["revision"], 2)
        self.assertEqual(
            self.client.post(EDITOR_URL, {"version": 1, "confirm_publish": "true"}).status_code,
            200,
        )
        self.assertEqual(self.client.get(PUBLIC_URL).json()["revision"], 1)

    def test_session_publication_requires_csrf_token(self):
        client = Client(enforce_csrf_checks=True)
        client.force_login(self.staff)
        denied = client.post(EDITOR_URL, {"version": 1, "confirm_publish": "true"})
        self.assertEqual(denied.status_code, 403)

        client.get(EDITOR_URL, HTTP_ACCEPT="text/html")
        token = client.cookies["csrftoken"].value
        response = client.post(
            EDITOR_URL,
            {"version": 1, "confirm_publish": "true"},
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, 200)
