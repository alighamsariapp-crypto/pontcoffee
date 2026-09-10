
````markdown
# PONT CAFE — PROJECT SPECIFICATION

## Document Purpose

This document is the project-specific source of truth for the PONT CAFE digital menu application.

It defines:

- Product scope
- Business behavior
- User types
- User journeys
- Features
- Technical stack
- Database requirements
- Admin requirements
- UX requirements
- Design requirements
- Localization
- Deployment requirements
- Project constraints
- Development phases
- Definition of Done

This document MUST be read together with the repository's global rules.

The project MUST NOT silently override security, accessibility, privacy, coding, database, testing, or deployment rules.

---

# 1. Project Identity

## Project Name

`PONT CAFE Digital Menu`

## Project Type

`QR Digital Restaurant / Cafe Menu`

## Version

`V1`

## Status

`Specification`

## Owner

`PONT CAFE`

## Primary Repository

`This GitHub repository`

---

# 2. Product Overview

## Product Summary

PONT CAFE is a mobile-first digital menu accessed primarily through a QR code at cafe and restaurant tables.

Customers scan the QR code and view the cafe and restaurant menu directly in their browser.

The product is a menu presentation system.

It is NOT an online ordering platform.

The application must provide a fast, elegant, simple and reliable menu experience for customers and a practical administration system for staff.

---

# 3. Primary Goal

The primary goal is:

> Provide customers with a fast, beautiful, simple and multilingual digital menu while allowing authorized staff to manage menu content from an administration panel.

The customer should be able to:

1. Open the menu.
2. Select a language.
3. Select Cafe or Restaurant.
4. Select a category.
5. Browse menu items.
6. Open an item.
7. Read its information.
8. Return to the previous level.

The staff should be able to:

1. Authenticate to the admin panel.
2. Manage categories.
3. Manage products.
4. Manage product translations.
5. Manage prices.
6. Manage images.
7. Mark products as sold out.
8. Manage service availability.
9. Manage basic menu settings.

---

# 4. Product Context

The application is intended for PONT CAFE and is primarily designed for QR-based customer access.

The product must prioritize:

- Speed
- Simplicity
- Visual quality
- Mobile usability
- Reliability
- Local hosting
- Low operating cost
- Easy content management
- Multilingual support

The system should avoid unnecessary infrastructure and unnecessary third-party dependencies.

---

# 5. Problem Definition

## Problem

Traditional printed menus become difficult to update, replace and maintain.

The digital menu should allow PONT CAFE to update products, prices, images and availability without rebuilding the customer interface manually.

## Current Situation

Menu content may change over time.

A database-backed administration system is therefore required.

## Why It Matters

The restaurant needs a menu that:

- Can be updated easily.
- Works well on mobile phones.
- Supports Persian, Arabic and English.
- Shows current prices and availability.
- Does not require customers to install an application.
- Does not require online ordering.

---

# 6. Target Users

## Primary User — Customer

| User Type | Description | Main Need | Priority |
|---|---|---|---|
| Customer | Cafe or restaurant guest scanning the QR code | Quickly view the menu | HIGH |

## Secondary User — Admin

| User Type | Description | Main Need | Priority |
|---|---|---|---|
| Admin | Authorized PONT CAFE staff | Manage menu content | HIGH |

## User Context

Customers:

- Primarily use mobile phones.
- May use the application through a QR code.
- May have limited technical ability.
- Need fast access to menu information.
- May use Persian, Arabic or English.
- Should not need an account.

Admins:

- Use desktop or mobile browsers.
- Need simple and reliable content management.
- Need clear editing workflows.
- Should not need technical knowledge.

---

# 7. Value Proposition

## Core Value

A fast, elegant and multilingual digital menu that is easy for customers to use and easy for PONT CAFE staff to maintain.

## Differentiators

- Mobile-first UX.
- Persian / Arabic / English.
- True RTL and LTR support.
- Simple navigation.
- No unnecessary ordering functionality.
- Local production hosting.
- Database-backed content management.
- Centralized design system.
- Controlled feature-by-feature development.

## User Outcome

Customers should find the desired food or drink with minimal interaction.

Staff should be able to update menu content without developer involvement.

---

# 8. Business Goals

| Goal | Metric | Target | Timeframe |
|---|---|---|---|
| Fast menu access | Customer can reach categories quickly | Minimal interaction | V1 |
| Easy menu maintenance | Admin can edit products without code | Yes | V1 |
| Multilingual menu | Supported languages | 3 | V1 |
| Reliable menu availability | Core menu availability | Production-ready | V1 |
| Low infrastructure cost | External paid services | Minimized | V1 |

---

# 9. Product Scope

## V1 — In Scope

### Customer

- Language selection
- Cafe selection
- Restaurant selection
- Category navigation
- Product listing
- Product detail
- Product images
- Product price
- Product description
- Ingredients when available
- Allergens when available
- Sold-out state
- Service availability state
- Loading state
- Empty state
- Error state
- Retry behavior
- Back navigation
- Responsive mobile/desktop layouts

### Admin

- Admin authentication
- Dashboard
- Category management
- Product management
- Product translations
- Product image management
- Price management
- Product availability
- Sold-out status
- Service hours
- Basic menu settings

### Technical

- Laravel application
- PHP
- MySQL / MariaDB
- Blade
- Tailwind CSS
- Alpine.js where appropriate
- Vite for asset compilation
- Server-side rendering
- Real database persistence
- Local file/image storage on the production host

---

# 10. V1 — Explicitly Out of Scope

The following MUST NOT be implemented in V1 unless the specification is formally changed:

- Online ordering
- Shopping cart
- Checkout
- Online payment
- Table selection
- Customer accounts
- Customer registration
- Customer login
- Customer profiles
- Order tracking
- Delivery
- Reservation system
- Loyalty system
- Reviews
- Ratings
- Favorites
- Wishlist
- Customer messaging
- AI customer assistant
- Push notifications
- Native mobile application
- Cryptocurrency/payment wallets
- Firebase
- Required external cloud database
- Required external image storage
- Complex analytics platform

The menu is a viewing system, not an ordering system.

---

# 11. Technology Stack

## Application

`Laravel`

## PHP

`PHP 8.3+`

## Database

`MySQL or MariaDB`

## Frontend

`Blade + Tailwind CSS`

## Client-side Enhancement

`Alpine.js only where useful`

## Build Tool

`Vite`

## Server

`Linux shared/cloud hosting`

## Production Hosting

Iran-based hosting is preferred.

The production architecture MUST NOT depend on Firebase or another foreign cloud service for core application functionality.

## Cache

Initial implementation should use Laravel-supported local/file/database caching.

Redis is NOT required for V1.

## Image Storage

Images should be stored on the application hosting environment.

Use optimized formats such as WebP where appropriate.

---

# 12. Architecture Requirements

The application MUST use a conventional Laravel architecture.

Preferred layers:

```text
Browser
   ↓
Laravel Route
   ↓
Controller
   ↓
Request Validation
   ↓
Service / Business Logic
   ↓
Model
   ↓
MySQL
````

For customer pages:

```text
Browser
   ↓
Laravel
   ↓
Database
   ↓
Blade
   ↓
HTML/CSS/JS
```

For admin:

```text
Admin Browser
   ↓
Authentication
   ↓
Authorization
   ↓
Controller
   ↓
Validation
   ↓
Service
   ↓
Database
```

Do not introduce unnecessary API layers when server-rendered Laravel functionality is sufficient.

---

# 13. Frontend Architecture

The customer menu should use Blade templates and reusable components.

Recommended structure:

```text
resources/views/
    layouts/
    components/
    menu/
        home.blade.php
        category.blade.php
        products.blade.php
        product-detail.blade.php

    admin/
        layouts/
        dashboard/
        categories/
        products/
        service-hours/
        media/
        settings/
```

Reusable components MUST be preferred over duplicated markup.

---

# 14. Backend Architecture

Recommended structure:

```text
app/
    Http/
        Controllers/
            MenuController.php
            CategoryController.php
            ProductController.php

            Admin/
                DashboardController.php
                CategoryController.php
                ProductController.php
                ServiceHourController.php
                MediaController.php
                SettingsController.php

        Requests/
            Admin/

    Models/
        User.php
        Category.php
        CategoryTranslation.php
        Product.php
        ProductTranslation.php
        ProductImage.php
        ServiceHour.php
        Setting.php

    Services/
        MenuService.php
        ProductService.php
        AvailabilityService.php
        ImageService.php

    Policies/
        CategoryPolicy.php
        ProductPolicy.php
```

The exact structure may be adjusted if the existing Laravel implementation provides a better verified pattern.

Do not create unnecessary abstractions.

---

# 15. Database Requirements

The application MUST use a real relational database.

Production functionality MUST NOT depend on:

* Arrays
* Hardcoded production data
* In-memory storage
* Mock data
* Browser local storage for core menu data

## Core Entities

### users

Purpose:

Admin authentication and authorization.

Suggested fields:

```text
id
name
email
password
role
is_active
last_login_at
created_at
updated_at
```

### categories

Purpose:

Menu hierarchy.

Suggested fields:

```text
id
parent_id
type
slug
sort_order
is_active
created_at
updated_at
```

### category_translations

Purpose:

Localized category names.

Suggested fields:

```text
id
category_id
locale
name
description
created_at
updated_at
```

Supported locales:

```text
fa
ar
en
```

### products

Purpose:

Core menu product records.

Suggested fields:

```text
id
category_id
slug
sku
price
sort_order
is_active
is_sold_out
created_at
updated_at
```

### product_translations

Purpose:

Localized product content.

Suggested fields:

```text
id
product_id
locale
name
description
ingredients
allergens
created_at
updated_at
```

### product_images

Purpose:

Product images.

Suggested fields:

```text
id
product_id
path
alt_text
sort_order
is_primary
created_at
updated_at
```

### service_hours

Purpose:

Control service availability.

Suggested fields:

```text
id
category_id
day_of_week
opens_at
closes_at
is_active
created_at
updated_at
```

### settings

Purpose:

General application/menu settings.

Suggested fields:

```text
id
key
value
type
updated_at
```

---

# 16. Database Relationships

Category:

```text
Category
 ├── CategoryTranslations
 ├── Products
 └── ServiceHours
```

Product:

```text
Product
 ├── Category
 ├── ProductTranslations
 └── ProductImages
```

Translations:

```text
Category → CategoryTranslation
Product → ProductTranslation
```

Foreign keys and indexes MUST be defined appropriately.

Database constraints MUST prevent invalid relationships.

---

# 17. Menu Information Architecture

The customer menu hierarchy is fixed for V1.

```text
Entry
│
├── Cafe
│   ├── Hot Bar
│   ├── Cold Bar
│   └── Dessert
│
└── Restaurant
    ├── Breakfast
    ├── Lunch
    └── Dinner
```

Do NOT mix Cafe and Restaurant categories.

Do NOT create additional top-level customer categories without specification approval.

---

# 18. Customer Routes

Preferred routes:

```text
/
```

```text
/menu/cafe
/menu/cafe/hot-bar
/menu/cafe/cold-bar
/menu/cafe/dessert
```

```text
/menu/restaurant
/menu/restaurant/breakfast
/menu/restaurant/lunch
/menu/restaurant/dinner
```

```text
/menu/product/{slug}
```

Routes may be implemented using Laravel route model binding where appropriate.

URLs should remain clean and human-readable.

---

# 19. Customer User Journey

## J-001 — Enter Menu

```text
QR Scan / Direct URL
        ↓
Language Selection
        ↓
Cafe / Restaurant
        ↓
Category
        ↓
Product List
        ↓
Product Detail
```

Success condition:

The customer can reach the desired product and understand its information.

---

# 20. Language Support

Supported languages:

```text
Persian
Arabic
English
```

Locale codes:

```text
fa
ar
en
```

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

The interface MUST change direction correctly.

Do not implement RTL by simply reversing text or applying random CSS overrides.

---

# 21. Design System

The project MUST follow:

```text
DESIGN_SYSTEM.md
```

The PONT CAFE visual identity is:

## Primary Brand Color

```text
#23336E
```

## Supporting Colors

```text
Deep Navy: #18244F
Soft Navy: #E9ECF5
Background: #FCFCFA
White: #FFFFFF
Main Text: #171A22
Secondary Text: #656A78
Border: #E6E7EB
Optional Warm Accent: #C8A978
```

These colors should be implemented as semantic design tokens.

Do not scatter raw color values throughout components.

---

# 22. Typography

Primary Persian/Arabic font:

```text
IranYekan
```

English should use an appropriate modern Latin companion font.

Typography MUST remain moderate and readable.

The application MUST NOT use oversized typography to fill empty space.

Default body text should normally remain around the project's established readable scale.

Typography hierarchy should be created through:

* Size
* Weight
* Line height
* Spacing
* Color
* Position

---

# 23. Customer UI Principles

The customer experience MUST be:

* Simple
* Elegant
* Fast
* Clean
* Uncluttered
* Mobile-first
* Easy to understand

Avoid:

* Excessive decoration
* Huge cards
* Huge buttons
* Huge typography
* Unnecessary badges
* Ratings
* Favorites
* Cart UI
* Ordering UI
* Excessive animation
* Emoji as primary interface icons

---

# 24. Product List

The default product card should contain only:

```text
Image
Name
Price
```

Do NOT automatically add:

* Rating
* Favorite
* Cart button
* Quantity selector
* Order button
* Badges
* Long metadata
* Ingredient lists
* Excessive descriptions

Additional product information belongs on the product detail page.

---

# 25. Product Detail

Product detail may contain:

```text
Back navigation
Large image
Product name
Full description
Ingredients when available
Allergens when available
Price
Availability
```

No ordering controls should be added.

---

# 26. Product Availability

Availability has distinct states.

## Active

The product is available normally.

## Sold Out

The product remains visible but is clearly marked:

```text
تمام شد
```

The visual treatment should be subtle.

Do not use aggressive bright-red presentation.

## Outside Service Hours

When a relevant category/service is unavailable because of service hours, display an appropriate state such as:

```text
فعلاً سرو نمی‌شود
```

Optional service time may be displayed.

Sold-out and outside-service-hours states MUST NOT be confused.

---

# 27. Loading State

The global PONT CAFE loading experience should use the PONT CAFE logo.

Requirements:

* Centered logo
* Subtle animation
* Approximately 0.6–1 second when loading is genuinely required
* No generic spinner as the primary brand loading experience
* No unnecessary loading text
* Background:

```text
#FCFCFA
```

The loading state must not appear unnecessarily between every page interaction.

---

# 28. Empty State

Empty categories or unavailable content must have a clear but minimal empty state.

Do not show broken-looking blank pages.

Do not add unnecessary decorative warning boxes.

---

# 29. Error State

Errors must:

* Be understandable.
* Avoid exposing technical implementation details.
* Explain what happened when useful.
* Provide retry/recovery when appropriate.

Example:

```text
مشکلی در دریافت منو پیش آمد.
دوباره تلاش کنید.
```

The exact wording may be localized.

---

# 30. Responsive Requirements

The product MUST be mobile-first.

Minimum supported widths:

```text
320px
360px
375px
390px
414px
```

Also verify:

```text
768px
1024px
1280px+
```

Mobile MUST NOT simply be a shrunk desktop implementation.

The layout may change between:

```text
Mobile
Tablet
Desktop
```

when required.

---

# 31. Mobile Requirements

The mobile experience is a first-class experience.

Requirements:

* No unintended horizontal page scrolling.
* Comfortable touch targets.
* Readable typography.
* Appropriate spacing.
* Dedicated mobile navigation where needed.
* Safe-area handling where relevant.
* Images must remain within containers.
* Long names must wrap correctly.
* No clipped content.
* No desktop-width components forced into mobile.

Do not use:

```css
overflow-x: hidden;
```

as a workaround for an incorrectly designed layout.

---

# 32. Desktop Requirements

Desktop should provide a clean and balanced reading experience.

Do not stretch content unnecessarily across the entire viewport.

Use intentional:

* Max widths
* Whitespace
* Grid layouts
* Typography hierarchy

The desktop design must remain visually consistent with the mobile experience.

---

# 33. Accessibility

Target baseline:

```text
WCAG 2.2 AA
```

The application should support:

* Keyboard navigation
* Visible focus
* Semantic HTML
* Accessible names
* Sufficient contrast
* Readable typography
* Reduced motion considerations
* Correct RTL/LTR behavior
* Screen-reader compatible structure

Interactive elements should have practical touch targets around:

```text
44–48px
```

where appropriate.

---

# 34. Admin Panel

The admin panel is a real application area.

It MUST NOT be built as a collection of large centered modals.

Major workflows require dedicated pages.

Preferred structure:

```text
AdminShell
├── Sidebar
├── Header
├── Breadcrumbs
├── PageHeader
└── MainContent
```

---

# 35. Admin Routes

Preferred:

```text
/admin
/admin/categories
/admin/categories/create
/admin/categories/{id}/edit

/admin/products
/admin/products/create
/admin/products/{id}/edit

/admin/service-hours
/admin/media
/admin/settings
```

The exact route implementation may use Laravel resource controllers where appropriate.

---

# 36. Admin Product Editor

Product management should be a dedicated page.

The product editor should be organized into clear sections/tabs where appropriate:

```text
Basic Information
Translations
Price
Ingredients / Allergens
Images
Availability
```

Do NOT place the entire product editor inside a small centered modal.

The editor should maintain the established PONT CAFE admin visual language.

---

# 37. Admin Product Requirements

Admin must be able to:

* Create product
* Edit product
* Delete product where allowed
* Activate/deactivate product
* Mark sold out
* Set price
* Edit translations
* Upload product image
* Replace product image
* Set primary image
* Control sort order
* Assign category

Data MUST persist to the real database.

---

# 38. Admin Category Requirements

Admin must be able to:

* Create category
* Edit category
* Activate/deactivate category
* Edit translations
* Set sort order
* Maintain the Cafe/Restaurant hierarchy

The predefined customer hierarchy must not be silently changed.

---

# 39. Admin Authentication

Customer authentication is NOT required.

Admin authentication IS required.

Admin pages must not be publicly accessible.

Unauthorized users must be prevented from accessing administrative functionality.

---

# 40. Admin Roles

V1 should initially use a simple role model.

Primary role:

```text
admin
```

If additional roles become necessary, the change must be explicitly documented.

AI MUST NOT invent additional business roles without approval.

---

# 41. Authorization

Authentication and authorization MUST be enforced server-side.

Do not rely on frontend visibility to protect admin functionality.

Policies/middleware should be used where appropriate.

---

# 42. Validation

All admin input must be validated server-side.

Validation must cover:

* Required fields
* String lengths
* Locale
* Price
* Category relationship
* Image type
* Image size
* Slug uniqueness
* Database relationships
* Status values

Client-side validation may improve UX but MUST NOT replace server-side validation.

---

# 43. Image Requirements

Product images should:

* Be optimized for web delivery.
* Use appropriate dimensions.
* Prefer WebP where practical.
* Have meaningful alt text.
* Avoid unnecessarily large file sizes.
* Preserve the intended visual ratio.
* Not break responsive layouts.

Image upload errors must be handled clearly.

---

# 44. Security

The application MUST follow:

```text
SECURITY_RULES.md
```

At minimum:

* Secure password handling.
* CSRF protection.
* Server-side authorization.
* Input validation.
* Secure file uploads.
* Safe output escaping.
* Secure session handling.
* Protection against unauthorized admin access.
* No secrets in Git.
* No production credentials in source control.

`.env` MUST NOT be committed.

---

# 45. Privacy

The application should collect the minimum personal information necessary.

Customers should not need to provide personal information to view the menu.

No customer account or customer profile is required for V1.

Admin authentication data must be protected.

---

# 46. SEO

Public menu pages may be indexable unless the business explicitly decides otherwise.

The application should provide:

* Meaningful page titles
* Meta descriptions where appropriate
* Canonical URLs where appropriate
* Semantic HTML
* Localized metadata where appropriate

Admin pages MUST NOT be publicly indexable.

---

# 47. Performance

The menu is primarily a read-heavy application.

Performance priorities:

1. Fast initial page load.
2. Optimized images.
3. Minimal JavaScript.
4. Server-side rendering.
5. Browser caching.
6. Laravel caching where appropriate.
7. Database indexes.
8. Avoid unnecessary database queries.
9. Avoid unnecessary external requests.

Do not introduce heavy infrastructure without a demonstrated need.

---

# 48. External Integrations

Core V1 functionality MUST NOT depend on:

* Firebase
* External cloud database
* External CMS
* External image storage
* External authentication provider
* Required third-party SaaS

External integrations may be introduced later only through explicit specification change.

---

# 49. Deployment

Production target:

```text
Iran-based Linux hosting
```

Preferred environment:

```text
Linux
PHP 8.3+
MySQL/MariaDB
Apache or compatible PHP web server
SSL
```

The Laravel public document root MUST point to:

```text
/public
```

Production `.env` must remain outside GitHub.

Production secrets must never be committed.

---

# 50. Development Environments

Preferred development flow:

```text
Local
 ↓
Development Verification
 ↓
Production Deployment
 ↓
Production Smoke Test
```

A separate staging environment is optional for V1 because the project is intentionally small.

The architecture must not depend on staging infrastructure.

---

# 51. Testing Requirements

The project must follow:

```text
TESTING_RULES.md
```

At minimum, test:

### Customer

* Home/entry
* Language switching
* Cafe navigation
* Restaurant navigation
* Category navigation
* Product listing
* Product detail
* Sold-out state
* Service availability
* Empty state
* Error state
* RTL
* LTR
* Mobile layout

### Admin

* Authentication
* Authorization
* Category CRUD
* Product CRUD
* Translation persistence
* Image upload
* Availability
* Service hours
* Validation

### Integration

Verify:

```text
Admin
 ↓
Database
 ↓
Customer Menu
```

When an admin changes a product, the customer menu must use the persisted database value.

---

# 52. Data Integrity

The customer menu must read real production data.

There must be no hidden fallback from database data to fake hardcoded production data.

If database data is unavailable, the application must show an appropriate error state.

---

# 53. Content Rules

Production menu content must come from the database.

Supported languages:

```text
fa
ar
en
```

Translations must not be stored by duplicating entire product records.

Use translation records associated with the main product/category entity.

---

# 54. Initial Category Structure

## Cafe

```text
Cafe
├── Hot Bar
├── Cold Bar
└── Dessert
```

## Restaurant

```text
Restaurant
├── Breakfast
├── Lunch
└── Dinner
```

---

# 55. Initial Product Content

Known breakfast products include:

```text
املت ایرانی
املت سوسیس
املت مخصوص
املت سبزیجات
آمریکایی پینینی
گودمونینگ برگر
نیمرو
سوسیس تخم مرغ
عدسی
خوراک لوبیا با قارچ
```

Additional menu products will be added through the database/admin system.

AI MUST NOT invent final production menu content.

Placeholder content may be used only during development when clearly marked as development content.

---

# 56. Design References

The customer UI has been designed through Google Stitch.

Design references are authoritative for visual intent but must be interpreted together with:

```text
PROJECT_SPEC.md
DESIGN_SYSTEM.md
UX_RULES.md
```

The current design direction includes:

### Entry

```text
Logo
Language switcher
Cafe
Restaurant
```

### Category Selection

Cafe:

```text
Hot Bar
Cold Bar
Dessert
```

Restaurant:

```text
Breakfast
Lunch
Dinner
```

### Product List

```text
Image
Name
Price
```

### Product Detail

```text
Back
Image
Name
Description
Ingredients
Allergens
Price
Availability
```

The implementation should preserve this hierarchy.

---

# 57. Animation

Animations must be subtle and purposeful.

Do not introduce decorative animation that slows the menu.

Respect reduced-motion preferences where applicable.

---

# 58. Component Strategy

Before creating a new component:

1. Check existing components.
2. Reuse if possible.
3. Extend if appropriate.
4. Create a new component only when necessary.

Do not create duplicate visual components.

All repeated UI patterns should use reusable components.

---

# 59. Modal Policy

Modal usage is intentionally limited.

Allowed examples:

* Short confirmation
* Short focused interaction
* Small information dialog

Not allowed for major workflows:

* Product editor
* Category management
* Settings
* Large forms
* Full admin workflows

Major workflows require dedicated pages.

---

# 60. Project Phases

The project follows this controlled development lifecycle:

```text
PHASE 00 — Discovery & Audit
PHASE 01 — Project Specification
PHASE 02 — UX / UI Design
PHASE 03 — Architecture & Technical Planning
PHASE 04 — Feature Implementation
PHASE 05 — Integration & Completion
PHASE 06 — Testing & Security
PHASE 07 — Final Audit & Quality Gate
```

No phase may be silently skipped.

---

# 61. Feature Development Strategy

Features must be implemented individually.

Example:

```text
Feature
 ↓
Design Review
 ↓
Technical Plan
 ↓
Implementation
 ↓
Integration
 ↓
Testing
 ↓
Audit
 ↓
Quality Gate
```

Only after the current Feature passes its gate should the next Feature begin.

---

# 62. Proposed Feature Queue

The initial implementation queue is:

```text
F-001 — Laravel Project Foundation
F-002 — Database Schema
F-003 — Admin Authentication
F-004 — Admin Shell
F-005 — Category Management
F-006 — Product Management
F-007 — Product Images
F-008 — Multilingual Content
F-009 — Service Hours & Availability
F-010 — Customer Entry Screen
F-011 — Customer Category Navigation
F-012 — Customer Product Listing
F-013 — Customer Product Detail
F-014 — Loading / Empty / Error States
F-015 — RTL / LTR Verification
F-016 — Responsive Verification
F-017 — Customer/Admin Integration
F-018 — Security Audit
F-019 — Performance Audit
F-020 — Final Production Audit
```

The queue may be reordered if technical dependencies require it.

The queue MUST NOT be expanded with unrelated features without approval.

---

# 63. Feature Priorities

```text
P0 = Required for core V1 operation
P1 = Important for V1
P2 = Optional / Future
```

Core menu functionality is P0.

Unnecessary platform features are P2 or Out of Scope.

---

# 64. Change Control

AI MUST NOT silently change:

* Architecture
* Database architecture
* Authentication model
* Authorization model
* Product scope
* Customer navigation
* Category hierarchy
* Design System
* Phase structure
* Deployment architecture

If a major change is required:

```text
STOP
 ↓
Explain
 ↓
Identify affected files
 ↓
Explain reason
 ↓
Explain risks
 ↓
Propose alternatives
 ↓
Wait for approval
```

Minor implementation decisions that do not change product behavior may be completed intelligently.

---

# 65. AI Decision Boundary

AI MAY decide automatically when:

* The missing detail is low-risk.
* The choice is consistent with the Design System.
* The choice does not change business behavior.
* The choice does not change architecture.
* The choice does not expand scope.
* The choice is necessary to complete an already-defined Feature.

AI MUST ask for clarification when:

* Business behavior is unclear.
* A decision changes scope.
* A decision changes database architecture.
* A decision changes authentication/authorization.
* A decision introduces a new external service.
* A decision significantly changes UX.
* A decision creates a new major Feature.

---

# 66. No Scope Expansion

AI MUST NOT interpret:

```text
Build the menu
```

as permission to build:

```text
Ordering
Cart
Checkout
Payment
Accounts
Reservations
Delivery
```

Only the documented PONT CAFE V1 scope is authorized.

---

# 67. Production Quality Rule

The project is intended to become a real production application.

Therefore:

* No fake production functionality.
* No permanent mock data.
* No fake database.
* No UI-only implementation where backend persistence is required.
* No unprotected admin pages.
* No silently ignored errors.
* No unverified claims of completion.

---

# 68. Phase Reporting

At the end of every Phase, report:

```text
Phase:
Status:

Completed:
- ...

Not Completed:
- ...

Blockers:
- ...

Files Changed:
- ...

Tests:
- ...

Quality Gate:
PASS / FAIL

Next Phase:
...
```

For every Feature:

```text
Feature:
Design Reference:
Frontend:
Backend:
Database:
Integration:
Tests:
Audit:
Status:
```

Reports must remain concise and factual.

---

# 69. Current Project Status

Current status:

```text
PHASE 00 — Discovery & Audit
```

The Laravel application itself has NOT yet been declared implemented.

The governance repository is the starting project-control layer.

Before implementation begins:

1. Validate this specification.
2. Validate the repository rules.
3. Complete the project audit.
4. Confirm architecture.
5. Define the implementation plan.
6. Begin implementation feature-by-feature.

---

# 70. Project Definition of Done

PONT CAFE V1 is complete only when:

* Specification is complete.
* Architecture is validated.
* Database is implemented.
* Admin authentication works.
* Admin authorization works.
* Categories persist correctly.
* Products persist correctly.
* Translations persist correctly.
* Images work correctly.
* Availability works correctly.
* Customer menu reads real database data.
* Cafe/Restaurant hierarchy works.
* Product listing works.
* Product detail works.
* Persian works correctly.
* Arabic works correctly.
* English works correctly.
* RTL/LTR works correctly.
* Mobile UX is verified.
* Desktop UX is verified.
* Accessibility is reviewed.
* Error states work.
* Empty states work.
* Loading states work.
* Security checks pass.
* Relevant tests pass.
* Production build succeeds.
* Production deployment succeeds.
* Production smoke test succeeds.
* No production mock functionality remains.
* No critical UX blocker remains.
* No critical security blocker remains.
* Final audit passes.

Only then:

```text
PROJECT STATUS = COMPLETE
```

---

# 71. Authority Model

The authority order for this project is:

```text
Global Project Rules
        ↓
PROJECT_SPEC.md
        ↓
Approved Feature Definition
        ↓
Approved Design Reference
        ↓
Existing Verified Implementation
```

Security and platform safety constraints remain non-overridable.

AI MUST identify conflicts rather than silently choosing one rule over another.

---

# 72. Master AI Operating Rule

The AI is responsible for maintaining project consistency across:

```text
Product
Architecture
Frontend
Backend
Database
Security
UX
UI
Accessibility
Testing
Deployment
```

The AI MUST operate as the project's technical manager during development.

Before each Feature:

```text
Read project context
 ↓
Check current Phase
 ↓
Check Feature
 ↓
Inspect existing implementation
 ↓
Identify dependencies
 ↓
Plan
 ↓
Implement only the approved Feature
 ↓
Test
 ↓
Audit
 ↓
Quality Gate
```

The AI MUST always know:

```text
Current Phase
Current Feature
Feature Status
Completed Work
Remaining Work
Blockers
Next Approved Step
```

The AI MUST NOT jump to a later Feature while a required dependency or critical blocker remains unresolved.

The AI MUST NOT report a Feature as complete unless its Definition of Done has been verified.

---

# 73. Final Principle

PONT CAFE should be built as:

```text
Controlled Development
+
Real Laravel Application
+
Real MySQL Database
+
Real Admin Panel
+
Real Customer Menu
+
Multilingual UX
+
Mobile-First Design
+
Secure Architecture
+
Feature-by-Feature Implementation
+
Continuous Testing
+
Continuous Audit
```

The goal is not to generate a large amount of code quickly.

The goal is to build a small, clean, reliable and production-ready digital menu correctly.
