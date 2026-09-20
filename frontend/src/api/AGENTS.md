# API boundary instructions

This directory owns the frontend's communication with jung-api.

- Add typed operations only for real backend contracts. Do not invent endpoints, responses, or production fallbacks.
- Keep requests and response mapping here; keep business decisions, persistence, tenant isolation, and provider calls in jung-api.
- Keep credentials and private base URLs server-side. Do not expose secrets through NEXT_PUBLIC_ variables or client bundles.
- Time out requests, surface failures clearly, and log operation and status context without tokens or personal data.
- Coordinate public contract changes with the backend and obtain human review before changing established contracts.
- Add focused tests for request construction and failure behavior when they protect a real integration risk.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
