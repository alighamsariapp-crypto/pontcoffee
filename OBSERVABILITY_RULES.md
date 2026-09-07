# OBSERVABILITY RULES

## 1. Purpose

Observability is a production requirement, not an optional enhancement.

The system MUST provide enough visibility to understand:

* What happened
* Where it happened
* Why it happened
* Who/what triggered it
* How often it happens
* How severely it affects users
* Whether the system recovered

Observability MUST cover frontend, backend, API, database, external services, background jobs, authentication, security events, and deployment/runtime failures.

---

## 2. Source of Truth

Observability implementation MUST follow:

1. `PROJECT_SPEC.md`
2. `DEVELOPMENT_RULES.md`
3. `ARCHITECTURE.md`
4. `SECURITY_RULES.md`
5. `DATABASE_RULES.md`
6. `API_RULES.md`
7. `PERFORMANCE_RULES.md`
8. `DEPLOYMENT_RULES.md`
9. `FIREBASE_RULES.md`
10. `AI_SECURITY_RULES.md`

Observability MUST NOT expose or weaken protected data.

---

## 3. Three Core Signals

Production systems SHOULD provide:

### 3.1 Logs

Structured records describing events.

### 3.2 Metrics

Numerical measurements over time.

Examples:

* Request count
* Error rate
* Latency
* Database operations
* Queue depth
* Authentication failures
* Resource consumption
* AI/API usage
* Cost-related measurements

### 3.3 Traces

Distributed request flow across:

```text
Client
  ↓
API
  ↓
Application
  ↓
Database
  ↓
External Service
```

Tracing SHOULD be used when multiple services or external dependencies make request diagnosis difficult.

---

## 4. Structured Logging

Logs MUST be structured and machine-readable where practical.

Logs SHOULD include:

* Timestamp
* Severity
* Environment
* Service/application
* Event name
* Request ID / correlation ID
* Trace ID when available
* Operation
* Relevant resource identifier
* Result/status
* Duration where useful

Example conceptual event:

```text
order.create.completed
request_id
user_id
order_id
duration_ms
status
```

Logs MUST NOT depend on arbitrary console messages as the primary production observability mechanism.

---

## 5. Log Levels

Use appropriate severity:

* `DEBUG` — development diagnostics
* `INFO` — normal important events
* `WARN` — abnormal but recoverable conditions
* `ERROR` — failed operations requiring investigation
* `FATAL` — critical process/system failure

Production logging MUST avoid excessive DEBUG-level output.

---

## 6. Sensitive Data

NEVER log:

* Passwords
* Authentication tokens
* Session secrets
* API keys
* Private keys
* Payment credentials
* Full sensitive personal information
* Security credentials
* Secrets from environment variables
* Raw authorization headers

Sensitive identifiers MUST be redacted, hashed, masked, or omitted when necessary.

Observability MUST follow `PRIVACY_RULES.md` and `SECURITY_RULES.md`.

---

## 7. Request Correlation

Every important server request SHOULD have a correlation/request ID.

The identifier SHOULD be propagated across:

```text
Frontend
→ API
→ Application
→ Database/External Service
```

This allows one user action to be traced across system boundaries.

---

## 8. API Observability

APIs SHOULD measure:

* Request count
* Response status
* Latency
* Error rate
* Timeout rate
* Rate-limit events
* Authentication failures
* Authorization failures
* Request size where relevant
* External dependency failures

API errors MUST be diagnosable without exposing internal implementation details to users.

---

## 9. Database Observability

Database operations SHOULD provide visibility into:

* Read/write volume
* Query latency
* Failed operations
* Transaction failures
* Retry behavior
* Contention
* Hotspots
* Unexpected read amplification
* High-cost operations

For Firestore, pay particular attention to:

* Document reads
* Document writes
* Query patterns
* Realtime listeners
* Transaction retries
* Large collections
* High-frequency writes

Observability MUST NOT become a source of unnecessary database cost.

---

## 10. Authentication & Security Events

Security-relevant events SHOULD be observable.

Examples:

* Login failures
* Account lockouts
* Token/session failures
* Permission denials
* Privilege changes
* Sensitive account changes
* Suspicious request patterns
* Rate-limit violations
* Administrative actions
* Security-rule failures where observable

Security logs MUST be protected from unauthorized access.

---

## 11. Frontend Observability

Production frontend applications SHOULD capture important failures such as:

* Unhandled exceptions
* Error Boundary failures
* Failed API requests
* Critical rendering failures
* Important user-flow failures
* JavaScript runtime failures

Frontend telemetry MUST respect privacy requirements.

Do not automatically collect sensitive user input or private application data.

---

## 12. Error Tracking

Errors SHOULD be grouped by meaningful cause rather than producing thousands of duplicate events.

Each important error SHOULD provide enough context to identify:

* Feature
* Route
* Operation
* Environment
* Request/correlation ID where available
* Version/release
* Relevant non-sensitive context

Errors MUST be reproducible or diagnosable whenever reasonably possible.

---

## 13. Performance Observability

Important performance measurements SHOULD be observable.

Examples:

* API latency
* Database latency
* Page/load performance
* Core Web Vitals
* Slow queries
* Slow external services
* Large payloads
* High client-side execution time

Follow `PERFORMANCE_RULES.md`.

---

## 14. Background Jobs & Scheduled Work

Background processes MUST be observable.

Track:

* Execution count
* Success/failure
* Duration
* Retries
* Timeouts
* Dead-letter/failure state where applicable
* Resource consumption

A background job MUST NOT silently fail.

---

## 15. External Services

External integrations SHOULD expose:

* Request count
* Success/failure
* Latency
* Timeout
* Retry
* Rate-limit responses
* Provider errors

Failures MUST have explicit fallback or failure behavior.

---

## 16. AI Features

AI-powered functionality MUST provide appropriate observability.

Track where applicable:

* Request count
* Model/provider
* Latency
* Failure rate
* Token/usage metrics
* Tool-call failures
* Validation failures
* Safety/security events
* Rate limits
* Cost-related metrics

NEVER log prompts, outputs, files, or user data indiscriminately.

Follow `AI_SECURITY_RULES.md` and `COST_AND_QUOTA_RULES.md`.

---

## 17. Alerts

Critical production conditions SHOULD have alerts.

Examples:

* Sustained high error rate
* Authentication/security anomaly
* Critical service unavailable
* Database failure
* High latency
* Quota exhaustion
* Unexpected cost increase
* Background job failure
* Deployment health failure

Alerts MUST be actionable.

Avoid alerts that produce continuous noise without requiring action.

---

## 18. Health Checks

Production services SHOULD expose appropriate health information.

Health checks MAY distinguish between:

* Process is running
* Application is ready
* Critical dependency is available

Health endpoints MUST NOT expose sensitive internal information.

---

## 19. Deployment Observability

Every production deployment SHOULD be traceable to:

* Version
* Commit
* Environment
* Deployment time
* Deployment result

After deployment, verify:

```text
Deployment
→ Health
→ Errors
→ Critical flows
→ Performance
→ External dependencies
```

Follow `DEPLOYMENT_RULES.md`.

---

## 20. Development vs Production

Development observability MAY be more verbose.

Production observability MUST prioritize:

* Signal quality
* Security
* Privacy
* Cost control
* Actionability

Development-only debugging MUST NOT accidentally expose secrets or sensitive production data.

---

## 21. Retention

Logs and telemetry MUST have an intentional retention policy.

Retention SHOULD consider:

* Operational requirements
* Security requirements
* Privacy requirements
* Legal requirements
* Storage cost

Do not retain telemetry indefinitely without justification.

---

## 22. Cost Control

Observability itself consumes resources.

The system MUST avoid:

* Excessive logging
* Duplicate telemetry
* High-cardinality metrics without justification
* Unnecessary tracing
* Logging large payloads
* Storing sensitive data unnecessarily

Observability design MUST follow `COST_AND_QUOTA_RULES.md`.

---

## 23. Testing

Observability MUST be tested for critical paths.

Verify:

* Errors generate useful signals
* Request IDs propagate correctly
* Critical events are recorded
* Sensitive data is not logged
* Alerts trigger correctly where configured
* Health checks behave correctly
* Failed external services remain diagnosable

---

## 24. AI Development Rules

AI MUST NOT:

* Add random logging without architectural purpose
* Log secrets
* Log authentication tokens
* Log complete user payloads unnecessarily
* Add telemetry that violates privacy requirements
* Disable error tracking to hide failures
* Ignore production errors
* Claim observability is complete without verification
* Add expensive telemetry without considering cost

AI MUST inspect existing observability before creating new infrastructure.

---

## 25. Observability Workflow

For every feature requiring observability:

```text
IDENTIFY
↓
DEFINE IMPORTANT EVENTS
↓
DEFINE METRICS
↓
DEFINE ERROR SIGNALS
↓
IMPLEMENT
↓
VERIFY
↓
SECURITY & PRIVACY REVIEW
↓
COST REVIEW
↓
AUDIT
↓
COMPLETE
```

---

## 26. Completion Gate

Observability is complete only when:

* Critical operations are observable
* Important errors are diagnosable
* Request correlation exists where needed
* Security events are covered
* Sensitive data is protected
* Performance signals exist where required
* External failures are visible
* Background failures are visible
* Alerts exist for genuinely critical conditions
* Health checks are appropriate
* Retention is intentional
* Cost impact is understood
* Tests/verification are completed
* No critical observability gap remains

Final status MUST be one of:

```text
COMPLETE
COMPLETE WITH WARNINGS
BLOCKED
```

---

## 27. Core Principle

> If a production failure cannot be understood, traced, or measured, the system is not operationally complete.
