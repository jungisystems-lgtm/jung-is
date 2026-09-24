# ADR 0002: Localized landing copy revisions

**Status:** Accepted for persistence; publication API remains pending review.
**Date:** 2026-09-21

## Context

Jung needs to change landing text without rebuilding the frontend and reuse the same text structure across similar sites. Developers and agents will edit the content in Django. The current visual design defines the component layout, while Spanish and English wording can evolve independently.

## Decision

Use one Site as a public content namespace and one LandingPage per site, slug, and locale. Keep complete v1 text snapshots in LandingCopyRevision. A nullable pointer on LandingPage identifies the published revision. Keep the fixed section and item IDs in a validated JSON document, while Next.js owns layout, artwork, destinations, and component order.

Seed Spanish and English Jung home drafts through a data migration. Do not publish them automatically. Exclude the reference design's testimonial and numerical performance claims until a human verifies them.

## Consequences

Copy changes can become new revisions without a schema migration or frontend rebuild. Each locale may publish at a different time. New visual sections or a changed text shape require a reviewed schema version and frontend change. The current app has no public read endpoint or publication workflow; these need separate implementation and review. Site is not a tenant security boundary. Direct database updates can bypass model validation and revision immutability, so editorial changes must use approved application operations.
