# Site configuration instructions

This directory holds site copy, branding, navigation, and other presentation values.

- Keep ordinary site values out of shared components and business logic.
- The current local Jung config is a starting point. Future customer or site configuration should come from a defined jung-api contract when that capability exists.
- Do not store secrets or sensitive customer data here, and do not use configuration to bypass backend authorization or tenant isolation.
- Avoid customer-name branches or frontend multi-tenancy scaffolding before a real contract and customer need exist.
- Use explicit types and defaults where they clarify current behavior; do not invent an extensive configuration schema prematurely.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
