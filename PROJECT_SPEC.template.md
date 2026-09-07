# Project Specification

## Document Purpose

This document is the project-specific source of truth for product requirements, scope, users, journeys, features, business goals, constraints, and success criteria.

This file MUST be completed before implementation begins.

It defines **what the product must achieve**.

It does not replace:

* `ARCHITECTURE.md`
* `DESIGN_SYSTEM.md`
* `CODING_RULES.md`
* `DATABASE_RULES.md`
* `API_RULES.md`
* `SECURITY_RULES.md`
* `TESTING_RULES.md`
* `UX_RULES.md`
* other governing project Rules

Those documents define **how the product must be built**.

---

# 1. Project Identity

## Project Name

`[PROJECT_NAME]`

## Project Type

`[E-commerce / SaaS / Marketplace / CMS / Dashboard / Service / Other]`

## Version

`[VERSION]`

## Status

`[Discovery / Specification / Design / Development / Production]`

## Owner

`[OWNER_OR_TEAM]`

---

# 2. Product Overview

## Product Summary

Describe the product in a few clear sentences.

`[PRODUCT_SUMMARY]`

## Primary Goal

What is the main outcome this product must achieve?

`[PRIMARY_GOAL]`

## Product Context

Why is this product being built?

`[PRODUCT_CONTEXT]`

---

# 3. Problem Definition

## Problem

What specific problem does the product solve?

`[PROBLEM]`

## Current Situation

How is this problem currently handled?

`[CURRENT_SITUATION]`

## Why It Matters

Why should this problem be solved?

`[WHY_IT_MATTERS]`

## Evidence / Assumptions

List known evidence and assumptions separately.

### Evidence

* `[EVIDENCE]`

### Assumptions

* `[ASSUMPTION]`

Unverified assumptions MUST NOT be treated as established facts.

---

# 4. Target Users

## Primary Users

| User Type | Description     | Main Need | Priority            |
| --------- | --------------- | --------- | ------------------- |
| `[USER]`  | `[DESCRIPTION]` | `[NEED]`  | `[HIGH/MEDIUM/LOW]` |

## Secondary Users

| User Type | Description     | Main Need | Priority            |
| --------- | --------------- | --------- | ------------------- |
| `[USER]`  | `[DESCRIPTION]` | `[NEED]`  | `[HIGH/MEDIUM/LOW]` |

## User Context

Define relevant:

* device usage
* technical ability
* accessibility needs
* geographic context
* language
* business context
* usage frequency

Only include context that materially affects product decisions.

---

# 5. Value Proposition

## Core Value

Why should the target user use this product?

`[VALUE_PROPOSITION]`

## Differentiators

What makes the product meaningfully different?

* `[DIFFERENTIATOR]`

## User Outcome

What should become easier, faster, safer, cheaper, or better for the user?

`[USER_OUTCOME]`

---

# 6. Business Goals

Define measurable business or organizational goals.

| Goal     | Metric     | Target     | Timeframe     |
| -------- | ---------- | ---------- | ------------- |
| `[GOAL]` | `[METRIC]` | `[TARGET]` | `[TIMEFRAME]` |

If the project has no business objective, explicitly state:

`No business objective defined.`

---

# 7. Product Scope

## MVP / V1

Define only the functionality required for the first meaningful release.

### In Scope

* `[FEATURE / CAPABILITY]`

### Out of Scope

* `[FEATURE / CAPABILITY]`

Out-of-scope functionality MUST NOT be implemented unless scope is formally changed.

---

# 8. Feature Map

List the product features before implementation.

| ID    | Feature     | User     | Priority     | Backend Required | Status      |
| ----- | ----------- | -------- | ------------ | ---------------- | ----------- |
| F-001 | `[FEATURE]` | `[USER]` | `[P0/P1/P2]` | `[YES/NO]`       | `[PLANNED]` |

### Priority

```text
P0 = Required for core product operation
P1 = Important for V1
P2 = Useful but not required for V1
```

Features MUST be implemented individually through the project's Feature Development workflow.

---

# 9. Core User Journeys

Define the most important user journeys.

## Journey J-001

### Name

`[JOURNEY_NAME]`

### User

`[USER_TYPE]`

### Goal

`[USER_GOAL]`

### Flow

```text
Entry
 ↓
Step 1
 ↓
Step 2
 ↓
Step 3
 ↓
Successful Outcome
```

### Failure / Alternative Paths

* `[ALTERNATIVE_PATH]`
* `[ERROR_PATH]`

### Success Condition

`[SUCCESS_CONDITION]`

Repeat for every critical journey.

---

# 10. Product Requirements

## Functional Requirements

| ID     | Requirement     | Priority     | Acceptance Condition |
| ------ | --------------- | ------------ | -------------------- |
| FR-001 | `[REQUIREMENT]` | `[P0/P1/P2]` | `[CONDITION]`        |

## Non-Functional Requirements

Define relevant requirements for:

* performance
* security
* accessibility
* reliability
* scalability
* privacy
* SEO
* localization
* observability
* deployment

| ID      | Requirement     | Priority     | Acceptance Condition |
| ------- | --------------- | ------------ | -------------------- |
| NFR-001 | `[REQUIREMENT]` | `[P0/P1/P2]` | `[CONDITION]`        |

---

# 11. UX Requirements

Define product-specific UX requirements that go beyond the global `UX_RULES.md`.

## Navigation

`[NAVIGATION_REQUIREMENTS]`

## Mobile

`[MOBILE_REQUIREMENTS]`

## Desktop

`[DESKTOP_REQUIREMENTS]`

## RTL / Localization

`[RTL_LOCALIZATION_REQUIREMENTS]`

## Accessibility

`[PROJECT_SPECIFIC_ACCESSIBILITY_REQUIREMENTS]`

Global UX and accessibility rules remain governed by `UX_RULES.md`.

---

# 12. Design Requirements

## Design References

List available design references.

| Feature     | Desktop | Mobile  | Tablet  | Source                        |
| ----------- | ------- | ------- | ------- | ----------------------------- |
| `[FEATURE]` | `[REF]` | `[REF]` | `[REF]` | `[Stitch / Existing / Other]` |

Design references are guidance.

They MUST be interpreted together with:

1. `PROJECT_SPEC.md`
2. `DESIGN_SYSTEM.md`
3. `UX_RULES.md`
4. Feature requirements

Missing design references MUST NOT block reasonable completion when the governing design system provides enough information.

---

# 13. Content Requirements

Define project-specific content requirements.

## Required Content

* `[CONTENT]`

## Content Sources

`[CMS / Database / Static / External / Other]`

## Content Status

```text
Draft
Approved
Production
```

Placeholder content MUST NOT be treated as production content unless explicitly approved.

---

# 14. SEO Requirements

Define SEO requirements for public/indexable routes.

## Indexable Routes

* `[ROUTE]`

## Non-Indexable Routes

* `[ROUTE]`

## URL Strategy

`[URL_STRATEGY]`

## Localization

`[LANGUAGE / REGION STRATEGY]`

## Structured Data

`[REQUIRED_SCHEMA_TYPES]`

Project-specific SEO requirements supplement `SEO_RULES.md`.

---

# 15. Data Requirements

## Core Entities

| Entity     | Purpose     | Owner     | Sensitive  | Notes     |
| ---------- | ----------- | --------- | ---------- | --------- |
| `[ENTITY]` | `[PURPOSE]` | `[OWNER]` | `[YES/NO]` | `[NOTES]` |

## Data Sources

* `[DATABASE]`
* `[EXTERNAL_SERVICE]`

## Data Retention

`[RETENTION_REQUIREMENTS]`

Database architecture and implementation remain governed by `DATABASE_RULES.md`.

---

# 16. Integrations

List required external systems.

| System      | Purpose     | Direction       | Required   | Status      |
| ----------- | ----------- | --------------- | ---------- | ----------- |
| `[SERVICE]` | `[PURPOSE]` | `[IN/OUT/BOTH]` | `[YES/NO]` | `[PLANNED]` |

Examples:

* Firebase
* Payment provider
* Email provider
* Analytics
* AI provider
* Storage
* Search service

---

# 17. Authentication & Roles

## Authentication

`[AUTHENTICATION_REQUIREMENTS]`

## Roles

| Role     | Purpose     |
| -------- | ----------- |
| `[ROLE]` | `[PURPOSE]` |

## Permissions

Define project-specific permissions only.

Authorization implementation remains governed by `SECURITY_RULES.md`.

---

# 18. AI Features

If the product uses AI, define:

## AI Capabilities

* `[AI_FEATURE]`

## Model / Provider

`[MODEL_PROVIDER]`

## User Input

`[INPUT_DESCRIPTION]`

## Expected Output

`[OUTPUT_DESCRIPTION]`

## Human Approval

`[REQUIRED / NOT_REQUIRED]`

## Failure Behavior

`[FAILURE_BEHAVIOR]`

AI functionality remains subject to `AI_SECURITY_RULES.md`.

---

# 19. Performance Requirements

Define measurable project-specific requirements where needed.

| Area      | Requirement     | Target     |
| --------- | --------------- | ---------- |
| Page Load | `[REQUIREMENT]` | `[TARGET]` |
| API       | `[REQUIREMENT]` | `[TARGET]` |
| Mobile    | `[REQUIREMENT]` | `[TARGET]` |

General performance rules remain governed by `PERFORMANCE_RULES.md`.

---

# 20. Privacy & Legal Requirements

Define applicable requirements.

* `[Privacy Requirement]`
* `[Consent Requirement]`
* `[Cookie Requirement]`
* `[Terms Requirement]`
* `[Refund Requirement]`

Legal text MUST receive appropriate human review before production publication.

---

# 21. Deployment Requirements

## Environments

```text
Local
 ↓
Preview
 ↓
Staging
 ↓
Production
```

## Production Requirements

* `[REQUIREMENT]`

## Rollback Requirement

`[ROLLBACK_STRATEGY]`

Deployment behavior remains governed by `DEPLOYMENT_RULES.md`.

---

# 22. Success Metrics

Define measurable product success.

| Metric     | Definition     | Target     | Measurement Method |
| ---------- | -------------- | ---------- | ------------------ |
| `[METRIC]` | `[DEFINITION]` | `[TARGET]` | `[METHOD]`         |

A product MUST NOT be considered successful solely because the application builds or pages render.

---

# 23. Constraints

List known constraints.

### Technical

* `[CONSTRAINT]`

### Business

* `[CONSTRAINT]`

### Time

* `[CONSTRAINT]`

### Budget

* `[CONSTRAINT]`

### Legal / Compliance

* `[CONSTRAINT]`

---

# 24. Risks

| Risk     | Probability         | Impact              | Mitigation     |
| -------- | ------------------- | ------------------- | -------------- |
| `[RISK]` | `[LOW/MEDIUM/HIGH]` | `[LOW/MEDIUM/HIGH]` | `[MITIGATION]` |

---

# 25. Open Questions

Unresolved product decisions MUST be recorded here.

| ID    | Question     | Impact     | Owner     | Status   |
| ----- | ------------ | ---------- | --------- | -------- |
| Q-001 | `[QUESTION]` | `[IMPACT]` | `[OWNER]` | `[OPEN]` |

AI MUST NOT silently resolve high-impact unanswered questions.

---

# 26. Decision Log

Important product decisions should be recorded.

| ID    | Decision     | Reason     | Date     |
| ----- | ------------ | ---------- | -------- |
| D-001 | `[DECISION]` | `[REASON]` | `[DATE]` |

---

# 27. Change Control

Changes to this specification MUST:

1. identify the affected requirement
2. explain the reason
3. identify affected Features
4. evaluate downstream impact
5. update related documentation when necessary
6. trigger re-verification when required

A change to the product specification MUST NOT silently invalidate existing implementation.

---

# 28. Project Completion Definition

The project is not complete merely because the application renders.

The project is complete only when applicable requirements are verified:

* Product requirements implemented
* Core user journeys work
* Real data flow works
* Required backend functionality works
* Required API integration works
* Database integration works
* Authentication works
* Authorization works
* UX requirements are verified
* Mobile behavior is verified
* Accessibility is reviewed
* SEO requirements are verified
* Performance requirements are reviewed
* Security requirements are verified
* Relevant tests pass
* Production build succeeds
* Deployment succeeds
* Production smoke test passes
* No known production mock functionality remains
* No unresolved blocker remains
* Final audit passes

---

# 29. Authority Model

This document defines **project-specific product requirements**.

The authority hierarchy is:

```text
Global Project Rules
        ↓
PROJECT_SPEC.md
        ↓
Feature Specification
        ↓
Design References
        ↓
Existing Verified Implementation
```

Where a project-specific requirement conflicts with a global technical, security, UX, database, or API rule, the conflict MUST be identified and resolved explicitly.

AI MUST NOT silently override governing rules.

---

# 30. AI Operating Rule

AI MUST treat this document as the product source of truth.

AI MUST NOT:

* invent undocumented business requirements
* invent user roles
* invent product capabilities
* expand MVP scope without approval
* silently remove requirements
* treat assumptions as facts
* mark incomplete requirements as complete
* skip unresolved high-impact decisions
* implement Features without understanding their acceptance conditions

When information is missing, AI SHOULD identify the gap and propose a reasonable option rather than silently changing the product definition.
