# Feature instructions

Create a feature module here when a real interface workflow needs related components or state to live together.

- Keep the module scoped to UI behavior and composition. The backend owns authoritative business rules and data.
- Use ../api for jung-api calls and ../config for site-level values. Move broadly reusable display pieces to ../components.
- Do not mirror the entire backend domain or create speculative feature folders, layers, or provider abstractions.
- Make loading, error, and success behavior observable and honest. Add tests for meaningful user behavior and regressions.
- Prefer one coherent change that can be reviewed and reversed easily.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
