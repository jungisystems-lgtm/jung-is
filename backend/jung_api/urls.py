"""Operational routes for the backend foundation."""

from django.urls import path

from jung_api.views import health

urlpatterns = [
    path("health/", health, name="health"),
]
