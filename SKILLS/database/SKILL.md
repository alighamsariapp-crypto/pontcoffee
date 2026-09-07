# Database Development Skill

## Purpose

This skill defines how the AI executes database work for a feature.

It operates under:

* `DATABASE_RULES.md`
* `ARCHITECTURE.md`
* `SECURITY_RULES.md`
* `API_RULES.md`
* `CODING_RULES.md`
* `TESTING_RULES.md`

Those files define the rules.
This skill defines the execution workflow.

---

## 1. Identify Data Requirements

Before changing the database, determine:

* What data the feature needs
* Which existing entities are involved
* New entities, if any
* Relationships between entities
* Read operations
* Write operations
* Ownership requirements
* State transitions
* Data lifecycle

Do not create data structures without a feature requirement.

---

## 2. Inspect Existing Data Model

Before creating or modifying anything, inspect:

* Existing collections/tables
* Existing documents/records
* Field conventions
* Relationships/references
* Existing indexes
* Existing queries
* Repository/data-access code
* Security rules
* Existing migrations or migration strategy
* Seed/test data

Prefer extending the existing model when appropriate.

---

## 3. Define the Data Contract

For every new or changed entity, determine:

```text id="h7q3mx"
Entity
├── Identity
├── Required Fields
├── Optional Fields
├── Relationships
├── Server-Controlled Fields
├── Immutable Fields
├── Status
└── Timestamps
```

The implementation must remain compatible with the project's database rules.

---

## 4. Design for Actual Queries

Before implementing the model, identify the queries the feature requires.

For each important query determine:

* Filters
* Sort order
* Pagination
* Required indexes
* Expected result size
* Frequency
* Ownership/authorization constraints

Do not create a data model first and discover later that the required queries are inefficient or impossible.

---

## 5. Implement Data Access

Keep database access behind the established data-access boundary.

Typical flow:

```text id="p8w2nc"
Feature
→ Use Case
→ Repository / Data Access
→ Database
```

Do not scatter database operations throughout unrelated application code.

---

## 6. Implement Writes Safely

For every write operation determine whether it requires:

* Single write
* Batch operation
* Transaction
* Idempotency
* Concurrency protection
* State-transition validation

Use the smallest mechanism that correctly preserves the required consistency.

---

## 7. Handle Transactions Correctly

When transactions are required:

```text id="n4k8zd"
Read Required State
→ Validate Conditions
→ Calculate Result
→ Commit Changes
```

Transaction callbacks must remain safe if retried.

Do not place non-idempotent external side effects inside retryable transaction logic.

---

## 8. Handle Existing Data

When changing an existing model, determine:

* Existing records affected
* Backward compatibility
* Default behavior
* Migration requirements
* Rollback considerations
* Old clients or code paths

Never assume the database contains only newly created data.

---

## 9. Verify Security Boundaries

For data accessed by users or clients, verify:

```text id="c5r9va"
Who can Read?
Who can Create?
Who can Update?
Who can Delete?
Which Fields?
Which Records?
```

Use the project's security architecture and database rules.

Do not rely on UI restrictions to protect database data.

---

## 10. Verify Performance

For important operations, check:

* Query efficiency
* Index requirements
* Pagination
* Result limits
* Large collections
* High-write paths
* Realtime listeners where applicable
* Unnecessary repeated reads/writes

Avoid premature optimization, but do not ignore known scalability risks.

---

## 11. Test the Data Layer

Run the applicable tests from `TESTING_RULES.md`.

Verify:

* Create
* Read
* Update
* Delete where applicable
* Validation
* Authorization boundaries
* Query behavior
* Pagination
* Transactions
* Concurrent operations where relevant
* Existing-data compatibility
* Failure and rollback behavior

---

## 12. Verify Real Integration

A database implementation is not complete merely because the collection/table exists.

Verify:

```text id="r2x6kf"
Frontend / API
→ Backend
→ Data Access
→ Database
→ Persisted Result
→ Response
```

Confirm that real data is created, retrieved, updated, and returned correctly where required.

---

## 13. Database Completion Gate

Before marking database work complete:

```text id="j8v4qp"
[ ] Data requirements identified
[ ] Existing model inspected
[ ] Data contract defined
[ ] Required queries verified
[ ] Data-access boundary respected
[ ] Writes implemented safely
[ ] Transactions handled where required
[ ] Existing data considered
[ ] Security boundaries verified
[ ] Performance risks reviewed
[ ] Tests pass
[ ] Real integration verified
```

---

## 14. Change Control

Database changes are high-impact changes.

Do not:

* modify unrelated entities
* delete existing data without explicit authorization
* change field meaning silently
* introduce incompatible structures without a migration strategy
* replace production persistence with mocks
* bypass established data-access patterns

If a broader schema change is required, document the impact before proceeding.

---

## Operating Principle

> **Design the database around real feature requirements and real query patterns, then verify that the complete application flow actually persists and retrieves the intended data.**
