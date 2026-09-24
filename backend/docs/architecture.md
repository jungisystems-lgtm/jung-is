# jung-api architecture

**Status:** Django foundation with landing copy persistence, public read, staff editing, and publication, September 2026.

## Purpose and boundaries

jung-api is the backend for Jung's own site and future customer-facing channels. It owns authoritative business behavior, data, tenant isolation, provider integrations, and meaningful product events. The Next.js frontend is a consumer of its API. Third-party sites should eventually be able to consume the same capabilities.

```text
Next.js or another client
          |
          v
      jung-api
   Django service
          |
          +-- product capability apps, added when real workflows need them
          +-- provider adapters behind small boundaries
          +-- persistence and tenant-aware access
```

The current implementation includes the Django project package and the landing_copy capability app. The HTTP routes include GET /health/, the public landing copy GET, DRF login/logout, staff model editing endpoints, and the landing copy review and publication endpoint. No tenant schema, provider adapter, or customer business API exists.

## Code ownership

- jung_api/settings.py configures the process from environment variables.
- jung_api/urls.py composes routes; jung_api/views.py owns only health. Product endpoints live with their capability app.
- jung_api/middleware.py and jung_api/logging.py provide request IDs and JSON console logs. They record method, resolved route, status, duration, and exception details without query strings or request bodies. Publication actions add site, page, locale, revision, and staff user ID.
- landing_copy/ owns public site namespaces, localized pages, immutable text revisions, the v1 copy validator, the public read route, staff model CRUD routes, and the publication route.
- tests/ verifies operational behavior and landing copy rules.
- Future Django apps should own one meaningful domain capability, with clear application rules and integration boundaries. Do not create an app per table or endpoint.

## Data and tenancy

SQLite remains a local development default; no production database has been chosen. Approved migrations create Site, LandingPage, and LandingCopyRevision plus Django auth tables. Site is a public content namespace, not a tenant authorization boundary. The data migration seeds one unpublished Jung home draft in each of es-CO and en-US. It excludes unverified testimonials and performance figures. Revisions are immutable through normal model saves; direct database updates bypass model validation and must not be used for editorial changes. Before the first real customer data, design and enforce tenant-aware ownership in the relevant access paths. Future migrations still require a human-approved brief before generation.

## Runtime and safety

The .env file is for local development and is ignored by Git. DEBUG is off unless explicitly enabled. Non-debug runs require DJANGO_SECRET_KEY. A development-only fallback key exists solely when DEBUG is enabled. Set deployment secrets and allowed hosts through environment variables.

The public landing copy route uses Django REST Framework, accepts anonymous GET requests, renders JSON or the browsable HTML interface, and filters by the exact site, page, and locale. It returns only the page's published revision and sets a public 60-second cache header on successful responses. Staff-only model routes create and edit site and page records and create immutable revision snapshots; revision PUT/PATCH creates a new version instead of overwriting the source. Dependent sites and pages cannot be renamed or deleted, and revision deletion is disabled. Publication fields remain read-only in model CRUD. The staff-only editor route shows complete revisions and provides a confirmed publication POST. Django session authentication, CSRF protection, and the is_staff permission guard this route; editor responses are never cached. Sessions use signed cookies, so this feature adds no session table or migration. The initial drafts remain unpublished and therefore return 404 until staff publication. The frontend must use a compatible cache policy for copy updates to appear without redeployment. The health endpoint does not check a database or an external provider; it reports process readiness only. Request logs are structured JSON with a generated request ID. They are diagnostic records, not a substitute for durable product events or an analytics product.

## Evolution

Start with a single Django service and add capability apps when validated workflows make ownership clear. Separate services only for meaningful deployment, reliability, security, scaling, or domain reasons. Preserve Jung-owned domain concepts and keep provider APIs outside core business rules. Record significant choices in docs/adr/.

## Open decisions

- Durable publication history beyond the latest pointer and structured request logs.
- Production database, authentication, and tenant isolation design.
- Deployment environment and log collection.
- Which product events to persist when customer workflows exist.
