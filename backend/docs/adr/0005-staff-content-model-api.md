# ADR 0005: Staff REST API for landing content models

**Status:** Accepted.
**Date:** 2026-09-21

## Context

The staff publication form selects an existing revision but cannot create new site, page, or copy records. The user wants to manage those records through Django REST Framework's browsable API while preserving immutable copy history and human approval before publication.

## Decision

Expose staff-only REST resources for Site, LandingPage, and LandingCopyRevision under /api/v1/editor/data/. Use session authentication, CSRF protection, and the Django is_staff permission. Site and page resources support ordinary REST writes. Block identity changes and deletion once dependent records exist. Make page publication fields read-only in these resources.

A revision POST creates the next version from a complete validated copy document. A revision PUT or PATCH creates a new immutable version from the selected source and returns 201 with a Location for the new record. PATCH merges partial copy fields into the source document before full schema validation. Disable revision DELETE. Publication remains a separate, confirmed staff action.

## Consequences

Staff can edit copy in the browsable API without redeployment. Every edit preserves prior revisions and records a change summary. Creating a revision does not change what the public API serves. Version changes can be reviewed and published or rolled back through the publication endpoint. The fixed v1 text schema still requires a reviewed backend and frontend change for a new section. This API is not a customer content management interface or a tenant authorization boundary.
