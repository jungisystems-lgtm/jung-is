# jung-api architecture

**Status:** Initial Django scaffold, September 2026.

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

The current implementation is only the Django project package in jung_api/. No business capability app, model, tenant schema, provider adapter, or customer API contract exists yet. The only route is GET /health/ for operational readiness.

## Code ownership

- jung_api/settings.py configures the process from environment variables.
- jung_api/urls.py and jung_api/views.py contain only the health route. Product endpoints should live with their capability app.
- jung_api/middleware.py and jung_api/logging.py provide request IDs and JSON console logs. They record method, resolved route, status, duration, and exception details without query strings or request bodies.
- tests/ verifies the operational boundary and logging format.
- Future Django apps should own one meaningful domain capability, with clear application rules and integration boundaries. Do not create an app per table or endpoint.

## Data and tenancy

SQLite is configured only as a local development default. There is no production database choice or application schema. No migrations were generated. Before the first real customer data, design tenant-aware ownership and enforce isolation in backend access paths. Database migrations require a human-approved brief before generation.

## Runtime and safety

The .env file is for local development and is ignored by Git. DEBUG is off unless explicitly enabled. Non-debug runs require DJANGO_SECRET_KEY. A development-only fallback key exists solely when DEBUG is enabled. Set deployment secrets and allowed hosts through environment variables.

The health endpoint does not check a database or an external provider; it reports process readiness only. Request logs are structured JSON with a generated request ID. They are diagnostic records, not a substitute for durable product events or an analytics product.

## Evolution

Start with a single Django service and add capability apps when validated workflows make ownership clear. Separate services only for meaningful deployment, reliability, security, scaling, or domain reasons. Preserve Jung-owned domain concepts and keep provider APIs outside core business rules. Record significant choices in docs/adr/.

## Open decisions

- First business capability and its public API contract.
- Production database, authentication, and tenant isolation design.
- Deployment environment and log collection.
- Which product events to persist when customer workflows exist.
