# Django project package instructions

This package holds process configuration and cross-cutting operational code.

- Keep settings, URL composition, WSGI/ASGI entry points, request logging, and the health route here.
- Put new business endpoints, models, and workflows in capability apps once their ownership is clear. Do not turn this package into a general-purpose domain module.
- Read configuration from environment variables. Keep secrets out of source control and never expose them in logs.
- Log important failures with request context while avoiding query strings, request bodies, and sensitive customer data.
- Keep the health route independent of databases and external providers; document any change to its meaning.
- Before changing public contracts, tenant isolation, or schema, follow the approval rules in backend/AGENTS.md.

## Change log

After changing any project-owned file in this directory, append one entry per changed file to the repository-root agent-log.md before finishing the task. Follow the format, exclusions, and append-only rule in the root AGENTS.md.
