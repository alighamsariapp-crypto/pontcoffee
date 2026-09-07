# Product Discovery Skill

Use this Skill before creating a new project or when the product scope is materially unclear.

## Workflow

```text
Problem → Users → Outcome → Journey → MVP scope → Requirements → Acceptance criteria → Open questions
```

Define the problem with evidence and assumptions separated. Identify primary users, context, main needs, value proposition, measurable goals, and the most important user journeys. Define what is in scope and explicitly exclude work that does not belong in the first release.

Convert the result into a completed `PROJECT_SPEC.md`. Every P0 feature needs an observable acceptance condition. Record unresolved high-impact questions instead of silently inventing answers. Record important decisions with an ADR when they affect architecture, security, data, cost, or deployment.

Do not begin broad implementation while the primary user, core journey, MVP scope, or required data behavior remains unknown. Low-risk visual details may be completed using the Design System; business and security decisions may not be guessed.

## Completion gate

- [ ] Problem and evidence are recorded
- [ ] Users and outcomes are defined
- [ ] Core journeys are documented
- [ ] MVP in/out scope is explicit
- [ ] P0 features have acceptance criteria
- [ ] Data, roles, integrations, and constraints are identified
- [ ] Open questions and decisions are recorded
- [ ] `PROJECT_SPEC.md` is complete enough to implement
