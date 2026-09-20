"""ASGI entry point for jung-api."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jung_api.settings")

application = get_asgi_application()
