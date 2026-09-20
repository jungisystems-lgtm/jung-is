"""Operational views. Product endpoints belong in capability modules."""

from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health(request):
    """Report process readiness without requiring a database connection."""
    return JsonResponse({"status": "ok"})
