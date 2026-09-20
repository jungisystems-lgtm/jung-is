# ADR 0001: Next.js and TypeScript for the web app

**Status:** Accepted for initial setup

## Context

Jung needs an official site that can become the foundation for later sites. The team prefers TypeScript for the frontend and wants a small, maintainable setup.

## Decision

Use Next.js App Router, React, and TypeScript strict mode. Keep this repository focused on presentation and API consumption.

## Consequences

Server rendering and routing are available without adding a second framework. Framework features may support the UI, but central business rules stay in `jung-api`. New frontend dependencies must justify their value.
