# jung-api

Jung's Django backend. It stores localized landing text revisions, exposes a read-only public API, and provides staff-only browsable editing and publication.

## Requirements

- Python 3.12 or later
- pip

## Local setup

Run these commands from backend/ in PowerShell:

```powershell
Copy-Item .env.example .env
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe manage.py check
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py runserver
```

Open http://localhost:8000/health/. It returns JSON with status ok and an X-Request-ID response header. Local request logs are JSON lines on the console.

The .env file is local and ignored by Git. Development uses a local-only key when DJANGO_DEBUG=1. A non-debug deployment must set DJANGO_SECRET_KEY and suitable DJANGO_ALLOWED_HOSTS.

## Initial landing copy data

From backend/, run:

    .venv\Scripts\python.exe manage.py migrate

This creates Jung home-page drafts in Spanish and English. Neither draft is published automatically. The public API returns 404 for a locale until a staff member reviews and publishes its revision.

## Published landing copy API

Request the exact language from a published page:

    GET /api/v1/sites/jung/pages/home/?locale=es-CO
    GET /api/v1/sites/jung/pages/home/?locale=en-US

A successful response contains schema_version, site_key, page_slug, locale, revision, published_at, and copy. Clients can request JSON, while a browser can display DRF's HTML interface. Successful responses have a 60-second public cache header. Missing or malformed locale values return 400; an absent or unpublished page returns 404. There are no public write routes or draft responses. The complete contract and pending editorial decisions are in docs/landing-copy-api-draft.md.

## Browsable review and publication

Create a Django staff account if you do not already have one:

    .venv\Scripts\python.exe manage.py createsuperuser

With the development server running, sign in at http://127.0.0.1:8000/api-auth/login/. Then open http://127.0.0.1:8000/api/v1/editor/sites/jung/pages/home/?locale=es-CO in the same browser. Review the complete revision text, enter version 1, check the confirmation box, and submit the POST form. Repeat with locale=en-US only after reviewing the English copy. Refresh the public API URL to see the published text. The form requires a staff account and CSRF protection. Browser requests to the public route show DRF's HTML interface, while clients requesting JSON receive the same public data.

## Staff content API

After signing in with a Django staff account, open http://127.0.0.1:8000/api/v1/editor/data/ to browse the model endpoints. These endpoints also accept JSON. Session authentication and CSRF protection apply to writes.

| Resource | List and create | Detail |
| --- | --- | --- |
| Sites | GET, POST /api/v1/editor/data/sites/ | GET, PUT, PATCH, DELETE /api/v1/editor/data/sites/{id}/ |
| Pages | GET, POST /api/v1/editor/data/pages/ | GET, PUT, PATCH, DELETE /api/v1/editor/data/pages/{id}/ |
| Revisions | GET, POST /api/v1/editor/data/revisions/ | GET, PUT, PATCH /api/v1/editor/data/revisions/{id}/ |

A new revision requires a page UUID, a complete validated copy document, and a change_summary. PUT on a revision takes a complete copy document; PATCH accepts the changed copy fields. Both create a new immutable version and return HTTP 201 with its new URL in Location. The source revision is unchanged. DELETE is disabled for revisions. Sites with pages and pages with revisions cannot be deleted or renamed; such requests return 409. Publication fields on pages are read-only here. New copy remains unpublished until a staff member reviews and confirms publication through the existing editor form.

## Checks

```powershell
.venv\Scripts\ruff.exe check .
.venv\Scripts\ruff.exe format --check .
.venv\Scripts\python.exe manage.py check
.venv\Scripts\python.exe manage.py test
```

Approved schema and data migrations seed unpublished home-page drafts for es-CO and en-US. The seed excludes unverified testimonial and performance claims. Future migrations require a human-approved change brief. SQLite is a local development default, not a production database decision.

## Structure

| Path                                  | Responsibility                        |
| ------------------------------------- | ------------------------------------- |
| jung_api/settings.py                  | Environment-backed Django settings    |
| jung_api/urls.py and views.py         | API routing and operational health    |
| jung_api/middleware.py and logging.py | Request correlation and JSON logs     |
| tests/                                | Behavior checks for the scaffold      |
| landing_copy/                         | Localized copy, revisions, and API    |
| docs/architecture.md                  | Backend boundaries and open decisions |
| docs/adr/                             | Recorded architecture decisions       |

Add further Django apps only for meaningful product capabilities. Read AGENTS.md and the local AGENTS.md in any folder you change.
