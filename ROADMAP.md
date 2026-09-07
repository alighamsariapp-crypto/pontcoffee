# ROADMAP

## 1. PURPOSE

This roadmap defines the mandatory development lifecycle for the project.

The project MUST NOT be designed, implemented, or modified as one large undivided task.

Development MUST be organized as:

```text
PROJECT
↓
PHASE
↓
FEATURE
↓
DESIGN REFERENCE
↓
IMPLEMENTATION
↓
INTEGRATION
↓
TESTING
↓
AUDIT
↓
NEXT FEATURE
```

The purpose is to prevent large uncontrolled AI changes and maintain consistency, quality, and traceability.

---

# 2. MASTER DEVELOPMENT MODEL

The system follows:

```text
Specification
↓
Design
↓
Technical Planning
↓
Feature-by-Feature Implementation
↓
Integration
↓
Testing
↓
Security / UX Audit
↓
Quality Gate
↓
Next Feature
```

AI MUST NOT attempt to build the entire application in one operation.

---

# 3. PHASES

```text
PHASE 00 — Discovery & Audit

PHASE 01 — Project Specification

PHASE 02 — UX / UI Design

PHASE 03 — Architecture & Technical Planning

PHASE 04 — Feature Implementation

PHASE 05 — Integration & Completion

PHASE 06 — Testing & Security

PHASE 07 — Final Audit & Quality Gate
```

---

# 4. PHASE 00 — DISCOVERY & AUDIT

## Goal

Understand the project before making architectural or implementation decisions.

AI MUST inspect:

* repository
* existing code
* documentation
* architecture
* frontend
* backend
* database
* APIs
* authentication
* authorization
* integrations
* UX
* responsive behavior
* mobile behavior
* technical debt

AI MUST identify:

* missing functionality
* incomplete functionality
* broken functionality
* duplicated logic
* architecture problems
* database problems
* API problems
* security problems
* UX problems
* mobile problems

## Output

```text
phases/PHASE_00_AUDIT.md
```

## Gate

The existing system is sufficiently understood.

No major unknown blocker remains.

---

# 5. PHASE 01 — PROJECT SPECIFICATION

## Goal

Convert the project requirements into an implementation-ready specification.

Define:

* product goals
* target users
* user roles
* permissions
* features
* user flows
* business rules
* entities
* pages
* admin requirements
* integrations
* constraints
* non-functional requirements

Every major requirement SHOULD be:

```text
Clear
Testable
Unambiguous
```

## Output

```text
PROJECT_SPEC.md
```

## Gate

The product scope and business behavior are sufficiently defined.

---

# 6. PHASE 02 — UX / UI DESIGN

## Goal

Design the product before implementation.

Define:

* information architecture
* navigation
* page hierarchy
* user flows
* desktop UX
* mobile UX
* tablet behavior
* admin UX
* responsive behavior
* components
* design tokens
* interaction patterns

The following are mandatory:

```text
DESIGN_SYSTEM.md
UX_RULES.md
```

---

# 7. DESIGN REFERENCE MODEL

Design references are GUIDANCE, not a hard lock.

A Feature MAY have:

```text
Desktop Design Reference
Mobile Design Reference
Tablet Design Reference
```

Any combination is valid.

Examples:

```text
Desktop + Mobile
Desktop only
Mobile only
No reference
```

---

# 8. DESIGN REFERENCE PRIORITY

When implementing a Feature, AI SHOULD use this priority:

```text
1. PROJECT_SPEC.md
2. DESIGN_SYSTEM.md
3. UX_RULES.md
4. Feature Design Reference
5. Existing Project Design Language
6. Reasonable AI Completion
```

The Design Reference MUST NOT override:

* business requirements
* security rules
* accessibility requirements
* architectural constraints
* established design-system rules

---

# 9. MISSING DESIGN REFERENCE

A missing screenshot MUST NOT automatically block development.

If part of a Feature has no Design Reference, AI SHOULD complete it using:

```text
PROJECT_SPEC.md
+
DESIGN_SYSTEM.md
+
UX_RULES.md
+
Existing Project UI
+
Established visual language
```

The result MUST feel like part of the same product.

---

# 10. DESIGN REFERENCE INTERPRETATION

AI MUST analyze a provided design reference before implementation.

Analyze:

* layout
* spacing
* typography
* colors
* hierarchy
* components
* interactions
* states
* responsive behavior
* content density
* navigation
* actions

The goal is to reproduce the intended UX and visual language, not merely copy visible pixels.

---

# 11. MOBILE DESIGN RULE

If a Desktop Reference exists but a Mobile Reference does not exist, AI MUST design the Mobile experience itself.

It MUST follow:

```text
DESIGN_SYSTEM.md
+
UX_RULES.md
+
Desktop Design Language
+
Project UX
```

Mobile MUST NOT simply be a scaled-down desktop.

---

# 12. PHASE 03 — ARCHITECTURE & TECHNICAL PLANNING

## Goal

Define the technical foundation before large-scale implementation.

Define:

* frontend architecture
* backend architecture
* database model
* API contracts
* authentication
* authorization
* data ownership
* validation
* security boundaries
* external services
* error handling
* integration boundaries

Use:

```text
ARCHITECTURE.md
DATABASE_RULES.md
API_RULES.md
SECURITY_RULES.md
CODING_RULES.md
```

## Gate

Major technical decisions are resolved before implementation.

---

# 13. PHASE 04 — FEATURE IMPLEMENTATION

## Goal

Implement the application Feature-by-Feature.

This phase MUST NOT be executed as:

```text
"Build the entire application."
```

Instead:

```text
Feature 01
↓
Complete
↓
Audit
↓
Feature 02
↓
Complete
↓
Audit
```

---

# 14. FEATURE BOUNDARY

Every Feature MUST have a defined boundary.

Example:

```text
Cart Feature
```

includes only the functionality necessary for the Cart.

It MUST NOT unexpectedly modify:

```text
Checkout
Profile
Orders
Admin
Authentication
```

unless the dependency is explicitly required and documented.

---

# 15. FEATURE IMPLEMENTATION FLOW

Every Feature SHOULD follow:

```text
Feature Definition
↓
Design Reference Review
↓
UX Review
↓
Component Mapping
↓
Technical Plan
↓
Frontend
↓
Backend
↓
API
↓
Database
↓
Integration
↓
Testing
↓
Audit
↓
Feature Complete
```

---

# 16. FEATURE FRONTEND IMPLEMENTATION

For every Feature AI MUST:

* reuse existing components
* reuse existing tokens
* maintain visual consistency
* maintain RTL
* implement responsive behavior
* implement loading states
* implement error states
* implement empty states
* implement required accessibility behavior

AI MUST NOT create duplicate components when an existing component can be reused or extended.

---

# 17. FEATURE BACKEND IMPLEMENTATION

When a Feature requires backend functionality, AI MUST implement the complete backend path.

```text
Frontend
↓
API
↓
Validation
↓
Authorization
↓
Business Logic
↓
Database
```

UI-only implementation is NOT considered Feature completion when backend behavior is required.

---

# 18. FEATURE DATABASE IMPLEMENTATION

When persistent data is required:

```text
Feature
↓
Data Model
↓
Database
↓
API
↓
Frontend
```

Production functionality MUST NOT depend on:

```text
mock data
fake persistence
in-memory arrays
hardcoded production data
```

---

# 19. FEATURE INTEGRATION

A Feature is NOT complete when its screen merely renders.

It is complete when the required system layers work together:

```text
UI
+
API
+
Backend
+
Database
+
Business Rules
```

---

# 20. FEATURE CHANGE CONTROL

While implementing a Feature, AI MUST NOT make unrelated large-scale changes.

If an architectural or cross-feature change becomes necessary:

```text
Identify
↓
Explain
↓
Assess Impact
↓
Approve / Update Plan
↓
Implement
```

Do not silently expand the Feature scope.

---

# 21. FEATURE QUALITY GATE

Every Feature MUST pass its own Quality Gate before the next Feature begins.

Check:

```text
Functionality
UX
UI
Responsive
Mobile
RTL
Accessibility
API
Database
Security
Tests
```

A failed Feature Gate means:

```text
STOP
↓
FIX
↓
TEST
↓
RE-AUDIT
```

---

# 22. PHASE 05 — INTEGRATION & COMPLETION

## Goal

Verify that completed Features work together.

Verify:

```text
Frontend
↓
API
↓
Backend
↓
Database
↓
External Services
```

Test cross-feature flows such as:

```text
Product
↓
Cart
↓
Checkout
↓
Order
```

or equivalent project-specific flows.

## Gate

Cross-feature behavior works correctly.

---

# 23. PHASE 06 — TESTING & SECURITY

Use:

```text
TESTING_RULES.md
SECURITY_RULES.md
```

Test:

* Unit
* Integration
* API
* Contract
* E2E
* Authentication
* Authorization
* Database isolation
* Security
* Accessibility
* Responsive behavior
* Mobile behavior
* RTL
* Error handling
* Loading states
* Empty states
* Concurrency
* Idempotency

Minimum responsive baseline:

```text
320px
360px
375px
390px
414px
768px
1024px
1280px+
```

---

# 24. PHASE 07 — FINAL AUDIT & QUALITY GATE

The final audit MUST review:

```text
Specification
Architecture
UX
UI
Mobile
Admin
Frontend
Backend
Database
API
Security
Accessibility
Testing
Performance
```

The final audit MUST verify that no critical blocker remains.

---

# 25. BLOCKER POLICY

Any of the following MAY block progression:

```text
Broken core workflow
Missing database persistence
Fake production functionality
Broken API integration
Authorization vulnerability
Critical security issue
Mobile page overflow
Broken Admin Table
Unusable mobile workflow
Major accessibility failure
```

A Critical blocker MUST stop the affected phase or Feature.

---

# 26. MOBILE QUALITY GATE

Every major Feature MUST be reviewed for mobile behavior.

Particular attention MUST be given to:

```text
navigation
forms
tables
filters
toolbars
drawers
modals
cards
actions
sticky controls
```

The entire page MUST NOT horizontally scroll because of an individual component.

---

# 27. ADMIN TABLE QUALITY GATE

Every Admin Feature containing tables MUST define a mobile presentation.

Acceptable patterns include:

```text
Table → Mobile Cards
Table → Expandable Rows
Table → Essential Columns + Details
Table → Isolated Table Container Scroll
```

Unacceptable:

```text
Desktop Table
↓
Shrink
↓
Entire Mobile Page Horizontally Scrolls
```

---

# 28. NO FAKE RESPONSIVE FIXES

The following MUST NOT be used to hide responsive problems:

```text
overflow-x: hidden
```

on the page/body when used only to conceal overflow.

Also prohibited:

```text
tiny text
compressed unreadable columns
fixed desktop widths
clipped controls
hidden essential information
page-level horizontal scrolling
```

---

# 29. PHASE REPORTING

At the end of every Phase, report:

```text
Phase:
Status:

Completed:
- ...

Not Completed:
- ...

Blockers:
- ...

Files Changed:
- ...

Tests:
- ...

Quality Gate:
PASS / FAIL

Next Phase:
...
```

For Feature implementation, also report:

```text
Feature:
Design Reference:
Frontend:
Backend:
API:
Database:
Integration:
Tests:
Audit:
Status:
```

Keep reports concise.

---

# 30. NO MASS GENERATION

AI MUST NOT perform uncontrolled mass implementation such as:

```text
"Build all pages."
"Build the entire frontend."
"Build the whole admin panel."
"Finish the whole application."
```

unless the user explicitly requests a broad operation AND the work has already been decomposed into approved Features.

Even then, implementation SHOULD remain internally Feature-by-Feature.

---

# 31. FEATURE QUEUE

A Phase MAY contain multiple Features.

Example:

```text
PHASE 04

Feature 01 — Header
Feature 02 — Home
Feature 03 — Product Listing
Feature 04 — Product Detail
Feature 05 — Cart
Feature 06 — Checkout
Feature 07 — Profile
Feature 08 — Orders
```

Each Feature is independently implemented and verified.

---

# 32. FEATURE DEPENDENCIES

Features MAY depend on other Features.

Example:

```text
Product
↓
Cart
↓
Checkout
↓
Order
```

AI MUST respect dependencies.

A dependent Feature MUST NOT be implemented against imaginary or fake functionality.

---

# 33. DESIGN CONSISTENCY ACROSS FEATURES

Feature-by-Feature development MUST NOT create unrelated visual systems.

Every new Feature MUST inherit:

```text
Colors
Typography
Spacing
Radius
Shadows
Components
Interaction Patterns
RTL Rules
Responsive Rules
```

from the project's existing system.

---

# 34. WHEN TO ASK FOR DESIGN

AI SHOULD proceed without asking for a screenshot when:

* the design system is sufficient
* the existing UI provides enough reference
* the missing detail is minor
* the decision is predictable and low-risk

AI SHOULD request clarification when:

* a missing design decision materially changes UX
* multiple valid patterns would produce significantly different behavior
* the requirement is ambiguous
* business behavior is unclear

Do not block progress over minor visual details.

---

# 35. FLEXIBLE DESIGN PRINCIPLE

The system balances:

```text
Design Accuracy
+
Design Consistency
+
AI Completion
+
User Control
```

The goal is NOT to force the AI to copy screenshots blindly.

The goal is to make the AI understand the intended product and complete missing details consistently.

---

# 36. PROJECT DEFINITION OF DONE

The project is complete only when:

* Specification is complete
* UX/UI is complete
* Architecture is validated
* Features are implemented
* Frontend is connected
* Backend is connected
* Database is persistent
* API contracts work
* Authentication works
* Authorization works
* Business rules work
* Integrations work
* Mobile UX is intentionally designed
* Admin mobile UX works
* Tables have mobile strategies
* RTL works
* Accessibility baseline passes
* Tests pass
* Security audit passes
* Final UX audit passes
* Production build succeeds

Only then:

```text
PROJECT STATUS = COMPLETE
```

---

# 37. MASTER RULE

The AI must build the project progressively.

```text
DO NOT:
Project → Build Everything

DO:
Project
 ↓
Phase
 ↓
Feature
 ↓
Design Reference
 ↓
Implementation
 ↓
Integration
 ↓
Testing
 ↓
Audit
 ↓
Quality Gate
 ↓
Next Feature
```

Design references guide the implementation.

They do not lock the AI into incomplete screenshots.

The AI may intelligently complete missing parts using the project's specification, design system, UX rules, and established visual language.

The objective is:

```text
Controlled Development
+
Consistent Design
+
Complete Full-Stack Functionality
+
High-Quality Mobile UX
+
Verified Production-Ready Software
```
