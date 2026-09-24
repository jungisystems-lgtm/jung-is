"""URL routes for public landing copy."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from landing_copy.views import LandingCopyEditorView, PublishedLandingCopyView
from landing_copy.viewsets import (
    LandingCopyRevisionViewSet,
    LandingPageViewSet,
    SiteViewSet,
)

editor_router = DefaultRouter()
editor_router.register("sites", SiteViewSet, basename="editor-site")
editor_router.register("pages", LandingPageViewSet, basename="editor-page")
editor_router.register("revisions", LandingCopyRevisionViewSet, basename="editor-revision")

urlpatterns = [
    path("editor/data/", include(editor_router.urls)),
    path(
        "editor/sites/<str:site_key>/pages/<str:page_slug>/",
        LandingCopyEditorView.as_view(),
        name="landing-copy-editor",
    ),
    path(
        "sites/<str:site_key>/pages/<str:page_slug>/",
        PublishedLandingCopyView.as_view(),
        name="published-landing-copy",
    ),
]
