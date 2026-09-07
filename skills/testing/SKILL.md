# Testing Skill

## Purpose

This skill defines how the AI executes testing and verification for a feature.

It operates under:

* `TESTING_RULES.md`
* `CODING_RULES.md`
* `SECURITY_RULES.md`
* `UX_RULES.md`
* `API_RULES.md`
* `DATABASE_RULES.md`

Those files define the testing requirements.
This skill defines the execution workflow.

---

## 1. Start From Requirements

Before testing, identify:

* Feature requirements
* Expected user behavior
* Expected system behavior
* Success conditions
* Failure conditions
* Security-sensitive operations
* Data changes
* Existing functionality that may be affected

Convert requirements into verifiable behaviors.

---

## 2. Inspect Existing Tests

Before creating new tests, inspect:

* Existing test structure
* Test utilities
* Fixtures
* Factories
* Mocking patterns
* Integration setup
* E2E setup
* Security tests
* Existing coverage

Reuse established testing infrastructure.

---

## 3. Build the Test Matrix

For the feature, determine the applicable scenarios:

```text id="k3f8qm"
Requirement
→ Expected Behavior
→ Test Scenario
→ Verification
```

Include both normal and failure paths.

Do not create tests simply to increase test count.

---

## 4. Test in Layers

Use the appropriate test level for each behavior:

```text id="p7v2nc"
Unit
→ Integration
→ Contract
→ E2E
→ Security
```

Not every behavior requires every layer.

Prefer the lowest appropriate level for isolated logic, while critical user flows should also be verified through higher-level tests.

---

## 5. Test Real Feature Integration

For features involving multiple layers, verify the actual flow:

```text id="w4q9xs"
UI
→ API
→ Backend
→ Database / External Service
→ Response
→ UI
```

Do not replace the entire application flow with mocks when real integration is what needs verification.

---

## 6. Test Failure Paths

For applicable operations, deliberately test:

* Invalid input
* Empty data
* Missing resource
* Authentication failure
* Authorization failure
* Server failure
* Network failure
* Dependency failure
* Duplicate request
* Concurrency conflict
* Timeout

Verify that the UI and backend respond correctly.

---

## 7. Test Data Integrity

When the feature modifies persistent data, verify:

```text id="d6n1ra"
Before
→ Operation
→ Database State
→ Result
```

Confirm that:

* expected data was created/updated/deleted
* unrelated data was not modified
* failed operations do not leave invalid state
* repeated operations behave correctly

---

## 8. Test Security Boundaries

For protected features, verify at minimum the applicable cases:

```text id="x8c5mv"
Unauthenticated
→ Unauthorized
→ Wrong Resource
→ Wrong Role
→ Unauthorized Field
```

Confirm that frontend restrictions are not the only protection.

---

## 9. Test Responsive Behavior

For user-facing features, verify the supported responsive states defined by the project.

Check:

* layout
* navigation
* forms
* tables
* drawers/modals
* touch interactions
* text wrapping
* overflow
* loading/error/empty states

Mobile verification must test actual mobile behavior, not only a reduced desktop layout.

---

## 10. Test Accessibility

For applicable features, verify:

* Keyboard operation
* Focus behavior
* Focus visibility
* Accessible names
* Form errors
* Dialog/drawer behavior
* Screen-reader relevant structure
* Reduced-motion behavior

Use the project's accessibility requirements as the source of truth.

---

## 11. Run Regression Tests

After feature implementation, identify existing areas that could be affected.

Run the relevant regression suite.

Examples:

```text id="m5r8kp"
Shared Component Change
→ All affected consumers

API Change
→ Existing API consumers

Database Change
→ Related data operations

Auth Change
→ Protected flows
```

Do not assume unchanged files mean unchanged behavior.

---

## 12. Verify Build and Static Checks

Before completion, run the project's applicable:

* Type checking
* Linting
* Build
* Test suite
* Contract validation
* Other configured CI checks

A passing build alone does not prove feature correctness.

---

## 13. Diagnose Failures

When a test fails:

```text id="q2v7fd"
Failure
→ Reproduce
→ Identify Root Cause
→ Fix
→ Re-run Failed Test
→ Run Relevant Regression Tests
```

Do not simply weaken or remove a failing test to obtain a green result.

---

## 14. Test Completion Gate

Before marking testing complete:

```text id="r9k4wc"
[ ] Requirements converted into testable behavior
[ ] Existing tests inspected
[ ] Appropriate test levels selected
[ ] Success paths verified
[ ] Failure paths verified
[ ] Data integrity verified where applicable
[ ] Security boundaries verified
[ ] Responsive behavior verified
[ ] Accessibility verified where applicable
[ ] Regression tests run
[ ] Static checks pass
[ ] Build passes
[ ] No unexplained test failures remain
```

---

## 15. Report Verification Clearly

After testing, report:

* Tests performed
* Important scenarios verified
* Failed tests
* Fixed issues
* Remaining blockers
* Areas not tested
* Final verification status

Never report a feature as fully verified when important areas were not tested.

---

## Operating Principle

> **Testing proves behavior, not merely code execution. A feature is verified when its required behavior works under both expected and relevant failure conditions.**
