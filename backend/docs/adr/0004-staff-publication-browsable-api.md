# ADR 0004: Staff publication through the browsable API

**Status:** Accepted.
**Date:** 2026-09-21

## Context

Jung's initial landing text is stored as unpublished Spanish and English revisions. The user wants to review and publish a selected revision from Django REST Framework's web interface. The public API must never expose drafts, and publication must record the human actor.

## Decision

Enable DRF's browsable renderer and login routes. Use Django session authentication with signed cookie sessions and CSRF protection. A staff-only editor endpoint shows complete localized revisions and offers a POST form requiring the selected version and explicit human confirmation. The publication transaction updates the page's revision pointer, publication time, and staff publisher. The same form can select an older revision for rollback. Keep public GET access separate from the editor route.

## Consequences

A staff member can review and publish without using a Django shell. No new database model or migration is required. The editor reveals drafts only to Django staff and marks responses private and non-cacheable. Signed cookie sessions avoid a session table; production use requires HTTPS and a stable secret key. The current schema records only the latest publication metadata, so a durable per-publication audit trail would need a separate approved model. Creating or editing revision content through the browser remains outside this decision.
