# Accessibility Development Skill

Use this Skill for every user-facing Feature. The baseline is WCAG 2.2 AA where applicable.

## Workflow

```text
Requirements → Semantics → Interaction → Responsive → Assistive Technology → Automated Checks → Audit
```

Before implementation, identify keyboard paths, focus behavior, labels, error feedback, contrast, motion, language, direction, and touch targets. Use semantic HTML and existing accessible components before creating new behavior.

Verify keyboard navigation with Tab, Shift+Tab, Enter, Space, Escape, and arrow keys where applicable. Dialogs and drawers require focus placement, focus containment, Escape behavior, background interaction prevention, and focus restoration.

Every form control needs an accessible name, an associated label, useful instructions where necessary, and field-level error feedback. Icon-only controls need an accessible name and visible focus state. Images need meaningful alternative text or an intentional decorative treatment.

Run the project's automated accessibility checks and manually inspect the critical flows at mobile width, desktop width, zoom, reduced motion, and RTL where applicable. Accessibility is not complete because an automated tool passes; manual verification is required for important workflows.

## Completion gate

- [ ] Semantic structure is correct
- [ ] Keyboard flow works
- [ ] Focus is visible and managed
- [ ] Forms and errors are accessible
- [ ] Contrast and target sizes are reviewed
- [ ] Responsive, RTL, zoom, and reduced-motion behavior are reviewed
- [ ] Automated and manual checks are recorded
