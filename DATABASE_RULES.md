# DATABASE RULES

## 1. PURPOSE

This document defines mandatory rules for database architecture and implementation.

It controls:

* Data modeling
* Collections and documents
* Relationships
* Validation
* Database access
* Queries
* Indexes
* Transactions
* Atomic writes
* Security
* Authorization
* Migrations
* Data integrity
* Performance
* Pagination
* Auditing
* Backup/recovery considerations
* Frontend/backend database boundaries

These rules apply to all production database implementations.

---

# 2. CORE PRINCIPLE

The database is a production system, not a temporary storage layer.

A feature is NOT complete when:

```text
UI exists
+
mock data exists
```

A feature is complete only when:

```text
UI
↓
API / Application Layer
↓
Validation
↓
Database Operation
↓
Persistence
↓
Response
↓
UI State
```

is fully connected and verified.

---

# 3. NO MOCK DATABASE IN PRODUCTION

The following are prohibited as production implementations:

```text
❌ In-memory arrays
❌ Hardcoded database objects
❌ Fake CRUD
❌ Fake persistence
❌ Local-only production storage
❌ Mock success responses
❌ Fake inventory
❌ Fake orders
❌ Fake users
❌ Fake payment records
```

Mocks may only exist in:

* tests
* development fixtures
* explicit prototypes

and MUST be clearly isolated from production code.

---

# 4. DATABASE SOURCE OF TRUTH

Each persistent entity MUST have one authoritative source of truth.

Example:

```text
Product
→ Database

Order
→ Database

User
→ Database

Inventory
→ Database
```

Do not maintain conflicting copies of the same authoritative data in:

* frontend state
* localStorage
* hardcoded constants
* multiple unrelated collections

Caching is allowed only when its synchronization strategy is explicit.

---

# 5. DATABASE TECHNOLOGY

The database technology is project-specific.

The project MUST define:

* database engine
* hosting
* environment
* access method
* schema/data model
* security model
* backup strategy
* migration strategy
* testing strategy

For Cloud Firestore projects, these rules apply to:

* collections
* documents
* subcollections
* queries
* indexes
* transactions
* batched writes
* Security Rules
* Firebase Authentication
* server-side IAM

---

# 6. FIRESTORE DATA MODEL

For Cloud Firestore:

```text
Collection
    ↓
Document
    ↓
Fields
    ↓
Subcollection
    ↓
Document
```

Collections MUST NOT contain raw fields directly.

Documents MUST NOT contain collections directly.

Use subcollections when hierarchical data is genuinely related to a parent document.

---

# 7. DOCUMENT DESIGN

Firestore documents should generally remain focused and appropriately sized.

Do NOT create giant documents containing an entire application state.

Bad:

```text
users
└── one-document-containing-everything
```

Prefer separate entities and subcollections where the data has different lifecycle, access, query or scaling requirements.

---

# 8. COLLECTION NAMING

Collection names MUST be:

* predictable
* consistent
* plural where the project convention requires it
* documented

Example:

```text
users
products
categories
orders
inventory
reviews
coupons
```

Do not randomly mix:

```text
product
products
Product
Products
```

within the same database.

---

# 9. FIELD NAMING

Field names MUST use one consistent naming convention.

Recommended:

```text
camelCase
```

Example:

```text
createdAt
updatedAt
productId
userId
orderStatus
unitPrice
```

Avoid inconsistent forms:

```text
created_at
createdAt
CreatedAt
created-date
```

in the same system.

---

# 10. IDENTIFIERS

Every persistent entity MUST have a stable unique identifier.

Identifiers MUST NOT depend on display names.

Bad:

```text
productId = "Samsung Router"
```

Better:

```text
productId = generatedStableId
```

Display names may change.

Identifiers should generally remain stable.

---

# 11. FIRESTORE DOCUMENT IDs

For Firestore:

* Do not use `/` in document IDs.
* Do not use `.` or `..`.
* Avoid predictable monotonically increasing IDs for high-write collections.
* Prefer generated/random IDs where appropriate.
* Use domain identifiers only when they are intentionally designed and safe.

Sequential IDs can create hotspotting under high write workloads.

---

# 12. REFERENCES BETWEEN ENTITIES

Relationships MUST be explicit.

Examples:

```text
productId
categoryId
userId
orderId
```

When using Firestore references, use them consistently according to the project's data model.

Do not create undocumented relationships through arbitrary field names.

---

# 13. DENORMALIZATION

NoSQL databases may require intentional denormalization.

Denormalized data is allowed only when:

* the reason is documented
* ownership is clear
* update synchronization is defined
* consistency requirements are understood

Example:

```text
Order
├── productId
├── productNameSnapshot
├── unitPriceSnapshot
└── ...
```

A historical order may intentionally store snapshots of product information.

This is different from accidental duplication.

---

# 14. DATA OWNERSHIP

Every field MUST have a clear owner.

For example:

```text
price
→ Product/Admin domain

inventory
→ Inventory domain

orderTotal
→ Order/Pricing domain
```

The frontend MUST NOT become the authoritative owner of business-critical values.

---

# 15. SERVER-AUTHORITATIVE VALUES

The server/database boundary MUST control business-critical values.

Examples:

```text
price
discount
inventory
orderTotal
shippingCost
tax
permissions
roles
paymentStatus
orderStatus
```

The client may submit an intention.

The server determines the authoritative result.

---

# 16. CLIENT DATA MUST BE UNTRUSTED

All client-provided data MUST be treated as untrusted.

Validate:

* IDs
* strings
* numbers
* enums
* dates
* quantities
* filters
* sorting parameters
* uploaded metadata
* nested objects
* arrays

Never assume that because TypeScript accepts a value, the database should accept it.

---

# 17. RUNTIME VALIDATION

TypeScript types do not provide runtime validation.

Database writes MUST validate input at the application boundary.

Recommended flow:

```text
Request
↓
Authentication
↓
Authorization
↓
Validation
↓
Business Rules
↓
Database Operation
```

Invalid data MUST be rejected before persistence.

---

# 18. DATABASE SCHEMA CONTRACT

Even schemaless databases require a documented data contract.

For every important entity define:

```text
Entity
Fields
Types
Required fields
Optional fields
Defaults
Relationships
Allowed values
Ownership
Indexes
Security
Lifecycle
```

Firestore being schemaless does NOT mean the application may use undocumented or inconsistent data shapes.

---

# 19. REQUIRED VS OPTIONAL FIELDS

Every important field MUST be intentionally classified:

```text
Required
Optional
Nullable
Computed
Server-controlled
Client-controlled
Immutable
Mutable
```

Do not allow accidental `undefined`/missing-field states.

---

# 20. ENUM FIELDS

Fields representing finite states MUST use controlled values.

Example:

```text
orderStatus:
pending
confirmed
processing
shipped
delivered
cancelled
```

Do not allow arbitrary strings when the domain has a fixed state machine.

---

# 21. STATUS TRANSITIONS

Important status fields MUST have defined valid transitions.

Example:

```text
pending
 ↓
confirmed
 ↓
processing
 ↓
shipped
 ↓
delivered
```

Invalid transitions MUST be rejected.

The frontend MUST NOT be trusted to enforce status transitions.

---

# 22. TIMESTAMPS

Important persistent entities SHOULD include appropriate timestamps.

Common fields:

```text
createdAt
updatedAt
```

Domain-specific timestamps may include:

```text
publishedAt
cancelledAt
paidAt
shippedAt
completedAt
```

Use a consistent timestamp representation throughout the project.

---

# 23. IMMUTABLE DATA

Certain values should become immutable after creation.

Examples:

```text
orderNumber
paymentTransactionId
historicalPrice
createdAt
userId
```

If a value must never change, enforce that rule at the appropriate server/database boundary.

---

# 24. SOFT DELETE

Soft deletion may be used when historical records must remain available.

Example:

```text
deletedAt
isDeleted
```

If soft delete is used:

* queries must consistently account for it
* indexes must account for common filters
* authorization must remain correct
* admin recovery behavior must be defined

Do not mix hard delete and soft delete randomly.

---

# 25. DELETE CASCADE

Do not assume deleting a Firestore document automatically deletes its subcollections.

If a parent document owns child data, the deletion strategy MUST explicitly define what happens to the child data.

Possible strategies:

```text
Cascade delete
Archive
Soft delete
Retain independently
```

The choice must be intentional.

---

# 26. TRANSACTIONS

Use a transaction when correctness depends on reading current database state before writing.

Examples:

```text
inventory decrement
balance update
counter update
conditional state transition
unique constraint simulation
```

Transactions MUST be used when multiple dependent operations must behave atomically.

Firestore transactions provide atomic read/write behavior.

---

# 27. BATCH WRITES

Use batched writes when multiple writes must be committed atomically but do not require reading current values first.

Example:

```text
Update document A
Update document B
Create document C
Delete document D
```

All should succeed or none should be committed.

---

# 28. TRANSACTION RETRIES

Transaction functions MUST be safe for retry.

Do not place non-idempotent external side effects directly inside transaction callbacks.

Bad:

```text
transaction callback
↓
send payment
↓
send email
```

A transaction may retry.

External side effects should be handled through an appropriate post-commit mechanism.

---

# 29. INVENTORY

Inventory operations MUST be server-authoritative.

Never trust:

```text
clientStock
```

for final inventory decisions.

Inventory changes that depend on current stock MUST use an atomic transaction or equivalent concurrency-safe mechanism.

Example:

```text
Read stock
↓
Verify stock >= requested quantity
↓
Decrease stock
↓
Create/update order
```

must be handled atomically when required by the business rules.

---

# 30. ORDERS

Order creation MUST NOT depend on frontend-calculated totals.

The server MUST calculate or verify:

```text
subtotal
discount
tax
shipping
total
inventory impact
```

The client may provide requested quantities/coupon codes, but the authoritative result comes from trusted backend logic.

---

# 31. PAYMENTS

Payment-related records MUST be treated as high-integrity data.

Never allow the frontend to directly set:

```text
paymentStatus = "paid"
```

or equivalent authoritative payment states.

Payment status MUST be established through trusted server-side verification or payment-provider callbacks.

---

# 32. QUERY DESIGN

Queries MUST be designed around actual product requirements.

Before creating a query determine:

* filters
* sort order
* pagination
* expected result size
* required indexes
* authorization constraints
* performance requirements

Do not retrieve the entire collection and filter it in the frontend when the database can perform the required query.

---

# 33. NO FULL COLLECTION SCANS WITHOUT JUSTIFICATION

Avoid:

```text
get all products
↓
filter in browser
```

for production-scale datasets.

Use server/database filtering and pagination.

Full collection reads require explicit justification.

---

# 34. PAGINATION

Large datasets MUST use pagination.

Prefer cursor-based pagination where supported.

For Firestore, use cursors rather than offsets.

Pagination MUST be consistent between API and UI.

---

# 35. INDEXES

Indexes MUST be treated as part of the database design.

For every important query verify:

```text
query
+
filters
+
sort
+
index
```

Do not blindly create indexes for every field.

Unused indexes increase storage and write overhead.

Firestore automatically manages many basic indexes, while compound queries may require additional indexes.

---

# 36. INDEX REVIEW

When adding an index:

1. Identify the query that requires it.
2. Confirm it is actually used.
3. Confirm the query is necessary.
4. Evaluate write/storage impact.
5. Document the index when appropriate.

Indexes MUST NOT be created blindly just because the database console suggests them.

---

# 37. LARGE ARRAYS / MAPS

Do not place unbounded or very large arrays/maps inside a single Firestore document.

If data can grow continuously:

```text
messages
logs
events
reviews
transactions
```

consider a collection/subcollection instead.

Large arrays/maps can create indexing and document-size/performance problems.

---

# 38. HIGH-WRITE DATA

High-write collections MUST be designed with scalability in mind.

Avoid:

* hotspot-prone sequential IDs
* unnecessary indexed fields
* constantly updating the same document
* unnecessary write amplification

Firestore write performance depends partly on indexing and document access patterns.

---

# 39. READ OPTIMIZATION

Prefer targeted reads.

Do not fetch fields/data the application does not need when the database technology supports appropriate projections or query patterns.

Use caching only when:

* cache ownership is clear
* invalidation is defined
* stale data is acceptable

---

# 40. REAL-TIME LISTENERS

Real-time listeners MUST be used intentionally.

Use them when the feature actually requires real-time updates.

Do not attach listeners to entire collections simply because the database supports realtime updates.

Listeners should:

* be scoped
* unsubscribe correctly
* avoid unnecessary reads
* respect authorization

---

# 41. DATABASE SECURITY

Database security MUST be enforced independently from UI visibility.

Hiding a button does NOT secure data.

Security must exist at the database/application boundary.

---

# 42. FIRESTORE SECURITY RULES

For client-accessible Firestore:

Security Rules MUST define:

* authentication requirements
* ownership
* authorization
* field validation
* allowed operations
* immutable fields
* allowed state changes

Rules MUST be tested.

---

# 43. SERVER-SIDE FIRESTORE ACCESS

Important:

Firestore server SDKs bypass Firestore Security Rules.

When using server-side SDKs:

```text
Application
↓
IAM / server credentials
↓
Firestore
```

must provide the security boundary.

Do not assume Firestore Security Rules protect server SDK operations.

---

# 44. AUTHORIZATION

Authorization MUST be enforced on the server/database boundary.

Examples:

```text
User
→ own data only

Admin
→ permitted administrative resources

Super Admin
→ elevated operations
```

Never trust a role sent from the client.

---

# 45. FIELD-LEVEL PROTECTION

Sensitive fields MUST NOT be freely writable by clients.

Examples:

```text
role
permissions
accountStatus
paymentStatus
inventory
verified
security flags
internal notes
```

Client writes should be explicitly allowlisted where possible.

---

# 46. DATA MINIMIZATION

Do not store sensitive information without a business requirement.

Avoid storing:

* unnecessary personal data
* unnecessary authentication secrets
* unnecessary payment data
* redundant copies of sensitive information

Store only what the application actually needs.

---

# 47. SECRETS

Never store secrets in ordinary application documents.

Do NOT store:

```text
API secret
private key
database password
JWT signing secret
payment secret
service credential
```

inside normal user/product/order documents.

Use the appropriate secret/configuration system.

---

# 48. AUDIT DATA

Security-sensitive or administrative operations SHOULD be auditable where required.

Examples:

```text
admin changed product price
admin changed user role
order status manually changed
inventory manually adjusted
```

Audit records should contain sufficient context to investigate the action without storing unnecessary sensitive information.

---

# 49. MIGRATIONS

Database structure changes MUST have a migration strategy.

Examples:

```text
rename field
change data type
split collection
merge fields
backfill data
remove deprecated field
```

Do not silently change production data shape.

---

# 50. BACKWARD COMPATIBILITY

When deploying application and database changes separately, consider compatibility between old and new application versions.

Prefer safe rollout patterns:

```text
Add
↓
Migrate
↓
Switch
↓
Remove
```

instead of destructive one-step changes when production compatibility matters.

---

# 51. DATABASE TESTING

Database behavior MUST be tested.

Tests SHOULD cover:

* create
* read
* update
* delete
* validation
* authorization
* ownership
* invalid data
* concurrency-sensitive operations
* transactions
* status transitions
* indexes/query behavior where appropriate

---

# 52. SECURITY RULE TESTING

Firestore Security Rules MUST have automated tests where the application relies on client-side Firestore access.

Test at minimum:

```text
Unauthenticated
Authenticated user
Wrong owner
Correct owner
Unauthorized role
Authorized role
Invalid fields
Forbidden field changes
```

---

# 53. DEVELOPMENT DATABASE

Development and production databases MUST be separated.

Never casually connect development tooling to production data.

Use explicit environment configuration.

---

# 54. SEED DATA

Seed data may be used for development/testing.

Seed data MUST be:

* clearly identified
* reproducible
* environment-specific
* safe

Seed data MUST NOT accidentally overwrite production data.

---

# 55. DATABASE ENVIRONMENTS

Where appropriate:

```text
Development
Staging
Production
```

should use separate database resources or clearly isolated namespaces.

Production credentials MUST NOT be embedded in development configuration.

---

# 56. OBSERVABILITY

Database operations should be observable enough to diagnose:

* slow queries
* failed writes
* permission errors
* transaction conflicts
* unexpected read volume
* unexpected write volume

Do not log sensitive database contents unnecessarily.

---

# 57. PERFORMANCE

Performance MUST be measured using actual workload characteristics.

Do not optimize based only on assumptions.

Review:

```text
read count
write count
document size
index count
query latency
transaction contention
listener activity
```

when performance matters.

---

# 58. COST AWARENESS

For usage-based databases, database design must consider cost.

Avoid:

```text
unnecessary reads
unbounded listeners
repeated full collection queries
excessive indexes
unnecessary writes
```

A technically functional database can still be architecturally incorrect if its usage pattern is economically unsustainable.

---

# 59. DATABASE CHANGE CONTROL

Changes to:

* collection structure
* field contracts
* indexes
* transactions
* authorization
* Security Rules
* data lifecycle
* migrations

MUST be reviewed when they affect architecture or production behavior.

---

# 60. AI DATABASE RULES

AI MUST NOT:

```text
❌ create mock persistence
❌ replace database with arrays
❌ bypass the database layer
❌ invent undocumented collections
❌ invent fields without updating the data contract
❌ trust client-calculated business values
❌ skip validation
❌ skip authorization
❌ remove transactions for convenience
❌ create unnecessary indexes
❌ perform full collection reads without justification
❌ silently change production data shape
❌ delete data without an explicit deletion strategy
❌ claim database integration is complete without verification
```

---

# 61. DATABASE IMPLEMENTATION LOOP

For every database feature:

```text
Requirement
↓
Data Model
↓
Access Pattern
↓
Validation
↓
Authorization
↓
Query Design
↓
Index Design
↓
Transaction Strategy
↓
Implementation
↓
Tests
↓
Performance Review
↓
Security Review
```

---

# 62. DEFINITION OF DONE

A database feature is complete only when:

* Data model is documented
* Data ownership is clear
* Runtime validation exists
* Authorization exists
* Queries are intentional
* Indexes are reviewed
* Transactions are used where required
* Concurrency behavior is considered
* No mock production persistence exists
* Frontend/backend/database boundaries are respected
* Security rules/IAM are correctly configured
* Relevant tests pass
* Migration strategy exists when needed
* Performance/cost implications are understood

---

# 63. SOURCE OF AUTHORITY

These rules are informed by:

* Firebase Cloud Firestore Data Model
* Firebase Cloud Firestore Best Practices
* Firebase Cloud Firestore Transactions and Batched Writes
* Firebase Cloud Firestore Security Rules
* Firebase Authentication
* Google Cloud IAM
* OWASP application security principles
* The project's `ARCHITECTURE.md`
* The project's `API_RULES.md`
* The project's `SECURITY_RULES.md`

Project-specific database requirements may extend these rules through `PROJECT_SPEC.md`.

---

# 64. FINAL RULE

The database is not a detail hidden behind the UI.

It is a core part of the product architecture.

Therefore:

```text
No fake persistence.
No undocumented data model.
No unvalidated writes.
No client-controlled authority.
No missing authorization.
No uncontrolled queries.
No unreviewed schema changes.
```

A feature is not complete until its data is correctly modeled, persisted, secured, queried, tested and verified.
