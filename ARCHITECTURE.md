# ARCHITECTURE

## 1. Purpose

This document defines the baseline architecture principles for projects using this development system.

Project-specific technology choices MUST be defined in `PROJECT_SPEC.md`.

---

## 2. Architecture Principles

The architecture MUST prioritize:

* Clear separation of responsibilities
* Explicit boundaries
* Maintainability
* Testability
* Security
* Scalability where required
* Simplicity
* Observable behavior
* Replaceable components where practical

Do not introduce architectural complexity without a requirement.

---

## 3. Application Layers

A full-stack web application SHOULD separate the following responsibilities:

```text
Presentation
    ↓
Application / Use Cases
    ↓
Domain / Business Rules
    ↓
Infrastructure
    ↓
Database / External Services
```

The exact implementation MAY differ depending on the technology stack.

The important requirement is that responsibilities and dependencies remain explicit.

---

## 4. Frontend Architecture

Frontend applications SHOULD be organized around:

```text
Pages / Routes
      ↓
Feature Components
      ↓
Shared Components
      ↓
UI Primitives
```

Business logic SHOULD NOT be unnecessarily embedded inside presentation components.

Reusable UI should be implemented as reusable components.

React's official guidance treats components as reusable UI building blocks and recommends decomposing interfaces into component hierarchies.

---

## 5. Component Architecture

Components SHOULD have clear responsibilities.

A component SHOULD:

* Receive required data through defined interfaces.
* Manage only the state it needs.
* Avoid unrelated business logic.
* Be composable.
* Be reusable when the same behavior appears elsewhere.

Avoid:

* Giant page components.
* Deeply coupled components.
* Duplicate UI implementations.
* Components that contain unrelated business domains.

React recommends thinking about UI as a component hierarchy and separating concerns within that hierarchy.

---

## 6. State Architecture

State MUST have a clear owner.

Prefer:

```text
Local state
    ↓
Shared feature state
    ↓
Application state
```

only when the scope requires it.

Do not make state global by default.

For each state value, determine:

* Who owns it?
* Who reads it?
* Who changes it?
* Does it need persistence?
* Is it server state or UI state?

React's guidance recommends identifying the minimal state and locating it in the closest appropriate common parent.

---

## 7. Data Flow

Data flow MUST remain predictable.

The frontend SHOULD follow a clear directional model:

```text
User Action
    ↓
UI Event
    ↓
State / Application Logic
    ↓
API
    ↓
Backend
    ↓
Persistence
    ↓
Response
    ↓
State Update
    ↓
UI
```

Avoid multiple independent sources of truth for the same data.

---

## 8. Backend Architecture

Backend applications SHOULD separate:

```text
HTTP / Transport
      ↓
Application Logic
      ↓
Domain Logic
      ↓
Infrastructure
      ↓
Persistence / External Services
```

HTTP handlers/controllers SHOULD NOT contain the entire business logic of the application.

Business rules SHOULD be independently testable where practical.

---

## 9. API Boundary

The API is an explicit boundary between clients and backend functionality.

API contracts MUST define:

* Endpoint
* HTTP method
* Request
* Response
* Authentication
* Authorization
* Validation
* Error behavior

Frontend code MUST NOT directly access protected database infrastructure.

All authorization decisions MUST be enforced on the server.

---

## 10. Database Boundary

The database is a persistence boundary.

Application code SHOULD access persistent data through a defined infrastructure/data-access layer.

Do not spread database queries throughout unrelated UI or business modules.

Database-specific implementation details SHOULD remain isolated from higher-level business logic where practical.

---

## 11. Stateless Application Processes

Application processes SHOULD NOT depend on local process memory or local filesystem state for required persistent application data.

Persistent data belongs in an appropriate backing service.

This follows the Twelve-Factor principle that application processes should be stateless and persistent state should be stored in backing services.

Caches MAY exist, but the application MUST NOT assume cached process state is permanently available.

---

## 12. TypeScript Architecture

When TypeScript is used:

* Modules SHOULD have clear boundaries.
* Shared types SHOULD have a defined ownership location.
* API/domain types SHOULD not be duplicated unnecessarily.
* Type dependencies SHOULD remain intentional.

For sufficiently large TypeScript systems, Project References MAY be used to separate logical projects and improve build organization and type-checking performance.

---

## 13. Dependency Direction

Dependencies SHOULD move toward stable abstractions and clearly defined boundaries.

Avoid circular dependencies.

Avoid allowing low-level infrastructure concerns to leak into unrelated presentation code.

Example:

```text
UI
 ↓
Application
 ↓
Domain
 ↓
Infrastructure
```

Avoid:

```text
Database
 ↓
UI
```

or direct database access from presentation components.

---

## 14. Feature Organization

When the application contains multiple business features, feature boundaries SHOULD be explicit.

Example:

```text
features/
├── auth/
├── users/
├── products/
├── orders/
└── payments/
```

Each feature MAY contain its own:

```text
components/
hooks/
services/
types/
validation/
tests/
```

Shared functionality belongs in shared modules only when it is genuinely shared.

---

## 15. Shared Code

Shared code SHOULD be created only when multiple parts of the application have a real common responsibility.

Avoid creating a generic `utils` or `helpers` module containing unrelated functionality.

Shared modules MUST have clear ownership and purpose.

---

## 16. External Services

External services MUST be accessed through controlled integration boundaries.

Examples:

```text
Payment Provider
Email Provider
Storage Provider
Authentication Provider
Analytics Provider
```

Application code SHOULD NOT spread provider-specific implementation throughout unrelated modules.

Provider-specific logic SHOULD be isolated where practical.

---

## 17. Security Architecture

Security MUST be part of architectural design.

Architecture MUST consider:

* Authentication
* Authorization
* Input validation
* Data protection
* Secret management
* Trust boundaries
* External integrations
* Failure behavior
* Logging and monitoring

Security requirements are defined in `SECURITY_RULES.md`.

OWASP's secure engineering guidance emphasizes integrating security into software engineering and architecture rather than treating it only as a final-stage activity.

---

## 18. Scalability

Do not introduce distributed architecture only because it is considered more scalable.

Choose the simplest architecture that satisfies current and reasonably foreseeable requirements.

A modular monolith MAY be preferable to microservices when independent deployment or scaling is not actually required.

Architecture decisions MUST be based on project requirements.

---

## 19. Testing Boundaries

Architecture SHOULD make important behavior testable independently.

Examples:

```text
UI tests
Application tests
Domain tests
API tests
Integration tests
End-to-end tests
```

External systems SHOULD be replaceable with controlled test doubles where appropriate.

---

## 20. Observability

Production systems SHOULD provide appropriate:

* Structured logging
* Error reporting
* Health checks
* Metrics
* Request tracing where justified

Sensitive information MUST NOT be written to logs.

Observability requirements depend on the project's production environment.

---

## 21. Architecture Changes

Architecture MUST NOT be changed casually.

Before a significant architectural change:

1. Identify the problem.
2. Document the current behavior.
3. Explain why the existing architecture is insufficient.
4. Evaluate alternatives.
5. Identify affected modules.
6. Identify migration requirements.
7. Update architecture documentation.
8. Verify affected functionality.

---

## 22. Architecture Decision Records

Significant architectural decisions SHOULD be documented as Architecture Decision Records (ADRs).

Recommended structure:

```text
decisions/
├── ADR-001-example.md
├── ADR-002-example.md
└── ADR-003-example.md
```

Each ADR SHOULD describe:

* Context
* Decision
* Alternatives
* Consequences
* Status

---

## 23. Technology Independence

This architecture document defines principles, not a mandatory technology stack.

A project MAY use:

* React
* Vue
* Angular
* Next.js
* Express
* Node.js
* PostgreSQL
* Firestore
* Other appropriate technologies

The chosen stack MUST be explicitly defined by the project's `PROJECT_SPEC.md` and implementation plan.

---

## 24. Architecture Completion Criteria

Before architecture is considered ready for implementation:

* Major application boundaries are defined.
* Frontend architecture is defined.
* Backend architecture is defined.
* API boundary is defined.
* Database boundary is defined.
* Authentication boundary is defined where required.
* External services are identified.
* Data flow is understood.
* Security boundaries are identified.
* Testing boundaries are identified.
* Major architectural decisions are documented.

Architecture MUST be understandable before large-scale implementation begins.
