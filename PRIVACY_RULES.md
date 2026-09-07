# PRIVACY RULES

## 1. Purpose

Privacy is a system requirement.

Every project MUST define how personal and sensitive data is:

* Collected
* Used
* Stored
* Processed
* Transmitted
* Shared
* Retained
* Deleted

Privacy decisions MUST be intentional and documented.

---

## 2. Source of Truth

Privacy implementation MUST follow:

1. `PROJECT_SPEC.md`
2. `SECURITY_RULES.md`
3. `DATABASE_RULES.md`
4. `API_RULES.md`
5. `FIREBASE_RULES.md`
6. `AI_SECURITY_RULES.md`
7. `OBSERVABILITY_RULES.md`
8. Applicable legal/privacy requirements for the project's target markets

Privacy requirements MUST NOT be overridden by convenience.

---

## 3. Data Classification

Every meaningful data category SHOULD be classified.

Recommended classification:

```text id="f7g3qk"
PUBLIC
INTERNAL
PERSONAL
SENSITIVE
SECRET
```

Classification determines:

* Storage
* Access
* Logging
* Transmission
* Retention
* Deletion
* Encryption requirements

---

## 4. Data Minimization

Collect only data that is necessary for:

* A defined product function
* Security
* Legal requirements
* Operational requirements
* Explicitly documented business needs

AI MUST NOT collect additional personal information simply because it may be useful later.

---

## 5. Purpose Limitation

Every personal-data collection SHOULD have a defined purpose.

The system MUST NOT silently reuse data for unrelated purposes.

If a new purpose materially changes how personal data is used, the requirement MUST be reviewed and documented.

---

## 6. User Data

Where applicable, identify:

* What user data is collected
* Why it is collected
* Where it is stored
* Who can access it
* How long it is retained
* When it is deleted
* Whether it is shared with third parties

The implementation MUST match the documented product behavior.

---

## 7. Authentication Data

Authentication systems MUST protect:

* Passwords
* Session identifiers
* Authentication tokens
* Recovery mechanisms
* MFA information
* Security credentials

Passwords MUST never be stored in plaintext.

Authentication secrets MUST never be logged.

Follow `SECURITY_RULES.md`.

---

## 8. Authorization & Data Isolation

A user MUST only be able to access data they are authorized to access.

The system MUST enforce:

```text id="y0o3si"
Authentication
↓
Authorization
↓
Resource Ownership / Permission
↓
Data Access
```

Client-side hiding is NOT a privacy control.

Server-side authorization MUST protect sensitive data.

---

## 9. API Privacy

APIs MUST return only the data required by the requesting operation.

Do not expose:

* Internal fields
* Security metadata
* Secrets
* Private administrative data
* Unnecessary personal information
* Internal database structures

API responses SHOULD use explicit DTOs rather than returning entire database objects by default.

---

## 10. Database Privacy

Database design MUST consider:

* Data ownership
* Access boundaries
* Sensitive fields
* Retention
* Deletion
* Backup implications
* Audit requirements

Sensitive data SHOULD be isolated or protected where appropriate.

Do not store personal data without a documented reason.

---

## 11. Firestore Privacy

For Firebase/Firestore projects:

* Security Rules MUST enforce appropriate client access.
* Server-side Firebase/Admin SDK access MUST use explicit authorization.
* Firestore Security Rules MUST NOT be treated as the only server authorization layer.
* Sensitive collections MUST have explicit access policies.
* Queries MUST respect user ownership and authorization boundaries.

Remember:

> Security Rules are not filters.

---

## 12. File & Storage Privacy

Uploaded files MUST be treated as untrusted data.

The system MUST define:

* Who can upload
* Who can access
* File type restrictions
* Size limits
* Storage location
* Retention
* Deletion
* Public/private visibility

Private files MUST NOT become publicly accessible through predictable URLs.

---

## 13. Logging & Observability

Logs MUST NOT contain unnecessary personal or sensitive information.

Never log:

* Passwords
* Tokens
* API keys
* Secrets
* Payment credentials
* Full private documents
* Sensitive user content without a clear operational reason

Use:

* Redaction
* Masking
* Hashing
* Omission

where appropriate.

Follow `OBSERVABILITY_RULES.md`.

---

## 14. Analytics & Tracking

Analytics MUST have a defined purpose.

Avoid collecting:

* Unnecessary user identifiers
* Sensitive form contents
* Private messages
* Authentication information
* Full URLs containing sensitive parameters

Tracking MUST NOT silently become a secondary source of personal-data collection.

---

## 15. Third-Party Services

Before sending personal data to an external provider, determine:

* What data is sent
* Why it is sent
* Which provider receives it
* Whether the provider requires the data
* Whether transmission is secure
* Whether retention is controlled
* Whether the project has the required legal basis/permission

Third-party integrations MUST follow least-data principles.

---

## 16. AI & Personal Data

AI features require additional privacy review.

Before sending user data to an AI provider, determine:

* What data is sent
* Whether it contains personal information
* Whether it contains sensitive information
* Why the model needs it
* Whether the data can be minimized or anonymized
* Provider retention/training behavior where applicable
* Whether the user needs notice or consent
* Whether the data can remain inside the application's trusted environment

AI MUST NOT receive more personal data than necessary.

Follow `AI_SECURITY_RULES.md`.

---

## 17. Prompt & Context Privacy

For AI applications, user data may enter:

* Prompts
* Conversation history
* Retrieved documents
* Tool arguments
* Memory
* Model context
* Logs
* Error reports

Each path MUST be reviewed.

Do not assume that because data is already inside the application it is safe to send to every AI component.

---

## 18. AI Memory

If persistent AI memory exists, define:

* What is remembered
* Why it is remembered
* Where it is stored
* Who can access it
* How it can be corrected
* How it can be deleted
* Retention period

Memory MUST remain isolated between users.

---

## 19. Data Retention

Every meaningful personal-data category SHOULD have an intentional retention policy.

Consider:

* Product requirements
* Security
* Legal requirements
* Operational needs
* Storage cost
* User expectations

Do not retain personal data indefinitely without justification.

---

## 20. Deletion

Deletion requirements MUST be defined before implementing persistent personal data.

Determine:

* What is deleted
* What is anonymized
* What must be retained
* What happens to related records
* What happens to backups
* What happens to cached copies
* What happens to AI memory
* What happens to uploaded files

Deletion MUST respect business and legal constraints.

---

## 21. Account Deletion

If account deletion is supported, the flow MUST define:

```text id="j7k3a2"
User Request
↓
Authorization
↓
Data Identification
↓
Deletion / Anonymization
↓
Related Data Handling
↓
External Services
↓
Verification
↓
Completion
```

The system MUST NOT claim that an account is fully deleted if relevant data remains.

---

## 22. Data Export

If the product supports user data export, define:

* Exportable data
* Format
* Authorization
* Generation process
* Download protection
* Expiration
* Auditability

Exports MUST NOT expose another user's data.

---

## 23. Privacy by Design

Privacy SHOULD be considered during:

```text id="lq4p5a"
Discovery
↓
Specification
↓
Architecture
↓
Design
↓
Implementation
↓
Testing
↓
Deployment
```

Privacy MUST NOT be postponed until the final audit.

---

## 24. Privacy & UX

Privacy controls MUST be understandable.

Important privacy-related actions SHOULD provide:

* Clear labels
* Understandable explanations
* Predictable behavior
* Accessible controls
* Confirmation for destructive actions where appropriate
* Safe defaults

Do not hide important privacy controls behind confusing UX.

---

## 25. Security Relationship

Privacy and security are related but not identical.

Security protects data against unauthorized access.

Privacy governs appropriate collection, use, sharing, retention, and deletion.

A system can be technically secure while still collecting excessive personal data.

Both MUST be reviewed.

---

## 26. Breach / Incident Readiness

The system SHOULD make it possible to determine:

* What data was affected
* Which users were affected
* When the event occurred
* What systems were involved
* What actions were taken

Observability MUST support investigation without creating additional privacy exposure.

---

## 27. Development & Test Data

Development and test environments SHOULD avoid real personal data.

Prefer:

* Synthetic data
* Anonymized data
* Minimal datasets
* Dedicated test accounts

Production personal data MUST NOT be copied into development environments without explicit authorization and appropriate controls.

---

## 28. Environment Separation

Personal data environments MUST remain appropriately separated.

Do not accidentally connect:

```text id="5h8s1e"
Development
→ Production Database
```

or expose production data through development tools.

---

## 29. Privacy Testing

Where applicable, test:

* Cross-user data isolation
* Unauthorized access
* API data minimization
* File access
* Account deletion
* Data export
* Retention behavior
* Logging redaction
* AI data boundaries
* Third-party transmission
* Admin access boundaries

Privacy failures affecting sensitive data SHOULD be treated as security blockers.

---

## 30. AI Development Rules

AI MUST NOT:

* Collect unnecessary personal data
* Store personal data without purpose
* Send sensitive data to external providers without review
* Log private user content unnecessarily
* Copy production personal data into development
* Expose another user's information
* Assume client-side restrictions provide privacy
* Claim deletion when data remains
* Add analytics without privacy review
* Ignore retention requirements

---

## 31. Completion Gate

Privacy is complete only when:

* Data categories are identified
* Purpose is defined
* Collection is minimized
* Access boundaries are enforced
* API exposure is minimized
* Database/storage handling is defined
* Logging is reviewed
* Third-party data sharing is reviewed
* AI data flows are reviewed where applicable
* Retention is intentional
* Deletion behavior is defined
* Development data is safe
* Privacy tests pass where applicable
* No critical privacy gap remains

Final status:

```text id="x4v8cz"
COMPLETE
COMPLETE WITH WARNINGS
BLOCKED
```

---

## 32. Core Principle

> Collect the minimum necessary, use it only for defined purposes, protect it throughout its lifecycle, and never assume technical security alone is sufficient for privacy.
