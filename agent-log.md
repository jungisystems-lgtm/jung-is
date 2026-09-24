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

- 2026-09-21T13:02:29-05:00 | Codex (/root) | Draft the public landing copy endpoint contract for review. | `backend/docs/landing-copy-api-draft.md`

- 2026-09-21T14:13:25-05:00 | Codex (/root) | Refine the landing copy API draft with a fixed text contract and data model diagram. | `backend/docs/landing-copy-api-draft.md`
- 2026-09-21T14:39:04-05:00 | Codex (/root) | Enable Django auth and localized landing copy models. | `backend/jung_api/settings.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Document landing copy ownership and editorial rules. | `backend/landing_copy/AGENTS.md`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Create the landing copy capability package. | `backend/landing_copy/__init__.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Register the landing copy Django app. | `backend/landing_copy/apps.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Add sites, localized pages, and immutable revisions. | `backend/landing_copy/models.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Validate the fixed text-only copy schema. | `backend/landing_copy/validation.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Document migration and seed safeguards. | `backend/landing_copy/migrations/AGENTS.md`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Create the landing copy migration package. | `backend/landing_copy/migrations/__init__.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Create the approved landing copy schema. | `backend/landing_copy/migrations/0001_initial.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Seed unpublished Spanish and English Jung drafts. | `backend/landing_copy/migrations/0002_seed_landing_copy.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Test seed, immutability, validation, and publication boundaries. | `backend/tests/test_landing_copy.py`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Document migration setup and draft data. | `backend/README.md`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Describe the implemented landing copy persistence boundary. | `backend/docs/architecture.md`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Mark persistence implemented and the public API as proposed. | `backend/docs/landing-copy-api-draft.md`

- 2026-09-21T14:39:04-05:00 | Codex (/root) | Record the localized revision decision. | `backend/docs/adr/0002-localized-landing-copy-revisions.md`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Add the Django REST Framework dependency. | `backend/requirements.txt`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Register Django REST Framework. | `backend/jung_api/settings.py`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Mount the versioned landing copy API routes. | `backend/jung_api/urls.py`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Expose exact published copy as read-only JSON. | `backend/landing_copy/views.py`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Define the public landing copy URL. | `backend/landing_copy/urls.py`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Verify published-only reads, locale isolation, validation, and cache rules. | `backend/tests/test_landing_copy_api.py`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Document the public read route and unpublished seed behavior. | `backend/README.md`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Describe the implemented Django REST Framework read boundary. | `backend/docs/architecture.md`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Update the API contract and pending editorial decisions. | `backend/docs/landing-copy-api-draft.md`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Clarify published-only API access for future agents. | `backend/landing_copy/AGENTS.md`

- 2026-09-21T14:46:43-05:00 | Codex (/root) | Record the Django REST Framework decision. | `backend/docs/adr/0003-drf-public-landing-copy-api.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Enable browsable DRF, signed-cookie staff sessions, CSRF, and static assets. | `backend/jung_api/settings.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Add DRF browser login and logout routes. | `backend/jung_api/urls.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Include publication context in structured logs. | `backend/jung_api/logging.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Add staff-only review and confirmed publication form. | `backend/landing_copy/views.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Route the staff landing copy editor. | `backend/landing_copy/urls.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Test browser login, staff access, CSRF, publication, and rollback. | `backend/tests/test_landing_copy_editor.py`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Explain how staff review and publish copy in the browser. | `backend/README.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Document the browsable editor and session security boundary. | `backend/docs/architecture.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Describe the implemented staff publication workflow. | `backend/docs/landing-copy-api-draft.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Require the confirmed staff editor for publication. | `backend/landing_copy/AGENTS.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Link the public API decision to the staff editor ADR. | `backend/docs/adr/0003-drf-public-landing-copy-api.md`

- 2026-09-21T15:01:01-05:00 | Codex (/root) | Record the browsable staff publication decision. | `backend/docs/adr/0004-staff-publication-browsable-api.md`

- 2026-09-21T16:17:43.4618369-05:00 | Codex (/root) | Add staff-only model serializers and validated copy revision creation. | `backend/landing_copy/serializers.py` Expose guarded staff REST viewsets and immutable revision replacement. | `backend/landing_copy/viewsets.py` Route the staff model resources under the editor API. | `backend/landing_copy/urls.py` Test staff permissions, CRUD guards, and revision versioning. | `backend/tests/test_landing_copy_management_api.py` Document the staff model API and editing workflow. | `backend/README.md` Describe staff content editing in the backend architecture. | `backend/docs/architecture.md` Specify staff model endpoints and immutable editing behavior. | `backend/docs/landing-copy-api-draft.md` Require versioned copy edits and separate confirmed publication. | `backend/landing_copy/AGENTS.md` Record the staff content model API decision. | `backend/docs/adr/0005-staff-content-model-api.md`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: add staff serializers and validated revision creation. | `backend/landing_copy/serializers.py`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: expose guarded staff REST viewsets. | `backend/landing_copy/viewsets.py`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: route staff model resources. | `backend/landing_copy/urls.py`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: test staff CRUD and immutable versioning. | `backend/tests/test_landing_copy_management_api.py`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: document staff editing workflow. | `backend/README.md`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: document staff editing architecture. | `backend/docs/architecture.md`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: specify staff model API contract. | `backend/docs/landing-copy-api-draft.md`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: instruct agents on versioned editing and publication. | `backend/landing_copy/AGENTS.md`

- 2026-09-21T16:18:28.427429-05:00 | Codex (/root) | Corrected entry: record staff model API decision. | `backend/docs/adr/0005-staff-content-model-api.md`
