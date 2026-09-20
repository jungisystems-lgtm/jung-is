# jung-api

Jung's Django backend foundation. This service will own business rules, persistent state, tenant isolation, and provider integrations as real product capabilities are added. The current scaffold exposes only an operational health endpoint.

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
.venv\Scripts\python.exe manage.py runserver
```

Open http://localhost:8000/health/. It returns JSON with status ok and an X-Request-ID response header. Local request logs are JSON lines on the console.

The .env file is local and ignored by Git. Development uses a local-only key when DJANGO_DEBUG=1. A non-debug deployment must set DJANGO_SECRET_KEY and suitable DJANGO_ALLOWED_HOSTS.

## Checks

```powershell
.venv\Scripts\ruff.exe check .
.venv\Scripts\ruff.exe format --check .
.venv\Scripts\python.exe manage.py check
.venv\Scripts\python.exe manage.py test
```

No application models or migrations have been created. Do not generate migrations before a human-approved change brief. SQLite is a local development default, not a production database decision.

## Structure

| Path                                  | Responsibility                        |
| ------------------------------------- | ------------------------------------- |
| jung_api/settings.py                  | Environment-backed Django settings    |
| jung_api/urls.py and views.py         | Operational health route only         |
| jung_api/middleware.py and logging.py | Request correlation and JSON logs     |
| tests/                                | Behavior checks for the scaffold      |
| docs/architecture.md                  | Backend boundaries and open decisions |
| docs/adr/                             | Recorded architecture decisions       |

Add Django apps for meaningful product capabilities only when the first real workflow requires them. Read AGENTS.md and the local AGENTS.md in any folder you change.
