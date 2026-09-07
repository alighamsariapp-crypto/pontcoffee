# Backend Development Skill

## Purpose

This skill defines how the AI executes backend development for a feature.

It works under the project's existing architecture, API, database, security, coding, and testing rules.

This skill defines the execution process, not those rules.

---

## 1. Start From the Feature

Identify the backend responsibilities of the current feature:

* Required business operations
* Required server-side data
* Required permissions
* Required API operations
* Required database operations
* External service dependencies
* Expected success and failure outcomes

Do not implement backend functionality unrelated to the current feature.

---

## 2. Inspect Before Changing

Before writing backend code, inspect:

* Server structure
* Existing routes
* Controllers/handlers
* Services/use cases
* Domain logic
* Repositories/data-access layer
* Validation schemas
* Authentication middleware
* Authorization middleware
* Database services
* External integrations
* Error handling
* Existing tests

Reuse established backend patterns whenever possible.

---

## 3. Define the Server Flow

Determine the complete server-side path:

```text id="7h2m4k"
Request
→ Authentication
→ Authorization
→ Validation
→ Use Case / Business Logic
→ Data Access
→ Database / External Service
→ Response
```

The exact layers may differ according to the project's architecture.

Do not bypass established boundaries without a documented reason.

---

## 4. Implement Business Logic

Business rules must be executed on the server when they affect:

* authorization
* prices
* discounts
* inventory
* orders
* payments
* ownership
* state transitions
* other security-sensitive or authoritative operations

Keep business logic independent from transport-specific details where practical.

Do not duplicate the same business rule across multiple endpoints.

---

## 5. Validate Server Input

For every externally supplied input:

```text id="9x4m2p"
Receive
→ Validate
→ Normalize if required
→ Process
```

Never assume that frontend validation is sufficient.

Use the project's established validation and error mechanisms.

---

## 6. Protect the Operation

For protected functionality, verify:

* Authentication requirement
* Required permission
* Resource ownership where applicable
* Property-level restrictions where applicable
* Server-authoritative values
* Cross-user access boundaries

Authorization must not depend on the frontend.

---

## 7. Connect Data Correctly

When persistence is required:

```text id="u1c8qa"
Use Case
→ Repository / Data Access
→ Database
```

Do not place database operations directly inside route definitions when the architecture provides a separate data-access boundary.

Do not introduce temporary in-memory persistence for production functionality.

---

## 8. Handle Transactions and Concurrency

When an operation changes multiple related pieces of state, determine whether atomicity or concurrency protection is required.

Examples include:

* inventory updates
* order creation
* payment state changes
* counters
* related document updates

Use the project's database rules and established transaction patterns.

Ensure retry-sensitive operations are safe.

---

## 9. Handle Errors Explicitly

Backend operations should distinguish applicable failure types, such as:

```text id="v8k3ld"
Validation
Authentication
Authorization
Not Found
Conflict
Business Rule
Rate Limit
Dependency Failure
Unexpected Server Error
```

Return the established API error structure.

Do not expose internal implementation details or sensitive information.

---

## 10. Integrate External Services Carefully

If the feature uses an external service:

```text id="z6q1wr"
Backend
→ External Service
→ Verify Result
→ Apply Business Rules
→ Persist Result
→ Respond
```

Do not trust external responses blindly.

Handle:

* timeout
* unavailable service
* invalid response
* retry behavior
* duplicate requests
* partial failure

according to the project's API, database, and security rules.

---

## 11. Test the Backend Flow

Run the applicable tests defined by `TESTING_RULES.md`.

Verify:

* successful operation
* invalid input
* unauthorized access
* forbidden access
* missing resources
* business-rule failures
* database behavior
* transaction/concurrency behavior where relevant
* external-service failures where relevant
* regression behavior

Do not test only the happy path.

---

## 12. Verify Frontend Integration

When the feature has a frontend:

```text id="3r6v8n"
Frontend Request
→ Backend
→ Database / Service
→ Backend Response
→ Frontend Behavior
```

Verify the actual end-to-end feature path.

A backend endpoint existing is not evidence that integration is complete.

---

## 13. Backend Completion Gate

Before marking the backend portion complete:

```text id="k9w4sf"
[ ] Feature scope respected
[ ] Existing backend patterns inspected
[ ] Business logic implemented
[ ] Input validation implemented
[ ] Authorization enforced
[ ] Database/service integration complete
[ ] Required transactions handled
[ ] Errors handled
[ ] Tests pass
[ ] Frontend integration verified where applicable
[ ] No known blocker remains
```

---

## 14. Change Control

Keep backend changes focused.

Do not:

* rewrite unrelated services
* introduce a new architecture without need
* duplicate existing infrastructure
* silently change API contracts
* silently change database behavior
* hide incomplete functionality behind mocks

If a broader change is required, document the reason before expanding scope.

---

## Operating Principle

> **Backend work is complete only when the server correctly validates, authorizes, executes, persists, and exposes the feature's real behavior.**
