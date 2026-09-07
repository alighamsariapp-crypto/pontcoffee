# SECURITY RULES

## 1. PURPOSE

This document defines the mandatory security rules for the entire application.

It covers:

* Authentication
* Authorization
* Session management
* Token security
* RBAC
* Input validation
* Output encoding
* XSS
* CSRF
* Injection
* SSRF
* Secrets
* Database security
* API security
* File uploads
* Dependencies
* Logging
* Monitoring
* Security testing
* Incident handling

Security is a system-wide responsibility.

---

# 2. SECURITY BASELINE

The default security baseline is:

```text
OWASP ASVS 5.0.0
OWASP API Security Top 10
OWASP Cheat Sheet Series
```

OWASP ASVS provides a structured set of requirements for developing and verifying secure web applications.

Security requirements MUST be treated as engineering requirements, not optional improvements.

---

# 3. SECURITY PRINCIPLES

The application MUST follow:

```text
Deny by default
Least privilege
Defense in depth
Fail securely
Validate untrusted input
Minimize exposed data
Server-authoritative security
Secure defaults
Explicit authorization
No security through obscurity
```

---

# 4. ZERO TRUST CLIENT

The frontend is untrusted.

Never trust client-provided:

```text
userId
role
permissions
price
discount
total
inventory
order status
payment status
isAdmin
```

The server MUST independently determine security-sensitive values.

---

# 5. AUTHENTICATION

Authentication MUST be handled by a trusted authentication mechanism.

The server MUST verify the authenticated identity before granting protected access.

Authentication MUST NOT rely on:

```text
localStorage flags
frontend state
hidden buttons
route guards alone
client-side role values
```

Frontend authentication checks are UX controls, not security controls.

---

# 6. PASSWORD SECURITY

If the application manages passwords:

* passwords MUST never be stored in plaintext
* passwords MUST never be logged
* passwords MUST be hashed using an approved password hashing algorithm
* password comparison MUST use secure verification
* password reset MUST use short-lived secure mechanisms
* password recovery MUST not reveal whether an account exists unnecessarily

Use established authentication libraries/services instead of inventing cryptography.

---

# 7. PASSWORD POLICY

Password rules MUST balance:

* minimum length
* resistance to guessing
* breached-password protection where appropriate
* usability

Do not create arbitrary complexity requirements that encourage insecure password behavior.

---

# 8. BRUTE-FORCE PROTECTION

Authentication endpoints MUST have protection against automated attacks.

Examples:

```text
login
password reset
OTP
verification
account recovery
```

Controls may include:

```text
rate limiting
progressive delays
temporary lockout
CAPTCHA
risk-based controls
MFA
```

The implementation must avoid creating an account-enumeration vulnerability.

OWASP explicitly recommends controls against automated authentication attacks and login throttling.

---

# 9. MULTI-FACTOR AUTHENTICATION

MFA SHOULD be supported for:

* administrators
* privileged accounts
* high-risk operations
* sensitive account changes

High-risk actions may require reauthentication even when a valid session exists.

---

# 10. SESSION SECURITY

Sessions MUST be:

* unpredictable
* securely generated
* validated server-side
* time-limited
* revocable
* protected during transport

Session identifiers must be treated as sensitive credentials.

OWASP notes that possession of a valid session identifier can effectively represent the authenticated identity of the user.

---

# 11. TOKEN STORAGE

For browser applications:

Authentication/session tokens MUST NOT be stored in:

```text
localStorage
sessionStorage
```

unless there is a documented architecture-specific reason and compensating controls.

Prefer secure cookie-based session mechanisms or an appropriately designed BFF architecture.

OWASP specifically warns that browser storage can expose authentication tokens to JavaScript and therefore to XSS attacks.

---

# 12. COOKIE SECURITY

Authentication cookies SHOULD use:

```text
Secure
HttpOnly
SameSite
```

Example baseline:

```text
Secure
HttpOnly
SameSite=Lax
```

Use `SameSite=Strict` when compatible with the application's authentication/navigation requirements.

Never rely on browser defaults for security-sensitive cookie attributes.

---

# 13. SESSION ROTATION

Session identifiers MUST be rotated when appropriate, especially after:

```text
authentication
privilege changes
account recovery
security-sensitive state changes
```

This helps prevent session fixation.

OWASP identifies session ID regeneration after privilege changes and authentication as an important defense.

---

# 14. SESSION EXPIRATION

Sessions MUST have appropriate:

```text
idle timeout
absolute timeout
revocation behavior
```

The exact values depend on the application's risk profile.

Privileged sessions SHOULD have stricter policies.

---

# 15. LOGOUT

Logout MUST invalidate or revoke the applicable session/token.

The frontend MUST NOT simply delete local UI state and claim the session has been securely terminated.

---

# 16. REAUTHENTICATION

Reauthentication SHOULD be required before high-risk operations such as:

```text
change password
change email
change MFA
disable security controls
change payment information
privilege escalation
sensitive administrative actions
```

---

# 17. AUTHORIZATION

Authorization MUST be enforced server-side.

Authorization must be checked at the appropriate levels:

```text
Function
↓
Object
↓
Property
```

A valid login does not imply permission to perform every action.

---

# 18. RBAC

Role-Based Access Control MUST be centrally defined.

Example:

```text
Role
↓
Permission
↓
Resource
↓
Action
```

Do not scatter arbitrary role checks throughout the application.

---

# 19. LEAST PRIVILEGE

Every user, service and process MUST have only the permissions required for its function.

Avoid:

```text
admin by default
full database access
full API access
wildcard permissions
```

---

# 20. SERVER-AUTHORITATIVE SECURITY

The server MUST determine:

```text
identity
role
permissions
ownership
price
discount eligibility
inventory
order state
payment state
security-sensitive configuration
```

The client may request an action but cannot authorize itself.

---

# 21. OBJECT-LEVEL AUTHORIZATION

Every resource access MUST verify ownership or permission where applicable.

Example:

```text
GET /orders/123
```

must verify whether the authenticated user is allowed to access order `123`.

Changing the ID must never be sufficient to access another user's resource.

OWASP API Security Top 10 identifies Broken Object Level Authorization as a major API risk.

---

# 22. PROPERTY-LEVEL AUTHORIZATION

Sensitive properties MUST have explicit access rules.

Example:

```text
User
├── name
├── email
├── role
├── permissions
└── internalNotes
```

A normal user MUST NOT be able to:

```text
read protected fields
write protected fields
```

simply because they exist in the underlying object.

---

# 23. FUNCTION-LEVEL AUTHORIZATION

Every privileged endpoint MUST explicitly check permission.

Example:

```text
DELETE /api/v1/products/:id
```

must independently verify the caller's permission.

Hiding the delete button in the UI is insufficient.

---

# 24. INPUT VALIDATION

All external input is untrusted.

Validate:

```text
URL parameters
query parameters
headers
JSON bodies
forms
files
cookies
webhooks
third-party responses
```

Validation MUST occur server-side.

---

# 25. ALLOWLISTING

Prefer allowlists over denylists.

Example:

```text
Allowed sort fields:
createdAt
name
price
```

Do not allow arbitrary database fields or expressions.

---

# 26. OUTPUT ENCODING

Output MUST be encoded appropriately for its context.

Never assume that data retrieved from a database is safe to render.

Untrusted content can become dangerous when inserted into:

```text
HTML
attributes
URLs
JavaScript
CSS
```

---

# 27. XSS PREVENTION

The application MUST prevent:

```text
Stored XSS
Reflected XSS
DOM-based XSS
```

Rules:

* use framework escaping by default
* avoid unsafe HTML injection
* sanitize HTML when HTML is genuinely required
* never trust CMS/user-generated HTML
* avoid unsafe dynamic script construction

---

# 28. DANGEROUS HTML

Do not use mechanisms such as:

```text
dangerouslySetInnerHTML
```

without a documented security reason and trusted sanitization pipeline.

Raw HTML from users MUST NEVER be rendered directly.

---

# 29. CSRF

If authentication relies on browser cookies, state-changing requests MUST have appropriate CSRF protection.

Controls may include:

```text
CSRF tokens
SameSite cookies
origin validation
referer/origin checks
```

SameSite is defense-in-depth and MUST NOT automatically be treated as the only CSRF control for sensitive applications.

---

# 30. SQL / NOSQL INJECTION

Never construct database queries by blindly concatenating user input.

Use:

```text
parameterized queries
safe SDK APIs
validated query builders
allowlisted fields
```

For Firestore, query structure MUST be explicitly controlled by application code.

---

# 31. COMMAND INJECTION

Never construct operating-system commands from untrusted input.

Avoid shell execution whenever possible.

If required:

```text
allowlist commands
validate arguments
avoid shell interpretation
use safe process APIs
```

---

# 32. SSRF

Any feature that retrieves a remote URL MUST treat the URL as untrusted.

Examples:

```text
webhooks
URL import
image fetch
remote document fetch
preview services
external integrations
```

SSRF protection should include:

```text
allowlists where possible
scheme restrictions
host validation
private-network blocking
redirect validation
DNS/rebinding considerations
timeouts
response-size limits
```

OWASP identifies SSRF as a major API security risk.

---

# 33. OPEN REDIRECT

User-controlled redirect targets MUST be validated.

Do not blindly redirect to arbitrary external URLs.

Prefer:

```text
allowlisted destinations
relative paths
signed/validated redirect targets
```

---

# 34. FILE UPLOAD SECURITY

File uploads MUST enforce:

```text
authentication
authorization
size limits
type restrictions
content validation
safe storage
safe filenames
malware scanning where appropriate
```

Never trust:

```text
filename
extension
Content-Type
client-provided metadata
```

---

# 35. FILE STORAGE

User-uploaded files MUST NOT automatically become executable application content.

Use isolated storage where possible.

Generated filenames SHOULD be used instead of trusting user filenames.

---

# 36. SECRETS

Secrets MUST NOT be committed to Git.

Never store:

```text
API keys
private keys
passwords
service credentials
database credentials
JWT secrets
payment secrets
```

inside source code.

---

# 37. ENVIRONMENT VARIABLES

Secrets SHOULD be supplied through secure environment/configuration systems.

Example:

```text
Development
Staging
Production
```

must use appropriately separated credentials.

---

# 38. PUBLIC ENVIRONMENT VARIABLES

Frontend-exposed environment variables are NOT secrets.

Anything shipped to the browser should be considered public.

Never place real secrets in frontend configuration.

---

# 39. FIREBASE / CLOUD SECURITY

When using Firebase/Google Cloud:

* Firestore Security Rules MUST be intentional
* client access MUST be restricted
* server credentials MUST remain server-side
* IAM permissions MUST follow least privilege
* admin/service credentials MUST never reach the browser
* sensitive collections MUST have explicit access rules

The frontend MUST never receive privileged server credentials.

---

# 40. DATABASE SECURITY

Database access MUST occur through controlled application boundaries.

Do not expose direct database administration to the client.

Sensitive fields SHOULD be minimized.

Security-sensitive operations MUST be performed server-side.

---

# 41. PAYMENT SECURITY

Payment-related operations MUST be server-authoritative.

The client MUST NOT determine:

```text
final price
payment status
transaction success
refund status
order paid state
```

Payment provider responses MUST be verified server-side.

---

# 42. INVENTORY SECURITY

Inventory changes MUST be controlled by trusted backend logic.

The client MUST NOT be able to submit:

```text
inventory = 999999
```

and have it accepted as authoritative state.

---

# 43. ORDER SECURITY

Order state transitions MUST be validated server-side.

Example:

```text
pending
→ paid
→ processing
→ shipped
→ completed
```

Invalid transitions MUST be rejected.

---

# 44. WEBHOOK SECURITY

Webhook endpoints MUST:

```text
verify signatures
validate payloads
prevent replay where applicable
use idempotent processing
limit resource consumption
log security events
```

A webhook MUST NOT be trusted merely because it comes from an expected URL.

---

# 45. CORS

CORS configuration MUST be explicit.

Production APIs MUST NOT use unnecessarily broad origins.

Credentialed requests MUST use carefully controlled origins.

---

# 46. HTTPS / TRANSPORT SECURITY

Production authentication and sensitive application traffic MUST use HTTPS/TLS.

Sensitive credentials MUST never be transmitted over insecure transport.

---

# 47. SECURITY HEADERS

Security-sensitive HTTP headers SHOULD be configured centrally.

Depending on architecture, consider:

```text
Content-Security-Policy
Strict-Transport-Security
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

Security headers must be compatible with the application's actual behavior.

---

# 48. CONTENT SECURITY POLICY

A CSP SHOULD be used where practical.

Avoid unnecessarily broad policies such as:

```text
unsafe-inline
*
```

unless explicitly justified.

---

# 49. DEPENDENCY SECURITY

Third-party dependencies MUST be treated as part of the security boundary.

The project SHOULD:

```text
scan dependencies
remove unused packages
keep important dependencies updated
review security advisories
lock versions appropriately
```

Do not install a package merely to avoid writing a small piece of code.

---

# 50. SUPPLY CHAIN SECURITY

Before adding a dependency, consider:

```text
maintainer reputation
maintenance activity
license
dependency tree
security history
package provenance
required permissions
```

Avoid unnecessary dependencies.

---

# 51. CLIENT-SIDE SECURITY

Frontend code MUST NOT contain:

```text
private keys
database admin credentials
service account credentials
server secrets
```

Client-side checks may improve UX but MUST never replace backend security.

---

# 52. SENSITIVE DATA MINIMIZATION

Collect and store only data required by the product.

Do not store sensitive data merely because it might be useful later.

Sensitive data MUST have:

```text
purpose
access rules
retention policy
deletion strategy
```

---

# 53. LOG SECURITY

Never log:

```text
passwords
authentication tokens
session IDs
API secrets
private keys
payment credentials
sensitive personal data
```

Logs themselves are security-sensitive assets.

---

# 54. SECURITY EVENTS

Important security events SHOULD be logged.

Examples:

```text
login failure
successful login
logout
password change
MFA change
permission change
role change
suspicious access
authorization failure
security-sensitive admin action
```

Logs must contain enough context for investigation without exposing secrets.

---

# 55. ERROR SECURITY

Production errors MUST NOT expose:

```text
stack traces
database queries
filesystem paths
environment variables
internal service details
credentials
tokens
```

Return safe errors to clients and detailed diagnostics to protected logs.

---

# 56. ACCOUNT ENUMERATION

Authentication and recovery flows SHOULD avoid revealing whether a specific account exists.

Examples:

```text
login
password reset
email verification
account recovery
```

Messages should be carefully designed to reduce enumeration risk.

---

# 57. RATE LIMITING

Security-sensitive operations MUST have appropriate limits.

Examples:

```text
login
OTP
password reset
search
file uploads
API calls
admin operations
coupon validation
payment attempts
```

Rate limits must account for abuse scenarios.

---

# 58. BUSINESS LOGIC SECURITY

Security is not only about technical exploits.

The application MUST protect sensitive business flows.

Examples:

```text
coupon abuse
inventory manipulation
price manipulation
order duplication
payment replay
refund abuse
account creation abuse
privilege escalation
```

OWASP API Security Top 10 explicitly includes unrestricted access to sensitive business flows as a security category.

---

# 59. RACE CONDITIONS

Critical operations MUST consider concurrent requests.

Examples:

```text
inventory
coupon usage
payment
order creation
withdrawal
resource allocation
```

Use appropriate transactions, locks, atomic operations or idempotency mechanisms.

---

# 60. SECURITY TESTING

Security tests MUST cover:

```text
unauthenticated access
unauthorized access
cross-user access
role escalation
property manipulation
input injection
XSS
CSRF
rate limits
file upload abuse
invalid tokens
expired sessions
replay attempts
business logic abuse
```

---

# 61. CROSS-USER TESTING

At minimum, important resource endpoints SHOULD be tested using two different users.

Example:

```text
User A creates Order A
User B attempts to access Order A
→ MUST be denied
```

This specifically tests object-level authorization.

---

# 62. PRIVILEGE ESCALATION TESTING

Test that:

```text
normal user
≠
admin
```

and that changing client-side values cannot grant privileges.

Examples:

```text
role=admin
isAdmin=true
permissions=["*"]
```

MUST NOT be sufficient to elevate privileges.

---

# 63. SECURITY AUDIT

Before production release, perform a security review covering:

```text
Authentication
Authorization
Session
API
Database
Secrets
Input validation
Output encoding
Files
Dependencies
Logging
Configuration
Business logic
```

---

# 64. SECURITY REGRESSION

Security fixes MUST have regression tests where practical.

A vulnerability that was fixed MUST NOT silently return in a future refactor.

---

# 65. AI SECURITY RULES

AI MUST NEVER:

```text
❌ disable authentication to make development easier
❌ disable authorization
❌ expose secrets
❌ put secrets in frontend code
❌ trust client roles
❌ trust client prices
❌ trust client totals
❌ bypass validation
❌ expose database admin credentials
❌ use insecure token storage without justification
❌ return stack traces in production
❌ create unrestricted CORS by default
❌ create unrestricted file uploads
❌ create arbitrary URL fetching
❌ ignore rate limiting for sensitive operations
❌ mark a security feature complete without testing
```

---

# 66. SECURITY CHANGE CONTROL

Any change involving:

```text
authentication
authorization
roles
permissions
sessions
tokens
database rules
API access
payment
files
secrets
security headers
```

MUST be treated as a security-sensitive change.

Such changes require:

```text
impact analysis
implementation
security review
tests
regression verification
```

---

# 67. SECURITY DEFINITION OF DONE

A security-sensitive feature is complete only when:

* Authentication is defined
* Authorization is defined
* Least privilege is respected
* Input is validated
* Sensitive output is minimized
* Session security is correct
* Secrets are protected
* Database access is controlled
* API access is controlled
* Abuse limits exist where required
* Errors do not leak sensitive information
* Security tests exist
* Regression tests exist where appropriate
* Logs do not expose secrets
* Production configuration is reviewed

---

# 68. SECURITY QUALITY GATE

The project MUST NOT be considered production-ready if any critical security issue remains unresolved.

Critical examples:

```text
authentication bypass
authorization bypass
privilege escalation
cross-user data access
secret exposure
payment manipulation
server-side credential exposure
arbitrary code execution
critical injection
critical SSRF
critical file upload vulnerability
```

---

# 69. SOURCE OF AUTHORITY

This document is based primarily on:

* OWASP ASVS 5.0.0
* OWASP API Security Top 10
* OWASP Authentication Cheat Sheet
* OWASP Session Management Cheat Sheet
* OWASP Cheat Sheet Series
* Project `API_RULES.md`
* Project `DATABASE_RULES.md`
* Project `ARCHITECTURE.md`
* Project `CODING_RULES.md`

Security requirements may be strengthened by `PROJECT_SPEC.md`.

---

# 70. FINAL SECURITY RULE

The application is secure only when:

```text
Identity
+
Session
+
Authorization
+
Input Validation
+
Output Protection
+
Data Protection
+
API Protection
+
Infrastructure Protection
+
Business Logic Protection
+
Security Testing
```

are all addressed.

A working feature is NOT automatically a secure feature.

Security MUST be designed before implementation and verified after implementation.
