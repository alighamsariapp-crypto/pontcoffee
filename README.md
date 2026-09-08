# AI Web Framework

A specification-driven starter framework for building complete web applications with AI coding assistants, including Google AI Studio.

## What this repository is

This is a **rules, workflow, and template repository**. It is not an executable website and does not contain a finished application.

It provides:

- product and feature specification templates;
- architecture, security, API, database, UX, SEO, performance, privacy, and deployment rules;
- Skills that define how an AI assistant should work;
- phase, audit, release, and decision templates;
- executable validation for references, structure, secrets, duplicate documents, and route-map integrity;
- a low-context feature router and an installable pre-commit hook.

## Quick start

1. Create a new repository from this repository or copy it into a project directory.
2. Copy `PROJECT_SPEC.template.md` to `PROJECT_SPEC.md`.
3. Complete the project specification before implementation.
4. Create the required feature specifications from `templates/FEATURE_SPEC.template.md`.
5. Use the phase templates under `phases/` to record progress.
6. Add the actual application source code and its package manager configuration.
7. Install the local gate with `bash scripts/install-hooks.sh`.
8. Run `python3 scripts/framework_check.py` before release.

If `PROJECT_SPEC.md` does not exist, an AI assistant MUST create it from the template and MUST NOT start implementation until the required decisions are complete.

## Google AI Studio workflow

Google AI Studio is an implementation assistant, not the source of truth. Import or connect the repository, then begin with a prompt such as:

> Read `AGENTS.md`, `PROJECT_SPEC.md`, the applicable rules, and the active phase/feature specification. Do not implement yet. First report the current project state, missing decisions, affected files, risks, and a small implementation plan.

For each feature, use this sequence:

```text
Read → Scope → Impact analysis → Plan → Implement → Integrate → Verify → Audit → Report
```

Do not ask the assistant to build the entire application in one prompt. Work feature by feature and keep changes small and reversible.

## Low-context routing

Do not load all governance files for every Feature. Select the current Phase and, when implementation begins, add one Feature overlay:

```bash
python3 scripts/framework_route.py --phase 01
python3 scripts/framework_route.py --phase 04 --feature frontend
python3 scripts/framework_route.py --phase 04 --feature ai --json
```

The routing tables are maintained in `config/phase-map.json` and `config/route-map.json`. Each Phase pack has a small reading budget, and the Feature overlay is loaded only after the active Feature is known. The executable checker fails if a pack points to a missing file or grows beyond the context limit. See `CONTEXT_LOADING.md` for the session protocol.

## Executable enforcement

The framework cannot prove that an external AI agent followed prose instructions during generation. It can, however, fail the change before merge when repository-level invariants are violated. Run:

```bash
python3 scripts/framework_check.py
python3 scripts/framework_check.py --project --phase 03
python3 scripts/framework_check.py --project --feature F-003
```

The first command validates the framework repository. Project mode additionally requires a completed `PROJECT_SPEC.md` and invokes the state machine: previous Phases must be `PASS`, the target Phase or Feature must be `PASS`, artifacts must exist, and blockers must be empty. The GitHub workflow runs the framework checks, while a generated project CI must run the project-mode command for its active target. `scripts/install-hooks.sh` installs the structural check as a local pre-commit hook.

## Project quality gate

When this framework is copied into a real application, create the `.webtow/` state files from `templates/project-state/`. Then gate progression with:

```bash
python3 scripts/project_gate.py --phase 03
python3 scripts/project_gate.py --feature F-003
```

`framework_check.py` checks the reusable framework. `project_gate.py` checks the application workflow: previous Phases must be `PASS`, the current Phase must have a report and evidence, and a Feature must have its specification, report, audit, declared checks, and no blockers. `IN_PROGRESS`, `NOT_RUN`, `WARN`, `BLOCKED`, and missing values never pass.

The generated application must have its own CI pipeline for install, typecheck, lint, unit, integration/API, E2E, security, build, accessibility, responsive, and other project-specific checks. The framework CI is not a substitute for that pipeline.

## Repository structure

```text
AGENTS.md / DEVELOPMENT_RULES.md / CODING_RULES.md   Operating and engineering rules
PROJECT_SPEC.template.md / ROADMAP.md                 Product and delivery templates
ARCHITECTURE.md / DESIGN_SYSTEM.md / UX_RULES.md      Architecture and experience rules
API_RULES.md / DATABASE_RULES.md / FIREBASE_RULES.md   Data and integration rules
SECURITY_RULES.md / AI_SECURITY_RULES.md               Security rules
TESTING_RULES.md / PERFORMANCE_RULES.md                Quality rules
SEO_RULES.md / CONTENT_RULES.md / PRIVACY_RULES.md     Public-content rules
DEPLOYMENT_RULES.md / OBSERVABILITY_RULES.md            Operations rules
COST_AND_QUOTA_RULES.md                                Cost and quota rules
skills/                                                 Procedure-specific AI Skills
config/route-map.json                                   Low-context feature routing
scripts/                                                Executable checks, router, and hook installer
templates/                                              Feature, API, data, ADR, and release templates
phases/ / audits/                                       Phase and audit templates
.github/workflows/                                      Framework CI
```

## Project-specific files

The following files are created or completed for each real project and are not generic framework defaults:

- `PROJECT_SPEC.md`
- feature specifications;
- API contracts and data models;
- phase reports and ADRs;
- application source code;
- environment and deployment configuration.

## Scope and authority

Security, privacy, legal, and platform constraints cannot be weakened by a project specification. When documents conflict, record the conflict and resolve it explicitly; never silently choose an interpretation.

## Limitations

This framework does not replace human review for legal text, production access, payment, destructive migrations, security-sensitive changes, or final release approval. AI-generated code remains unverified until the relevant checks and user-flow verification pass.
