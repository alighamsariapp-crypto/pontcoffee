# DESIGN SYSTEM

## 1. Purpose

This document defines the reusable UI/UX system for all projects.

The Design System is the single source of truth for:

* Typography
* Colors
* Spacing
* Sizing
* Buttons
* Forms
* Components
* Layout
* Responsive behavior
* RTL behavior
* Interaction states
* Overlays
* Drawers
* Modals
* Admin layouts
* Accessibility
* Visual consistency

The implementation MUST NOT invent visual rules locally when an existing Design System rule exists.

---

# 2. Core Principle

The UI must be designed as a SYSTEM, not as a collection of independent screens.

Every visual decision MUST come from:

1. Design Tokens
2. Reusable Components
3. Layout Patterns
4. Interaction Patterns
5. Accessibility Rules

No arbitrary values should be introduced without justification.

---

# 3. NO DEFAULT HTML UI

## 3.1 Absolute Rule

Production UI MUST NOT visually rely on browser/User-Agent default styling.

HTML elements may be used for semantic and accessibility purposes, but their visual presentation MUST be controlled by the project's Design System.

Examples:

* `<button>` → `Button`
* `<input>` → `Input`
* `<select>` → `Select`
* `<textarea>` → `Textarea`
* `<details>/<summary>` → `Accordion/Disclosure`
* native checkbox → `Checkbox`
* native radio → `Radio`
* native dropdown → `Dropdown/Select`
* native dialog → `Dialog/Modal`
* table → `DataTable`
* navigation → `Navigation`
* pagination → `Pagination`

The HTML element is an implementation primitive, not the visual design.

Browser default appearance MUST NOT be treated as the final UI.

---

# 4. COMPONENT-FIRST RULE

Before creating any UI element:

1. Check whether the component already exists.
2. Reuse the existing component.
3. Extend the component if the behavior is compatible.
4. Create a new component only when the interaction or visual behavior is genuinely different.

Do NOT create multiple visually different versions of the same component without a documented reason.

---

# 5. COMPONENT STATES

Interactive components MUST define their relevant states.

Minimum supported states:

* Default
* Hover
* Active
* Focus
* Disabled
* Loading
* Error
* Selected
* Open
* Closed

Not every component requires every state, but every applicable state MUST be designed.

Focus MUST always be visually distinguishable.

---

# 6. DESIGN TOKENS

All reusable visual decisions MUST use Design Tokens.

Token categories:

* Color
* Typography
* Font weight
* Font size
* Line height
* Letter spacing
* Spacing
* Sizing
* Radius
* Border
* Shadow
* Z-index
* Motion
* Breakpoints
* Component states

Prefer semantic tokens over raw values.

Example:

```text
color.text.primary
color.text.secondary
color.surface.default
color.surface.elevated
color.border.default
color.action.primary
color.action.danger
color.focus.ring

spacing.xs
spacing.sm
spacing.md
spacing.lg
spacing.xl

button.height.sm
button.height.md
button.height.lg
```

A component MUST NOT randomly define its own color, spacing, radius or shadow when an existing token applies.

---

# 7. SPACING SYSTEM

Use a consistent spacing scale.

Default project scale:

```text
space-1   = 4px
space-2   = 8px
space-3   = 12px
space-4   = 16px
space-5   = 20px
space-6   = 24px
space-8   = 32px
space-10  = 40px
space-12  = 48px
space-16  = 64px
space-20  = 80px
```

These values are project defaults, not WCAG requirements.

The purpose is consistency.

Do NOT use arbitrary values such as:

```text
13px
17px
23px
29px
37px
```

unless there is a documented component-specific reason.

---

# 8. TYPOGRAPHY SYSTEM

## 8.1 General Rule

Typography MUST use a predefined scale.

AI MUST NOT make text unnecessarily large simply to fill visual space.

Typography must establish hierarchy through:

* Size
* Weight
* Line height
* Color
* Spacing
* Position

NOT through excessive font size.

---

## 8.2 Default Typography Scale

Recommended baseline:

```text
Caption      12px
Small        14px
Body         16px
Body Large   18px
Title Small  20px
Title Medium 24px
Title Large  30px
Display Small 36px
Display      48px
```

These are default Design System tokens and may be overridden by a project's `PROJECT_SPEC.md`.

Body text SHOULD normally start at 16px unless the project has a documented reason to use another base size.

---

## 8.3 Line Height

Recommended defaults:

```text
Caption       1.4
Small         1.5
Body          1.6
Body Large    1.6
Title         1.25
Display       1.15
```

Typography must remain readable when users increase text size.

WCAG 2.2 requires text to remain usable when resized up to 200% without loss of content or functionality.

---

## 8.4 Typography Restrictions

DO NOT:

* use huge text to fill empty space
* randomly change font sizes
* create a new font size for every component
* use inconsistent heading sizes
* use multiple unrelated fonts without justification
* use font size as the primary method of visual hierarchy

DO:

* use typography tokens
* use consistent hierarchy
* use weight and spacing to establish hierarchy
* preserve readability
* test at 200% text scaling

---

# 9. FONT SYSTEM

Font families MUST be defined as tokens.

Example:

```text
font.family.primary
font.family.secondary
font.family.monospace
```

For Persian/RTL projects, the project MUST explicitly define a Persian-capable font.

Example:

```text
Vazirmatn
```

is a valid project choice, but the Design System itself MUST remain font-agnostic.

The selected font must support the languages used by the project.

---

# 10. COLOR SYSTEM

Colors MUST be semantic.

Do not build the application directly around arbitrary hex values.

Example semantic structure:

```text
background.default
background.subtle
background.elevated

surface.default
surface.raised
surface.overlay

text.primary
text.secondary
text.muted
text.inverse

border.default
border.subtle
border.strong

action.primary
action.secondary
action.danger

status.success
status.warning
status.error
status.info

focus.ring
```

Text contrast MUST satisfy WCAG 2.2 AA.

Normal text:

```text
minimum 4.5:1
```

Large text:

```text
minimum 3:1
```

---

# 11. BUTTON SYSTEM

Buttons MUST have predefined sizes.

Default sizes:

```text
Small:
height: 36px
font-size: 14px

Medium:
height: 44px
font-size: 16px

Large:
height: 48px
font-size: 16px
```

Optional icon-only buttons MUST have their own size tokens.

Example:

```text
icon-button-sm
icon-button-md
icon-button-lg
```

Buttons MUST NOT automatically become oversized.

Use:

* Small → compact actions
* Medium → default action
* Large → primary/high-emphasis actions

Do NOT use Large buttons everywhere.

Button width should normally be content-based unless the component pattern explicitly requires full width.

Mobile layouts may use full-width primary actions when appropriate.

Interactive targets MUST satisfy WCAG 2.2 Target Size requirements.

WCAG 2.2 AA requires pointer targets to be at least 24×24 CSS pixels or satisfy an allowed exception.

For touch-heavy interfaces, larger practical targets SHOULD be preferred.

---

# 12. ICON BUTTONS

Icon-only buttons MUST:

* have an accessible name
* have a visible focus state
* use a predefined size
* use consistent icon sizing
* use consistent spacing
* not rely only on color
* not use arbitrary hit areas

Icons MUST NOT randomly change size across the application.

---

# 13. FORM CONTROLS

Every form control MUST use the Design System.

Required patterns:

* Input
* Textarea
* Select
* Combobox
* Checkbox
* Radio
* Switch
* Date Picker
* File Upload
* Search
* Number Input
* Password Input

Each control MUST support applicable:

* Default
* Hover
* Focus
* Filled
* Disabled
* Error
* Success
* Loading

Form labels, help text and errors MUST follow a consistent hierarchy.

---

# 14. ACCORDION / DISCLOSURE

## 14.1 No Browser Default Accordion

Do NOT ship a browser-default:

```html
<details>
<summary>...</summary>
</details>
```

as the final visual component.

If `<details>` is used for semantic behavior, it MUST be fully styled and integrated into the Design System.

---

## 14.2 Custom Accordion

Accordion MUST have:

* custom trigger
* custom icon
* custom spacing
* custom typography
* custom borders/background
* custom open state
* custom hover state
* custom focus state
* consistent animation
* keyboard accessibility

Accordion behavior MUST be predictable.

Do NOT nest accordions unless there is a strong documented reason.

Avoid using accordion when normal headings, page sections, tabs or navigation would provide a clearer experience.

---

# 15. TABS

Tabs are for switching between related content sections.

Tabs MUST:

* have a custom visual style
* have clear active state
* have clear focus state
* support keyboard navigation
* use consistent spacing
* not look like browser defaults

Do NOT use tabs as a replacement for page navigation.

If users need to understand or compare all sections simultaneously, prefer normal page sections.

---

# 16. DROPDOWN / SELECT

Native select appearance MUST NOT automatically become the application's final visual design.

A custom Select/Combobox component should be used when the product requires custom styling or advanced behavior.

The component MUST define:

* trigger
* menu
* option
* selected state
* hover state
* focus state
* disabled state
* loading state
* empty state
* keyboard behavior

Do not create custom dropdown behavior without accessibility support.

---

# 17. MODAL / DIALOG RULE

## 17.1 Modal Is NOT a Page

A Modal is a temporary focused interaction.

It MUST NOT become a container for an entire page.

DO NOT put:

* large dashboards
* complex forms
* large tables
* multi-section workflows
* long checkout flows
* complex admin management screens
* entire application pages

inside a normal centered modal.

---

## 17.2 Decision Rule

Use:

```text
Simple + short task
→ Modal
```

```text
Medium task + context needed
→ Side Panel / Drawer
```

```text
Complex task
→ Dedicated Page
```

```text
Multi-step / critical workflow
→ Dedicated Full Page / Flow
```

---

## 17.3 Modal Size

Modal sizes MUST be tokenized.

Example:

```text
modal.sm
modal.md
modal.lg
modal.xl
```

If the content continuously requires scrolling, complex interaction, large tables or multiple sections, the workflow SHOULD be moved to a dedicated page.

A modal MUST NOT be stretched simply because the content does not fit.

---

# 18. DRAWER / SIDE PANEL

Use Drawer/Side Panel when:

* the user needs context from the current page
* the task is medium complexity
* the task can be completed without becoming a full page
* editing a small/medium amount of information is required

Drawer MUST define:

* width
* header
* body
* footer
* close behavior
* overlay
* focus behavior
* responsive behavior

On mobile, important drawers SHOULD become a near-full-screen experience when required by the task.

Use `100dvh` where appropriate for viewport-height layouts.

---

# 19. ADMIN PANEL RULE

## 19.1 No "One Window" Admin

The admin application MUST NOT be implemented as:

```text
Dashboard
    ↓
Click item
    ↓
Large centered modal
    ↓
Entire management interface inside modal
```

This is prohibited for major workflows.

---

## 19.2 Admin Layout

Admin applications SHOULD use a real application layout:

```text
┌─────────────────────────────────────┐
│ Header / Top Bar                    │
├──────────────┬──────────────────────┤
│              │                      │
│ Sidebar      │ Main Content         │
│              │                      │
│ Navigation   │ Page                 │
│              │                      │
│              │                      │
└──────────────┴──────────────────────┘
```

Typical structure:

```text
AdminShell
├── Sidebar
├── Header
├── Breadcrumbs
├── PageHeader
├── MainContent
└── Optional SecondaryPanel
```

---

## 19.3 Admin Pages

Major admin resources MUST have dedicated routes/pages.

Examples:

```text
/products
/products/new
/products/:id
/products/:id/edit

/orders
/orders/:id

/customers
/customers/:id

/categories
/categories/:id

/settings
```

Do NOT hide an entire resource-management workflow inside a modal.

---

# 20. PAGE-FIRST PRINCIPLE

When deciding between Page, Drawer and Modal:

```text
Is this a major workflow?
        ↓
      YES
        ↓
Dedicated Page
```

```text
Is this a medium task where page context matters?
        ↓
      YES
        ↓
Drawer / Side Panel
```

```text
Is this a short, focused task?
        ↓
      YES
        ↓
Modal
```

This rule applies to:

* Checkout
* Product management
* Order management
* Customer management
* Settings
* Large forms
* Multi-step workflows
* Data management
* Admin operations

---

# 21. TABLES

Tables MUST use a dedicated DataTable component.

DataTable should support applicable:

* loading
* empty
* error
* pagination
* sorting
* filtering
* row selection
* bulk actions
* responsive behavior

Large tables MUST NOT automatically be placed inside small modals.

Complex table workflows SHOULD use dedicated pages.

---

# 22. CARDS

Cards MUST have consistent:

* padding
* radius
* border
* shadow
* typography
* action placement
* image ratio

Do not create a different card style for every page.

---

# 23. OVERLAY RULE

Every overlay component MUST define:

* z-index token
* overlay/background behavior
* focus behavior
* keyboard behavior
* escape behavior where appropriate
* scroll locking behavior
* mobile behavior

Do not randomly assign:

```text
z-index: 999
z-index: 9999
z-index: 99999
```

Use centralized z-index tokens.

---

# 24. RESPONSIVE SYSTEM

Responsive design MUST be mobile-first.

The interface MUST NOT simply shrink the desktop layout.

Components may change:

* layout
* density
* navigation
* interaction pattern
* button arrangement
* drawer behavior
* table behavior
* typography scale
* spacing

between viewport sizes.

---

# 25. REFLOW

The UI MUST support content reflow.

The design must remain usable around:

```text
320 CSS px
```

for normal page content.

Horizontal scrolling MUST NOT be required for normal content.

Exceptions may apply to content that inherently requires two-dimensional presentation, such as certain data tables or diagrams.

WCAG 2.2 Reflow requires content to remain usable at a width equivalent to 320 CSS pixels without loss of information or functionality.

---

# 26. RTL / LTR

The Design System MUST support writing direction.

Never hard-code visual direction using physical properties when a logical property is appropriate.

Prefer:

```css
margin-inline
padding-inline
inset-inline
border-inline
text-align: start
```

instead of:

```css
margin-left
margin-right
padding-left
padding-right
left
right
text-align: left
```

unless the physical direction is genuinely required.

This allows the same Design System to support RTL and LTR.

---

# 27. RESPONSIVE NAVIGATION

Desktop navigation and mobile navigation do NOT have to be identical.

Recommended patterns:

Desktop:

```text
Sidebar / Header Navigation
```

Mobile:

```text
Bottom Navigation
Mobile Header
Full-screen Navigation Drawer
```

The mobile experience MUST be intentionally designed rather than being a collapsed desktop layout.

---

# 28. MOBILE TOUCH TARGETS

Interactive controls MUST provide sufficient touch area.

WCAG 2.2 AA defines a minimum target size of 24×24 CSS pixels, with specific exceptions.

The Design System SHOULD generally use larger practical touch targets for mobile interfaces.

Default mobile controls SHOULD generally target approximately:

```text
44–48px
```

when appropriate.

This is a usability/design-system recommendation, not a WCAG minimum.

---

# 29. ACCESSIBILITY

Baseline:

```text
WCAG 2.2 AA
```

The Design System MUST consider:

* Keyboard navigation
* Focus visibility
* Screen readers
* Accessible names
* Color contrast
* Target size
* Reflow
* Text resizing
* Reduced motion
* Error identification
* Form labels
* Semantic HTML

WCAG 2.2 is the accessibility baseline unless the project specification explicitly requires a stricter target.

---

# 30. FOCUS

Every interactive component MUST have a visible focus state.

Do NOT remove browser focus indicators without replacing them with an equivalent or stronger Design System focus treatment.

Focus styling MUST be consistent across the application.

---

# 31. MOTION

Motion MUST be tokenized.

Example:

```text
motion.fast
motion.normal
motion.slow
```

Animations MUST communicate state or hierarchy.

Do NOT add animation simply because a component can animate.

Respect reduced-motion preferences.

---

# 32. DARK MODE

If the project supports dark mode:

Do NOT simply invert colors.

Define separate semantic theme mappings:

```text
Light Theme
Dark Theme
```

All semantic tokens MUST remain valid in both themes.

Contrast must continue to meet the accessibility requirements.

---

# 33. EMPTY / LOADING / ERROR STATES

Every major component MUST consider:

```text
Loading
Empty
Error
Success
Disabled
```

The UI MUST NOT rely on blank space when data is unavailable.

Do not use:

```text
Loading...
```

as the only loading experience for complex areas.

Use appropriate skeletons, progress indicators or contextual feedback.

---

# 34. SPACING AND DENSITY

Do not make the UI unnecessarily spacious.

Do not make the UI unnecessarily dense.

Density MUST match the context.

Examples:

```text
Marketing:
more whitespace

E-commerce:
balanced density

Admin/Data-heavy:
higher information density

Mobile:
touch-friendly density
```

The Design System may provide:

```text
compact
comfortable
spacious
```

density variants where needed.

---

# 35. VISUAL HIERARCHY

Every page MUST have a clear hierarchy:

```text
Page
 ├── Page Header
 │    ├── Title
 │    ├── Description
 │    └── Primary Actions
 │
 ├── Main Content
 │
 └── Secondary Content
```

Do not create hierarchy by making everything larger.

Hierarchy should primarily come from:

* placement
* spacing
* typography
* weight
* color
* grouping
* component structure

---

# 36. COMPONENT COMPOSITION

Prefer composition over duplicated components.

Example:

```text
Button
ButtonGroup
IconButton
SplitButton
```

instead of:

```text
HugeBlueButton
SmallBlueButton
AdminBlueButton
ProductBlueButton
CheckoutBlueButton
```

Variants must be intentional and token-driven.

---

# 37. DESIGN SYSTEM COMPONENT INVENTORY

The project SHOULD maintain reusable components for common patterns.

Core:

```text
Button
IconButton
Input
Textarea
Select
Combobox
Checkbox
Radio
Switch
Badge
Avatar
Tooltip
Popover
Dropdown
Tabs
Accordion
Dialog
Modal
Drawer
Toast
Alert
Card
Table
DataTable
Pagination
Breadcrumb
Navigation
Sidebar
Header
PageHeader
Form
FormField
Search
Filter
DatePicker
FileUpload
Skeleton
EmptyState
ErrorState
LoadingState
```

Not every project requires every component.

Only components required by the project should be implemented.

---

# 38. DESIGN SYSTEM EXTENSION RULE

A project may extend the Design System.

However:

```text
Existing token
→ reuse

Existing component
→ reuse/extend

New behavior
→ create variant or component

Completely new interaction
→ create new component
```

Do not bypass the Design System for speed.

---

# 39. AI IMPLEMENTATION RULE

AI MUST NOT invent UI patterns during implementation.

Before creating UI, AI MUST identify:

1. Required page pattern
2. Required component
3. Required tokens
4. Required responsive behavior
5. Required states
6. Accessibility requirements
7. Interaction model

If a required component does not exist, AI must create the reusable component before repeatedly implementing the same pattern.

---

# 40. DESIGN REVIEW GATE

Before implementation is considered complete, verify:

### Components

* No browser-default UI
* All major controls use Design System components
* No duplicated component styles
* All states are handled

### Typography

* Correct scale
* No oversized text
* Correct line-height
* Consistent hierarchy
* 200% text resize remains usable

### Buttons

* Correct size
* Correct hierarchy
* Correct touch target
* No oversized buttons without reason

### Layout

* Correct page structure
* Correct responsive behavior
* No unnecessary centered modal
* Major workflows use dedicated pages
* Admin uses real application layout

### Responsive

* Mobile-first
* Reflow works
* No unnecessary horizontal scrolling
* Touch targets are appropriate
* Mobile navigation is intentionally designed

### RTL

* Logical CSS properties
* Correct direction
* No accidental left/right assumptions

### Accessibility

* WCAG 2.2 AA baseline
* Keyboard accessible
* Visible focus
* Correct contrast
* Accessible names
* Correct form semantics

---

# 41. HARD PROHIBITIONS

The following are NOT allowed without explicit justification:

```text
❌ Browser-default visual controls
❌ Default accordion appearance
❌ Default select appearance
❌ Default button appearance
❌ Random font sizes
❌ Random spacing values
❌ Random border radius values
❌ Random shadows
❌ Oversized buttons
❌ Oversized typography
❌ Full application inside a modal
❌ Complex admin workflow inside a modal
❌ Multi-step major workflow inside a small modal
❌ Nested modals
❌ Desktop layout simply shrunk for mobile
❌ Hard-coded left/right for RTL-sensitive layout
❌ Arbitrary z-index values
❌ Repeated one-off component styles
```

---

# 42. DEFINITION OF DONE

A UI is NOT complete merely because it renders.

A UI is complete only when:

```text
Design Tokens
        ↓
Components
        ↓
Page/Layout
        ↓
Responsive behavior
        ↓
Interaction states
        ↓
Accessibility
        ↓
RTL/LTR
        ↓
Mobile UX
        ↓
Visual QA
        ↓
Design System compliance
```

have all been verified.

---

# 43. SOURCE OF AUTHORITY

This Design System is informed by:

* W3C WCAG 2.2
* W3C Design Tokens Community Group specification
* HTML specifications
* CSS Logical Properties
* MDN Web Platform documentation
* Carbon Design System
* GOV.UK Design System
* Established responsive and accessibility practices

Specific project values such as font scale, spacing scale, button heights, radius and breakpoints are Design System defaults, not universal web standards.

Project-specific requirements may override these defaults only through `PROJECT_SPEC.md` or an approved architecture/design decision.

---

# 44. FINAL RULE

The AI MUST treat this file as an enforceable UI contract.

The goal is not:

"Make something that looks okay."

The goal is:

"Build a consistent, reusable, responsive, accessible and intentionally designed interface using the Design System."

If a component looks like an unstyled browser control, it is NOT complete.

If a major workflow is hidden inside a centered modal, it is NOT complete.

If typography or button sizing is invented page-by-page, it is NOT complete.

If mobile is only a smaller desktop version, it is NOT complete.

If the UI violates the Design System, the implementation MUST NOT pass the Design QA gate.
