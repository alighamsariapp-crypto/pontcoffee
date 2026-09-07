# Google AI Studio Skill

## Purpose

This Skill defines how to use Google AI Studio safely inside this framework. It is a procedure, not a second copy of the project's architecture, security, database, API, UX, SEO, performance, privacy, or deployment rules. Those rules remain canonical in their named files.

## Before implementation

1. Confirm that `PROJECT_SPEC.md` exists. If it does not, create it from `PROJECT_SPEC.template.md` and stop implementation.
2. Identify one Feature Specification and one active phase.
3. Read only the canonical rules relevant to that Feature.
4. Inspect the existing code, routes, components, contracts, data model, configuration, and tests.
5. Report missing decisions, affected files, risks, and a small reversible plan.

## Required loop

```text
READ → SCOPE → IMPACT → PLAN → IMPLEMENT → INTEGRATE → VERIFY → AUDIT → REPORT
```

Work on one Feature at a time. Do not rewrite unrelated Features, replace working infrastructure without a recorded reason, or expand the MVP silently.

## Scope and impact

Before changing shared components, authentication, authorization, API contracts, database models, design tokens, Firebase configuration, deployment files, or environment configuration, inspect known consumers and record regression, migration, security, cost, and deployment impact.

If a high-impact decision is missing or documents conflict, do not implement the disputed behavior. Create a BLOCKED report containing the conflict, affected files, impact, options, and required decision. Unrelated low-risk work may continue.

## Implementation constraints

Use existing components and patterns before creating new ones. Keep business logic behind the appropriate boundary. Use real data flow when persistence is required. Do not leave fake success responses, dead controls, placeholder production content, disabled validation, exposed secrets, or unverified generated code.

AI-generated output is untrusted. Validate model output before rendering, storing, querying, executing, or sending it to another service. Apply `AI_SECURITY_RULES.md` whenever the Feature uses AI.

## Verification

Run the checks supported by the project in this order:

```text
Type check → Lint → Relevant tests → Build → User-flow verification → Feature audit
```

Add API, database, Firebase Rules, authorization, accessibility, responsive, SEO, performance, privacy, cost, and deployment checks when applicable. A passing build does not prove that the Feature is complete.

If verification fails, report it, diagnose it, fix only within scope, rerun the failed checks, and report the final result. Never disable a check to obtain a pass.

## Change report

Every meaningful change must report the Feature and scope, files changed, API/database/auth/security/privacy/cost/deployment impact, migrations and rollback needs, checks executed, results, and remaining issues.

## Completion gate

The Feature is complete only when its acceptance criteria, required real integrations, applicable canonical rules, tests, responsive behavior, accessibility, security checks, and audit evidence pass. Use `PASS`, `PASS WITH WARNINGS`, or `BLOCKED`; never claim production readiness from a screenshot or local build alone.
