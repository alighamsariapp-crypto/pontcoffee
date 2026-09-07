# API Development Skill

## Purpose

This skill defines how the AI designs, implements, integrates, and verifies API functionality for a feature.

It operates under the project's existing:

* `API_RULES.md`
* `ARCHITECTURE.md`
* `SECURITY_RULES.md`
* `DATABASE_RULES.md`
* `CODING_RULES.md`
* `TESTING_RULES.md`

Those files define the requirements.
This skill defines the execution workflow.

---

## 1. Identify API Responsibility

For the current feature, determine:

* What operations require an API
* Who can call them
* What data is submitted
* What data is returned
* Which business operation is executed
* Which database or external service is involved

Do not create endpoints without a real feature requirement.

---

## 2. Inspect Existing API

Before creating or changing an endpoint, inspect:

* Existing routes
* API versioning
* Request/response schemas
* Controllers/handlers
* Services/use cases
* Authentication
* Authorization
* Error handling
* Pagination patterns
* Validation utilities
* API tests
* Existing client integration

Reuse established API patterns.

---

## 3. Define the Contract First

For each endpoint define:

```text id="x7k3qa"
Method
→ Path
→ Authentication
→ Authorization
→ Request
→ Validation
→ Response
→ Errors
```

The contract must be clear before implementation.

If the project maintains an OpenAPI specification, update it as part of the API change.

---

## 4. Map the API to the Feature

Determine the complete operation:

```text id="m4p8cz"
Frontend
→ API Request
→ Route
→ Validation
→ Authorization
→ Use Case
→ Data Access / External Service
→ Response
```

The endpoint should expose a business capability, not leak internal implementation details.

---

## 5. Implement Request Handling

Process requests in a predictable sequence:

```text id="q9v2ls"
Receive
→ Authenticate
→ Authorize
→ Validate
→ Execute
→ Return
```

Do not trust:

* IDs
* roles
* prices
* permissions
* ownership claims
* client-calculated totals
* other security-sensitive values

when the server can determine them authoritatively.

---

## 6. Control Input and Output

For request data:

* Accept only required fields.
* Validate externally supplied values.
* Reject unexpected or unauthorized fields where applicable.

For responses:

* Return only required data.
* Use established DTO/response structures.
* Do not expose internal database structures unnecessarily.

---

## 7. Implement Errors Consistently

Map expected failures to the project's API error conventions.

Consider applicable cases:

```text id="b6r1wd"
400 / Validation
401 / Authentication
403 / Authorization
404 / Not Found
409 / Conflict
429 / Rate Limit
5xx / Server or Dependency Failure
```

Do not expose stack traces, secrets, internal paths, or sensitive implementation details.

---

## 8. Handle Lists and Search

When an endpoint returns collections, determine:

* Pagination
* Maximum page size
* Filtering
* Sorting
* Search behavior
* Empty results
* Query limits

Follow existing project conventions rather than introducing a different pattern for one endpoint.

---

## 9. Handle Mutations

For create/update/delete operations, determine whether the operation requires:

* Idempotency
* Transaction
* Concurrency protection
* State-transition validation
* Duplicate-request protection

This is especially important for operations involving orders, payments, inventory, or other business-critical state.

---

## 10. Connect the Real Client

After implementing an endpoint, connect the actual frontend data layer.

Verify:

```text id="n5c8rt"
User Interaction
→ Frontend Request
→ API
→ Backend
→ Database / Service
→ API Response
→ Frontend State
→ UI Result
```

Do not leave an endpoint unused while the UI continues using mock data.

---

## 11. Test the Contract

Run applicable API tests.

Verify:

* Valid request
* Invalid request
* Missing required data
* Unauthorized request
* Forbidden request
* Missing resource
* Business-rule failure
* Conflict/duplicate request
* Pagination/filtering where applicable
* Server/dependency failure
* Response shape

Also verify the frontend integration when applicable.

---

## 12. Verify API Security

Before completion, verify the endpoint against the project's security requirements.

Pay particular attention to:

* Function-level authorization
* Object-level authorization
* Property-level authorization
* Input validation
* Sensitive data exposure
* Resource consumption
* Rate limiting
* SSRF where applicable
* Unsafe external integrations

Use `SECURITY_RULES.md` as the authoritative security reference.

---

## 13. API Completion Gate

Before marking API work complete:

```text id="z4q7hn"
[ ] Endpoint has a defined contract
[ ] Existing API patterns inspected
[ ] Request validation implemented
[ ] Authorization verified
[ ] Response contract implemented
[ ] Error behavior implemented
[ ] Pagination/filtering handled where required
[ ] Idempotency/concurrency considered where required
[ ] Real database/service integration complete
[ ] Frontend connected where applicable
[ ] API tests pass
[ ] Security checks pass
```

---

## 14. Change Control

Keep API changes focused.

Do not:

* create duplicate endpoints
* silently break existing consumers
* change response structures without considering compatibility
* expose database internals unnecessarily
* bypass authentication or authorization
* create mock endpoints as substitutes for real functionality

If a breaking API change is genuinely required, document it before implementation.

---

## Operating Principle

> **An API is complete only when its contract, validation, authorization, business operation, data flow, client integration, and verification all work together.**
