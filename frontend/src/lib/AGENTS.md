# Shared utility instructions

This directory is for small utilities that have multiple real callers.

- Keep functions narrow, pure when practical, and independent of page-specific copy or provider APIs.
- Do not turn lib into a catch-all for business rules, API clients, or feature code; those have dedicated owners.
- Add an abstraction only after demonstrated repetition or an important boundary.
- Add focused tests for nontrivial transformations and edge cases. Avoid wrappers that merely rename a standard API.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
