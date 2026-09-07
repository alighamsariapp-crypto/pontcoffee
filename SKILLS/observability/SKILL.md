# OBSERVABILITY SKILL

## 1. Purpose

This skill defines how AI MUST design, implement, verify, and audit observability for a feature or system.

Observability MUST make important production behavior measurable, diagnosable, and traceable without violating security, privacy, or cost requirements.

---

## 2. Source of Truth

Before implementation, read and follow:

1. `PROJECT_SPEC.md`
2. `AGENTS.md`
3. `DEVELOPMENT_RULES.md`
4. `ARCHITECTURE.md`
5. `SECURITY_RULES.md`
6. `PRIVACY_RULES.md`
7. `PERFORMANCE_RULES.md`
8. `COST_AND_QUOTA_RULES.md`
9. `DEPLOYMENT_RULES.md`
10. `FIREBASE_RULES.md`
11. `OBSERVABILITY_RULES.md`

Existing project observability infrastructure MUST be inspected and reused where appropriate.

---

## 3. Feature Scope

For every feature, determine whether observability is required for:

* Frontend
* Backend
* API
* Database
* Authentication
* Authorization
* External services
* Background jobs
* AI functionality
* Performance
* Deployment
* Security events

Do not add telemetry without a clear operational purpose.

---

## 4. Inspect Before Changing

Before implementation, inspect:

* Existing logging
* Error tracking
* Metrics
* Tracing
* Request/correlation IDs
* Health checks
* Monitoring
* Alerting
* Existing telemetry utilities
* Environment configuration
* Privacy controls
* Security controls
* Deployment configuration
* Existing tests

Do not create a second observability system when an existing one can be extended.

---

## 5. Identify Important Events

For the feature, identify meaningful operational events.

Examples:

* Operation started
* Operation completed
* Operation failed
* Authorization denied
* External dependency failed
* Transaction failed
* Background job failed
* Important security event
* Critical user-flow failure

Every event MUST have a reason to exist.

---

## 6. Define Signals

Determine which signals are appropriate:

### Logs

Use for detailed event context.

### Metrics

Use for trends, rates, counts, latency, and resource usage.

### Traces

Use when a request crosses multiple application or service boundaries.

Do not automatically implement all three when the feature does not require them.

---

## 7. Request Correlation

For request-based systems, determine whether a request/correlation ID is required.

Where appropriate:

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

The same correlation context SHOULD be preserved across important boundaries.

---

## 8. Error Observability

Every important failure path MUST be diagnosable.

Verify:

* Error is captured
* Error is classified correctly
* Useful context exists
* Sensitive data is excluded
* Duplicate noise is minimized
* User-facing error remains safe
* Internal diagnostic information remains available to authorized operators

Never hide failures merely to make a feature appear successful.

---

## 9. Frontend Observability

When frontend telemetry is required:

1. Identify critical runtime failures.
2. Capture unhandled errors.
3. Integrate Error Boundary failures.
4. Track important failed operations.
5. Include safe contextual information.
6. Avoid collecting unnecessary user data.
7. Verify telemetry does not degrade UX.

Frontend telemetry MUST follow `UX_RULES.md`, `SECURITY_RULES.md`, and `PRIVACY_RULES.md`.

---

## 10. API Observability

For API features, verify:

* Request count
* Status codes
* Latency
* Errors
* Timeouts
* Authorization failures
* Rate-limit events
* External dependency failures

Where appropriate, connect API telemetry with request/correlation IDs.

---

## 11. Database Observability

For database operations, inspect:

* Read volume
* Write volume
* Query latency
* Transaction failures
* Retries
* Contention
* High-cost queries
* Unexpected read amplification

For Firestore specifically, inspect:

* Document reads
* Document writes
* Listener usage
* Transaction retries
* Large collection access
* High-frequency writes

Observability MUST NOT introduce unnecessary database operations.

---

## 12. Security Observability

Identify security-relevant events.

Examples:

* Authentication failures
* Authorization denials
* Privilege changes
* Sensitive account changes
* Suspicious activity
* Rate-limit violations
* Administrative actions

Security telemetry MUST be protected from unauthorized access.

---

## 13. AI Observability

For AI-enabled features, determine whether the system needs visibility into:

* AI request count
* Provider/model
* Latency
* Failure rate
* Token/usage metrics
* Tool-call failures
* Validation failures
* Safety events
* Rate limits
* Cost

Do not automatically log complete prompts, outputs, uploaded files, or private user data.

Follow:

* `AI_SECURITY_RULES.md`
* `COST_AND_QUOTA_RULES.md`
* `PRIVACY_RULES.md`

---

## 14. External Services

For every critical external dependency, determine:

* What can fail?
* How is failure detected?
* How is latency measured?
* Are timeouts visible?
* Are retries visible?
* Are rate limits visible?
* Is fallback behavior observable?

External service failure MUST NOT silently disappear.

---

## 15. Background Jobs

For scheduled or asynchronous work, verify:

* Execution
* Success
* Failure
* Duration
* Retry
* Timeout
* Final failure state

A background process MUST NOT fail silently.

---

## 16. Health Checks

Determine whether the feature affects application health.

Where appropriate, verify:

* Process health
* Readiness
* Critical dependency availability

Health checks MUST remain safe and MUST NOT expose sensitive internal information.

---

## 17. Metrics

Define metrics only when they answer useful operational questions.

Examples:

```text
request_count
error_rate
latency_ms
transaction_failures
authentication_failures
external_service_failures
job_failures
ai_requests
ai_usage
```

Avoid unnecessary high-cardinality metrics.

---

## 18. Alerts

Determine whether the feature requires alerts.

Alerts SHOULD exist for genuinely actionable conditions such as:

* Sustained high error rate
* Critical service failure
* Security anomaly
* Quota exhaustion
* Severe latency
* Critical background-job failure
* Deployment health failure

Do not create noisy alerts that operators will ignore.

---

## 19. Privacy & Security Check

Before completion, verify:

* No passwords logged
* No tokens logged
* No API keys logged
* No secrets logged
* No unnecessary personal data logged
* No payment credentials logged
* No sensitive payloads unnecessarily stored
* Access to telemetry is controlled
* Retention is intentional

Observability MUST NOT become a secondary data-leak channel.

---

## 20. Cost Check

Before completion, evaluate telemetry cost.

Check:

* Log volume
* Metric volume
* Trace volume
* Storage retention
* Database impact
* Network impact
* AI telemetry cost
* High-frequency events

Reduce or sample telemetry when appropriate without losing critical signals.

---

## 21. Testing

Test important observability behavior.

At minimum where applicable:

* Successful event
* Failure event
* Authorization failure
* External service failure
* Timeout
* Retry
* Request correlation
* Sensitive-data redaction
* Health check
* Background failure
* Alert condition

Observability tests MUST verify behavior, not merely that a logging function was called.

---

## 22. Implementation Workflow

Follow this sequence:

```text
IDENTIFY
↓
INSPECT
↓
DEFINE EVENTS
↓
DEFINE SIGNALS
↓
DEFINE CORRELATION
↓
DEFINE ERRORS
↓
IMPLEMENT
↓
VERIFY
↓
PRIVACY REVIEW
↓
SECURITY REVIEW
↓
COST REVIEW
↓
REGRESSION CHECK
↓
AUDIT
↓
COMPLETE
```

---

## 23. Failure Handling

If observability implementation fails:

1. Do not claim completion.
2. Identify the missing signal.
3. Identify whether the problem is implementation, configuration, infrastructure, privacy, security, or cost.
4. Fix the underlying issue.
5. Re-run verification.
6. Re-audit the affected flow.

Critical observability gaps are blockers.

---

## 24. AI Hard Prohibitions

AI MUST NOT:

* Add random logging
* Duplicate existing telemetry
* Log secrets
* Log authentication tokens
* Log sensitive user data unnecessarily
* Disable error tracking
* Hide production failures
* Create expensive telemetry without justification
* Claim observability completion without evidence
* Ignore privacy or security requirements
* Modify monitoring infrastructure unrelated to the feature without authorization

---

## 25. Completion Gate

The feature is observability-complete only when:

* Important events are identified
* Appropriate signals exist
* Critical failures are visible
* Request correlation exists where needed
* Security events are covered
* Sensitive data is protected
* External failures are observable
* Background failures are observable
* Required alerts exist
* Health checks are appropriate
* Cost impact is understood
* Tests/verification pass
* No critical observability gap remains

Final status:

```text
COMPLETE
COMPLETE WITH WARNINGS
BLOCKED
```

---

## 26. Final Report

At the end of the work, report:

```text
Observability Status:
Scope:
Events Added:
Metrics Added:
Tracing:
Error Tracking:
Security Events:
Alerts:
Health Checks:
Privacy Review:
Cost Review:
Tests:
Remaining Issues:
Final Gate:
```

---

## 27. Core Principle

> Observe what matters, protect what is sensitive, measure what costs resources, and never claim operational completeness without evidence.
