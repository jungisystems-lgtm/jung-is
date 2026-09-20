# Agent change log

This append-only log tracks project-owned file changes from its creation onward. Earlier changes predate the log, so their exact per-file timestamps are not reconstructed.

## Entries

- 2026-09-20T12:04:15-05:00 | Codex (/root) | Define repository-wide change logging rules. | AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | backend/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/docs/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/docs/adr/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/public/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/api/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/app/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/components/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/config/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/features/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/lib/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/src/styles/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Require changes in this directory to be recorded in the root log. | frontend/tests/AGENTS.md
- 2026-09-20T12:04:15-05:00 | Codex (/root) | Create the append-only agent change log. | agent-log.md
- 2026-09-20T12:05:06-05:00 | Codex (/root) | Switch to stable, append-only bullet entries. | agent-log.md

- 2026-09-20T12:06:00-05:00 | Codex (/root) | Clarify append-only log formatting and correction rules. | AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Ignore local Python environments, secrets, caches, and SQLite files. | backend/.gitignore

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Document local Django environment variables. | backend/.env.example

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Declare Django and dotenv runtime dependencies. | backend/requirements.txt

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Declare Ruff for local checks. | backend/requirements-dev.txt

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Configure Ruff lint and formatting. | backend/pyproject.toml

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add the Django management entry point. | backend/manage.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Create the Django project package. | backend/jung_api/**init**.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add the ASGI entry point. | backend/jung_api/asgi.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add the WSGI entry point. | backend/jung_api/wsgi.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Configure environment-backed Django settings and JSON logging. | backend/jung_api/settings.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Route the operational health endpoint. | backend/jung_api/urls.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Implement the process health response. | backend/jung_api/views.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add JSON log formatting and request correlation. | backend/jung_api/logging.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Log request outcomes with generated request IDs. | backend/jung_api/middleware.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Create the backend test package. | backend/tests/**init**.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Test the health response and structured logging. | backend/tests/test_health.py

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Document backend setup, checks, and current scope. | backend/README.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Align backend agent rules with the Django scaffold. | backend/AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Document Django boundaries, safety, and open decisions. | backend/docs/architecture.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Record the initial Django foundation decision. | backend/docs/adr/0001-django-foundation.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add local rules for Django project configuration. | backend/jung_api/AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add local backend test rules. | backend/tests/AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add backend documentation rules. | backend/docs/AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Add backend ADR rules. | backend/docs/adr/AGENTS.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Update repository overview for the Django backend. | README.md

- 2026-09-20T13:52:27-05:00 | Codex (/root) | Update frontend architecture notes to reflect the Django scaffold. | frontend/docs/architecture.md

- 2026-09-20T13:53:58-05:00 | Codex (/root) | Clarify that log paths use inline code. | `AGENTS.md`

- 2026-09-20T13:53:58-05:00 | Codex (/root) | Correct the rendered path for the Django package initializer. | `backend/jung_api/__init__.py`

- 2026-09-20T13:53:58-05:00 | Codex (/root) | Correct the rendered path for the test package initializer. | `backend/tests/__init__.py`

- 2026-09-20T17:56:58-05:00 | Codex (/root) | Add Git clone, commit, and publishing instructions. | `GIT-README.md`

- 2026-09-20T17:56:58-05:00 | Codex (/root) | Link the Git guide and configured GitHub remote. | `README.md`

- 2026-09-20T18:03:07-05:00 | Codex (/root) | Update the GitHub repository link to jung-is. | `README.md`

- 2026-09-20T18:03:07-05:00 | Codex (/root) | Update Git clone and publishing guidance for jung-is. | `GIT-README.md`
