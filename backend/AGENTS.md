# Backend instructions

This directory contains the Django scaffold for jung-api. Read ../frontend/docs/engineering-constitution.md and docs/architecture.md before changing its boundaries. Read the local AGENTS.md in each folder you modify.

- Python and Django are the chosen backend foundation. Create modules and service boundaries from real product capabilities rather than speculative decomposition.
- The backend owns Jung's business rules, persistent state, tenant isolation, provider integrations, and meaningful product events. The website consumes these capabilities through explicit API contracts.
- Keep Django project configuration and operational routes in jung_api/. Put product capabilities in focused Django apps when they exist.
- Model Jung concepts independently of WhatsApp, calendars, payment vendors, and other providers. Isolate integrations behind small interfaces when a real boundary warrants it.
- Make important failures diagnosable with contextual logs. Do not swallow errors or log secrets and personal data unnecessarily.
- Define critical workflows deterministically before adding AI behavior. Protect business rules and tenant boundaries with meaningful tests.
- Do not generate database migrations before human approval. Provide a brief covering the change, affected data, risks, and recovery plan first.
- Do not add infrastructure, services, or major dependencies without a concrete need and architectural review.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
