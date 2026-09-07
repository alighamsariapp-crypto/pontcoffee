# Firebase Rules

## 1. Purpose

This document defines mandatory rules for projects using Firebase services.

It covers:

* Firebase Authentication
* Cloud Firestore
* Firebase Storage
* Firebase Security Rules
* Firebase Admin SDK
* Firebase client SDK
* Firebase App Check where applicable
* Firebase Functions / backend integrations where applicable

Firebase configuration MUST remain consistent with:

* `PROJECT_SPEC.md`
* `ARCHITECTURE.md`
* `DATABASE_RULES.md`
* `API_RULES.md`
* `SECURITY_RULES.md`
* `PRIVACY_RULES.md`

---

# 2. Firebase Is Infrastructure, Not the Architecture

Firebase MAY provide infrastructure services, but it MUST NOT silently determine the application's architecture.

AI MUST NOT:

* replace an existing backend with direct client access
* replace server authorization with Firestore Rules alone
* replace the application's database model without approval
* introduce Firebase services without a requirement
* change authentication architecture silently

Firebase MUST serve the approved project architecture.

---

# 3. Environment Separation

Firebase environments MUST be separated where appropriate.

At minimum, distinguish:

```text
Development
↓
Preview / Staging
↓
Production
```

Production data MUST NOT be casually used for local development.

Development or test operations MUST NOT accidentally target production Firebase resources.

---

# 4. Firebase Configuration

Firebase configuration MUST be environment-aware.

Public Firebase configuration MAY exist in frontend code when required by the Firebase client SDK.

However:

* credentials
* service account keys
* Admin SDK credentials
* private API keys
* server secrets
* privileged configuration

MUST NOT be exposed to the client.

---

# 5. Firebase Authentication

Authentication MUST use an approved authentication architecture.

AI MUST define:

* supported sign-in methods
* account lifecycle
* session behavior
* email verification where applicable
* password recovery where applicable
* account disablement
* logout behavior
* reauthentication for sensitive operations where required

Authentication MUST NOT be considered equivalent to authorization.

---

# 6. Authentication vs Authorization

The system MUST distinguish:

```text id="fb001"
Authentication
    =
Who is the user?

Authorization
    =
What is the user allowed to do?
```

A valid Firebase user MUST NOT automatically receive access to application resources.

Authorization MUST remain server-authoritative for protected business operations.

---

# 7. Firestore Security Rules

Firestore Security Rules MUST be configured for client-accessible Firestore operations.

Rules MUST follow:

* deny by default
* least privilege
* explicit access conditions
* user/resource ownership checks
* role checks where appropriate
* validation of writable fields
* protection against unauthorized reads
* protection against unauthorized writes

Security Rules MUST NOT be treated as optional production configuration.

---

# 8. Security Rules Are Not Filters

Firestore Security Rules do not transform an unsafe query into a safe filtered query.

Queries MUST be designed so that the requested data is authorized by the applicable rule conditions.

AI MUST NOT assume:

```text id="fb002"
Query broad collection
+
Security Rule
=
Automatically filtered results
```

The data access pattern itself MUST be compatible with the authorization model.

---

# 9. Admin SDK

The Firebase Admin SDK is privileged.

When using the Admin SDK:

* validate all client input
* authenticate the request
* authorize the operation
* enforce ownership/resource access
* validate writable fields
* enforce business rules
* protect sensitive operations

Admin SDK access MUST NOT be exposed directly to clients.

---

# 10. Server Authority

The server MUST remain authoritative for security-sensitive and business-critical operations.

Examples:

* prices
* discounts
* inventory
* order totals
* payment status
* refunds
* permissions
* role changes
* account privileges
* sensitive state transitions

The client MUST NOT be trusted to provide authoritative values.

---

# 11. Firestore Data Model

Firestore data models MUST follow `DATABASE_RULES.md`.

Before creating collections, AI MUST determine:

* entity ownership
* document structure
* relationships
* query patterns
* indexes
* access patterns
* write frequency
* transaction requirements
* retention requirements

AI MUST NOT create collections merely because they are convenient for a UI component.

---

# 12. Document IDs

Document IDs MUST follow a deliberate strategy.

Possible strategies:

* generated IDs
* user IDs
* business identifiers
* stable slugs where appropriate

IDs MUST NOT expose sensitive information.

Predictable IDs MUST NOT be treated as a security boundary.

---

# 13. Firestore Writes

Client writes MUST be restricted to fields that the client is actually allowed to control.

Protected fields include, where applicable:

* role
* permissions
* price
* discount
* inventory
* payment state
* order state
* ownership
* audit fields
* server timestamps
* security-sensitive flags

Mass assignment MUST be prevented.

---

# 14. Transactions

Firestore transactions MUST be used when multiple reads/writes require atomic consistency.

Examples:

* inventory updates
* order creation
* stock reservation
* balance updates
* counters
* state transitions

Transaction callbacks MUST be safe to retry.

Do not perform non-idempotent external side effects inside a transaction callback.

---

# 15. Batch Writes

Batch writes MAY be used when multiple writes must be committed together without requiring transactional reads.

AI MUST distinguish:

```text
Transaction
=
read + validate + atomic write

Batch
=
multiple writes committed together
```

Use the simplest mechanism that preserves correctness.

---

# 16. Inventory & Commerce

For commerce systems:

```text id="fb003"
Client
  ↓
Request
  ↓
Server Validation
  ↓
Authorization
  ↓
Firestore Transaction
  ↓
Authoritative Result
```

The client MUST NOT directly determine:

* final price
* inventory availability
* discount validity
* order total
* payment status

---

# 17. Firebase Storage

If Firebase Storage is used:

* file types MUST be validated
* file size MUST be limited
* access MUST be authorized
* ownership MUST be verified
* filenames MUST be handled safely
* untrusted files MUST NOT automatically become trusted content

Storage Rules MUST be implemented where client access exists.

---

# 18. File Upload Security

Uploads MUST consider:

* extension spoofing
* MIME validation
* file size
* executable content
* malicious payloads
* path traversal
* access control
* public exposure
* retention

Do not assume a filename or client-provided MIME type is trustworthy.

---

# 19. Firebase App Check

App Check SHOULD be evaluated for client-accessible Firebase services where it materially improves abuse protection.

App Check MUST NOT replace:

* authentication
* authorization
* input validation
* server-side security controls

It is an additional protection layer, not the primary authorization system.

---

# 20. Cloud Functions / Serverless Functions

When Firebase Functions are used:

* functions MUST have a defined responsibility
* authentication MUST be verified
* authorization MUST be enforced
* input MUST be validated
* secrets MUST use appropriate secret management
* errors MUST be handled safely
* retries MUST be considered
* idempotency MUST be implemented where necessary

Do not create a Function merely to move code without architectural justification.

---

# 21. Firebase Hosting / App Hosting

Hosting configuration MUST be treated as production infrastructure.

Review:

* environment configuration
* redirects
* rewrites
* headers
* caching
* HTTPS
* deployment environment
* rollback strategy
* domain configuration

Hosting behavior MUST remain compatible with the selected rendering architecture.

---

# 22. Firebase Rules & Server SDK

When the server uses privileged Firebase server libraries, Firestore Security Rules may not provide the same authorization boundary as client SDK access.

Therefore:

```text id="fb004"
Client
→ Firebase Rules

Server
→ Server Authentication
→ Server Authorization
→ IAM / Service Account Permissions
→ Firestore
```

Server-side authorization MUST NOT be omitted because Firestore Rules exist.

---

# 23. Role-Based Access

Application roles MUST NOT be trusted solely because they are supplied by the client.

If Firebase custom claims are used:

* claims MUST be assigned through trusted server-side processes
* sensitive role changes MUST be authorized
* claim propagation behavior MUST be understood
* stale claims MUST be handled appropriately

Role management MUST remain server-authoritative.

---

# 24. User-Owned Data

For user-owned resources, authorization MUST verify the relationship between:

```text id="fb005"
Authenticated User
        ↓
Requested Resource
        ↓
Resource Owner / Allowed Principal
```

Knowing a document ID MUST NOT be sufficient to access protected data.

---

# 25. Data Exposure

Firestore queries and API responses MUST return only data required by the client.

Do not expose:

* internal administrative fields
* private metadata
* secrets
* privileged configuration
* unnecessary personal data
* internal audit information

Data minimization remains governed by `SECURITY_RULES.md` and `PRIVACY_RULES.md`.

---

# 26. Emulator Usage

Firebase Emulator Suite SHOULD be used for local development and automated testing where practical.

Relevant services may include:

* Authentication
* Firestore
* Storage
* Functions

Tests SHOULD avoid modifying production Firebase resources.

---

# 27. Testing

Firebase implementations MUST be tested for relevant:

* authentication
* authorization
* Firestore Rules
* ownership
* role access
* invalid writes
* protected fields
* transactions
* concurrent operations
* Storage Rules
* file upload validation
* API integration
* emulator behavior

Security tests MUST include negative cases.

---

# 28. Production Data Protection

Production Firebase resources MUST be protected from:

* accidental deletion
* uncontrolled test writes
* development credentials
* overly broad permissions
* unrestricted client access
* unauthorized administrative access

Destructive operations SHOULD require explicit authorization.

---

# 29. Monitoring & Costs

Firebase usage SHOULD be monitored for:

* Firestore reads
* Firestore writes
* Storage usage
* authentication activity
* function invocations
* bandwidth
* errors
* unusual traffic

Cost controls remain governed by `COST_AND_QUOTA_RULES.md`.

---

# 30. Backup & Recovery

Projects with important production data MUST define an appropriate backup and recovery strategy.

The strategy MUST consider:

* backup frequency
* retention
* restoration procedure
* recovery testing
* production ownership
* disaster scenarios

A backup that has never been restored/tested MUST NOT be assumed reliable.

---

# 31. AI Prohibitions

AI MUST NOT:

* expose Firebase Admin credentials
* place service-account keys in frontend code
* disable Security Rules to make development easier
* use production Firebase for arbitrary testing
* trust client-provided roles
* trust client-provided prices
* trust client-provided inventory
* bypass server authorization
* expose unrestricted collections
* allow arbitrary field updates
* create public Storage access without justification
* claim Firebase security is complete without testing
* silently replace the project's database architecture

---

# 32. Firebase Change Control

Any change affecting:

* authentication
* Firestore schema
* Security Rules
* Storage Rules
* indexes
* Functions
* service accounts
* IAM
* production Firebase configuration

MUST undergo impact analysis.

Security-sensitive Firebase changes SHOULD be reviewed before production deployment.

---

# 33. Completion Gate

Firebase implementation is complete only when applicable requirements are verified:

```text id="fb006"
Firebase Architecture Defined
↓
Environment Separation Verified
↓
Authentication Verified
↓
Authorization Verified
↓
Security Rules Verified
↓
Server Authority Verified
↓
Data Model Verified
↓
Transactions / Writes Verified
↓
Storage Verified
↓
Emulator / Integration Tests Passed
↓
Production Configuration Reviewed
↓
Monitoring / Recovery Considered
↓
Security Audit Passed
```

Final status:

```text id="fb007"
Firebase Status: PASS

Authentication: PASS
Authorization: PASS
Firestore: PASS
Security Rules: PASS
Server Authority: PASS
Storage: [PASS / N/A]
Functions: [PASS / N/A]
Emulator Tests: PASS
Production Config: PASS
Security Audit: PASS
```

Firebase MUST NOT be considered complete merely because the application successfully connects to Firebase.
