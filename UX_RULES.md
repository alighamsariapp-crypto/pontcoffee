
# UX RULES — PONT CAFE

Version: 1.0
Status: Active
Project: PONT CAFE Digital Menu

---

## 1. Purpose

This document defines the user experience rules for PONT CAFE.

The goal is to provide a menu experience that is:

- Simple
- Fast
- Elegant
- Clear
- Mobile-first
- Accessible
- Consistent
- Easy to understand without instruction

PONT CAFE is a QR-based digital menu.

It is not an online ordering application.

---

## 2. Source of Truth

`PROJECT_SPEC.md` is the primary project-specific source of truth.

The UX implementation must also follow:

- `DESIGN_SYSTEM.md`
- `CODING_RULES.md`
- `PERFORMANCE_RULES.md`

If a conflict exists, `PROJECT_SPEC.md` takes priority.

---

## 3. Core UX Principle

The main principle is:

> Show the user what they need, and nothing they do not need.

The interface must avoid:

- Visual clutter
- Unnecessary information
- Excessive controls
- Oversized components
- Decorative elements without purpose
- Unnecessary animations
- Unnecessary popups
- Unnecessary steps

---

## 4. QR Menu First

The customer usually reaches the menu by scanning a QR code.

The user should understand the interface immediately without onboarding.

Do not require:

- Registration
- Login
- Tutorial
- Account creation
- App installation
- Extra confirmation screens

---

## 5. Customer Journey

The primary information architecture is:

```text
Entry
  ↓
Cafe OR Restaurant
  ↓
Category
  ↓
Product List
  ↓
Product Detail
````

Do not mix Cafe and Restaurant content.

---

## 6. Main Entry Screen

The first screen should provide:

* PONT CAFE branding
* Language switcher
* Cafe entry
* Restaurant entry

The screen must remain simple.

Do not add:

* Product lists
* Promotional banners
* Ordering controls
* Cart
* Search
* Ratings
* Favorites
* Unnecessary marketing sections

---

## 7. Cafe Structure

Cafe categories are:

```text
Cafe
├── Hot Bar
├── Cold Bar
└── Dessert
```

Do not add additional Cafe categories unless the project specification changes.

---

## 8. Restaurant Structure

Restaurant categories are:

```text
Restaurant
├── Breakfast
├── Lunch
└── Dinner
```

Do not mix Cafe categories into Restaurant navigation.

---

## 9. Category Navigation

Category navigation must be predictable.

Users should always understand:

* Where they are
* What category they are viewing
* How to go back

Do not create deep or unnecessary navigation levels.

---

## 10. Back Navigation

Back navigation must preserve the information hierarchy.

Example:

```text
Product
  ↓ Back
Product List
  ↓ Back
Category
  ↓ Back
Cafe / Restaurant
  ↓ Back
Entry
```

Do not unexpectedly send users to the homepage when a normal back action should return them to the previous logical level.

---

## 11. Product List

The product card should contain only the required information.

Primary content:

* One product image
* Product name
* Price

Availability may also be shown when relevant.

Do not add:

* Long descriptions
* Ingredients
* Ratings
* Favorites
* Quantity controls
* Add-to-cart buttons
* Order buttons
* Review counts
* Unnecessary badges

---

## 12. Product Image

Each product card should use one primary image.

Images should be:

* Clear
* Consistent
* Appropriately cropped
* Visually aligned

Do not use multiple images on the product card.

---

## 13. Product Detail

The product detail page may contain:

* Back navigation
* Large product image
* Product name
* Full description
* Ingredients when available
* Allergens when available
* Price
* Availability state

Do not add ordering functionality.

---

## 14. No Ordering UX

PONT CAFE V1 does not support online ordering.

Do not implement:

* Add to cart
* Cart
* Checkout
* Quantity selector
* Order submission
* Delivery
* Online payment
* Table selection
* Customer account

The menu is informational.

---

## 15. No Customer Account

Customers must not be required to:

* Sign up
* Log in
* Provide an email
* Provide a phone number
* Create a profile

The menu should be immediately accessible after scanning the QR code.

---

## 16. Language Selection

Supported languages:

```text
FA
العربية
EN
```

Language selection must be easy to find.

Do not hide language selection inside unnecessary menus.

---

## 17. RTL / LTR

Persian:

```text
RTL
```

Arabic:

```text
RTL
```

English:

```text
LTR
```

The layout must adapt properly rather than simply changing text alignment.

---

## 18. RTL Mirroring

RTL layouts should correctly mirror directional UI where appropriate.

Examples:

* Navigation direction
* Back controls
* Arrows
* Spacing
* Alignment
* Navigation flow

Do not manually duplicate the entire interface for RTL.

Use reusable direction-aware components.

---

## 19. Typography

Typography must remain moderate and readable.

Use:

```text
IranYekan
```

for Persian and Arabic.

English should use the approved Latin companion font defined by the design system.

Avoid:

* Extremely large headings
* Tiny text
* Excessive font weights
* Too many typography styles

---

## 20. Visual Hierarchy

The interface must have a clear hierarchy.

Users should immediately recognize:

1. Current section
2. Category
3. Product name
4. Price
5. Optional supporting information

Do not make secondary information visually stronger than primary content.

---

## 21. Brand Usage

Primary brand color:

```text
#23336E
```

Brand color should be used intentionally.

Do not fill the entire interface with the brand color.

Avoid excessive visual decoration.

---

## 22. Whitespace

Whitespace is an important part of the PONT CAFE visual identity.

Use consistent spacing.

Do not overcrowd:

* Product cards
* Navigation
* Headers
* Buttons
* Text blocks

Do not create excessive empty areas that make the interface feel unfinished.

---

## 23. Component Size

UI elements should use comfortable but restrained dimensions.

Avoid:

* Oversized buttons
* Oversized cards
* Oversized headers
* Excessively large icons
* Excessively large typography

The interface should feel premium through balance and spacing, not size.

---

## 24. Touch Targets

Interactive elements must be comfortable to use on mobile.

Target minimum touch area:

```text
48 × 48 px
```

Do not place tiny clickable controls close together.

---

## 25. Mobile-First

Mobile is the primary UX environment.

Design and implement for:

```text
320px
360px
375px
390px
414px
```

before optimizing larger layouts.

Mobile must not be treated as a compressed desktop layout.

---

## 26. Desktop

Desktop layouts should preserve the same visual language as mobile.

Desktop may use:

* More horizontal space
* Larger content areas
* Multi-column layouts when appropriate

Do not redesign the application into a completely different visual system on desktop.

---

## 27. No Horizontal Scrolling

The customer interface must not create unintended horizontal scrolling.

Check:

* Images
* Cards
* Navigation
* Text
* Buttons
* Containers
* Tables if any

at small mobile widths.

---

## 28. Navigation

Navigation must remain simple.

Users should not need to understand complex menus.

Avoid unnecessary:

* Mega menus
* Nested dropdowns
* Hamburger menus for simple category structures
* Floating controls
* Persistent UI that blocks content

---

## 29. Mobile Navigation

Mobile navigation must be fully usable.

If a drawer is used:

* It must open completely.
* It must not be partially visible.
* It must have clear close behavior.
* It must respect safe areas.
* It must not create horizontal scrolling.

---

## 30. Modals

Do not use small centered modals for major workflows.

Major content should use a dedicated page.

Examples:

* Product detail
* Major menu navigation
* Admin product creation/editing

A modal may be used only for genuinely small contextual interactions.

---

## 31. Product Detail on Mobile

Product detail should be a proper mobile page.

It must not be implemented as a tiny desktop-style popup.

The content should fit the viewport naturally.

---

## 32. Search

Search is not required for V1 unless explicitly included in the approved specification.

Do not add search merely because other menu applications use it.

If search is introduced later, it must have a clear UX purpose.

---

## 33. Filters

Complex filtering is not required for the customer menu V1.

Do not add filter drawers or advanced filter interfaces unless explicitly required.

---

## 34. Loading States

Loading states must be subtle.

The PONT CAFE loading animation should:

* Use the PONT CAFE logo
* Be centered
* Be brief
* Use brand styling
* Avoid a generic spinner

Do not show loading UI when there is no actual loading operation.

---

## 35. Empty States

Empty states must explain what happened.

Examples:

```text
This category currently has no products.
```

Do not show a completely blank page.

Do not use oversized warning boxes.

---

## 36. Error States

Error messages should be:

* Clear
* Short
* Human-readable
* Actionable when possible

Avoid technical messages such as:

```text
SQLSTATE[HY000]
500 Internal Server Error
Undefined variable
```

for normal customers.

---

## 37. Service Availability

The menu may be unavailable outside defined service hours.

This state should be clearly different from a sold-out product.

Example:

```text
Currently unavailable
```

or the approved localized equivalent.

Do not use aggressive warning styling.

---

## 38. Sold-Out Products

Sold-out products should remain visible when appropriate.

The product may show:

```text
Sold Out
```

using a subtle visual treatment.

Avoid bright red warning styles.

Do not make sold-out products look like application errors.

---

## 39. Availability Distinction

These states must remain visually and logically distinct:

```text
Available
Sold Out
Outside Service Hours
```

Do not use the same message or visual treatment for all three.

---

## 40. Animation

Animations must be:

* Subtle
* Short
* Purposeful
* Consistent

Avoid:

* Excessive transitions
* Large movement
* Decorative animations
* Continuous animations
* Distracting effects

---

## 41. Accessibility

The interface must support accessible use.

Requirements include:

* Semantic HTML
* Keyboard navigation
* Visible focus states
* Accessible labels
* Adequate contrast
* Meaningful alt text
* Appropriate heading hierarchy

---

## 42. Color Accessibility

Do not communicate important information through color alone.

For example, sold-out state should not depend only on gray color.

Use:

* Text
* Visual state
* Structure
* Appropriate labels

in combination.

---

## 43. Content Density

The menu should remain visually calm.

Do not put too much information into a single card.

Product cards should prioritize:

```text
Image
Name
Price
Availability when required
```

Additional information belongs on the product detail page.

---

## 44. No Decorative Clutter

Avoid unnecessary:

* Badges
* Icons
* Dividers
* Shadows
* Gradients
* Patterns
* Decorative illustrations

Every visual element should have a clear purpose.

---

## 45. Icons

Use a consistent icon system when icons are required.

Do not mix multiple unrelated icon styles.

Do not use emoji as primary interface icons.

Icons should support meaning rather than decorate every element.

---

## 46. Images and UX

Food photography should support the menu experience.

Images should be:

* High quality
* Consistent
* Relevant
* Properly cropped

Do not use random stock images that do not represent the actual product.

---

## 47. Content Accuracy

The UI must display real product information.

Do not use:

* Fake names
* Fake prices
* Placeholder products
* Random descriptions
* Fake availability

in production.

---

## 48. Admin UX

The Admin interface should use the same overall PONT CAFE design language.

Do not create a separate visual language for Admin.

Admin should remain:

* Compact
* Practical
* Consistent
* Easy to scan

---

## 49. Admin Forms

Admin forms should be organized into logical sections.

Do not create extremely long unstructured forms.

Use:

* Clear labels
* Appropriate grouping
* Validation messages
* Helpful defaults
* Clear save/cancel actions

---

## 50. Admin Product Editor

The product editor should provide clear sections for:

* Basic information
* Translations
* Price
* Ingredients
* Allergens
* Image
* Availability
* Status

Do not force all information into one visually overwhelming block.

---

## 51. Admin Mobile

Admin must remain usable on mobile.

Do not simply shrink desktop tables.

For complex data:

* Use responsive cards
* Stack information appropriately
* Provide accessible actions
* Avoid horizontal page scrolling

---

## 52. Sticky Actions

For long mobile Admin forms, important actions may use a sticky action area.

The sticky area must:

* Remain accessible
* Respect safe-area insets
* Not cover form content
* Contain clear primary actions

---

## 53. Feedback

After an Admin action, provide clear feedback.

Examples:

* Product saved
* Product updated
* Product deleted
* Image uploaded
* Settings updated

Feedback should be visible without being intrusive.

---

## 54. Destructive Actions

Destructive actions such as deletion require clear confirmation when accidental activation could cause meaningful data loss.

The confirmation should clearly identify what will be affected.

Do not use vague messages such as:

```text
Are you sure?
```

when more context is appropriate.

---

## 55. No Small Modals for Major Admin Workflows

Major Admin workflows should use dedicated pages/workspaces.

Do not place important product creation or editing inside a narrow centered modal.

---

## 56. Consistency

The same interaction must behave the same way across the application.

Examples:

* Back navigation
* Buttons
* Form validation
* Language switching
* Availability states
* Product cards
* Admin actions

Do not create different interaction patterns for similar components.

---

## 57. State Completeness

Every important interactive or data-driven component should consider:

```text
Default
Loading
Empty
Error
Success
Disabled
Unavailable
```

Only states relevant to the specific component need to be implemented.

---

## 58. Performance UX

UX decisions must support performance.

Prefer:

* Server-rendered content
* Optimized images
* Minimal JavaScript
* Small assets
* Simple navigation

Do not introduce heavy client-side systems only for visual effects.

---

## 59. Offline / Network Failure

The application does not need a full offline-first architecture for V1.

However, network failures should not result in confusing blank screens.

Where appropriate, provide a clear retry or error state.

Do not fake offline data unless an offline feature is explicitly implemented.

---

## 60. Third-Party Dependence

Core customer UX must not depend on external services.

The menu should remain functional without:

* Firebase
* External database
* External image storage
* External analytics
* External UI services

Optional third-party services must never block the core menu.

---

## 61. No Feature Creep

Do not add UX features simply because they are common in other restaurant apps.

Do not add:

* Favorites
* Reviews
* Ratings
* Ordering
* Cart
* Checkout
* Customer accounts
* Loyalty
* Reservations
* Delivery tracking
* AI assistant

unless the project specification changes.

---

## 62. UX Review

Before completing a feature, verify:

```text
[ ] User understands where they are
[ ] Navigation is clear
[ ] Back navigation works
[ ] Mobile layout works
[ ] RTL works
[ ] LTR works
[ ] Touch targets are usable
[ ] Typography is readable
[ ] No horizontal scrolling
[ ] Loading state is appropriate
[ ] Empty state is appropriate
[ ] Error state is appropriate
[ ] Availability states are distinct
[ ] No unnecessary modal
[ ] No unnecessary feature
[ ] Accessibility considered
[ ] Visual style matches PONT CAFE
```

---

## 63. Final UX Rule

The PONT CAFE UX principle is:

> Simple, elegant, fast, clear, and focused on viewing the menu.

The interface should feel like a carefully designed digital menu, not a complex e-commerce application.

Every component, interaction, animation, and piece of information must justify its existence.

```


بعدش می‌ریم سراغ آخرین فایل اصلی یعنی **`DESIGN_SYSTEM.md`**.
```
