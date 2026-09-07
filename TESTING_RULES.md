# TESTING RULES

## 1. PURPOSE

This document defines the mandatory testing standards for the entire application.

Testing MUST verify:

* Functional correctness
* Frontend behavior
* Backend behavior
* API contracts
* Database integration
* Authentication
* Authorization
* Security
* Accessibility
* Responsive behavior
* Business logic
* Error handling
* Regression protection
* Production readiness

A feature is NOT considered complete because the application starts or a page renders.

---

# 2. CORE PRINCIPLE

Testing follows:

```text
Requirement
↓
Expected Behavior
↓
Test
↓
Implementation
↓
Verification
↓
Regression Check
```

Tests MUST verify actual behavior rather than implementation details whenever possible.

---

# 3. NO FAKE TESTING

The following are prohibited:

```text
❌ Tests that only check that code exists
❌ Tests that only check HTTP 200
❌ Tests that mock the entire application
❌ Tests that never reach the database when DB behavior matters
❌ Tests that skip authorization
❌ Tests that test only the happy path
❌ Tests that are written to match broken implementation
❌ Tests that pass while the real user flow is broken
```

Mocks are allowed only where isolation provides genuine value.

---

# 4. TESTING PYRAMID

Use multiple test levels:

```text
                 E2E
              /       \
        Integration   Contract
          /               \
       API / DB         Security
          \               /
             Unit Tests
```

No single test type is sufficient for the entire system.

---

# 5. TEST LEVELS

The project SHOULD use:

```text
Unit Tests
Integration Tests
API Tests
Contract Tests
Database Tests
Security Tests
Component Tests
Accessibility Tests
Responsive Tests
End-to-End Tests
Regression Tests
```

The exact tooling is project-specific.

---

# 6. UNIT TESTS

Unit tests verify isolated logic.

Good candidates:

```text
validation
formatters
calculations
business rules
permissions
pure utilities
state transformations
pricing logic
discount logic
```

Unit tests SHOULD be:

* fast
* deterministic
* isolated
* easy to understand

---

# 7. BUSINESS LOGIC TESTS

Business-critical logic MUST have dedicated tests.

Examples:

```text
price calculation
discount calculation
coupon validation
inventory rules
order state transitions
permission evaluation
shipping calculation
tax calculation
```

Do not rely exclusively on UI tests for business logic.

---

# 8. EDGE CASES

Tests MUST include relevant edge cases.

Examples:

```text
empty input
zero
negative values
maximum values
missing fields
duplicate records
expired data
invalid state
concurrent requests
large input
unexpected external response
```

---

# 9. FRONTEND COMPONENT TESTS

Reusable components SHOULD have tests for important behavior.

Examples:

```text
Button
Input
Select
Dropdown
Tabs
Accordion
Modal
Drawer
Pagination
Table
ProductCard
Form
```

Tests should verify behavior and accessibility where relevant.

---

# 10. COMPONENT STATES

Important components MUST be tested across relevant states:

```text
default
hover
focus
active
disabled
loading
error
empty
selected
open
closed
```

Not every state applies to every component.

---

# 11. FORM TESTING

Forms MUST test:

```text
valid submission
invalid submission
required fields
field validation
server validation errors
loading state
submission failure
successful submission
duplicate submission
keyboard interaction
```

---

# 12. API TESTING

Every important API endpoint MUST have tests for applicable scenarios.

Minimum baseline:

```text
success
invalid request
unauthenticated request
unauthorized request
not found
conflict
validation failure
server failure
rate limiting where applicable
```

---

# 13. API CONTRACT TESTING

API tests SHOULD verify:

```text
HTTP method
status code
request schema
response schema
required fields
field types
error structure
authentication
authorization
```

The frontend and backend MUST conform to the same contract.

---

# 14. API SECURITY TESTING

Protected endpoints MUST test:

```text
No token
Invalid token
Expired token
Wrong role
Missing permission
Wrong object owner
Unauthorized property access
Mass assignment attempts
```

Example:

```text
User A
↓
tries to access
↓
User B's resource
↓
MUST be rejected
```

---

# 15. OBJECT-LEVEL AUTHORIZATION TESTS

For resource-based APIs, test cross-user access.

Example:

```text
User A → Order A
User B → Order B

User B → Order A
→ MUST fail
```

This test is mandatory for sensitive user-owned resources.

---

# 16. PROPERTY-LEVEL AUTHORIZATION TESTS

Test that protected properties cannot be:

```text
read
created
updated
```

by unauthorized users.

Example:

```json
{
  "role": "admin",
  "permissions": ["*"]
}
```

must NOT allow a normal user to elevate privileges.

---

# 17. DATABASE TESTING

Database-dependent behavior MUST be tested against a realistic database environment.

Do not rely exclusively on:

```text
mockDatabase()
```

when the feature depends on actual database behavior.

---

# 18. FIRESTORE TESTING

For Firestore projects, test applicable:

```text
Security Rules
read permissions
write permissions
query behavior
transactions
atomic updates
concurrent updates
data validation
indexes where relevant
```

Firestore emulator/testing infrastructure SHOULD be used where appropriate.

---

# 19. DATABASE SECURITY RULE TESTING

For client-accessible Firestore data, test:

```text
authorized read
unauthorized read
authorized write
unauthorized write
cross-user access
privileged access
protected fields
```

Security Rules MUST be treated as production code.

---

# 20. TRANSACTION TESTING

Critical transactions MUST test:

```text
success
failure
rollback
concurrent modification
duplicate request
retry behavior
```

Example:

```text
Create Order
+
Decrease Inventory
```

must not leave inconsistent state if one part fails.

---

# 21. INTEGRATION TESTS

Integration tests verify multiple real layers together.

Example:

```text
API
↓
Service
↓
Database
```

or:

```text
Frontend
↓
API
↓
Backend
```

Use integration tests where isolated unit tests cannot prove correctness.

---

# 22. END-TO-END TESTS

E2E tests verify complete user journeys.

Important flows SHOULD have E2E coverage.

Examples:

```text
Registration
Login
Product browsing
Search
Filtering
Product details
Add to cart
Update cart
Checkout
Order creation
Order history
Admin product creation
Admin product editing
```

---

# 23. CRITICAL USER FLOWS

Critical business flows MUST have E2E coverage.

Examples:

```text
Authentication
Checkout
Payment
Order creation
Inventory changes
Admin operations
Account security changes
```

A critical workflow MUST NOT rely only on unit tests.

---

# 24. E2E TEST PRINCIPLE

E2E tests should represent realistic user behavior.

Prefer:

```text
User clicks
User types
User navigates
User submits
User sees result
```

rather than directly manipulating internal application state.

---

# 25. RESPONSIVE TESTING

Responsive behavior MUST be tested at important viewport sizes.

Minimum baseline SHOULD include:

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

Exact breakpoints may differ by project.

---

# 26. MOBILE-FIRST TESTING

Mobile MUST NOT be treated as a reduced desktop version.

Test:

```text
navigation
menus
drawers
filters
forms
tables
cards
checkout
dialogs
sticky actions
keyboard behavior
safe areas
```

on actual mobile-sized viewports.

---

# 27. MOBILE WORKFLOW TESTS

Important mobile workflows MUST be independently tested.

Examples:

```text
Open navigation
Open filters
Apply filter
Close filter
Add product
Open cart
Checkout
Submit form
Admin workflow
```

A desktop-passing test does NOT prove mobile correctness.

---

# 28. TOUCH TARGET TESTING

Interactive elements MUST provide usable touch targets.

Test:

```text
buttons
icons
checkboxes
radio buttons
tabs
close controls
quantity controls
navigation items
```

Avoid interactions that require precision tapping.

---

# 29. RTL TESTING

For RTL applications, tests MUST verify:

```text
text direction
layout direction
navigation
forms
icons
spacing
tables
drawers
dialogs
pagination
```

Do not assume that changing:

```text
direction: rtl;
```

automatically produces a correct RTL interface.

---

# 30. ACCESSIBILITY TESTING

Accessibility MUST be tested as part of normal QA.

Baseline:

```text
WCAG 2.2 AA
```

Test applicable:

```text
keyboard navigation
focus visibility
focus order
labels
form errors
semantic structure
screen-reader behavior
contrast
zoom/reflow
reduced motion
```

---

# 31. KEYBOARD TESTING

Important workflows MUST be usable without a mouse.

Test:

```text
Tab
Shift + Tab
Enter
Space
Escape
Arrow keys
```

where applicable.

Focus MUST remain understandable.

---

# 32. FOCUS TESTING

Every interactive component MUST have a visible focus state.

Test:

```text
buttons
links
inputs
selects
tabs
dialogs
drawers
menus
```

Do not remove browser focus indicators without providing an accessible replacement.

---

# 33. DIALOG / DRAWER TESTING

Dialogs and drawers MUST test:

```text
open
close
Escape
focus management
keyboard navigation
background interaction
scroll behavior
mobile behavior
```

Major workflows should not be implemented as small centered modals.

---

# 34. LOADING STATES

Every asynchronous operation SHOULD have an appropriate loading state.

Test:

```text
initial loading
submit loading
button loading
data refresh
pagination loading
mutation loading
```

Prevent duplicate submissions where necessary.

---

# 35. ERROR STATES

Every important async operation MUST test failure behavior.

Examples:

```text
network error
401
403
404
409
422
429
500
timeout
database failure
external service failure
```

The UI MUST provide a meaningful recovery path where appropriate.

---

# 36. EMPTY STATES

Collections MUST have tested empty states.

Examples:

```text
No products
No search results
Empty cart
No orders
No notifications
No admin records
```

Empty state is a product state, not an error.

---

# 37. ERROR BOUNDARIES

Frontend error boundaries SHOULD be tested.

Verify that an unexpected component failure:

```text
does not destroy the entire application
shows a useful fallback
provides recovery where possible
does not expose sensitive technical details
```

---

# 38. CONCURRENCY TESTING

Critical mutable resources SHOULD be tested under concurrent operations.

Examples:

```text
two users buying last inventory item
two simultaneous coupon uses
duplicate order submission
parallel admin updates
```

---

# 39. IDEMPOTENCY TESTING

Idempotent operations MUST test repeated requests.

Example:

```text
Request A
Request A again
```

Expected result:

```text
One logical side effect
```

not:

```text
Two orders
Two charges
Two inventory deductions
```

---

# 40. SECURITY REGRESSION TESTING

Every important security fix SHOULD receive a regression test.

Example:

```text
Bug:
User B could access User A's order.

Fix:
Authorization added.

Required:
Regression test proving User B remains blocked.
```

---

# 41. PERFORMANCE TESTING

Performance-sensitive areas SHOULD be tested.

Examples:

```text
large product catalog
search
filtering
pagination
admin tables
large forms
high-volume API endpoints
```

Measure where appropriate:

```text
response time
render time
query cost
payload size
memory
```

---

# 42. DATABASE PERFORMANCE

Test database behavior for:

```text
large collections
pagination
indexes
high-read operations
high-write operations
expensive queries
```

Avoid accidentally introducing full collection scans.

---

# 43. API PERFORMANCE

API tests SHOULD detect:

```text
unbounded queries
large responses
slow external services
missing pagination
N+1 database access
unnecessary repeated calls
```

---

# 44. NETWORK FAILURE TESTING

The application MUST behave predictably when network conditions fail.

Test:

```text
timeout
offline
slow response
request failure
connection interruption
duplicate retry
```

The UI should not falsely display success.

---

# 45. THIRD-PARTY SERVICE TESTING

External services SHOULD be tested using controlled mocks/stubs for failure scenarios.

Examples:

```text
payment provider unavailable
email provider unavailable
storage unavailable
shipping service unavailable
```

The application must define safe fallback behavior.

---

# 46. TEST DATA

Test data MUST be:

```text
predictable
isolated
repeatable
safe
non-production
```

Never use real production secrets or sensitive production data in tests.

---

# 47. TEST ISOLATION

Tests SHOULD NOT depend on execution order.

Each test must establish the state it needs.

Avoid:

```text
Test A creates data
↓
Test B assumes Test A ran
```

---

# 48. TEST CLEANUP

Tests MUST clean up or isolate created state where necessary.

Database test environments should be reset, isolated or seeded deterministically.

---

# 49. DETERMINISTIC TESTS

Avoid tests dependent on:

```text
random timing
real external services
current production data
unstable network
system clock
execution order
```

When time matters, use controllable clocks where supported.

---

# 50. TEST ENVIRONMENTS

Separate:

```text
Development
Test
Staging
Production
```

Test environments MUST NOT accidentally connect to production resources.

---

# 51. CI TESTING

CI SHOULD automatically run applicable:

```text
type checking
linting
unit tests
integration tests
API tests
build
security checks
```

Critical projects SHOULD also run appropriate E2E and accessibility checks.

---

# 52. BUILD VERIFICATION

A production build MUST be tested.

Passing development mode does not prove production correctness.

At minimum verify:

```text
build
start
routes
API integration
assets
environment configuration
```

---

# 53. TYPE CHECKING

TypeScript projects MUST run type checking independently from runtime tests.

Example:

```text
tsc --noEmit
```

or the project's equivalent.

A successful test suite does not replace type checking.

---

# 54. LINTING

Linting SHOULD run in CI.

Lint failures MUST NOT be ignored unless explicitly justified.

---

# 55. COVERAGE

Coverage SHOULD be used as a signal, not the sole quality metric.

High coverage does NOT guarantee:

```text
correct UX
secure authorization
correct business logic
mobile correctness
real database integration
```

Critical paths should receive stronger testing than trivial code.

---

# 56. TEST NAMING

Tests should clearly describe behavior.

Prefer:

```text
allows an authenticated user to update their profile
```

over:

```text
test1
```

Test names should explain expected behavior.

---

# 57. TEST ORGANIZATION

Tests SHOULD be organized around features/domains where practical.

Example:

```text
features/
  products/
    products.service.ts
    products.test.ts
    products.api.test.ts

  orders/
    orders.service.ts
    orders.test.ts
    orders.e2e.test.ts
```

Project structure may vary.

---

# 58. NO IMPLEMENTATION-LOCKED TESTS

Avoid tests that fail merely because internal implementation changed while behavior remains correct.

Test public behavior and contracts wherever possible.

---

# 59. REGRESSION TESTING

Before completing a change:

```text
Run targeted tests
↓
Run affected integration tests
↓
Run regression suite
↓
Run build/type checks
```

The scope depends on the change.

---

# 60. PHASE QUALITY GATE

A development phase MUST NOT be marked complete until:

```text
Functional tests
+
Integration tests
+
Security checks
+
Responsive checks
+
Accessibility checks
+
Build verification
```

have passed at the required level.

---

# 61. BUG FIX RULE

Every reproducible bug SHOULD follow:

```text
Bug reproduced
↓
Root cause identified
↓
Regression test created
↓
Fix implemented
↓
Regression test passes
↓
Related tests pass
```

Do not fix only the visible symptom when the underlying behavior remains broken.

---

# 62. TESTING AI RULES

AI MUST NOT:

```text
❌ claim tests passed without running them
❌ invent test results
❌ delete failing tests to achieve green CI
❌ weaken assertions without justification
❌ skip authorization tests
❌ skip mobile testing
❌ skip accessibility testing for UI work
❌ mock the database when real DB behavior is being tested
❌ mark E2E flows complete without executing them
❌ ignore build/type errors
❌ hide failures
```

---

# 63. TEST REPORTING

After meaningful implementation work, AI SHOULD report:

```text
Tests run
Tests passed
Tests failed
Tests skipped
Known limitations
Remaining risks
```

Never report:

```text
"Everything works"
```

without evidence.

---

# 64. FAILURE HANDLING

A failed test MUST trigger investigation.

Do not automatically:

```text
disable test
increase timeout
remove assertion
skip suite
mock more dependencies
```

unless the change is justified and documented.

---

# 65. TEST DEFINITION OF DONE

A feature is test-complete only when:

* Expected behavior is defined
* Unit coverage exists where appropriate
* Integration coverage exists where required
* API behavior is tested
* Database behavior is tested where required
* Authorization is tested
* Error states are tested
* Critical flows have E2E coverage
* Responsive behavior is verified
* Accessibility is verified
* Regression tests exist for fixed bugs
* Type checking passes
* Linting passes
* Production build passes
* No known critical test failure remains

---

# 66. FINAL TESTING RULE

The application is NOT considered verified because:

```text
The page loads.
```

It is verified only when the relevant chain has been proven:

```text
Requirement
↓
UI
↓
API
↓
Backend
↓
Database
↓
Security
↓
UX
↓
Tests
↓
Production Build
```

Testing MUST prove that the feature works correctly, securely and consistently in the real architecture.
