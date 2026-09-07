# AI Web Framework

A specification-driven starter framework for building complete web applications with AI coding assistants, including Google AI Studio.

## What this repository is

This is a **rules, workflow, and template repository**. It is not an executable website and does not contain a finished application.

It provides:

- product and feature specification templates;
- architecture, security, API, database, UX, SEO, performance, privacy, and deployment rules;
- Skills that define how an AI assistant should work;
- phase, audit, release, and decision templates;
- CI validation for this framework repository.

## Quick start

1. Create a new repository from this repository or copy it into a project directory.
2. Copy `PROJECT_SPEC.template.md` to `PROJECT_SPEC.md`.
3. Complete the project specification before implementation.
4. Create the required feature specifications from `templates/FEATURE_SPEC.template.md`.
5. Use the phase templates under `phases/` to record progress.
6. Add the actual application source code and its package manager configuration.
7. Run the project-specific CI checks before release.

If `PROJECT_SPEC.md` does not exist, an AI assistant MUST create it from the template and MUST NOT start implementation until the required decisions are complete.

## Google AI Studio workflow

Google AI Studio is an implementation assistant, not the source of truth. Import or connect the repository, then begin with a prompt such as:

> Read `AGENTS.md`, `PROJECT_SPEC.md`, the applicable rules, and the active phase/feature specification. Do not implement yet. First report the current project state, missing decisions, affected files, risks, and a small implementation plan.

For each feature, use this sequence:

```text
Read → Scope → Impact analysis → Plan → Implement → Integrate → Verify → Audit → Report
```

Do not ask the assistant to build the entire application in one prompt. Work feature by feature and keep changes small and reversible.

## Repository structure

```text
AGENTS.md                  AI operating rules
PROJECT_SPEC.template.md   Project specification template
SKILLS/                    Procedure-specific AI Skills
templates/                 Feature, API, data, ADR, and release templates
phases/                    Phase report templates
audits/                    Audit report templates
.github/workflows/          Framework CI
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
