# Feature Development Skill

## Purpose

This skill defines the operational workflow for implementing a single feature from definition to completion.

It works together with:

* `AGENTS.md`
* `PROJECT_SPEC.md`
* `ARCHITECTURE.md`
* `DESIGN_SYSTEM.md`
* `CODING_RULES.md`
* `DATABASE_RULES.md`
* `API_RULES.md`
* `SECURITY_RULES.md`
* `TESTING_RULES.md`
* `UX_RULES.md`
* `ROADMAP.md`
* `skills/design-workflow/SKILL.md`

These files define the requirements and rules.
This skill defines the execution sequence.

---

## 1. Feature Boundary

Every implementation task must begin with a clearly defined feature.

Define:

* Feature name
* User goal
* Scope
* Expected behavior
* Required screens/states
* Required data
* Dependencies
* Out-of-scope items

Do not expand the feature into unrelated work.

---

## 2. Inspect Before Implementing

Before writing code, inspect the existing project.

Check:

* Relevant routes/pages
* Existing components
* Existing feature modules
* Existing API endpoints
* Existing database models/data structures
* Existing authentication/authorization
* Existing utilities and services
* Existing tests
* Existing design references

Reuse existing functionality whenever appropriate.

---

## 3. Resolve the Feature Design

Use:

`skills/design-workflow/SKILL.md`

to process available design references.

Confirm:

* screen structure
* interactions
* responsive behavior
* required states
* reusable components
* missing design decisions

Do not begin implementation while fundamental behavior is still undefined.

---

## 4. Determine Technical Scope

Classify the feature:

### Frontend Only

Use when the feature requires no persistent or server-side behavior.

### Full-Stack

Use when the feature requires:

```text
Frontend
→ API
→ Backend Logic
→ Database
```

### External Integration

Use when the feature depends on:

```text
Frontend
→ API
→ Backend
→ External Service
```

Do not create unnecessary backend or database layers for genuinely frontend-only functionality.

---

## 5. Create the Implementation Plan

Before coding, create a concise plan covering:

```text
Feature
├── UI
├── Components
├── State
├── API
├── Backend
├── Database
├── External Services
├── Security
└── Tests
```

Only include sections actually required by the feature.

---

## 6. Implement in Dependency Order

Prefer this sequence:

```text
Types / Contracts
→ Data Model
→ Backend Logic
→ API
→ Frontend Data Layer
→ Components
→ Page / Route
→ Integration
```

Adjust the order when the architecture requires it.

Do not build isolated UI that later needs to be rewritten because its data contract was unknown.

---

## 7. Keep Boundaries Explicit

Each layer should have a clear responsibility.

```text
UI
↓
Feature Logic
↓
API Contract
↓
Backend / Use Case
↓
Data Access
↓
Database / External Service
```

Avoid:

* database logic inside UI components
* business rules inside presentation components
* direct database access from unrelated layers
* duplicated business logic
* bypassing established service boundaries

---

## 8. Implement Real Data Flow

If the feature requires persistence:

```text
User Action
→ Frontend
→ API
→ Server Validation
→ Authorization
→ Business Logic
→ Database
→ Response
→ UI Update
```

Every required connection must be real.

Do not replace missing implementation with:

* hardcoded values
* fake API responses
* local-only persistence
* temporary in-memory storage
* simulated success messages

unless explicitly defined as development-only behavior.

---

## 9. Handle All Required States

For each user-facing operation, identify the applicable states:

```text
Initial
Loading
Success
Empty
Validation Error
Permission Error
Not Found
Server Error
Network Failure
```

Implement only the states relevant to the feature, but do not leave important states undefined.

---

## 10. Integrate Before Declaring Complete

A feature is not complete when its individual files compile.

Verify the complete path:

```text
UI
→ State
→ API
→ Backend
→ Database / External Service
→ Response
→ UI
```

For frontend-only features, verify the complete equivalent interaction flow.

---

## 11. Test the Feature

Run the applicable checks defined by `TESTING_RULES.md`.

At minimum, verify:

* expected behavior
* failure behavior
* validation
* authorization where applicable
* data persistence where applicable
* responsive behavior
* relevant regression paths

Fix failures before moving to the next feature.

---

## 12. Feature Audit

Before completion, review:

```text
[ ] Scope respected
[ ] Existing code reused where appropriate
[ ] Design behavior implemented
[ ] Required states implemented
[ ] Data flow is real
[ ] API integration complete where required
[ ] Database integration complete where required
[ ] Authorization enforced where required
[ ] Tests pass
[ ] No unrelated regressions
[ ] Desktop/mobile behavior reviewed
```

---

## 13. Completion Gate

Only mark the feature as complete when:

```text
Defined
→ Designed
→ Planned
→ Implemented
→ Integrated
→ Tested
→ Audited
```

A partially implemented feature must remain explicitly incomplete.

Do not report a feature as complete because:

* the page exists
* the UI looks correct
* the API exists
* the database exists
* the build passes

All required layers must work together.

---

## 14. Change Control

During implementation:

* Keep changes focused on the current feature.
* Avoid unrelated refactoring.
* Do not silently change established architecture.
* Do not introduce new patterns when an existing pattern is sufficient.
* If a broader architectural change is genuinely required, stop and document the reason before expanding scope.

---

## 15. Next Feature Rule

After a feature passes its completion gate:

```text
Feature Complete
→ Record Result
→ Identify Dependencies
→ Start Next Feature
```

Do not begin the next feature while the current feature has unresolved critical blockers.

---

## Operating Principle

> **Build one complete feature at a time. A feature is finished only when its required design, code, data flow, integration, and verification work together.**
