# DEVELOPMENT RULES

## 1. Purpose

This document defines the baseline engineering rules for all projects using this development system.

Project-specific requirements belong in `PROJECT_SPEC.md`.

Architecture decisions belong in `ARCHITECTURE.md`.

Security requirements belong in `SECURITY_RULES.md`.

UX and accessibility requirements belong in `UX_RULES.md`.

Design tokens and visual rules belong in `DESIGN_SYSTEM.md`.

---

## 2. Development Method

Projects MUST use a specification-driven workflow.

The default workflow is:

```text
Specify
  ↓
Clarify
  ↓
Plan
  ↓
Design / Contracts / Data Model
  ↓
Tasks
  ↓
Implement
  ↓
Verify
  ↓
Converge
```

Requirements MUST be defined before implementation.

Implementation MUST be traceable to documented requirements.

When requirements change, the specification and its derived artifacts MUST be updated so they remain consistent.

For large features, decompose the work into smaller independently testable specifications.

This approach follows the principles of Spec-Driven Development used by GitHub Spec Kit.

---

## 3. Repository Rules

The repository is the source of truth for the project.

Important decisions MUST be documented in version control.

Do not rely on undocumented instructions, temporary chat context, or memory for permanent project decisions.

Project configuration MUST be separated from source code where appropriate.

Secrets and credentials MUST NOT be committed to the repository.

Environment-specific configuration MUST use environment/configuration mechanisms rather than hardcoded credentials or deployment-specific values.

These principles are consistent with the Twelve-Factor App methodology.

---

## 4. Requirements Before Code

Before implementation:

* Understand the requested behavior.
* Identify acceptance criteria.
* Identify dependencies.
* Identify affected frontend areas.
* Identify affected backend areas.
* Identify database changes.
* Identify API contracts.
* Identify security requirements.
* Identify testing requirements.
* Identify UX and accessibility requirements.

If important requirements are ambiguous, clarify them before implementation.

Do not silently invent business requirements.

---

## 5. Architecture

Follow `ARCHITECTURE.md`.

Do not introduce architectural patterns without a documented reason.

Architecture decisions SHOULD consider:

* Separation of concerns
* Clear module boundaries
* Testability
* Maintainability
* Security
* Scalability
* Operational requirements
* Simplicity

Avoid speculative abstractions and unnecessary complexity.

Do not solve hypothetical future requirements unless the project explicitly requires them.

---

## 6. Implementation

Implementation MUST follow the approved specification and plan.

Code SHOULD be:

* Clear
* Cohesive
* Testable
* Maintainable
* Understandable
* Consistent with the existing codebase

Prefer the simplest implementation that correctly satisfies the requirement.

Do not introduce unnecessary frameworks, abstractions, dependencies, or patterns.

---

## 7. Component and Module Reuse

Before creating new code:

1. Search for an existing implementation.
2. Determine whether it can be reused.
3. Determine whether it can be safely extended.
4. Create a new implementation only when necessary.

Do not duplicate existing functionality.

Do not create multiple sources of truth for the same behavior.

---

## 8. Type Safety

When TypeScript is used:

* Use strict type checking appropriate to the project.
* Avoid `any` unless there is a documented and justified reason.
* Define explicit types for important domain and API structures.
* Keep API contracts typed.
* Do not use type assertions to hide actual type problems.
* Validate untrusted external data at runtime.

Static typing does not replace runtime validation.

Typed linting MAY be used to detect problems that ordinary linting cannot detect.

---

## 9. API and Backend

APIs MUST have explicit contracts.

A contract SHOULD define:

* Endpoint
* HTTP method
* Authentication requirements
* Authorization requirements
* Request structure
* Response structure
* Validation
* Error behavior

Backend authorization MUST be enforced server-side.

The frontend MUST NOT be treated as a security boundary.

API security MUST follow `SECURITY_RULES.md` and the applicable OWASP standards.

---

## 10. Database

Persistent functionality MUST use the project's defined persistence layer.

Before implementing database-dependent functionality:

* Define the data model.
* Define required fields.
* Define relationships where applicable.
* Define validation rules.
* Define indexes where needed.
* Consider transaction requirements.
* Consider concurrency and consistency.

Temporary in-memory data MUST NOT replace required production persistence.

Database access MUST remain behind the appropriate application boundary.

---

## 11. Frontend and Backend Integration

A feature requiring server functionality is not complete when only the UI exists.

The implementation MUST verify the complete path:

```text
UI
 ↓
Client State
 ↓
API
 ↓
Backend Logic
 ↓
Database
 ↓
Response
 ↓
UI State
```

Mock data MAY be used for prototyping or tests when explicitly intended.

Mock data MUST NOT silently remain as a substitute for required production functionality.

---

## 12. Validation and Error Handling

All untrusted input MUST be validated at the appropriate boundary.

Applications MUST handle expected failure conditions.

Depending on the feature, this includes:

* Validation errors
* Authentication failures
* Authorization failures
* Network failures
* Database failures
* Timeouts
* Empty results
* Unexpected server errors

Errors MUST NOT be silently ignored.

User-facing error messages MUST NOT expose sensitive implementation details.

---

## 13. Testing

Tests MUST correspond to the behavior being implemented.

Use the appropriate level:

* Unit
* Integration
* API
* End-to-end

Tests for changed behavior SHOULD accompany the implementation change.

A passing test suite alone does not prove that the requirements are complete; requirements and acceptance criteria must also be verified.

Google's engineering practices emphasize testing changed behavior and keeping tests with the corresponding change.

---

## 14. Code Review

Changes SHOULD be:

* Focused
* Understandable
* Reviewable
* Testable
* Limited to the intended scope

Prefer small, self-contained changes over large unrelated changes.

Separate large refactorings from feature changes when practical.

Code review SHOULD evaluate:

* Design
* Functionality
* Complexity
* Tests
* Naming
* Documentation
* Maintainability
* Security where relevant
* Accessibility where relevant

These principles are based on Google's published engineering code-review practices.

---

## 15. Git

Use version control for all project changes.

Commit messages SHOULD follow a consistent convention.

When Conventional Commits are adopted, use:

```text
type(scope): description
```

Examples:

```text
feat(auth): add password reset
fix(cart): correct quantity calculation
docs(api): update order contract
refactor(ui): simplify product card
test(order): add checkout integration tests
```

Conventional Commits provides a standardized structure for machine-readable commit history.

---

## 16. Dependencies

Before adding a dependency:

* Check whether the project already provides the functionality.
* Check whether an existing dependency can solve the problem.
* Evaluate maintenance and security.
* Keep dependencies justified and minimal.

Do not add dependencies for trivial functionality without a reason.

---

## 17. Configuration and Secrets

Environment-specific configuration MUST be separated from source code.

Secrets MUST NOT be:

* Hardcoded
* Committed to Git
* Exposed to the client unnecessarily
* Included in logs

Use the project's approved secret and configuration mechanism.

---

## 18. Accessibility

Web interfaces MUST follow the project's accessibility requirements.

Where applicable, use WCAG 2.2 as the accessibility baseline.

Consider:

* Keyboard access
* Focus management
* Labels
* Accessible names
* Semantic structure
* Contrast
* Touch interaction
* Error identification
* Responsive usage

WCAG 2.2 is a W3C Recommendation and was approved as ISO/IEC 40500:2025.

---

## 19. Security

Security requirements MUST be applied during development, not only during final review.

Web application security MUST follow `SECURITY_RULES.md`.

OWASP ASVS 5.0.0 is the baseline verification standard for applicable web application security requirements.

---

## 20. No Fake Completion

The following MUST NOT be reported as complete:

* UI without required backend functionality.
* Backend without required database persistence.
* Database without application integration.
* API without frontend integration when required.
* Unvalidated forms.
* Unimplemented buttons/actions.
* Mock data replacing required production data.
* Happy-path-only functionality where failure handling is required.
* Untested critical functionality.

---

## 21. Change Control

If implementation reveals that the approved specification or architecture is incorrect:

1. Document the discovery.
2. Determine what artifact must change.
3. Update the relevant specification or plan.
4. Reconcile dependent artifacts.
5. Verify the resulting implementation.

Do not leave the specification, plan, tasks, and implementation contradicting one another.

Spec Kit explicitly recommends keeping these artifacts aligned when requirements or implementation discoveries change.

---

## 22. Completion

A feature is complete only when:

* Requirements are satisfied.
* Acceptance criteria are satisfied.
* Implementation matches the approved plan.
* Required frontend functionality works.
* Required backend functionality works.
* Required database persistence works.
* API integration works.
* Validation works.
* Security requirements are satisfied.
* Accessibility requirements are satisfied where applicable.
* Relevant tests pass.
* Integration has been verified.
* No known critical blocker remains.

The status MUST accurately reflect reality.

Never claim that something was tested if it was not tested.

Never claim that something is complete if required work remains.

---

## 23. Source Standards

This development system uses authoritative standards and references rather than invented project rules.

Primary references currently include:

* GitHub Spec Kit — Spec-Driven Development
* OWASP ASVS — Application Security Verification
* OWASP API Security guidance
* W3C WCAG 2.2 — Accessibility
* Twelve-Factor App — Application operational principles
* Google Engineering Practices — Code Review
* Conventional Commits — Commit convention
* Semantic Versioning — Versioning where applicable

Standards MUST be versioned or linked explicitly when a requirement depends on a specific version.
