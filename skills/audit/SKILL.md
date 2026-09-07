# Audit Skill

## Purpose

This skill defines how the AI performs a final audit of a feature, phase, or project.

It does not redefine project requirements or quality standards.

It uses the project's existing specifications, rules, tests, and design references as the source of truth.

---

## 1. Define Audit Scope

Before auditing, identify the scope:

```text id="q7m3kd"
Feature
Phase
Project
```

Only audit the requested scope and its directly affected dependencies.

---

## 2. Collect Evidence

Inspect the actual implementation and available evidence:

* Source code
* Routes
* Components
* API contracts
* Backend services
* Database operations
* Tests
* Design references
* Configuration
* Relevant documentation
* Existing audit results

Do not audit from assumptions or screenshots alone when the implementation can be inspected.

---

## 3. Compare Against Source of Truth

Evaluate the implementation against the applicable project sources:

```text id="w5c8ra"
Project Specification
→ Architecture
→ Design
→ UX
→ Implementation
→ Integration
→ Tests
→ Security
```

Identify differences between:

* Required
* Implemented
* Partially implemented
* Missing
* Incorrect

---

## 4. Trace Critical User Flows

For important features, follow the real flow:

```text id="n2v9xf"
User
→ UI
→ State
→ API
→ Backend
→ Database / External Service
→ Response
→ UI
```

Confirm that each required connection actually works.

Do not accept the existence of individual layers as proof of integration.

---

## 5. Review Completeness

Check whether the scoped functionality is complete.

Look for:

* Missing screens
* Missing states
* Missing API connections
* Missing database operations
* Missing permissions
* Broken integrations
* Placeholder implementations
* Mock production behavior
* Unhandled failures
* Incomplete responsive behavior
* Missing tests

---

## 6. Review Regressions

Identify whether the change affected existing functionality.

Inspect:

* Shared components
* Shared utilities
* API consumers
* Authentication flows
* Database operations
* Related user journeys
* Responsive behavior

Use existing regression tests where available.

---

## 7. Classify Findings

Every finding should be classified clearly:

```text id="c4x8mz"
BLOCKER
CRITICAL
HIGH
MEDIUM
LOW
OBSERVATION
```

Prioritize issues that prevent correct, secure, or usable operation.

Do not inflate minor inconsistencies into blockers.

---

## 8. Verify Findings

Before reporting a finding:

1. Reproduce or confirm it.
2. Identify the affected area.
3. Determine the actual impact.
4. Identify the likely root cause.
5. Record evidence.
6. Avoid speculative findings.

The audit should distinguish confirmed problems from recommendations.

---

## 9. Fix-and-Reaudit Loop

When fixes are requested:

```text id="f8q2ln"
Finding
→ Fix
→ Test
→ Regression Check
→ Re-audit
```

Do not mark an issue resolved merely because code was changed.

Verify the resulting behavior.

---

## 10. Quality Gate

At the end of the audit, determine:

```text id="z6r4vp"
PASS
PASS WITH WARNINGS
BLOCKED
```

### PASS

No unresolved issue prevents completion.

### PASS WITH WARNINGS

The scoped work is functional, but non-blocking issues remain documented.

### BLOCKED

One or more unresolved issues prevent safe or correct completion.

---

## 11. Do Not Hide Incomplete Work

The AI must not mark work as complete because:

* the application builds
* tests partially pass
* the UI looks finished
* endpoints exist
* database collections exist
* screenshots look correct

Completion requires evidence that the required system behavior works.

---

## 12. Audit Report

Produce a concise report containing:

```text id="p3k7ws"
Scope
Status
Findings
Severity
Evidence
Fixes
Remaining Issues
Tests Verified
Final Quality Gate
```

For large audits, group findings by area:

* Frontend
* Backend
* API
* Database
* Security
* UX
* Testing
* Integration

---

## 13. Stop Conditions

Stop progression when a finding is a true blocker for the next stage.

Examples:

* Critical security failure
* Broken core user flow
* Missing required backend integration
* Data integrity issue
* Unresolved critical authorization problem
* Feature fundamentally incomplete

Do not bypass a blocker merely to continue the roadmap.

---

## 14. Audit Completion Gate

The audit is complete when:

```text id="k8m2qd"
[ ] Scope defined
[ ] Implementation inspected
[ ] Source of truth compared
[ ] Critical flows traced
[ ] Completeness reviewed
[ ] Regression risk reviewed
[ ] Findings verified
[ ] Findings classified
[ ] Fixes re-tested where applicable
[ ] Final quality gate assigned
[ ] Remaining issues documented
```

---

## Operating Principle

> **An audit is evidence-based verification of what actually exists, not a confirmation of what was intended to exist.**
