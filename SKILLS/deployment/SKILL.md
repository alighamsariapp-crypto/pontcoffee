# DEPLOYMENT SKILL

## 1. Purpose

This skill defines how AI MUST plan, implement, verify, and audit deployment changes safely.

Deployment is part of the product lifecycle.

A feature is NOT complete merely because it works locally.

---

## 2. Source of Truth

Before deployment work, read:

1. `PROJECT_SPEC.md`
2. `AGENTS.md`
3. `DEVELOPMENT_RULES.md`
4. `ARCHITECTURE.md`
5. `SECURITY_RULES.md`
6. `DATABASE_RULES.md`
7. `FIREBASE_RULES.md`
8. `OBSERVABILITY_RULES.md`
9. `PERFORMANCE_RULES.md`
10. `PRIVACY_RULES.md`
11. `COST_AND_QUOTA_RULES.md`
12. `DEPLOYMENT_RULES.md`

Existing deployment infrastructure MUST be inspected before creating or changing deployment configuration.

---

## 3. Deployment Scope

First determine what is changing:

* Frontend
* Backend
* API
* Database
* Firebase
* Storage
* Cloud/server infrastructure
* Environment variables
* Secrets
* CI/CD
* Domain/HTTPS
* Background jobs
* External integrations

Do not change unrelated infrastructure.

---

## 4. Inspect Before Changing

Inspect:

* Build configuration
* Package scripts
* Environment configuration
* Existing CI/CD
* Hosting configuration
* Firebase configuration
* Server configuration
* Database configuration
* Deployment scripts
* Health checks
* Monitoring
* Secrets
* Domain configuration
* Existing production workflow

Reuse existing infrastructure where appropriate.

---

## 5. Environment Model

Confirm the environments required by the project.

Typical model:

```text id="jv8p3n"
Development
↓
Staging / Preview
↓
Production
```

Environment boundaries MUST be explicit.

AI MUST NOT accidentally connect development builds to production data or services.

---

## 6. Configuration & Secrets

Determine:

* Required environment variables
* Public configuration
* Server-only configuration
* Secrets
* Firebase configuration
* External service credentials

Secrets MUST NOT be committed to Git.

Secrets MUST NOT be embedded into client bundles unless they are explicitly public configuration values.

---

## 7. Build Verification

Before deployment, verify:

* Dependencies install successfully
* Type checking passes
* Linting passes
* Tests pass
* Production build succeeds
* Required environment configuration exists
* No accidental development configuration is included

A successful local development server is NOT sufficient evidence.

---

## 8. CI/CD Verification

If CI/CD exists, verify:

```text id="b8d2e4"
Pull Request
↓
Install
↓
Type Check
↓
Lint
↓
Test
↓
Build
↓
Security / Quality Checks
↓
Merge
↓
Deployment
```

Deployment SHOULD NOT bypass required quality gates.

---

## 9. Database Changes

Before deploying database changes:

1. Identify schema/data impact.
2. Determine backward compatibility.
3. Identify migrations if required.
4. Determine deployment order.
5. Verify rollback implications.
6. Test against realistic data conditions.

Never deploy destructive database changes without an explicit migration strategy.

---

## 10. Firebase Deployment

For Firebase-based projects, verify the affected services:

* Authentication
* Firestore
* Storage
* Functions
* Hosting/App Hosting
* Security Rules
* Indexes

Deploy only the required services.

After deployment, verify that:

* Authentication works
* Database access works
* Security Rules remain correct
* Required indexes exist
* Storage permissions work
* Backend/API connectivity works

---

## 11. Deployment Order

When multiple layers change, determine a safe order.

Typical dependency:

```text id="c7k3sx"
Database / Infrastructure
↓
Backend
↓
API
↓
Frontend
↓
Verification
```

The actual order MUST follow the project's compatibility requirements.

Do not assume one universal deployment order.

---

## 12. Health Checks

Before declaring deployment successful, verify:

* Application starts
* Health endpoint works where applicable
* Readiness works where applicable
* Critical dependencies are available
* No immediate crash loop exists

Health checks MUST NOT expose secrets or sensitive infrastructure details.

---

## 13. Smoke Testing

After deployment, test critical flows.

Examples:

* Application loads
* Authentication
* Main navigation
* Core feature
* API requests
* Database read/write
* Critical user journey
* Error handling
* Mobile layout
* Important admin workflow

Smoke tests MUST use production-safe test behavior.

---

## 14. Production Verification

Deployment verification SHOULD cover:

```text id="e7n5ka"
Availability
↓
Critical User Flows
↓
API
↓
Database
↓
Authentication
↓
Security
↓
Performance
↓
Observability
```

Check monitoring and error signals immediately after release.

---

## 15. Rollback

Every meaningful production deployment SHOULD have a rollback strategy.

Determine:

* What can be rolled back
* How it is rolled back
* Whether database changes are reversible
* Whether previous frontend/backend versions remain compatible
* What happens to already-created data

Do not claim rollback capability without verifying it.

---

## 16. Zero-Downtime & Compatibility

Where required, deployment SHOULD preserve service availability.

For breaking changes, consider:

* Backward-compatible API changes
* Dual-read/dual-write strategies where necessary
* Feature flags
* Staged rollout
* Migration before code removal

Do not introduce breaking changes without an explicit plan.

---

## 17. Assets & Caching

After deployment, verify:

* Static assets resolve
* Cache behavior is correct
* Old assets do not break new code
* CDN behavior is correct where applicable
* Cache invalidation occurs where required

Avoid aggressive caching of dynamic or sensitive data.

---

## 18. Domain & HTTPS

Production deployment MUST verify:

* Correct domain
* HTTPS
* Certificate validity
* Redirect behavior
* Environment-specific domain configuration
* Secure cookie behavior where applicable

HTTP MUST NOT remain the intended production transport for sensitive application traffic.

---

## 19. Security Verification

Before production completion, verify:

* No secrets exposed
* Authentication works
* Authorization works
* Security headers are appropriate
* CORS is intentional
* Production debug mode is disabled
* Error responses do not expose internals
* Firebase Security Rules are correct
* Public resources are intentionally public

Follow `SECURITY_RULES.md`.

---

## 20. Observability Verification

After deployment, inspect:

* Error rate
* Request latency
* Availability
* Authentication failures
* Database failures
* External service failures
* Background job failures
* Important security events

Follow `OBSERVABILITY_RULES.md`.

---

## 21. Performance Verification

After deployment, verify that the release does not introduce major regressions in:

* Page performance
* Core Web Vitals
* API latency
* Database usage
* JavaScript payload
* Image loading
* Mobile performance

Follow `PERFORMANCE_RULES.md`.

---

## 22. Cost & Quota Verification

For production deployment, verify:

* Resource usage
* AI/API quotas
* Firestore usage
* Storage usage
* Serverless execution
* Background jobs
* Monitoring costs

Unexpected resource amplification MUST be investigated.

Follow `COST_AND_QUOTA_RULES.md`.

---

## 23. Privacy Verification

Before production release, verify:

* Production data remains isolated
* Logging does not expose personal data
* Analytics configuration is intentional
* External services receive only required data
* Privacy-sensitive configuration is correct

Follow `PRIVACY_RULES.md`.

---

## 24. Failure Handling

If deployment fails:

1. Stop and classify the failure.
2. Preserve evidence.
3. Determine whether production is affected.
4. Roll back if required.
5. Fix the root cause.
6. Re-run verification.
7. Re-deploy only after required gates pass.

Never hide deployment failures.

---

## 25. Post-Deployment Monitoring

Immediately after deployment:

```text id="w1z5cb"
Deploy
↓
Health Check
↓
Smoke Test
↓
Monitor Errors
↓
Monitor Performance
↓
Monitor Critical Flows
↓
Confirm Stability
```

The deployment is not complete until the system remains stable after release.

---

## 26. AI Hard Prohibitions

AI MUST NOT:

* Deploy directly to production without the required workflow
* Skip CI checks
* Skip tests
* Commit secrets
* Change production infrastructure without authorization
* Delete production data
* Run destructive migrations without approval
* Disable security controls to make deployment succeed
* Ignore failed health checks
* Ignore post-deployment errors
* Claim deployment success without verification
* Modify unrelated infrastructure
* Automatically roll back without an approved strategy

---

## 27. Completion Gate

Deployment is complete only when:

* Correct environment is confirmed
* Configuration is verified
* Secrets are protected
* Build succeeds
* Required tests pass
* CI/CD gates pass
* Database changes are safe
* Deployment succeeds
* Health checks pass
* Critical smoke tests pass
* Security is verified
* Observability is verified
* Performance is checked
* Cost/quota impact is understood
* Privacy requirements are satisfied
* Rollback strategy is known
* No critical production issue remains

Final status:

```text id="k0q4hf"
COMPLETE
COMPLETE WITH WARNINGS
BLOCKED
```

---

## 28. Final Report

AI MUST report:

```text id="m5c8qa"
Deployment Status:
Environment:
Version / Commit:
Services Changed:
Database Changes:
Configuration:
CI/CD:
Health Check:
Smoke Tests:
Security Verification:
Observability:
Performance:
Cost / Quota:
Privacy:
Rollback:
Remaining Issues:
Final Gate:
```

---

## 29. Core Principle

> Deployment is complete only when the released system is verified in its real environment, not merely when the build succeeds.
