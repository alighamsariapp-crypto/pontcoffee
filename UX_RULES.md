# UX RULES

## 1. PURPOSE

This document defines the mandatory UX and responsive UI rules for the entire application.

It covers:

* UX architecture
* Mobile-first design
* Responsive behavior
* Desktop/mobile separation
* RTL
* Navigation
* Forms
* Tables
* Admin Panel
* Modals
* Drawers
* Page-first workflows
* Touch interaction
* Accessibility
* Loading states
* Empty states
* Error states
* Responsive quality gates

These rules are mandatory.

---

# 2. CORE UX PRINCIPLE

The application MUST be designed around real user workflows.

The goal is NOT:

```text
Desktop UI
↓
Shrink
↓
Mobile
```

The goal is:

```text
Desktop Experience
        +
Mobile Experience
        +
Tablet Experience
        ↓
One coherent product
```

Mobile MUST NOT be treated as a smaller desktop.

---

# 3. MOBILE IS A FIRST-CLASS EXPERIENCE

Mobile layouts MUST be intentionally designed and implemented.

AI MUST NOT simply:

```text
reduce width
reduce font size
stack everything
hide overflow
```

and consider the mobile version complete.

Mobile may require different:

* layouts
* navigation
* information hierarchy
* controls
* actions
* component variants
* interaction patterns
* content density
* table presentation
* filtering patterns
* checkout flow

---

# 4. MOBILE-FIRST IMPLEMENTATION

Responsive implementation SHOULD begin from the smallest practical viewport and progressively enhance for larger screens.

Minimum supported viewport:

```text
320px
```

The interface MUST remain usable at:

```text
320px
360px
375px
390px
414px
```

unless the project explicitly defines another supported range.

---

# 5. NO GLOBAL HORIZONTAL SCROLL

The application MUST NOT create unintended horizontal page scrolling.

This is a HARD RULE.

The following is considered a UX failure:

```text
Mobile
↓
Page extends beyond viewport
↓
User can horizontally scroll the entire website
```

If a component is wider than the viewport, that component MUST be redesigned or isolated.

---

# 6. DO NOT HIDE OVERFLOW TO MASK BUGS

The following is NOT an acceptable fix for responsive problems:

```css
overflow-x: hidden;
```

when it merely hides content that does not fit.

Also prohibited as a fake fix:

```text
❌ body overflow hiding
❌ clipping buttons
❌ clipping table columns
❌ hiding content outside viewport
❌ negative positioning to force-fit content
```

The underlying layout problem MUST be fixed.

---

# 7. RESPONSIVE ARCHITECTURE

Responsive behavior MUST be intentional.

Every major component should define:

```text
Desktop behavior
Tablet behavior
Mobile behavior
```

Example:

```text
Navigation
Desktop → Sidebar/Header
Tablet  → Compact navigation
Mobile  → Dedicated mobile navigation
```

Do not assume one layout works equally well everywhere.

---

# 8. COMPONENT RESPONSIVE VARIANTS

Reusable components MAY have responsive variants.

Example:

```text
ProductGrid
Desktop → multi-column
Tablet  → reduced columns
Mobile  → optimized single/two-column layout
```

Example:

```text
AdminActions
Desktop → inline actions
Mobile  → action menu
```

Responsive variants MUST preserve the same design language.

---

# 9. MOBILE NAVIGATION

Mobile navigation MUST be designed specifically for mobile.

It should consider:

* thumb reach
* touch targets
* hierarchy
* safe area
* scrolling
* closing behavior
* keyboard interaction
* focus management

Do not simply shrink desktop navigation.

---

# 10. MOBILE HEADER

Mobile headers MUST have a dedicated layout.

Avoid:

```text
Desktop header
+
smaller font
=
mobile header
```

The mobile header should explicitly define:

```text
logo
menu/navigation
search
cart
account
actions
```

according to the project requirements.

---

# 11. TOUCH TARGETS

Interactive elements MUST be comfortably touchable.

Recommended practical target:

```text
44–48px
```

Do not create tiny controls simply to fit more content.

This applies especially to:

```text
buttons
icons
checkboxes
radio controls
quantity controls
tabs
navigation
table actions
close buttons
```

---

# 12. MOBILE FORMS

Forms MUST be optimized for touch.

Rules:

* fields should have adequate height
* labels must remain clear
* errors must be visible
* keyboard behavior must be considered
* important actions must remain reachable
* fields must not cause horizontal overflow

---

# 13. MOBILE TYPOGRAPHY

Mobile typography MUST remain readable.

Do NOT solve layout problems by making text extremely small.

Default body text SHOULD remain around:

```text
16px
```

unless the design system defines otherwise.

---

# 14. MOBILE SPACING

Mobile spacing may be reduced compared with desktop, but must remain intentional.

Do not compress the entire interface until:

```text
text touches controls
buttons become cramped
cards become unreadable
sections lose hierarchy
```

---

# 15. MOBILE CARDS

Cards MUST adapt to mobile.

Do not allow:

```text
fixed-width desktop cards
```

to overflow the viewport.

Cards should use:

```text
width: 100%
max-width
responsive grid
content wrapping
```

as appropriate.

---

# 16. MOBILE TABLES

Tables require special treatment.

A complex desktop table MUST NOT simply be placed inside a mobile page and considered responsive.

Preferred mobile patterns:

```text
Table
↓
Mobile Card List
```

or:

```text
Table Row
↓
Compact Row
↓
Expandable Details
```

or:

```text
Essential Columns
+
Details View
```

---

# 17. TABLE RESPONSIVE STRATEGY

For every table, explicitly decide:

```text
What information is essential?
What information is secondary?
What actions are essential?
What can move into details?
What can become an action menu?
```

This decision MUST happen before implementation.

---

# 18. ADMIN PANEL MOBILE

The Admin Panel MUST have a dedicated mobile UX strategy.

Admin desktop layouts MUST NOT simply be compressed.

This applies to:

```text
Sidebar
Header
Breadcrumbs
Page header
Toolbars
Filters
Tables
Forms
Actions
Charts
Dashboards
```

---

# 19. ADMIN TABLE HARD RULE

A desktop Admin Table MUST NEVER cause the entire mobile website to horizontally scroll.

Invalid:

```text
┌──────────────────────────────────────────────┐
│ Mobile viewport                              │
│                                              │
│   <-------- huge table -------->             │
│                                              │
└──────────────────────────────────────────────┘
```

where the entire page moves horizontally.

---

# 20. ADMIN TABLE ALLOWED PATTERNS

When a table cannot reasonably fit on mobile, use one of:

### Pattern A — Mobile Cards

```text
Desktop:
Table

Mobile:
┌──────────────────────┐
│ Product              │
│ SKU                   │
│ Price                 │
│ Stock                 │
│ Status                │
│ ⋮ Actions             │
└──────────────────────┘
```

### Pattern B — Expandable Row

```text
Primary information
        ↓
More details
        ↓
Actions
```

### Pattern C — Essential Columns

Only the most important columns remain visible.

Secondary information moves into:

```text
Details
Drawer
Expandable section
Dedicated page
```

### Pattern D — Isolated Table Scroll

If horizontal scrolling is genuinely necessary:

```text
Page
 └── Table Container
       └── horizontal scroll
```

NOT:

```text
Page
 └── horizontal scroll
```

The horizontal scroll MUST be limited to the table container.

---

# 21. ADMIN TABLE PROHIBITIONS

The following are prohibited:

```text
❌ Fixed desktop table width on mobile
❌ min-width on the entire page
❌ Giant column compression
❌ Tiny unreadable text
❌ Buttons overflowing rows
❌ Hidden content that becomes inaccessible
❌ Global horizontal page scroll
❌ overflow-x:hidden as a fake fix
```

---

# 22. ADMIN ACTIONS ON MOBILE

Desktop:

```text
Edit | View | Delete
```

may become mobile:

```text
⋮
```

with:

```text
View
Edit
Delete
```

inside a suitable action menu.

Actions MUST remain accessible.

---

# 23. ADMIN TOOLBAR

Desktop admin toolbar may contain:

```text
Search
Filter
Sort
Export
Create
Bulk Actions
```

Mobile SHOULD reorganize these controls.

Example:

```text
Search
Filter
More
```

instead of forcing all controls into one horizontal row.

---

# 24. ADMIN FILTERS

Complex filters MUST NOT create an oversized desktop sidebar on mobile.

Mobile filters SHOULD use:

```text
Full-screen filter page
```

or:

```text
Near-full-screen bottom sheet/drawer
```

with:

```text
Fixed header
Scrollable content
Sticky footer
Primary CTA
```

---

# 25. MOBILE FILTER CTA

For result-based filtering, the mobile filter experience SHOULD provide a clear action such as:

```text
Show 24 results
```

The CTA should remain accessible without requiring the user to scroll to the bottom.

---

# 26. SAFE AREA

Mobile interfaces MUST account for device safe areas where relevant.

Especially:

```text
bottom navigation
sticky actions
full-screen drawers
bottom sheets
checkout actions
```

---

# 27. MOBILE DRAWERS

Important mobile drawers SHOULD use nearly the full available viewport.

For full-height interactions:

```text
100dvh
```

SHOULD be preferred over assumptions based only on `100vh`.

---

# 28. MODAL RULE

Use a modal only for short, focused interactions.

Good examples:

```text
confirmation
short form
quick information
small decision
```

Bad examples:

```text
entire checkout
large admin workflow
large table
complex multi-step form
full application page
```

---

# 29. PAGE-FIRST PRINCIPLE

When a workflow becomes complex, move it to a page.

Decision rule:

```text
Simple
→ Modal

Medium
→ Drawer / Side Panel

Complex
→ Dedicated Page

Multi-step / Critical
→ Full Page / Dedicated Flow
```

---

# 30. NO NESTED MODALS

Avoid:

```text
Modal
↓
Modal
↓
Modal
```

If a workflow requires nested dialogs, reconsider the UX architecture.

---

# 31. CHECKOUT MOBILE

Checkout MUST be treated as a dedicated mobile workflow.

It MUST NOT depend on a small centered modal.

Mobile checkout should provide:

```text
clear steps
readable forms
sticky primary action where appropriate
visible totals
easy navigation
error recovery
```

---

# 32. MOBILE CART

Cart interactions MUST be designed specifically for mobile.

Consider:

```text
quantity controls
product information
remove action
subtotal
shipping
discount
checkout CTA
```

Do not allow cart rows to become wider than the viewport.

---

# 33. RESPONSIVE IMAGES

Images MUST remain within their containers.

Avoid fixed dimensions that cause overflow.

Product images SHOULD preserve their intended aspect ratio.

---

# 34. RESPONSIVE CONTENT

Long content MUST wrap safely.

Test:

```text
long product names
long usernames
long email addresses
large numbers
long translations
large prices
```

No important content should become inaccessible because of text length.

---

# 35. RTL

For RTL applications:

```text
dir="rtl"
```

must be defined intentionally.

Use CSS logical properties where possible:

```text
margin-inline
padding-inline
inset-inline
border-inline
text-align: start
```

Avoid unnecessary physical-direction rules:

```text
margin-left
margin-right
left
right
```

---

# 36. RTL COMPONENT TESTING

RTL MUST be verified for:

```text
navigation
tables
forms
dropdowns
drawers
modals
pagination
icons
breadcrumbs
admin layouts
```

Icons that communicate direction MUST also be reviewed.

---

# 37. ACCESSIBILITY

The UX baseline is:

```text
WCAG 2.2 AA
```

Important requirements include:

```text
keyboard navigation
visible focus
labels
semantic structure
contrast
reflow
zoom
screen-reader compatibility
reduced motion
```

---

# 38. KEYBOARD ACCESS

All important interactions MUST be keyboard accessible.

Especially:

```text
menus
dialogs
drawers
tabs
forms
tables
dropdowns
filters
admin actions
```

---

# 39. FOCUS MANAGEMENT

Dialogs and drawers MUST manage focus correctly.

When opened:

```text
Focus
↓
Relevant interactive content
```

When closed:

```text
Focus
↓
Trigger
```

where appropriate.

---

# 40. LOADING STATES

Every async interface MUST define a loading state where appropriate.

Avoid:

```text
blank screen
frozen button
unclear waiting
```

---

# 41. ERROR STATES

Errors MUST be understandable.

Provide:

```text
what happened
what failed
what the user can do
```

Do not expose technical implementation details.

---

# 42. EMPTY STATES

Empty data is not automatically an error.

Examples:

```text
No products
No orders
No search results
Empty cart
No notifications
```

Each important empty state SHOULD provide useful context or next action.

---

# 43. SKELETONS

Skeleton loading states SHOULD represent the actual content structure.

Do not create decorative skeletons that cause layout shifts when real content appears.

---

# 44. LAYOUT STABILITY

Avoid unnecessary layout shifts.

Reserve space for:

```text
images
async content
alerts
validation messages
dynamic controls
```

---

# 45. RESPONSIVE BREAKPOINTS

Breakpoints MUST be based on layout needs, not device-name assumptions.

Do not create unnecessary breakpoints such as:

```text
iPhone
iPad
Samsung
Laptop
```

unless a real design requirement exists.

---

# 46. NO ARBITRARY RESPONSIVE FIXES

Do not accumulate:

```text
@media
@media
@media
@media
```

to patch an incorrectly designed component.

If responsive CSS becomes excessively complex:

```text
STOP
↓
Review component structure
↓
Review layout strategy
↓
Refactor
```

---

# 47. DESKTOP-MOBILE DESIGN PARITY

Desktop and mobile do NOT need identical layouts.

They MUST have consistent:

```text
brand
visual language
information hierarchy
terminology
business behavior
```

but may have different interaction patterns.

---

# 48. RESPONSIVE TESTING

Every major page MUST be tested at minimum:

```text
320px
360px
375px
390px
414px
768px
1024px
1280px+
```

Testing should verify:

```text
layout
overflow
navigation
forms
tables
actions
images
typography
spacing
```

---

# 49. HORIZONTAL OVERFLOW TEST

Every page MUST be checked for unintended horizontal overflow.

Conceptually:

```text
document width
≤
viewport width
```

except for intentionally isolated components such as a table container.

---

# 50. ADMIN RESPONSIVE QUALITY GATE

Every Admin page containing a table MUST pass:

```text
320px
360px
375px
390px
414px
```

without:

```text
❌ page-level horizontal scroll
❌ clipped content
❌ inaccessible actions
❌ unreadable text
❌ broken filters
❌ overflowing toolbar
```

---

# 51. MOBILE QUALITY GATE

A page FAILS the UX Quality Gate if:

```text
Desktop works
BUT
Mobile is only a compressed desktop layout
```

or:

```text
Mobile creates unintended horizontal page scrolling
```

or:

```text
Admin table breaks the page width
```

---

# 52. AI MOBILE IMPLEMENTATION RULE

Before declaring a responsive page complete, AI MUST inspect:

```text
Desktop
Tablet
Mobile
```

and explicitly verify:

```text
No horizontal page overflow
No clipped content
No inaccessible actions
No broken tables
No broken forms
No broken navigation
```

---

# 53. AI RESPONSIVE PROHIBITIONS

AI MUST NOT:

```text
❌ simply shrink desktop
❌ hide overflow to hide bugs
❌ reduce everything to tiny text
❌ compress tables until unreadable
❌ use fixed desktop widths on mobile
❌ force every desktop component into mobile unchanged
❌ assume one breakpoint solves responsiveness
❌ use page-level horizontal scrolling as a table solution
❌ sacrifice accessibility to fit content
```

---

# 54. UX IMPLEMENTATION LOOP

For every major interface:

```text
Requirement
↓
User Flow
↓
Desktop UX
↓
Mobile UX
↓
Component Design
↓
Implementation
↓
Responsive Testing
↓
Accessibility Testing
↓
UX Review
↓
Quality Gate
```

---

# 55. UX DEFINITION OF DONE

A UX feature is complete only when:

* Desktop behavior is correct
* Mobile behavior is intentionally designed
* Tablet behavior is acceptable
* RTL is correct where required
* Touch interaction is usable
* Keyboard interaction works
* Focus behavior works
* Loading states exist
* Error states exist
* Empty states exist
* Important workflows are page-first
* Complex tables have a mobile strategy
* No unintended page-level horizontal scroll exists
* Admin mobile behavior has been tested
* Accessibility baseline is satisfied

---

# 56. FINAL UX RULE

The following is NOT acceptable:

```text
Desktop Design
↓
CSS shrink
↓
"Responsive Complete"
```

The required process is:

```text
Desktop UX
+
Mobile UX
+
Tablet UX
+
RTL
+
Accessibility
+
Real User Flows
↓
Implementation
↓
Responsive Verification
↓
UX Quality Gate
```

Mobile is a first-class product experience.

Admin tables and complex data interfaces MUST be specifically designed for mobile.

No component is allowed to break the width of the application and force the user to horizontally scroll the entire website.
