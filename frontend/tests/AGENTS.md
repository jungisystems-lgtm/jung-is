# Test instructions

This directory contains tests for observable frontend behavior and integration boundaries.

- Test business-relevant UI behavior, API failure handling, and regressions. Do not chase coverage percentages or mirror implementation details.
- Keep unit tests deterministic and fast. Stub external HTTP calls; never call production services or use real credentials.
- Use fixtures that clearly represent test data. Do not let mock data become production behavior.
- Place tests near a feature when that improves ownership; use this directory for shared or cross-cutting tests.
- Run the relevant tests, typecheck, lint, and build before reporting a change complete.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
