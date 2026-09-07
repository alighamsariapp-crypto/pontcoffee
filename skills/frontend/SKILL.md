# Frontend Development Skill

## Purpose

This skill defines how the AI executes frontend development for a feature.

It does not redefine frontend architecture, coding standards, UX rules, or design tokens. Those are defined by the project's governing files.

---

## 1. Start With the Feature Contract

Before creating or changing UI code, identify:

* Feature purpose
* Required route/page
* User actions
* Required data
* API dependencies
* Required states
* Design references

The frontend must be driven by the feature requirements, not by isolated visual implementation.

---

## 2. Inspect Existing Frontend

Before creating new code, inspect:

* Routes
* Pages
* Feature modules
* Shared components
* UI primitives
* Hooks
* State management
* API/data services
* Types
* Existing patterns
* Existing tests

Prefer extending existing patterns over introducing parallel implementations.

---

## 3. Map the UI

Convert the approved design into a component structure.

Typical structure:

```text id="a83kf2"
Route
└── Page
    ├── Feature Components
    ├── Shared Components
    └── UI Primitives
```

Keep page composition separate from reusable component behavior.

---

## 4. Define Frontend Data Contracts

Before connecting UI to remote data, determine:

* Request shape
* Response shape
* Loading behavior
* Error behavior
* Empty behavior
* Mutation behavior
* Cache/state requirements

Use existing API contracts where available.

Do not invent frontend data structures that conflict with the backend contract.

---

## 5. Build the Interaction Flow

Implement the user's actual flow:

```text id="q71x5m"
User Action
→ UI State
→ Data Request
→ Server Response
→ State Update
→ UI Feedback
```

For local-only interactions, use the equivalent local state flow.

Avoid duplicating business rules in multiple components.

---

## 6. Manage State Deliberately

For every piece of state, determine:

* Who owns it?
* Who needs it?
* Is it derived?
* Is it local or shared?
* Does it come from the server?
* Does it need persistence?

Prefer the smallest appropriate state scope.

Do not create global state simply for convenience.

---

## 7. Implement Required UI States

For each relevant feature interaction, implement the applicable states:

```text id="h1s8cz"
Initial
Loading
Success
Empty
Validation Error
Permission Error
Not Found
Server Error
Network Failure
```

Do not hide failures behind generic successful-looking UI.

---

## 8. Responsive Implementation

Implement responsive behavior from the approved design workflow.

Where references exist:

```text id="6b1x4a"
Desktop Reference
Mobile Reference
Tablet Reference
```

Use each as guidance for its intended viewport.

Where a reference is missing, determine the appropriate behavior using the project's UX and design rules.

Do not simply scale desktop UI down.

---

## 9. Integrate With the Real API

When backend functionality exists, connect the frontend to the real API.

Verify:

```text id="f7k2px"
UI Action
→ Request
→ Authentication
→ Authorization
→ Validation
→ Server Processing
→ Response
→ UI Update
```

Do not use fake production data to hide missing integration.

---

## 10. Forms and Mutations

For forms and user-triggered mutations:

1. Validate user input.
2. Submit through the established data layer.
3. Show submission state.
4. Handle server validation errors.
5. Handle unexpected failures.
6. Update or invalidate affected data.
7. Provide clear success feedback where appropriate.

Do not assume a successful HTTP request means the business operation succeeded.

---

## 11. Performance and Stability

During implementation, watch for:

* unnecessary renders
* duplicated requests
* excessive client-side state
* unstable list keys
* unnecessary large bundles
* layout shifts
* unbounded lists
* expensive work during rendering

Optimize when there is a real reason, without adding unnecessary complexity.

---

## 12. Accessibility and Interaction Verification

Verify the implemented feature using the project's accessibility and UX requirements.

Check applicable:

* keyboard interaction
* focus behavior
* focus visibility
* semantic structure
* accessible names
* forms and validation
* dialogs/drawers
* loading feedback
* error feedback
* responsive interaction

Do not treat accessibility as a final cosmetic step.

---

## 13. Test the Frontend

Run the applicable tests defined in `TESTING_RULES.md`.

Verify both:

```text id="2f9v0c"
Component Behavior
+
Real Feature Flow
```

Include regression checks for affected existing functionality.

---

## 14. Frontend Completion Gate

Before reporting frontend work complete:

```text id="c5w8na"
[ ] Existing components/patterns inspected
[ ] Correct route/page structure implemented
[ ] Required states implemented
[ ] Data contracts respected
[ ] Real API connected where required
[ ] Responsive behavior verified
[ ] Accessibility reviewed
[ ] Tests pass
[ ] No known regression
```

A visually complete page is not sufficient.

---

## 15. Handoff

When frontend implementation is complete:

* Report what was implemented.
* Report API/backend dependencies.
* Report unresolved blockers.
* Report tests performed.
* Identify anything required from the next development layer.

Do not silently compensate for missing backend functionality with mock behavior.

---

## Operating Principle

> **Build the frontend as the real client of the system, not as a visual prototype disconnected from the application's data and business flow.**
