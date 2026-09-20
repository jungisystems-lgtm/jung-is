# Next.js route instructions

This directory owns routes, layouts, metadata, and page composition.

- Prefer server components. Use client components only when browser interaction or state is needed.
- Keep route files thin: compose components and obtain data through the api boundary. Do not implement Jung's business rules in pages, route handlers, or server actions.
- Put reusable display pieces in ../components and site copy or branding in ../config.
- Handle loading, empty, and error states honestly when a real API-backed feature is added. Never silently replace failures with fake data.
- Preserve accessibility, semantic HTML, and responsive behavior.
- Consult the installed Next.js documentation before using version-sensitive APIs, as required by the parent AGENTS.md.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
