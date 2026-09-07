# Design Workflow Skill

## Purpose

This skill defines **how the AI executes the design workflow** for a project.

It does not replace or duplicate:

* `PROJECT_SPEC.md`
* `DESIGN_SYSTEM.md`
* `UX_RULES.md`
* `ROADMAP.md`
* `AGENTS.md`

Those files define the rules and requirements.
This skill defines the operational process used to apply them.

---

## 1. Start From the Feature

Design work must be handled **feature-by-feature**, not as one large application-wide generation task.

For each feature:

```text
Feature
→ Design References
→ Design Analysis
→ UX/Component Mapping
→ Design Decision
→ Implementation Handoff
```

Do not design unrelated features during the same task unless explicitly requested.

---

## 2. Collect Available References

Before designing a feature, inspect all available references:

* Desktop screenshots
* Mobile screenshots
* Tablet screenshots
* Stitch designs
* Existing implemented screens
* Existing reusable components
* Project specification

References may be incomplete.

The AI must determine which parts are:

* explicitly defined
* visually implied
* missing and requiring reasonable completion

A missing reference is **not automatically a blocker**.

---

## 3. Analyze Before Creating

Before producing or implementing a design, identify:

* page purpose
* user goal
* primary actions
* information hierarchy
* required states
* responsive behavior
* reusable components
* feature-specific components
* interactions
* missing design decisions

Do not immediately start implementation after receiving a screenshot.

---

## 4. Handle Desktop and Mobile Independently

Treat each provided viewport as a design reference for that viewport.

If both Desktop and Mobile references exist:

```text
Desktop Reference → Desktop behavior
Mobile Reference → Mobile behavior
```

Do not mechanically scale one into the other.

If only Desktop exists:

```text
Desktop Reference
→ infer Mobile UX
→ apply project UX rules
→ create appropriate mobile behavior
```

If only Mobile exists, use the same principle in reverse for larger layouts.

---

## 5. Resolve Missing Design

When a required state or screen is not shown in the reference, complete it using this priority:

```text
PROJECT_SPEC.md
→ DESIGN_SYSTEM.md
→ UX_RULES.md
→ Existing Project UI
→ Feature Context
→ Reasonable Design Decision
```

The AI should choose the smallest reasonable addition necessary to make the feature complete.

Do not invent unrelated functionality.

---

## 6. Reuse Before Creating

Before introducing a new component:

1. Search the existing component system.
2. Identify a matching reusable component.
3. Extend it when the interaction is substantially the same.
4. Create a new component only when the interaction or responsibility is genuinely different.

Avoid visually similar duplicate components.

---

## 7. Stitch Workflow

When Google Stitch is used:

```text
Feature Definition
→ Stitch Design
→ Design Review
→ Responsive Review
→ Final Design Reference
→ Implementation
```

Stitch output is treated as a **design reference**, not as an unquestionable implementation specification.

If Stitch produces an incomplete or unreasonable design, correct the design according to the project specifications and system rules before implementation.

---

## 8. Design Handoff to Implementation

Before implementation begins, the AI must have enough information to determine:

* page/screen structure
* component structure
* interaction behavior
* responsive behavior
* required states
* data required by the UI
* actions requiring backend/API support

The handoff should be clear enough that implementation does not require guessing about fundamental feature behavior.

---

## 9. Design Review Gate

Before implementation, verify:

```text
[ ] Feature purpose is clear
[ ] References were reviewed
[ ] Missing states were resolved
[ ] Desktop/mobile behavior is understood
[ ] Existing components were checked
[ ] New components are justified
[ ] Major interactions are defined
[ ] Backend/API requirements are identified
```

If a critical design decision remains unresolved, stop at the design stage rather than silently inventing behavior.

---

## 10. Implementation Feedback Loop

Design is not permanently frozen.

During implementation, if technical constraints reveal that a design decision is incomplete or impractical:

```text
Implementation Finding
→ Design Adjustment
→ Review
→ Continue Implementation
```

Do not create large visual or UX deviations silently.

---

## 11. Feature Completion

A design is considered ready for implementation when:

```text
Reference
+ UX behavior
+ Responsive behavior
+ Components
+ Required states
+ Technical handoff
```

are sufficiently defined for the feature.

After implementation, the actual UI must be reviewed against the intended design and behavior.

---

## 12. Hard Prohibitions

The AI must not:

* generate the entire application's design in one operation
* assume a screenshot defines every state
* blindly copy a screenshot without understanding its behavior
* create duplicate components unnecessarily
* treat Desktop as a shrunken Mobile design
* invent unrelated features to fill missing references
* start implementation while fundamental feature behavior is unknown
* replace existing project design language without justification

---

## Operating Principle

> **References show what the feature should look like; the project specifications determine what it must do; this skill determines how the AI moves from one to the other.**
