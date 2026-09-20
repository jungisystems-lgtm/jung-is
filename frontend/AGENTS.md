# AI engineering rules for Jung web app

Before a change, read `docs/engineering-constitution.md` and `docs/architecture.md`, inspect the affected code, and identify the owner of the behavior.

## Documentation language

- Write and edit all project-owned Markdown files in English, including README files, this AGENTS.md, architecture documents, and ADRs.
- Use English for headings, prose, tables, comments, and examples. Preserve product names, code identifiers, commands, and file paths.
- If a touched Markdown section contains Spanish prose, translate it so the document stays consistently in English.

## Scope and ownership

- Keep each change small and reviewable. Do not refactor unrelated files.
- Put routing and layout in `src/app`, reusable display pieces in `src/components`, site values in `src/config`, and API communication in `src/api`.
- Create feature folders only when real functionality needs them. Avoid speculative layers.
- Keep lead, booking, messaging, tenant, and other business rules in `jung-api`. Do not implement parallel rules in Next.js routes, server actions, or components.
- Do not introduce customer-specific forks or conditions in shared components. Represent legitimate variation as configuration.
- Do not invent API responses, live integrations, or production behavior. Label prototypes clearly.

## Changes needing a brief and human approval

Before generating database migrations, modifying public API contracts, changing service boundaries or tenant isolation, introducing major dependencies or infrastructure, or performing broad refactors, provide a concise brief of the proposed change, reasons, affected data/contracts, risks, and rollback path, then wait for human approval. Never generate migrations first.

## Quality

- Use TypeScript strict mode and keep server-only secrets off the client.
- Prefer server components; add client components only for browser interaction.
- When integrating `jung-api`, use explicit types, handle failures visibly, and log enough context to locate the failure without logging secrets or personal data.
- Add tests for meaningful behavior and regressions, not to chase coverage.
- Run lint, formatting check, typecheck, relevant tests, and build before calling a change complete. Report any check that could not run.
- Update an ADR when a consequential architecture choice is made. Architecture must not silently contradict the Constitution.

<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
