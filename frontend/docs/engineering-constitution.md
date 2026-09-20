# Jung Engineering Constitution

**Status:** Draft v0.1  
**Scope:** All software developed as part of the Jung platform and its products.

This Constitution defines the engineering principles that should remain stable even as Jung's products, architecture, providers, frameworks, and infrastructure evolve.

Architecture documents and ADRs may define _how_ these principles are implemented. They must not silently contradict them.

## 1. Build to Learn, Sell, and Deliver

Jung optimizes first for validating real customer needs, selling the product, and delivering working solutions.

We do not build infrastructure, abstractions, administration tools, or platform capabilities solely because we expect they may eventually be useful.

Speed is important, but speed does not justify decisions that knowingly make future evolution prohibitively difficult.

Temporary technical debt is acceptable when it is:

- explicit;
- localized;
- understood;
- reasonably reversible.

Security, tenant isolation, data integrity, and basic operational visibility are not acceptable forms of intentional technical debt.

---

## 2. Prefer the Simplest Sufficient Solution

Choose the simplest implementation that correctly solves the current validated problem.

Avoid speculative architecture and premature optimization.

Complexity must be justified by an existing requirement, an observed operational problem, an important architectural boundary, or a reasonably imminent need.

We prefer boring, explicit, understandable code over clever code.

Future-proofing should preserve important boundaries rather than attempt to predict every future feature.

---

## 3. Abstract from Evidence, Not Imagination

Do not introduce abstractions solely because something might vary in the future.

Create abstractions when there is:

- demonstrated repetition;
- a meaningful domain boundary;
- a need to isolate an external provider;
- a concrete requirement for replaceability.

External integrations are an intentional exception: small interfaces may be introduced before multiple implementations exist when doing so prevents providers from defining Jung's domain.

Abstractions should remain as small as possible.

---

## 4. Build a Shared Product, Not Individual Customer Projects

Jung builds one evolving platform.

Customer implementations should reuse shared components, services, integrations, templates, and domain capabilities.

Customer differences should primarily be expressed through configuration.

Independent forks or completely separate customer implementations are not the default operating model.

When commercially justified custom work is accepted, it should be designed as a reusable capability or component whenever reasonably possible.

---

## 5. Configuration Is Separate from Code

Business-specific configuration must not be embedded unnecessarily in core product logic.

Branding, content, schedules, integrations, services, provider identifiers, and similar customer-specific values should be represented as configuration or data.

Avoid customer-specific conditions such as:

`if customer == "customer_x"`

inside shared domain logic.

Secrets must always remain separate from both source code and ordinary customer configuration.

---

## 6. Jung Owns Its Domain

Jung's business model must be represented using Jung concepts.

Core concepts such as:

`Tenant`, `Business`, `Lead`, `Conversation`, `Message`, `Service`, `Appointment`, and future domain concepts

must not be defined by external providers.

Google Calendar does not define an Appointment.

WhatsApp does not define a Conversation.

A provider can store, transmit, synchronize, or expose information, but it does not own Jung's business model.

---

## 7. External Providers Are Replaceable Infrastructure

External services should be isolated behind small, explicit integration boundaries.

The domain and application logic should interact with concepts such as:

`CalendarProvider`

`MessagingProvider`

rather than depending throughout the system on vendor-specific APIs.

This principle applies to current and future integrations including messaging, calendar, payments, email, storage, authentication, and AI providers where appropriate.

Provider isolation should remain pragmatic and should not produce unnecessary abstraction layers.

---

## 8. Backend Capabilities Belong to Jung, Not to a Website

Jung Sites and Jung Core are conceptually separate concerns.

Websites are interfaces into Jung's product capabilities; they are not the product itself.

Jung must be capable of serving:

- websites built and operated by Jung;
- Jung's own website;
- third-party websites owned by customers.

Jung should use its own product capabilities wherever practical.

The Jung website and demo should therefore become real consumers of `jung-api`, rather than parallel implementations of the same business logic.

Customer-facing sites should maximize reusable templates, components, and configuration so that the first implementation becomes the foundation for subsequent sites.

---

## 9. Service Boundaries Must Be Deliberate

The Jung backend is intended to evolve as a service-oriented platform rather than a single inseparable application.

Microservices are acceptable and intentional, but service boundaries must represent meaningful capabilities rather than arbitrary technical decomposition.

Do not create one service per entity, table, endpoint, or minor feature.

A service should exist because it provides a meaningful boundary in areas such as:

- responsibility;
- deployment;
- reliability;
- scaling;
- integration ownership;
- security;
- domain capability.

Avoid creating a distributed monolith in which services cannot operate or evolve without intimate knowledge of each other's internal implementation.

Major changes to service boundaries require human architectural review.

---

## 10. Design for Multi-Tenancy from the Backend

Jung should be capable of evolving into a multi-tenant platform.

The backend must avoid architectural decisions that prevent tenant-aware operation later.

Tenant isolation is a critical security property.

Once Jung manages real customer data, information belonging to one tenant must never be exposed to another tenant through normal application behavior.

Multi-tenancy does not need to be fully exposed or implemented in the frontend during the initial product validation phase.

Frontend complexity should not be introduced solely to simulate future multi-tenancy.

---

## 11. Deterministic Systems Before AI Autonomy

Critical workflows should first be understandable, deterministic, observable, and testable.

AI should initially improve:

- language understanding;
- classification;
- FAQs;
- lead qualification;
- exception handling;
- decision support.

AI should not be introduced merely to replace deterministic logic that is simpler and more reliable.

Core actions such as creating or modifying appointments should have explicit business rules even when AI participates in interpreting user intent.

---

## 12. AI Implements Within Human-Owned Architecture

AI development agents are implementation accelerators, not autonomous owners of Jung's architecture.

Agents may implement features within established architectural boundaries.

They must not independently:

- redefine major architectural patterns;
- introduce significant infrastructure;
- change service boundaries;
- create database migrations;
- perform destructive schema operations;
- change tenant isolation strategy;
- change public contracts;
- introduce major dependencies.

Database migrations require human approval **before generation**.

Database changes must be preceded by a concise brief explaining:

- what will change;
- why;
- affected data;
- migration implications;
- risks;
- rollback or recovery considerations.

Refactoring related to the current task is acceptable.

Unrelated or broad refactoring requires explicit approval.

AI must never silently replace real implementations with placeholders, fake data, unfinished stubs, or TODO-based behavior unless explicitly requested for prototyping.

---

## 13. Python and TypeScript Are Jung's Primary Languages

Jung favors technologies that the core engineering team can understand, maintain, and operate directly.

Python and TypeScript are the primary programming languages.

Other languages should only be introduced when there is a concrete technical advantage that materially outweighs the added operational and cognitive complexity.

Major language additions require an Architecture Decision Record.

Frameworks should be used aggressively where they improve productivity, but domain logic should avoid unnecessary dependence on framework-specific behavior.

---

## 14. Buy Commodity Infrastructure, Build Differentiation

Jung should invest engineering effort primarily in capabilities that differentiate the product.

Commodity capabilities should generally use mature managed services or established libraries when doing so reduces engineering and operational burden.

Build custom infrastructure only when Jung gains meaningful product, economic, performance, reliability, or control advantages from doing so.

Initial infrastructure should remain low-cost and operable by a very small engineering team.

---

## 15. Dependencies Must Earn Their Place

Prefer mature, maintained, widely understood dependencies.

Do not introduce a large dependency to solve a trivial problem.

Significant dependencies should be evaluated for:

- maintenance;
- security;
- ecosystem maturity;
- operational impact;
- lock-in;
- long-term support.

Architecturally significant dependencies require explicit review.

---

## 16. Business Behavior Matters More Than Coverage Percentage

Testing exists to protect behavior and enable confident change.

Tests should prioritize:

- domain rules;
- important application behavior;
- integration boundaries;
- security-sensitive behavior;
- tenant isolation;
- regression prevention.

Every important bug fix should include a regression test when reasonably possible.

A high test coverage percentage is not itself an engineering objective.

A change is not considered complete if relevant automated tests fail.

---

## 17. Important Operations Must Be Diagnosable

Observability is a first-class product requirement.

When an important operation fails in production, an engineer should be able to determine:

- what operation was attempted;
- where it failed;
- what component or provider was involved;
- which tenant or request context was affected where safe to record;
- what error occurred;
- what happened immediately before the failure.

Production systems should use structured, contextual logging.

Errors must not disappear silently.

Patterns such as swallowing exceptions without reporting them are prohibited unless there is a deliberate and documented reason.

Observability should be designed into features rather than added only after incidents occur.

---

## 18. Capture Product Behavior for Future Analytics

Jung should retain meaningful product and business activity required to understand how its systems are used.

The objective is not to build an analytics product prematurely.

The objective is to avoid discovering later that important historical behavior was never captured.

Meaningful events may include actions such as:

- conversations started;
- messages exchanged;
- booking intentions;
- availability queries;
- appointments created;
- appointments completed or cancelled;
- funnel transitions;
- integration failures;
- relevant customer interactions.

Instrumentation should capture useful business events with appropriate tenant and domain context.

Collection should remain intentional: Jung should collect information because it supports product operation, diagnostics, analytics, or a foreseeable business capability—not merely because data can be collected.

---

## 19. Security Basics Are Part of Definition of Done

Security is not deferred until Jung becomes large.

At minimum:

- secrets stay outside source control;
- inputs are validated at system boundaries;
- permissions follow least privilege;
- tenant isolation is protected;
- sensitive data is not unnecessarily exposed;
- authentication and authorization boundaries are explicit.

More sophisticated compliance capabilities may evolve as the product and customer base require them.

---

## 20. Database Changes Are Deliberate

Data is harder to recover than code.

Schema evolution must therefore receive a higher standard of review than ordinary application changes.

Database migrations always require human approval before generation.

Destructive changes require an explicit migration brief and human authorization.

Application code should avoid unnecessarily coupling core business rules to database-specific implementation details.

---

## 21. Prefer Direct Communication Until Asynchrony Is Needed

Do not introduce queues, event buses, or distributed event architectures by default.

Start with direct and understandable communication when it satisfies the requirement.

Introduce asynchronous processing when there is demonstrated value such as:

- retries;
- long-running work;
- reliability isolation;
- real decoupling;
- asynchronous workflows;
- independent scaling.

Infrastructure complexity must solve a real problem.

---

## 22. Optimize Performance After Measurement

Do not optimize for hypothetical scale.

Measure first.

Optimize the bottleneck that actually exists.

During Jung's early stages, repeatability of implementation and speed of product evolution are generally more valuable than extreme request throughput.

---

## 23. Prefer Reversible Decisions

Move quickly when decisions are inexpensive to reverse.

Apply deeper analysis to decisions with large migration costs, including:

- data models;
- tenant architecture;
- authentication;
- public APIs;
- infrastructure topology;
- provider lock-in;
- service boundaries.

Important decisions that are difficult to reverse should be documented with an Architecture Decision Record.

---

## 24. Changes Should Be Small and Deployable

Prefer small, coherent changes over large batches.

A task should produce the smallest complete change that satisfies the requirement.

Do not modify unrelated areas simply because an opportunity to clean them up was discovered.

The main development branch should remain deployable.

Changes should be easy to review, test, understand, and reverse.

---

## 25. Developer Experience Is a First-Class Requirement

Developer experience is fundamental to Jung's ability to scale.

The repository and platform should be designed so that an engineer can:

- understand the major architecture quickly;
- identify which component owns a capability;
- find where a feature is implemented;
- run the project locally with minimal setup;
- run relevant tests easily;
- understand failures from logs;
- change one capability without understanding the entire platform;
- understand architectural decisions and their reasoning;
- safely use AI agents without losing architectural consistency.

Complex setup, unclear ownership, hidden conventions, and unnecessary cognitive load are engineering problems.

As Jung grows, the platform must scale not only in traffic and customers, but in the ability of humans and AI agents to safely understand and modify it.

---

# Governing Principle

When several principles compete, prefer the solution that allows Jung to:

**learn quickly, deliver real customer value, remain understandable, preserve critical boundaries, and evolve without unnecessary rewrites.**

AI may accelerate implementation.

Architecture remains deliberate.

Data remains protected.

Failures remain visible.

The codebase must remain understandable.
