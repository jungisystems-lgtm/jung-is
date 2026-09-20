"""Basic operational behavior for the backend scaffold."""

import json
import logging
from unittest import TestCase

from django.test import SimpleTestCase

from jung_api.logging import JsonFormatter


class HealthViewTests(SimpleTestCase):
    def test_health_is_available_without_a_database(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
        self.assertTrue(response["X-Request-ID"])


class JsonFormatterTests(TestCase):
    def test_includes_operation_context_without_extra_request_data(self):
        record = logging.LogRecord(
            name="jung_api.test",
            level=logging.ERROR,
            pathname=__file__,
            lineno=1,
            msg="request_failed",
            args=(),
            exc_info=None,
        )
        record.request_id = "abc123"
        record.route = "health/"
        record.status_code = 500

        payload = json.loads(JsonFormatter().format(record))

        self.assertEqual(payload["message"], "request_failed")
        self.assertEqual(payload["request_id"], "abc123")
        self.assertEqual(payload["route"], "health/")
        self.assertEqual(payload["status_code"], 500)
        self.assertNotIn("path", payload)
