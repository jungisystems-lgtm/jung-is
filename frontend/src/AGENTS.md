# Frontend source instructions

This source tree renders Jung's website and provides reusable foundations for later sites.

- Follow the folder boundaries: app for routes, components for reusable presentation, features for proven UI behavior, config for site values, api for jung-api access, lib for small shared utilities, and styles for global styling.
- Keep authoritative lead, booking, messaging, tenant, and other business rules in jung-api.
- Use strict TypeScript. Prefer explicit, readable code and small changes over speculative abstractions.
- Keep customer differences in configuration and reusable components rather than forks or customer-name conditions.
- Keep secrets server-side. Handle failures visibly and log useful context without leaking sensitive information.
- Read the local AGENTS.md in the folder you change as well as the parent instructions.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
