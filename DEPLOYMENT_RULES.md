# Deployment Rules

## 1. Purpose

This document defines mandatory rules for building, deploying, releasing, monitoring, and rolling back the application across environments.

Deployment MUST be treated as a controlled engineering process.

A successful local build MUST NOT be considered proof of production readiness.

---

# 2. Deployment Principles

Production deployment MUST be:

* reproducible
* traceable
* reviewable
* secure
* reversible where practical
* environment-aware
* tested
* observable

No deployment should depend on undocumented manual steps.

---

# 3. Environment Model

Projects SHOULD separate environments:

```text id="d001"
Local
↓
Development
↓
Preview / Staging
↓
Production
```

The exact environment model MAY differ by project.

The environment strategy MUST be documented in `PROJECT_SPEC.md`.

---

# 4. Environment Isolation

Development and staging MUST NOT accidentally modify production resources.

Verify separation of:

* databases
* Firebase projects
* Storage
* authentication
* API credentials
* third-party services
* analytics
* payment providers
* domains
* environment variables

Production credentials MUST NOT be used casually in local development.

---

# 5. Configuration

Configuration MUST be environment-specific.

Separate:

```text id="d002"
Application Configuration
Secrets
Infrastructure Configuration
Feature Flags
```

Configuration MUST NOT be scattered throughout source code.

---

# 6. Secrets

Secrets MUST NEVER be committed to the repository.

Examples:

* API keys
* service-account credentials
* private tokens
* database credentials
* payment secrets
* signing keys
* webhook secrets

Secrets MUST be provided through secure environment or secret-management systems.

Client-exposed configuration MUST be explicitly classified as public.

---

# 7. Build Requirements

Production builds MUST verify:

* dependency installation
* type checking
* linting
* tests
* required integration tests
* security checks
* production build
* required environment configuration

A production build MUST fail when critical checks fail.

---

# 8. CI/CD

Where CI/CD is configured, the pipeline SHOULD automatically verify:

```text id="d003"
Install
↓
Typecheck
↓
Lint
↓
Unit Tests
↓
Integration / Contract Tests
↓
Security Checks
↓
Build
↓
Deploy
↓
Smoke Test
```

Deployment MUST NOT bypass required quality gates.

---

# 9. Pull Requests

Production-bound changes SHOULD pass CI before merge.

CI SHOULD verify at minimum:

* typecheck
* lint
* tests
* build

Additional checks MUST be added when required by the project.

---

# 10. Branching

The project MUST define a clear branching strategy.

Example:

```text id="d004"
main
  ↓
feature/*
  ↓
Pull Request
  ↓
CI
  ↓
Review
  ↓
main
  ↓
Production Deployment
```

The exact strategy MAY differ.

AI MUST NOT create a new branching model without justification.

---

# 11. Release Strategy

The project MUST define how releases are identified.

Possible strategies:

* semantic versioning
* release tags
* deployment commit
* platform release identifier

Every production deployment SHOULD be traceable to a specific source revision.

---

# 12. Database Changes

Database changes MUST be deployment-aware.

Before deployment:

1. identify schema/data changes
2. evaluate backward compatibility
3. define migration strategy
4. define rollback implications
5. test migration
6. verify production safety

For Firestore, schema evolution MUST consider existing documents and old application versions.

---

# 13. Migration Safety

Migrations SHOULD follow:

```text id="d005"
Backward-Compatible Change
↓
Deploy Compatible Application
↓
Migrate Data
↓
Enable New Behavior
↓
Remove Legacy Behavior Later
```

Avoid destructive migrations when an additive migration can safely achieve the same result.

---

# 14. Firebase Deployment

When Firebase is used, verify applicable:

* Firebase project
* environment
* Authentication configuration
* Firestore configuration
* Security Rules
* Storage Rules
* indexes
* Functions
* Hosting/App Hosting
* secrets
* environment variables

Deployment MUST NOT silently target the wrong Firebase project.

---

# 15. Infrastructure Changes

Infrastructure changes MUST be reviewed for:

* security
* cost
* availability
* scalability
* rollback
* environment isolation

Examples:

* domains
* DNS
* hosting
* server configuration
* Firebase configuration
* Cloud Run
* storage
* IAM
* service accounts

AI MUST NOT make high-impact production infrastructure changes silently.

---

# 16. Deployment Order

When multiple systems must be deployed, define a safe order.

Example:

```text id="d006"
Infrastructure
↓
Database-Compatible Changes
↓
Backend
↓
API
↓
Frontend
↓
Data Migration
↓
Feature Activation
```

The actual order MUST follow project dependencies.

---

# 17. Health Checks

Production services SHOULD expose appropriate health checks where supported.

Health checks MUST distinguish between:

```text id="d007"
Process Is Running
```

and:

```text id="d008"
Application Is Healthy
```

A service that starts successfully but cannot access required dependencies MUST NOT be considered fully healthy.

---

# 18. Smoke Tests

After deployment, critical flows SHOULD be verified.

Examples:

* application loads
* authentication works
* public routes work
* API responds
* database reads work
* database writes work
* critical Feature works
* payment flow works where applicable
* admin access works
* authorization works

Smoke tests MUST use safe test procedures and MUST NOT corrupt production data.

---

# 19. Rollback

Every production deployment SHOULD have a documented rollback strategy.

Rollback MAY involve:

* previous application version
* previous container/image
* previous hosting release
* feature flag disablement
* backward-compatible database handling

Database rollback MUST be treated separately from application rollback.

A deployment MUST NOT claim to be safely reversible when irreversible data changes have occurred without a recovery strategy.

---

# 20. Feature Flags

Feature flags MAY be used for:

* gradual rollout
* risky Features
* experimental functionality
* staged activation
* emergency disablement

Feature flags MUST have:

* owner
* purpose
* default behavior
* activation strategy
* removal plan

Do not accumulate permanent unused flags.

---

# 21. Zero-Downtime Considerations

For systems requiring availability, deployments SHOULD consider:

* backward compatibility
* connection handling
* graceful shutdown
* health checks
* rolling deployments
* startup time
* migration ordering

Do not claim zero downtime unless the deployment architecture actually supports it.

---

# 22. Static Assets & Caching

When deploying frontend assets:

* asset versioning SHOULD be used where appropriate
* cache behavior MUST be understood
* stale assets MUST NOT break application/API compatibility
* HTML and static asset caching MUST be compatible

Deployment MUST account for clients that temporarily hold older cached assets.

---

# 23. Domains & HTTPS

Production public services MUST use HTTPS.

Verify:

* domain configuration
* TLS certificate
* redirects
* canonical host
* security headers
* environment-specific domains

HTTP-to-HTTPS behavior MUST NOT create redirect loops.

---

# 24. Observability

Production deployments MUST be observable enough to detect critical failures.

Where applicable monitor:

* deployment status
* application errors
* API errors
* latency
* availability
* database failures
* authentication failures
* infrastructure failures
* unusual traffic

Observability requirements remain governed by `OBSERVABILITY_RULES.md`.

---

# 25. Deployment Security

Production deployment MUST enforce:

* least privilege
* protected secrets
* secure CI credentials
* protected production environments
* restricted deployment permissions
* dependency integrity
* auditability

CI/CD credentials MUST NOT be embedded in source code.

---

# 26. Dependency Changes

New dependencies MUST be reviewed before production deployment.

Evaluate:

* necessity
* maintenance
* license
* security
* bundle impact
* transitive dependencies
* compatibility

Dependency installation MUST NOT silently introduce unrelated packages.

---

# 27. Production Data

Production data MUST NOT be used for development or testing unless explicitly authorized and appropriately protected.

Never use:

* real customer credentials
* real payment data
* unnecessary personal data
* sensitive production records

for ordinary development testing.

---

# 28. Backups & Recovery

Projects with important production data MUST have an appropriate backup strategy.

Verify:

* backup exists
* retention is appropriate
* restoration process is documented
* restoration has been tested where practical

A backup that cannot be restored reliably MUST NOT be treated as sufficient recovery protection.

---

# 29. Deployment Failure

If deployment fails:

1. stop further rollout when appropriate
2. identify the failing stage
3. preserve logs/evidence
4. determine impact
5. rollback or repair safely
6. verify system health
7. verify critical user flows
8. document the cause
9. prevent recurrence where practical

Do not hide deployment failures by bypassing CI checks.

---

# 30. Post-Deployment Verification

After production deployment verify:

```text id="d009"
Version
↓
Health
↓
Critical Routes
↓
Authentication
↓
Authorization
↓
API
↓
Database
↓
Critical User Journeys
↓
Monitoring
```

Only then may the release be considered successfully deployed.

---

# 31. AI Prohibitions

AI MUST NOT:

* deploy directly to production without authorization
* expose secrets
* commit credentials
* disable CI checks
* bypass tests
* bypass security checks
* target production Firebase accidentally
* run destructive production migrations without explicit approval
* claim successful deployment without verification
* assume build success means deployment success
* assume deployment success means application health
* silently modify infrastructure
* silently change deployment architecture
* delete production data to resolve deployment problems

---

# 32. Completion Gate

A production deployment is complete only when:

```text id="d010"
Code Verified
↓
CI Passed
↓
Build Passed
↓
Security Checks Passed
↓
Deployment Succeeded
↓
Health Checks Passed
↓
Smoke Tests Passed
↓
Monitoring Confirmed
↓
Rollback Strategy Confirmed
↓
Release Reported
```

Final report:

```text id="d011"
Deployment Status: PASS

Environment:
[LOCAL / STAGING / PRODUCTION]

Version:
[VERSION / COMMIT]

Build:
PASS

Tests:
PASS

Security:
PASS

Deployment:
PASS

Health:
PASS

Smoke Test:
PASS

Monitoring:
PASS

Rollback:
[READY / N/A]

Release:
COMPLETE
```
