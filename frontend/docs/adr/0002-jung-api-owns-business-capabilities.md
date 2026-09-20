# ADR 0002: jung-api owns business capabilities

**Status:** Accepted for initial setup

## Context

Jung's own site should use the product Jung sells. Future sites may be built by Jung or by customers, so product capabilities cannot depend on this website's implementation.

## Decision

The web app consumes `jung-api` for leads, conversations, appointments, scheduling, messaging, and future product operations. It may validate basic UI input, but authoritative rules, persistence, tenant isolation, and provider integrations belong in the backend.

## Consequences

The frontend starts with a small, explicit HTTP boundary. API contracts and error behavior must be defined with the backend as features arrive. This also permits third-party sites to use Jung's capabilities.
