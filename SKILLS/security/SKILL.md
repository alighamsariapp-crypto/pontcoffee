# Security Development Skill

## Purpose

This skill defines how the AI performs security work during feature development.

It operates under:

* `SECURITY_RULES.md`
* `API_RULES.md`
* `DATABASE_RULES.md`
* `ARCHITECTURE.md`
* `CODING_RULES.md`
* `TESTING_RULES.md`

Those files define the security requirements.
This skill defines the execution process.

---

## 1. Start With Threat Identification

For the current feature, identify:

* User-controlled inputs
* Protected operations
* Sensitive data
* Resources being accessed
* User/resource ownership
* Privileged actions
* External services
* State-changing operations
* Abuse or misuse possibilities

Do not perform a generic security review detached from the feature.

---

## 2. Inspect Existing Security Controls

Before implementing security-related changes, inspect:

* Authentication flow
* Session/token handling
* Authorization middleware
* Permission model
* Resource ownership checks
* Validation mechanisms
* API protections
* Database security
* Security headers
* Rate limiting
* Logging/security events
* Existing security tests

Reuse established security mechanisms.

---

## 3. Map the Trust Boundaries

For each important operation, identify the trust boundary:

```text id="r8k2mf"
User / Client
→ API
→ Authentication
→ Authorization
→ Validation
→ Business Logic
→ Data / External Service
```

Treat client-provided information as untrusted.

Determine where each security decision must be enforced.

---

## 4. Verify Authentication

For protected operations, verify:

* Is authentication required?
* Is the authentication state valid?
* Is the session/token handled through the established mechanism?
* Is logout/revocation behavior respected?
* Are sensitive operations subject to stronger verification where required?

Do not implement a second authentication mechanism for one feature.

---

## 5. Verify Authorization

For every protected action, determine:

```text id="q4v9cx"
Can the user perform this action?
Can the user access this resource?
Can the user modify this resource?
Which fields can the user modify?
```

Verify authorization on the server.

Do not rely on:

* hidden UI controls
* disabled buttons
* frontend routes
* client-side role checks

as the security boundary.

---

## 6. Validate Untrusted Input

Identify every externally controlled value:

* URL parameters
* Query parameters
* Request body
* Headers
* Uploaded files
* Webhook data
* External API responses

Verify that the established validation and normalization mechanisms are applied before sensitive processing.

---

## 7. Protect Sensitive Operations

For operations involving important business state, inspect:

* Race conditions
* Duplicate requests
* Replay behavior
* Idempotency
* State transitions
* Privilege escalation
* Cross-user access
* Unauthorized field modification

Pay particular attention to financial, inventory, account, administrative, and permission-changing operations.

---

## 8. Check Data Exposure

Verify that responses and logs do not expose unnecessary:

* Personal information
* Credentials
* Tokens
* Secrets
* Internal identifiers
* Authorization information
* Database internals
* Stack traces

Return only what the feature requires.

---

## 9. Check External Boundaries

If the feature communicates with an external service, evaluate:

```text id="m2f7ks"
Input
→ Validation
→ External Request
→ Response Validation
→ Business Processing
```

Consider applicable:

* SSRF
* unsafe redirects
* untrusted responses
* credential leakage
* timeout/resource exhaustion
* webhook authenticity
* replay/duplicate delivery

---

## 10. Add Security Tests

Use the testing process defined in `TESTING_RULES.md`.

Verify applicable cases:

```text id="n6x3qa"
Unauthenticated
Unauthorized
Wrong Resource Owner
Wrong Role
Unauthorized Field
Invalid Input
Duplicate Request
Concurrent Request
Sensitive Data Exposure
Abuse / Rate Limit
```

Do not test only that legitimate users can successfully complete the operation.

---

## 11. Perform Feature Security Review

Before completion, ask:

```text id="v5k8pd"
What can the user control?
What can the user access?
What can the user modify?
What must the server decide?
What happens if the request is repeated?
What happens if the request is manipulated?
What sensitive data could be exposed?
```

Resolve applicable risks before completion.

---

## 12. Security Completion Gate

Before marking security work complete:

```text id="s9c4mw"
[ ] Trust boundaries identified
[ ] Existing security controls inspected
[ ] Authentication verified
[ ] Authorization verified
[ ] Input validation verified
[ ] Sensitive operations reviewed
[ ] Data exposure reviewed
[ ] External integrations reviewed where applicable
[ ] Abuse/concurrency risks considered
[ ] Security tests pass
[ ] No known critical security blocker remains
```

---

## 13. Security Blocker Rule

If a critical security issue is discovered:

```text id="f3q7lz"
Stop Feature Completion
→ Document Issue
→ Fix
→ Retest
→ Re-audit
→ Continue
```

Do not mark the feature complete while a critical security blocker remains.

---

## 14. Change Control

Security changes must remain focused on the identified risk.

Do not:

* disable an existing security control to make functionality work
* bypass authorization for convenience
* weaken validation to accommodate frontend behavior
* expose sensitive information for debugging
* introduce parallel authentication/authorization systems
* hide security failures behind generic success responses

If an architectural security change is required, document it before expanding scope.

---

## Operating Principle

> **Security is verified at the trust boundary where the decision matters, not assumed from the behavior of the client.**
