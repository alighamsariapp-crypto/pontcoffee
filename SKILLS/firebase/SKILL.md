# Firebase Skill

## Purpose

Use this Skill when a Feature requires Firebase services such as:

* Firebase Authentication
* Cloud Firestore
* Firebase Storage
* Firebase Functions
* Firebase App Check
* Firebase Hosting / App Hosting

Firebase MUST be implemented according to the project's approved architecture and security model.

---

# 1. Workflow

Follow this sequence:

```text id="fbskill01"
IDENTIFY
↓
INSPECT
↓
MODEL
↓
SECURE
↓
IMPLEMENT
↓
INTEGRATE
↓
TEST
↓
AUDIT
↓
REPORT
```

Do not connect a Feature to Firebase without first understanding its data and security requirements.

---

# 2. Identify

Determine:

* which Firebase service is required
* why it is required
* whether the client accesses it directly
* whether the server accesses it
* whether authentication is required
* whether authorization is required
* whether sensitive data is involved
* whether transactions are required
* whether realtime updates are required
* whether storage is required

If Firebase is not required:

`Firebase impact: None`

Do not introduce Firebase unnecessarily.

---

# 3. Inspect

Before implementation, inspect:

* `PROJECT_SPEC.md`
* `FIREBASE_RULES.md`
* `DATABASE_RULES.md`
* `SECURITY_RULES.md`
* `API_RULES.md`
* `ARCHITECTURE.md`
* existing Firebase configuration
* existing authentication
* existing Firestore model
* existing Security Rules
* existing Storage Rules
* Firebase indexes
* emulator configuration
* environment configuration
* existing tests

Reuse existing infrastructure where appropriate.

---

# 4. Determine Access Architecture

Explicitly determine whether the Feature uses:

```text id="fbskill02"
Client
  ↓
Firebase Client SDK
  ↓
Firebase Rules
```

or:

```text id="fbskill03"
Client
  ↓
Application API
  ↓
Server
  ↓
Firebase Admin SDK
  ↓
Firestore / Storage
```

or a deliberate combination.

Do not use direct client access simply because it is easier.

---

# 5. Authentication

If authentication is required:

1. identify supported authentication method
2. verify Firebase Auth configuration
3. verify session behavior
4. verify logout behavior
5. verify account lifecycle
6. verify protected routes/actions
7. verify error behavior

Authentication MUST NOT be treated as authorization.

---

# 6. Authorization

For every protected operation determine:

```text id="fbskill04"
Who?
↓
What resource?
↓
What operation?
↓
Under what conditions?
```

Verify authorization at the correct boundary.

For server operations:

```text id="fbskill05"
Authentication
↓
Authorization
↓
Validation
↓
Business Rules
↓
Firebase Operation
```

Never trust client-provided roles or permissions.

---

# 7. Firestore Data Model

Before creating or modifying Firestore data:

1. identify entities
2. identify ownership
3. identify relationships
4. identify queries
5. identify indexes
6. identify read/write frequency
7. identify transaction requirements
8. identify security boundaries
9. identify retention requirements

Do not design collections around temporary UI structure.

---

# 8. Read Operations

For every Firestore read evaluate:

* required fields
* query scope
* authorization
* pagination
* indexing
* expected result size
* read cost
* realtime requirement

Avoid broad collection reads.

Avoid duplicate listeners.

Use bounded queries for large datasets.

---

# 9. Write Operations

For every write determine:

* client-controlled fields
* server-controlled fields
* required validation
* ownership
* authorization
* transaction requirement
* audit requirements
* idempotency

Never allow arbitrary client field updates.

---

# 10. Transactions

Use Firestore transactions when correctness requires atomic read/write behavior.

Typical cases:

* inventory
* order creation
* counters
* balance updates
* reservations
* concurrent state changes

Transaction callbacks MUST be safe for retries.

Do not place non-idempotent external side effects inside transaction callbacks.

---

# 11. Batch Operations

Use batched writes when multiple writes should be committed together and transactional reads are not required.

Do not use batches simply because they appear faster.

Correctness comes first.

---

# 12. Security Rules

For client-accessible Firebase resources:

1. inspect current Rules
2. determine required access
3. implement least-privilege Rules
4. protect sensitive fields
5. verify ownership
6. verify role requirements
7. test allowed operations
8. test denied operations

Never disable Rules to make development easier.

---

# 13. Server-Side Firebase

When using Admin SDK or other privileged server access:

The Skill MUST verify:

* authentication
* authorization
* input validation
* business rules
* resource ownership
* data minimization
* error handling
* audit requirements

Firestore Security Rules MUST NOT be assumed to protect privileged server operations.

---

# 14. Storage

If Storage is required:

### Before implementation

Define:

* accepted file types
* maximum size
* ownership
* access model
* path strategy
* retention
* public/private behavior

### During implementation

Verify:

* upload validation
* Storage Rules
* authorization
* safe file paths
* file size limits
* failure handling

Do not make uploaded files public by default.

---

# 15. App Check

If App Check is appropriate:

1. determine protected services
2. configure App Check
3. understand enforcement behavior
4. test legitimate clients
5. test rejected/invalid requests

App Check is additional abuse protection.

It MUST NOT replace authentication or authorization.

---

# 16. Functions

For Firebase Functions:

Define:

* trigger
* responsibility
* input
* output
* authentication
* authorization
* retry behavior
* idempotency
* timeout
* failure behavior
* logging
* secrets

Functions SHOULD remain focused and bounded.

Do not place unrelated business logic into one large Function.

---

# 17. Realtime Features

If realtime listeners are required:

Evaluate:

* why realtime is necessary
* listener scope
* listener lifetime
* listener count
* unsubscribe behavior
* data volume
* read cost
* offline behavior

Listeners MUST be cleaned up when no longer required.

---

# 18. Emulator

Use Firebase Emulator Suite where practical for:

* Auth testing
* Firestore testing
* Storage testing
* Functions testing
* Security Rules testing

Local tests MUST NOT accidentally modify production data.

---

# 19. Environment Configuration

Verify that the Feature uses the correct Firebase environment.

Check:

```text id="fbskill06"
Local
Preview / Staging
Production
```

Never hardcode production configuration into development workflows.

Secrets MUST remain outside client code.

---

# 20. Integration

After Firebase implementation:

Verify the complete flow.

Example:

```text id="fbskill07"
User Action
↓
Frontend
↓
API / Firebase SDK
↓
Authentication
↓
Authorization
↓
Validation
↓
Business Logic
↓
Firestore / Storage
↓
Response
↓
UI State
```

The Feature MUST use real data flow.

Mocks MUST NOT be used as proof of production integration.

---

# 21. Testing

Relevant tests MUST include:

### Authentication

* valid session
* invalid session
* expired session
* logout

### Authorization

* authorized user
* unauthorized user
* wrong owner
* wrong role
* privilege escalation attempt

### Firestore

* valid read
* denied read
* valid write
* denied write
* protected field modification
* transaction behavior
* concurrency

### Storage

* valid upload
* invalid file
* oversized file
* unauthorized access

### Integration

* frontend → backend/Firebase
* backend → Firebase
* real production-shaped data flow

---

# 22. Performance Review

Evaluate:

* document reads
* document writes
* listener count
* query size
* transaction frequency
* document size
* Storage usage
* function invocations

Follow `PERFORMANCE_RULES.md`.

---

# 23. Failure Handling

If Firebase integration fails:

1. identify the failing layer
2. inspect authentication
3. inspect authorization
4. inspect validation
5. inspect Rules
6. inspect data model
7. inspect indexes
8. inspect environment configuration
9. inspect network/API behavior
10. reproduce using emulator where appropriate
11. fix
12. retest

Do not bypass security controls to make a Feature work.

---

# 24. Audit

Before marking the Feature complete:

```text id="fbskill08"
[ ] Correct Firebase service selected
[ ] Architecture reviewed
[ ] Environment verified
[ ] Authentication verified
[ ] Authorization verified
[ ] Firestore model verified
[ ] Security Rules verified
[ ] Protected fields verified
[ ] Transactions verified
[ ] Storage verified where applicable
[ ] Functions verified where applicable
[ ] App Check evaluated where applicable
[ ] Emulator tests run where practical
[ ] Integration uses real data
[ ] Performance reviewed
[ ] Production configuration reviewed
```

---

# 25. Hard Prohibitions

AI MUST NOT:

* expose Admin SDK credentials
* expose service-account keys
* disable Security Rules
* bypass authorization
* trust client roles
* trust client prices
* trust client inventory
* expose unrestricted collections
* allow arbitrary field updates
* use production Firebase for arbitrary testing
* make private files public without approval
* put secrets in frontend code
* use mocks as proof of integration
* silently replace the project's architecture

---

# 26. Completion Gate

Firebase work is complete only when:

```text id="fbskill09"
Requirement
↓
Firebase Architecture
↓
Data Model
↓
Security Model
↓
Implementation
↓
Real Integration
↓
Testing
↓
Security Verification
↓
Audit PASS
```

Final report:

```text id="fbskill10"
Firebase Status: PASS

Service:
[AUTH / FIRESTORE / STORAGE / FUNCTIONS / APP CHECK]

Authentication:
[PASS / N/A]

Authorization:
[PASS / N/A]

Security Rules:
[PASS / N/A]

Data Model:
[PASS / N/A]

Transactions:
[PASS / N/A]

Integration:
[PASS]

Tests:
[PASS]

Security Audit:
PASS
```
