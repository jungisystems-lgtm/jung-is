"""Public landing copy API contract and draft isolation tests."""

from copy import deepcopy

from django.test import TestCase
from django.utils import timezone

from landing_copy.models import LandingCopyRevision, LandingPage

URL = "/api/v1/sites/jung/pages/home/"


class PublishedLandingCopyApiTests(TestCase):
    def publish(self, locale: str) -> LandingPage:
        page = LandingPage.objects.get(site__key="jung", slug="home", locale=locale)
        page.published_revision = page.revisions.get(version=1)
        page.published_at = timezone.now()
        page.save()
        return page

    def test_drafts_are_not_public_even_to_anonymous_clients(self):
        for locale in ("es-CO", "en-US"):
            response = self.client.get(URL, {"locale": locale})
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response["Cache-Control"], "no-store")
            self.assertNotIn("copy", response.json())

    def test_response_contains_only_the_exact_published_locale_and_metadata(self):
        page = self.publish("es-CO")
        response = self.client.get(URL, {"locale": "es-CO"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response["Cache-Control"], "public, max-age=60")
        payload = response.json()
        self.assertEqual(
            set(payload),
            {
                "schema_version",
                "site_key",
                "page_slug",
                "locale",
                "revision",
                "published_at",
                "copy",
            },
        )
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual(payload["site_key"], "jung")
        self.assertEqual(payload["page_slug"], "home")
        self.assertEqual(payload["locale"], "es-CO")
        self.assertEqual(payload["revision"], 1)
        self.assertEqual(payload["copy"], page.published_revision.copy)
        self.assertNotIn("trust", payload["copy"])
        self.assertNotIn("results", payload["copy"])
        self.assertEqual(
            self.client.get(URL, {"locale": "en-US"}).status_code,
            404,
        )

    def test_new_unpublished_revision_does_not_replace_live_content(self):
        page = self.publish("en-US")
        draft_copy = deepcopy(page.published_revision.copy)
        draft_copy["hero"]["heading_accent"] = "into more appointments."
        LandingCopyRevision.objects.create(
            page=page,
            version=2,
            copy=draft_copy,
            change_summary="Try a different headline",
        )

        payload = self.client.get(URL, {"locale": "en-US"}).json()
        self.assertEqual(payload["revision"], 1)
        self.assertNotEqual(payload["copy"], draft_copy)

    def test_invalid_or_missing_locale_returns_400_without_fallback(self):
        self.publish("es-CO")
        for query in ("", "?locale=es", "?locale=EN-us", "?locale=en-US&locale=es-CO"):
            response = self.client.get(URL + query)
            self.assertEqual(response.status_code, 400, query)
            self.assertNotIn("copy", response.json())

    def test_unknown_site_page_and_locale_return_404(self):
        self.publish("es-CO")
        for url in (
            "/api/v1/sites/missing/pages/home/?locale=es-CO",
            "/api/v1/sites/jung/pages/missing/?locale=es-CO",
            URL + "?locale=fr-FR",
        ):
            self.assertEqual(self.client.get(url).status_code, 404)

    def test_malformed_site_and_page_return_400(self):
        for url in (
            "/api/v1/sites/Jung/pages/home/?locale=es-CO",
            "/api/v1/sites/jung/pages/Home_bad/?locale=es-CO",
        ):
            self.assertEqual(self.client.get(url).status_code, 400)

    def test_writes_are_not_exposed(self):
        self.assertEqual(self.client.post(URL, {"locale": "es-CO"}).status_code, 405)
