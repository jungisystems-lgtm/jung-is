# ADR 0001: Django foundation for jung-api

**Status:** Accepted for initial scaffold

## Context

Jung needs a Python backend that the core developer can maintain directly. The website should consume shared backend capabilities. The first customer workflows and their service boundaries are not defined yet.

## Decision

Use Django 5.2 LTS as the initial jung-api service. Start with one small Django project and add capability apps only when real workflows establish their boundaries. Expose only a process health endpoint in the scaffold. Use environment-backed settings and JSON request logs.

Do not create business models or migrations in this setup. SQLite is a local development default; the production database remains undecided.

## Consequences

The backend can start, report health, and run checks immediately. Business APIs, persistence, authentication, tenancy, and provider adapters still require explicit product contracts and architectural decisions. Any database migration requires human approval before generation.
