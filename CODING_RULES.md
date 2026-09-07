# CODING RULES

## 1. PURPOSE

This document defines mandatory coding rules for all projects.

It controls:

* Code structure
* React development
* TypeScript
* Components
* Hooks
* State
* Business logic
* API integration
* Error handling
* Validation
* Naming
* Reusability
* Dependencies
* Testing boundaries
* Git changes
* Code quality

These rules apply to both human and AI-generated code.

---

# 2. CORE PRINCIPLE

Code MUST be:

* Correct
* Typed
* Readable
* Maintainable
* Reusable
* Testable
* Predictable
* Secure
* Consistent with the architecture

Working code is NOT automatically good code.

The goal is not:

"Make the feature work."

The goal is:

"Make the feature work correctly within the architecture."

---

# 3. BEFORE WRITING CODE

AI MUST NOT immediately start coding.

Before implementation:

1. Read `AGENTS.md`
2. Read `PROJECT_SPEC.md`
3. Read `ARCHITECTURE.md`
4. Read `DESIGN_SYSTEM.md`
5. Read the relevant rules files
6. Inspect the existing codebase
7. Identify reusable components
8. Identify existing services/utilities/hooks
9. Identify affected frontend/backend/database/API areas
10. Identify tests that must change or be added

If an existing implementation already solves the problem, reuse or extend it.

---

# 4. NO DUPLICATE LOGIC

Do NOT copy and paste logic between files.

Bad:

```text
ProductPage
ProductCard
AdminProduct
CheckoutProduct
```

all implementing their own price calculation.

Good:

```text
pricing/
└── calculatePrice()
```

Business rules MUST have one authoritative implementation.

---

# 5. SINGLE RESPONSIBILITY

A module, function or component should have one clear responsibility.

Avoid components such as:

```text
MegaPage.tsx
HugeDashboard.tsx
Everything.tsx
```

A component that handles:

* UI
* API calls
* validation
* business calculations
* database logic
* notifications
* routing
* permissions

simultaneously MUST be reviewed and decomposed.

---

# 6. COMPONENT SIZE

There is no universal numeric line limit.

However, a component SHOULD be split when it has:

* multiple independent responsibilities
* repeated UI structures
* complex state transitions
* large conditional rendering
* embedded business logic
* unrelated API operations
* difficult testing requirements

Component extraction MUST improve responsibility boundaries.

Do not split components purely to create dozens of meaningless files.

---

# 7. REACT COMPONENT RULES

React components MUST remain focused on presentation and UI behavior.

Business logic SHOULD live outside the visual component when it is reusable or complex.

Preferred structure:

```text
Page
 ↓
Feature
 ↓
Components
 ↓
UI primitives
```

Components MUST be reusable when the same behavior appears in multiple places.

---

# 8. REACT PURITY

Components and Hooks MUST be pure.

Do NOT perform side effects during render.

Do NOT:

```text
fetch()
localStorage.setItem()
document manipulation
random generation
date/time generation
global mutation
```

directly during rendering.

Side effects belong in appropriate event handlers, effects, services or other controlled boundaries.

React props and state MUST NOT be mutated directly.

---

# 9. REACT HOOKS

Hooks MUST follow the Rules of Hooks.

Hooks MUST:

* be called at the top level
* be called only from React components or custom Hooks
* remain deterministic
* avoid hidden side effects
* have correct dependencies

Do NOT call Hooks:

```text
inside if
inside loops
inside nested functions
inside callbacks
after conditional returns
```

Custom Hooks SHOULD represent reusable behavior, not simply hide large amounts of unrelated code.

---

# 10. STATE MANAGEMENT

State MUST have a clear owner.

Prefer the smallest appropriate scope.

Use:

```text
Local state
```

when only one component needs it.

Use:

```text
Shared state
```

when multiple related components require it.

Use:

```text
Global state
```

only when the state genuinely belongs to the application.

Do NOT put every piece of state into a global store.

---

# 11. DERIVED STATE

Do not store data that can be calculated from existing state.

Bad:

```text
items
totalItems
```

when `totalItems` can be derived from `items`.

Good:

```text
items
→ calculate totalItems
```

This prevents state duplication and synchronization bugs.

---

# 12. TYPESCRIPT

TypeScript MUST use strong typing.

The project SHOULD enable:

```json
{
  "compilerOptions": {
    "strict": true
  }
}
```

The `strict` family provides stronger guarantees and should be the default baseline.

---

# 13. NO UNNECESSARY `any`

`any` MUST NOT be used merely to bypass TypeScript errors.

Bad:

```ts
const data: any = response;
```

Preferred:

```ts
const data: ProductResponse = response;
```

If `any` is unavoidable because of an external boundary:

1. isolate it
2. document why
3. validate the value
4. convert it into a known type immediately

---

# 14. UNKNOWN OVER ANY

When external data has an unknown shape, prefer:

```ts
unknown
```

over:

```ts
any
```

Then validate/narrow it before use.

---

# 15. RUNTIME VALIDATION

TypeScript does not validate runtime data.

All external input MUST be treated as untrusted.

Validate:

* API responses
* request bodies
* query parameters
* URL parameters
* form submissions
* environment variables
* external service responses
* imported user data

Validation should happen at system boundaries.

---

# 16. API DATA TYPES

API contracts MUST have explicit types.

Do NOT pass untyped API objects throughout the application.

Preferred:

```text
API Response
↓
Validation
↓
Typed Domain/Application Data
↓
UI
```

The UI should not directly depend on unknown backend shapes.

---

# 17. BUSINESS LOGIC

Business logic MUST NOT be duplicated inside UI components.

Avoid:

```tsx
if (user.role === ...)
```

spread throughout the application.

Prefer centralized:

```text
authorization rules
permission helpers
domain rules
use cases
services
```

when the rule is reused or security-sensitive.

---

# 18. SECURITY-SENSITIVE LOGIC

Frontend checks are NOT security controls.

Examples:

```text
role
permission
price
discount
ownership
inventory
order status
payment status
admin access
```

MUST be enforced server-side.

Frontend checks may improve UX but MUST NOT be trusted for authorization.

---

# 19. ASYNC CODE

Async operations MUST handle:

* loading
* success
* failure
* cancellation/race conditions where applicable
* unexpected responses

Do not silently ignore rejected Promises.

Bad:

```ts
saveData();
```

when failure can occur and no handling exists.

---

# 20. ERROR HANDLING

Errors MUST be handled at the correct boundary.

Do NOT use:

```ts
catch {
  // ignore
}
```

unless intentionally justified.

Errors should be:

* logged appropriately
* transformed into safe user-facing messages
* handled by the correct UI state
* prevented from exposing sensitive information

---

# 21. USER-FACING ERROR MESSAGES

Never expose raw technical errors directly to users.

Bad:

```text
FirestoreError: PERMISSION_DENIED...
```

Good:

```text
We couldn't save your changes. Please try again.
```

Detailed technical information belongs in logs/diagnostics.

---

# 22. LOADING STATES

Every async UI operation that can take noticeable time MUST have an appropriate loading state.

Examples:

```text
Button → loading state
Page → skeleton/loading state
Table → loading state
Form → submission state
```

Do not freeze the interface without feedback.

---

# 23. EMPTY STATES

Data-driven components MUST define meaningful empty states.

Example:

```text
No products found.
```

is preferable to:

```text
blank screen
```

Empty state may include:

* explanation
* next action
* reset filters
* create action

when appropriate.

---

# 24. COMPONENT PROPS

Props should be explicit and meaningful.

Avoid:

```ts
isBlue
isLarge
hasBorder
isSpecial
isAdmin
```

when these represent uncontrolled visual variations.

Prefer controlled variants:

```ts
variant
size
tone
state
```

that map to the Design System.

---

# 25. BOOLEAN PROP EXPLOSION

Do not create components with dozens of boolean props.

Bad:

```tsx
<Component
  isLarge
  isBlue
  isRounded
  isDark
  isCompact
  isAdmin
  isSpecial
/>
```

Prefer:

```tsx
<Component
  variant="primary"
  size="md"
/>
```

---

# 26. NAMING

Names MUST describe intent.

Prefer:

```text
calculateOrderTotal()
validateCoupon()
createProduct()
ProductCard
OrderDetails
```

Avoid:

```text
doStuff()
handleThing()
processData()
temp()
data2()
componentNew()
```

Names should be understandable without opening the implementation.

---

# 27. FILE NAMING

Use consistent naming.

Examples:

```text
ProductCard.tsx
ProductService.ts
useCart.ts
orderSchema.ts
authMiddleware.ts
```

Avoid:

```text
productcardfinal.tsx
ProductCardNew.tsx
helper2.ts
utilsFinal.ts
```

---

# 28. UTILITY FUNCTIONS

Do not create giant utility files.

Avoid:

```text
utils.ts
```

containing unrelated functionality.

Prefer domain-focused utilities:

```text
pricing/
date/
validation/
formatting/
permissions/
```

---

# 29. CONSTANTS

Repeated constants MUST have a clear owner.

Examples:

```text
MAX_UPLOAD_SIZE
ORDER_STATUS
SUPPORTED_CURRENCIES
PERMISSION_CODES
```

Do not duplicate magic values throughout the codebase.

---

# 30. MAGIC NUMBERS

Avoid unexplained magic numbers.

Bad:

```ts
if (retryCount > 7)
```

Better:

```ts
const MAX_RETRIES = 7;
```

If the value is part of the Design System, use the relevant token.

---

# 31. COMMENTS

Comments should explain WHY, not WHAT.

Bad:

```ts
// Increment counter
counter++;
```

Good:

```ts
// Prevent duplicate submissions during the server retry window.
```

Do not use comments to justify bad architecture.

---

# 32. TODO

TODO comments MUST NOT become permanent unfinished functionality.

If a TODO represents required work:

* create a tracked task
* document the reason
* define ownership where appropriate

Do not ship fake functionality hidden behind TODOs.

---

# 33. NO FAKE FUNCTIONALITY

The following are prohibited in production unless explicitly defined as a prototype:

```text
fake API
fake database
mock success response
hardcoded product data
fake payment success
fake authentication
fake permissions
fake order creation
fake inventory
```

If the feature is not connected to its real boundary, it is incomplete.

---

# 34. NO SILENT FALLBACKS

Do not hide system failures by silently falling back to fake data.

Bad:

```text
API fails
↓
show hardcoded products
```

This creates false production behavior.

The system should instead expose an appropriate loading/error/empty state.

---

# 35. DATABASE ACCESS

Frontend code MUST NOT directly access the production database unless the architecture explicitly defines that pattern.

Preferred:

```text
UI
↓
Application/API
↓
Backend
↓
Database
```

Database logic belongs to the appropriate infrastructure boundary.

---

# 36. API CALLS

Do not scatter raw API calls throughout random components.

Prefer centralized API clients/services.

Bad:

```text
ProductPage → fetch()
ProductCard → fetch()
AdminProduct → fetch()
```

without a defined API boundary.

Preferred:

```text
api/
services/
features/
```

with clear ownership.

---

# 37. ENVIRONMENT VARIABLES

Secrets MUST NOT be hardcoded.

Never commit:

```text
API keys
private keys
database credentials
tokens
passwords
service credentials
```

Environment configuration MUST follow the project's configuration architecture.

---

# 38. DEPENDENCIES

Do not install a dependency for a trivial function that can be safely implemented with existing platform capabilities.

Before adding a dependency:

1. Check existing dependencies.
2. Check native platform support.
3. Check project architecture.
4. Check maintenance/security status.
5. Confirm the dependency is actually necessary.

Do not add libraries simply because AI commonly uses them.

---

# 39. IMPORT RULES

Imports should be:

* explicit
* organized
* minimal
* stable

Remove unused imports.

Avoid circular dependencies.

Architecture boundaries MUST be respected.

---

# 40. DEPENDENCY DIRECTION

Dependencies should flow according to `ARCHITECTURE.md`.

Higher-level UI code MUST NOT bypass application/domain boundaries simply because direct access is easier.

Avoid:

```text
Component
↓
Database
```

when the architecture requires:

```text
Component
↓
Application/API
↓
Infrastructure
↓
Database
```

---

# 41. TESTABILITY

Code should be structured so important behavior can be tested independently.

Business rules should not be tightly coupled to:

* DOM
* browser globals
* database implementations
* network calls

when separation is practical.

---

# 42. CHANGES MUST INCLUDE RELATED TESTS

When changing behavior:

```text
Code change
+
Affected tests
```

should normally be updated together.

Do not change production behavior and leave known outdated tests behind.

---

# 43. REFACTORING

Refactoring MUST preserve behavior unless the task explicitly changes behavior.

A refactor should:

* improve structure
* reduce duplication
* improve readability
* preserve contracts
* keep tests passing

Do not combine large unrelated refactors with feature work unless necessary.

---

# 44. SMALL CHANGES

Prefer small, focused changes.

A change should ideally have:

```text
one purpose
one logical scope
clear verification
```

Avoid mixing:

```text
new feature
unrelated redesign
dependency migration
database rewrite
large refactor
```

in one uncontrolled change.

---

# 45. CODE REVIEW

Every significant change should be reviewable.

Review for:

* correctness
* architecture
* functionality
* complexity
* tests
* naming
* maintainability
* security
* documentation
* unintended side effects

Code that works but violates architecture MUST NOT automatically pass review.

---

# 46. FORMATTING AND LINTING

Projects MUST use automated formatting/linting where practical.

The exact tools are project-specific.

Typical stack:

```text
TypeScript
ESLint
Prettier
React Hooks linting
```

Linting MUST be part of the quality process.

---

# 47. TYPE ERRORS

Do NOT suppress TypeScript errors merely to make the build pass.

Avoid:

```ts
// @ts-ignore
```

unless explicitly justified.

Prefer fixing the underlying type problem.

If suppression is unavoidable, document the reason.

---

# 48. BUILD MUST BE CLEAN

Before completion:

```text
TypeScript
↓
Lint
↓
Build
↓
Tests
```

must pass according to the project's configured quality gates.

Do not declare completion while known build errors remain.

---

# 49. GIT COMMITS

Use Conventional Commits.

Format:

```text
<type>[optional scope]: <description>
```

Examples:

```text
feat: add product filtering
fix: prevent duplicate order submission
refactor: simplify cart state
test: add checkout validation tests
docs: update architecture rules
chore: update dependencies
```

Breaking changes MUST be explicitly identified according to Conventional Commits.

---

# 50. COMMIT QUALITY

Commits SHOULD be:

* focused
* understandable
* logically grouped
* independently reviewable

Avoid commits such as:

```text
fix stuff
changes
update
final
final2
```

---

# 51. NO UNRELATED CHANGES

When implementing a task, do not silently modify unrelated files or systems.

If an unrelated change is necessary:

1. explain why
2. identify the dependency
3. keep the change minimal

---

# 52. AI CHANGE CONTROL

AI MUST NOT:

* rewrite architecture without approval
* replace libraries without reason
* create duplicate components
* introduce a new state-management system casually
* introduce a new styling system casually
* bypass API boundaries
* bypass validation
* bypass authorization
* disable lint/type checks to finish faster
* hide errors
* generate fake functionality
* silently modify unrelated features

---

# 53. AI IMPLEMENTATION LOOP

For each task:

```text
Read
 ↓
Understand
 ↓
Inspect
 ↓
Plan
 ↓
Implement
 ↓
Type Check
 ↓
Lint
 ↓
Test
 ↓
Build
 ↓
Review
```

If a step fails, fix it before claiming completion.

---

# 54. COMPLETION REPORT

When a coding task is completed, report:

```text
Implemented:
- ...

Changed:
- ...

Tests:
- ...

Validation:
- ...

Known limitations:
- ...
```

Never report "complete" when important known work remains.

---

# 55. DEFINITION OF DONE

Code is complete only when:

* Architecture is respected
* Types are valid
* No unjustified `any`
* No duplicate business logic
* No fake functionality
* Errors are handled
* Loading/empty/error states exist where needed
* Security boundaries are respected
* Relevant tests exist
* Lint passes
* Type checking passes
* Build passes
* Design System rules are respected
* No unrelated changes were introduced

---

# 56. SOURCE OF AUTHORITY

These rules are informed by:

* React official Rules of React
* React official Hooks guidance
* TypeScript strict type checking
* Google Engineering Practices
* Conventional Commits 1.0.0
* The project's `ARCHITECTURE.md`
* The project's `DESIGN_SYSTEM.md`
* The project's security, API, database and testing rules

Project-specific rules may extend these rules through the appropriate project specification or architecture decision.

---

# 57. FINAL RULE

The AI must optimize for:

```text
Correctness
+
Clarity
+
Maintainability
+
Reusability
+
Type Safety
+
Testability
+
Security
```

NOT:

```text
Fastest possible code generation.
```

If the easiest implementation violates the architecture, Design System or security model, it MUST NOT be used.
