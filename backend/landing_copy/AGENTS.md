# Landing copy app instructions

This app owns public landing text, localized pages, and immutable text revisions. Site is a public content namespace, never a tenant authorization boundary.

- Keep page layout, assets, destinations, and icons in the frontend. The v1 JSON contract is for text only.
- Keep revision snapshots immutable through normal model operations. New copy requires a new version and a change summary. PUT/PATCH on a revision must create a new version, never mutate the source.
- Never seed or publish unverified testimonials, customer identities, or numerical performance claims.
- The public API reads only the exact published site, page, and locale. Never expose drafts, editor identities, or revision history.
- Publishing uses the staff-only browsable editor with explicit human confirmation. Keep publication metadata and the revision pointer consistent. The staff model API must not write publication fields directly.
- Add a reviewed schema version for structural copy changes; ordinary wording changes use a new revision.
- Follow the repository and backend AGENTS.md rules, including per-file entries in the root agent-log.md.
