"""Operational routes for the backend foundation."""

from django.urls import include, path

from jung_api.views import health

urlpatterns = [
    path("health/", health, name="health"),
    path("api/v1/", include("landing_copy.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
