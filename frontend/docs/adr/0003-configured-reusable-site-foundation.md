# ADR 0003: Configuration and reusable site foundation

**Status:** Accepted for initial setup

## Context

Jung wants its first site to be a base for the next sites while avoiding a speculative site platform.

## Decision

Keep site copy, navigation, and branding values outside shared components. Build reusable display components from demonstrated needs. Do not create customer forks, an abstract page builder, or frontend multi-tenancy before the first customer and a backend contract exist.

## Consequences

Jung's current site configuration is local and easy to change. When `jung-api` provides site configuration, the data source can move behind a defined contract. Reuse will grow from actual repeated patterns.
