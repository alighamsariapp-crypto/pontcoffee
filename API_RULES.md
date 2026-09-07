# API RULES

## 1. PURPOSE

This document defines the mandatory rules for all application APIs.

It controls:

* API architecture
* Endpoint design
* HTTP methods
* Request contracts
* Response contracts
* Validation
* Authentication
* Authorization
* Error handling
* Pagination
* Filtering
* Sorting
* Rate limiting
* Idempotency
* API versioning
* Security
* Logging
* Observability
* API testing
* Frontend/API integration

The API is a formal contract between application layers.

---

# 2. CORE PRINCIPLE

The API is NOT simply a collection of URLs.

It is a controlled contract:

```text
Client
↓
HTTP Request
↓
Authentication
↓
Authorization
↓
Validation
↓
Application / Business Logic
↓
Database / External Service
↓
Response Contract
↓
Client
```

Every production endpoint MUST follow this boundary.

---

# 3. NO FAKE API

Production APIs MUST NOT return fake success responses.

Prohibited:

```text
❌ Hardcoded JSON
❌ Fake CRUD
❌ Fake database response
❌ Simulated order creation
❌ Fake payment success
❌ Fake inventory response
❌ Fake authentication
❌ Fake authorization
❌ Random generated production data
```

Mock APIs are allowed only for:

* automated tests
* local development
* explicit prototypes

and MUST be isolated from production code.

---

# 4. API CONTRACT FIRST

Before implementing an endpoint, define:

```text
Endpoint
HTTP method
Authentication
Authorization
Request parameters
Request body
Validation
Response
Error responses
Side effects
Idempotency
Pagination
Rate limits
```

The API contract MUST be known before implementation.

---

# 5. API SPECIFICATION

Projects SHOULD maintain a machine-readable API specification.

Recommended standard:

```text
OpenAPI
```

The specification should describe applicable:

* paths
* methods
* parameters
* request bodies
* response schemas
* authentication
* errors
* reusable schemas

The API implementation MUST NOT silently diverge from the documented contract.

---

# 6. HTTP METHODS

Use HTTP methods according to their intended semantics.

Typical REST mapping:

```text
GET
→ retrieve

POST
→ create / trigger a non-idempotent operation

PUT
→ replace/update a resource

PATCH
→ partially update a resource

DELETE
→ remove a resource
```

Do not use `POST` for everything simply because it is convenient.

---

# 7. RESOURCE-ORIENTED ENDPOINTS

Prefer predictable resource-oriented URLs.

Example:

```text
GET    /api/v1/products
GET    /api/v1/products/:id
POST   /api/v1/products
PATCH  /api/v1/products/:id
DELETE /api/v1/products/:id
```

Avoid unclear endpoints such as:

```text
/api/doProductThing
/api/processData
/api/updateEverything
```

unless the endpoint represents a genuine domain action.

---

# 8. DOMAIN ACTIONS

Some operations are actions rather than simple CRUD.

Examples:

```text
POST /api/v1/orders/:id/cancel
POST /api/v1/orders/:id/confirm
POST /api/v1/orders/:id/pay
POST /api/v1/inventory/:id/adjust
```

Domain actions MUST:

* have explicit authorization
* validate state transitions
* validate input
* be server-authoritative
* define side effects
* be safe against unintended repetition where required

---

# 9. API VERSIONING

Production APIs SHOULD have an explicit versioning strategy.

Example:

```text
/api/v1/...
```

Versioning must be consistent.

Do not introduce incompatible breaking changes to a public API without an intentional versioning/migration strategy.

---

# 10. REQUEST VALIDATION

Every external request MUST be validated server-side.

Validate:

* path parameters
* query parameters
* headers where relevant
* request body
* arrays
* nested objects
* strings
* numbers
* dates
* enums
* pagination values
* filtering values
* sorting values

Never trust frontend validation.

---

# 11. VALIDATION ORDER

Preferred flow:

```text
Request
↓
Parse
↓
Authentication
↓
Authorization
↓
Validation
↓
Business Rules
↓
Database / Service
↓
Response
```

The exact order may vary for security or performance reasons, but authorization and validation MUST NOT be accidentally bypassed.

---

# 12. SCHEMA VALIDATION

Request and response schemas SHOULD be explicit.

Example:

```text
CreateProductRequest
UpdateProductRequest
ProductResponse
ProductListResponse
ErrorResponse
```

Do not pass arbitrary objects between API layers.

---

# 13. MASS ASSIGNMENT PROTECTION

Do NOT automatically bind the entire client payload to a database object.

Bad:

```text
PATCH /users/:id

{
  "name": "...",
  "role": "super-admin",
  "permissions": [...]
}
```

when the user is only allowed to change their name.

Use explicit allowlists.

Example:

```text
Allowed fields:
name
phone
avatar
```

Sensitive fields must be controlled server-side.

---

# 14. RESPONSE MINIMIZATION

Return only the fields required by the client/use case.

Do NOT automatically serialize an entire database object.

Never expose sensitive/internal fields accidentally.

Examples of potentially restricted fields:

```text
passwordHash
internalNotes
permissions
securityFlags
privateTokens
internalMetadata
paymentSecrets
```

Response DTOs SHOULD explicitly define what is exposed.

OWASP specifically identifies excessive exposure and unauthorized property access as API security risks.

---

# 15. RESPONSE CONTRACT

Responses MUST have predictable structures.

Example:

```json
{
  "data": {},
  "meta": {}
}
```

or the project's explicitly defined equivalent.

The project MUST choose one consistent response convention.

Do not randomly mix:

```text
{ data: ... }

{ result: ... }

{ payload: ... }

{ item: ... }
```

without a documented reason.

---

# 16. LIST RESPONSES

List endpoints SHOULD have a consistent structure.

Example:

```json
{
  "data": [],
  "pagination": {
    "hasNextPage": true,
    "nextCursor": "..."
  }
}
```

The exact structure is project-specific.

Consistency is mandatory.

---

# 17. PAGINATION

Large collections MUST be paginated.

The server MUST enforce maximum page size.

Example:

```text
?page=1&limit=20
```

or cursor-based pagination:

```text
?cursor=...
&limit=20
```

The client MUST NOT be allowed to request unlimited records.

OWASP identifies unrestricted response size/resource consumption as an API risk.

---

# 18. CURSOR PAGINATION

Cursor-based pagination SHOULD be preferred for large or frequently changing datasets when supported by the database.

Cursors MUST NOT expose sensitive internal information.

Avoid building cursors from secret or private data.

---

# 19. FILTERING

Filtering MUST use an explicit allowlist.

Example:

```text
/products?category=networking&status=active
```

Do not allow arbitrary database expressions to pass from the client.

---

# 20. SORTING

Sorting fields MUST be allowlisted.

Example:

```text
?sort=createdAt
&order=desc
```

Do NOT allow the client to inject arbitrary database field expressions.

---

# 21. SEARCH

Search endpoints MUST enforce:

* maximum query length
* pagination
* allowed searchable fields
* rate limits where appropriate
* safe query construction

Do not pass raw search syntax directly to the database.

---

# 22. RESPONSE SIZE LIMITS

Every API should define reasonable limits for:

* request body size
* response size
* page size
* array size
* string length
* file upload size
* batch operation size

Limits MUST reflect business requirements.

---

# 23. RATE LIMITING

Rate limiting MUST be applied where resource consumption or abuse is possible.

High-risk examples:

```text
login
password reset
OTP
search
file upload
email sending
SMS
coupon validation
payment creation
bulk operations
admin actions
```

Limits should be based on:

* endpoint
* user
* IP
* authentication state
* business risk

where appropriate.

---

# 24. RESOURCE CONSUMPTION

APIs MUST protect expensive operations.

Limit:

```text
CPU-heavy operations
memory-heavy operations
large payloads
large result sets
batch size
file uploads
external API calls
database reads/writes
```

OWASP API4 specifically recommends limits for request size, number of records, interaction frequency and expensive operations.

---

# 25. AUTHENTICATION

Protected endpoints MUST verify authentication.

Authentication MUST happen server-side.

Do NOT trust:

```text
userId
role
email
permissions
isAdmin
```

provided by the client as proof of identity or authority.

---

# 26. AUTHORIZATION

Authentication answers:

```text
Who are you?
```

Authorization answers:

```text
What are you allowed to do?
```

Both are required where applicable.

---

# 27. FUNCTION-LEVEL AUTHORIZATION

Every protected endpoint MUST explicitly enforce the required permission.

Do NOT rely on the frontend hiding a button.

Example:

```text
DELETE /api/v1/products/:id
```

must independently verify the caller can delete products.

OWASP identifies missing function-level authorization as a major API security risk.

---

# 28. OBJECT-LEVEL AUTHORIZATION

Authorization MUST also verify access to the specific resource.

Example:

```text
GET /api/v1/orders/123
```

must verify that the current user is allowed to access order `123`.

Being authenticated does NOT automatically grant access to every object.

---

# 29. PROPERTY-LEVEL AUTHORIZATION

Authorization may also apply to individual fields.

Example:

```text
User:
name
email

Admin:
name
email
role
permissions
internalNotes
```

The API MUST NOT expose or accept protected fields simply because the underlying object contains them.

---

# 30. ADMIN APIs

Administrative endpoints MUST have explicit authorization.

Do not assume:

```text
/api/admin/*
```

is automatically secure.

Security must be enforced by authorization middleware/business rules, not URL naming.

---

# 31. DEFAULT DENY

Authorization SHOULD follow:

```text
Deny by default
↓
Explicit permission
↓
Allow
```

Do not create broad access and attempt to remove permissions afterward.

---

# 32. AUTHORIZATION MATRIX

Projects with multiple roles SHOULD maintain a permission matrix.

Example:

```text
Role
+
Resource
+
Action
=
Permission
```

Example:

```text
admin
products
create
```

Do not scatter role checks throughout random controllers.

---

# 33. ERROR STATUS CODES

Use HTTP status codes according to their semantics.

Typical baseline:

```text
200 OK
201 Created
202 Accepted
204 No Content

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Content
429 Too Many Requests

500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

The exact use of each status must remain consistent.

HTTP status codes communicate the class and result of the request.

---

# 34. 401 VS 403

Use:

```text
401
```

when authentication is required or invalid.

Use:

```text
403
```

when the caller is authenticated but is not allowed to perform the operation.

Do not randomly use one for the other.

---

# 35. 404 VS AUTHORIZATION

Resource existence and authorization must be handled intentionally.

For sensitive resources, the API may choose not to reveal whether an unauthorized resource exists.

The behavior MUST be consistent with the security model.

---

# 36. ERROR RESPONSE

Errors MUST use a predictable structure.

Example:

```json
{
  "error": {
    "code": "PRODUCT_NOT_FOUND",
    "message": "Product not found.",
    "details": {}
  }
}
```

The exact structure is project-specific.

---

# 37. ERROR CODES

Business/application errors SHOULD have stable machine-readable codes.

Example:

```text
PRODUCT_NOT_FOUND
INVALID_COUPON
INSUFFICIENT_INVENTORY
ORDER_ALREADY_CANCELLED
PERMISSION_DENIED
VALIDATION_FAILED
```

Do not make frontend logic depend on human-readable messages.

---

# 38. ERROR MESSAGES

User-facing messages MUST NOT expose:

* stack traces
* SQL/database errors
* internal paths
* secret values
* tokens
* infrastructure details

Detailed technical information belongs in logs.

---

# 39. VALIDATION ERRORS

Validation failures SHOULD identify the affected fields.

Example:

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "fields": {
      "email": "Invalid email address.",
      "quantity": "Quantity must be greater than zero."
    }
  }
}
```

---

# 40. IDEMPOTENCY

Operations that create financial, order, inventory or other important side effects SHOULD support idempotency when retries could cause duplication.

Example:

```text
POST /api/v1/orders
Idempotency-Key: <unique-key>
```

The server MUST ensure the same logical request does not unintentionally create multiple side effects.

Idempotency is especially important when clients retry after network failures. Established payment APIs use this pattern for safe retries.

---

# 41. IDEMPOTENCY KEY RULES

For endpoints using idempotency:

* key must be unique
* key must have a defined lifetime
* same key + different payload should be rejected
* stored result behavior must be defined
* concurrent requests must be handled safely

Do not treat an idempotency key as a generic request ID.

---

# 42. RETRIES

Clients may retry transient failures.

Servers MUST distinguish:

```text
Retryable
Non-retryable
```

operations.

Do NOT blindly retry:

```text
payment creation
order creation
inventory mutation
external side effect
```

without idempotency protection.

---

# 43. TRANSACTIONS AND API OPERATIONS

When an API operation changes multiple pieces of critical state, the backend MUST use the appropriate transaction/atomic mechanism.

Example:

```text
Create Order
+
Decrease Inventory
+
Apply Coupon
```

must have a defined consistency strategy.

The API MUST NOT report success if required persistence failed.

---

# 44. EXTERNAL SERVICES

When an API calls another service:

```text
API
↓
External Service
```

must define:

* timeout
* retry strategy
* error handling
* authentication
* response validation
* rate limits
* fallback behavior
* logging

Do not trust third-party responses blindly.

---

# 45. THIRD-PARTY API RESPONSES

External responses MUST be validated before entering business logic.

Never assume:

```text
externalResponse.data
```

has the shape the application expects.

---

# 46. TIMEOUTS

External and expensive operations MUST have explicit timeouts.

An API request must not remain indefinitely blocked because an external service is unavailable.

---

# 47. WEBHOOKS

Webhooks MUST be treated as untrusted external input.

Webhook handling should include:

* signature verification
* authentication
* payload validation
* replay protection where applicable
* idempotent processing
* event logging
* safe retry handling

Never trust a webhook merely because it reaches a known URL.

---

# 48. FILE UPLOAD APIs

File uploads MUST enforce:

* authentication
* authorization
* maximum size
* allowed types
* filename rules
* content validation
* storage rules
* abuse protection

Do not trust the file extension alone.

---

# 49. BULK APIs

Bulk endpoints MUST have explicit limits.

Example:

```text
POST /products/bulk
```

must define:

```text
maximum records
maximum payload
authorization
validation
partial failure behavior
transaction behavior
rate limits
```

Do not allow unlimited bulk operations.

---

# 50. CACHING

Caching MUST be intentional.

Do not cache:

* private data
* authorization-sensitive responses
* user-specific information

without a defined caching policy.

Cache invalidation rules must be explicit.

---

# 51. CORS

CORS MUST be explicitly configured.

Do NOT use unrestricted origins in production without a documented reason.

Avoid:

```text
Access-Control-Allow-Origin: *
```

for authenticated/private APIs when credentials are involved.

---

# 52. SECURITY HEADERS

Production APIs should use appropriate HTTP security headers according to the application architecture.

Security headers MUST be configured centrally rather than randomly per endpoint.

---

# 53. REQUEST IDs

Every API request SHOULD have a traceable request/correlation identifier.

Example:

```text
X-Request-ID
```

The exact header is project-specific.

Request IDs help correlate:

```text
Client
↓
API
↓
Database
↓
External Service
↓
Logs
```

Do not use request IDs as authorization credentials.

---

# 54. LOGGING

API logs SHOULD capture enough information to diagnose failures.

Useful information:

```text
request ID
endpoint
method
status
duration
authenticated subject where appropriate
error code
```

Do NOT log:

```text
passwords
tokens
private keys
payment secrets
full sensitive payloads
```

---

# 55. API OBSERVABILITY

Monitor:

* error rate
* latency
* throughput
* rate-limit events
* authentication failures
* authorization failures
* external service failures
* database failures

Important endpoints SHOULD have defined operational expectations.

---

# 56. API TESTING

Every important endpoint MUST have tests covering applicable:

```text
success
validation failure
unauthenticated access
unauthorized access
object ownership
invalid parameters
empty result
not found
conflict
rate limiting
server failure
```

Security tests are not optional for security-sensitive endpoints.

---

# 57. CONTRACT TESTING

Where practical, API contract tests SHOULD verify:

```text
Request schema
Response schema
Status codes
Error schema
Authentication behavior
Authorization behavior
```

The frontend and backend MUST agree on the same contract.

---

# 58. API DOCUMENTATION

Every production endpoint SHOULD document:

* purpose
* method
* path
* authentication
* permissions
* request schema
* response schema
* errors
* pagination
* limits
* side effects

Undocumented production APIs are difficult to maintain safely.

---

# 59. AI API RULES

AI MUST NOT:

```text
❌ create fake endpoints
❌ return hardcoded production data
❌ bypass authentication
❌ bypass authorization
❌ trust client roles
❌ trust client prices
❌ trust client totals
❌ accept arbitrary object fields
❌ expose entire database objects
❌ return unlimited records
❌ omit validation
❌ omit error handling
❌ ignore rate limits for sensitive operations
❌ create duplicate endpoints for existing functionality
❌ silently change API contracts
❌ claim API integration is complete without testing
```

---

# 60. API IMPLEMENTATION LOOP

For every endpoint:

```text
Requirement
↓
API Contract
↓
Authentication
↓
Authorization
↓
Request Validation
↓
Business Logic
↓
Database / External Service
↓
Response Mapping
↓
Error Mapping
↓
Rate / Resource Limits
↓
Tests
↓
Documentation
```

---

# 61. DEFINITION OF DONE

An API feature is complete only when:

* Endpoint contract is defined
* Request validation exists
* Response schema exists
* Authentication is correct
* Authorization is correct
* Object-level access is correct
* Property-level access is correct where applicable
* Errors use consistent status codes
* Error structure is consistent
* Pagination exists where needed
* Resource limits exist
* Rate limiting exists where required
* Idempotency exists where required
* External services are validated
* Database operations are correctly integrated
* Tests pass
* Documentation is updated
* No fake production behavior exists

---

# 62. SOURCE OF AUTHORITY

These rules are informed by:

* IETF RFC 9110 HTTP Semantics
* OpenAPI Specification
* OWASP API Security Top 10
* OWASP Application Security Verification Standard
* Firebase/Google Cloud API and security practices
* The project's `ARCHITECTURE.md`
* The project's `DATABASE_RULES.md`
* The project's `SECURITY_RULES.md`

Project-specific API requirements may extend these rules through `PROJECT_SPEC.md`.

---

# 63. FINAL RULE

An API is NOT complete because:

```text
The endpoint returns 200.
```

An API is complete only when:

```text
Contract
+
Validation
+
Authentication
+
Authorization
+
Business Logic
+
Persistence
+
Error Handling
+
Resource Protection
+
Testing
+
Documentation
```

are correctly implemented.

The API MUST be treated as a security boundary and a long-term contract.
