"""Request correlation and completion logging."""

import logging
from time import perf_counter
from uuid import uuid4

from jung_api.logging import request_id_context

logger = logging.getLogger(__name__)


class RequestLogMiddleware:
    """Log method, resolved route, result, and duration without query data."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = uuid4().hex
        token = request_id_context.set(request_id)
        started = perf_counter()

        try:
            response = self.get_response(request)
            route = request.resolver_match.route if request.resolver_match else "<unresolved>"
            logger.info(
                "request_completed",
                extra={
                    "method": request.method,
                    "route": route,
                    "status_code": response.status_code,
                    "duration_ms": round((perf_counter() - started) * 1000, 2),
                },
            )
            response["X-Request-ID"] = request_id
            return response
        except Exception:
            logger.exception(
                "request_failed",
                extra={"method": request.method, "route": "<unresolved>"},
            )
            raise
        finally:
            request_id_context.reset(token)
