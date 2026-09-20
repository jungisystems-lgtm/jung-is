# Jung web app architecture

**Status:** Starter, September 2026. This document describes this repository, not a completed design for all of Jung.

## Purpose

This Next.js application renders Jung's own website and establishes reusable site foundations. Jung should use the same product capabilities that future customer sites use. The web app is an interface to jung-api, not a second backend for leads, conversations, scheduling, messaging, or customer configuration.

```text
Browser
  |
  v
Next.js web app (presentation, site composition, API calls)
  |
  v
jung-api (business rules, data ownership, integrations)
  |
  +-- meaningful backend services as those boundaries are defined
  +-- external providers through backend integration boundaries
```

The backend/ directory now contains a Django scaffold and a process health endpoint. There is still no active product integration between this frontend and jung-api. src/api/jung-api.ts is a small server-side HTTP boundary that fails clearly when the base URL is absent, reports HTTP errors, and can be extended when a real contract exists. It is not a mock API.

## Frontend boundaries

- src/app: Next.js routes, layouts, metadata. Route files compose UI and request data; they do not own business policy.
- src/components: reusable presentation components. Keep them independent of a particular customer or provider.
- src/features: coherent UI behavior as features emerge. Do not create layers or domain mirrors before they are needed.
- src/config: Jung site copy and branding. The current TypeScript config is a first step, not a permanent substitute for API-backed site configuration.
- src/api: requests to jung-api and response types. When API contracts become stable, consider generated types from OpenAPI after review.
- src/lib: small shared utilities only when they have actual users.
- src/styles: global design primitives.

## Reuse model

The first site is Jung's own. Reuse should come from components, page composition, and configuration demonstrated by subsequent sites. No customer-specific forks or general-purpose page builder are planned. Branding, content, and navigation are kept out of component markup where practical. Future customer configuration belongs in the backend when the product contract is ready.

## Backend relationship

The backend scaffold uses Python and Django. Its internal service boundaries, product endpoints, tenant isolation design, and production database remain open decisions. Multi-tenancy and tenant isolation are backend concerns; do not simulate them in this frontend before a real requirement and contract exist.

## Operations and safety

- Secrets stay in local environment files or deployment secret stores, never in Git or NEXT_PUBLIC_ variables.
- API failures should identify the operation and HTTP status in server logs without exposing tokens or personal data.
- Capture useful product events in jung-api when corresponding customer workflows exist; do not add speculative frontend analytics infrastructure now.
- Test behavior and regressions. Keep the full local checks available through npm run check.

## Open decisions

- Actual jung-api base URL, authentication flow, and versioned API contracts.
- Site configuration contract and which fields live in the backend.
- First customer workflow and the reusable UI it proves.
- Deployment and observability provider.

Record consequential choices in docs/adr once they are made.
