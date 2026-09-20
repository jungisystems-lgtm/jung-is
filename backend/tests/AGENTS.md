# Backend test instructions

This directory verifies observable backend behavior.

- Test real rules, security boundaries, request and failure behavior, and regressions. Avoid tests that only mirror implementation.
- Keep tests deterministic. Do not call real providers, rely on production data, or require network access.
- Use Django's test tools for request behavior. Add database tests when real models and approved migrations exist.
- Verify logging context without recording secrets or personal data.
- Run Django system checks, tests, Ruff lint, and Ruff formatting checks before reporting a backend change complete.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
