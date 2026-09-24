# ADR 0003: Django REST Framework for the public copy API

**Status:** Accepted.
**Date:** 2026-09-21

## Context

Jung needs a stable, read-only JSON route for published landing text. The backend already uses Django, and the user explicitly requested Django REST Framework. The route must keep draft revisions private and return a complete published snapshot for one exact locale.

## Decision

Use Django REST Framework for the public copy view. Pin the compatible 3.18 release line. Keep the route in the landing_copy capability app and include it under api/v1/ from the Django project URL configuration. Use JSON rendering, anonymous read permission, no authentication processing on this route, and no public write action. Return only the revision referenced by the requested page's published pointer. Advertise a 60-second public cache lifetime on successful responses.

## Consequences

The frontend can retrieve changed published wording without a new build if it honors compatible cache freshness. The initial seeded drafts return 404 until they are reviewed and published. This decision adds one mature framework dependency, but no new database table or migration. The staff publication workflow is recorded in ADR 0004. Frontend integration and deployment cache behavior remain separate work.
