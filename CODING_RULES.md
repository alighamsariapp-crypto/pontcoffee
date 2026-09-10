
# CODING RULES — PONT CAFE

Version: 1.0
Status: Active
Project: PONT CAFE Digital Menu

---

## 1. Purpose

This document defines the coding standards for the PONT CAFE project.

The goal is to keep the codebase:

- Simple
- Maintainable
- Consistent
- Secure
- Testable
- Production-ready
- Appropriate for the actual project scope

These rules apply to all Laravel, PHP, Blade, JavaScript, CSS, database, and configuration code.

---

## 2. Source of Truth

`PROJECT_SPEC.md` is the primary project-specific source of truth.

If this document conflicts with `PROJECT_SPEC.md`, the project specification takes priority.

Do not introduce technologies, features, architecture, or dependencies that are outside the project specification without approval.

---

## 3. Technology Stack

The production stack is:

- Laravel
- PHP 8.3+
- MySQL or MariaDB
- Blade
- Tailwind CSS
- Alpine.js only when useful
- Vite
- Linux hosting

Do not introduce React, Vue, Next.js, Firebase, Node.js runtime requirements, or other major frameworks unless the project specification is explicitly changed.

Node/npm may be used during development/build processes when required by Vite, but Node.js must not be required as the production application runtime.

---

## 4. Production-Ready Code

Production code must be real.

Do not implement production functionality using:

- Fake data
- Mock data
- Static arrays
- Placeholder business logic
- Simulated API responses
- Fake database records
- Temporary hardcoded workflows

If a feature requires persistent data, it must use the real database.

---

## 5. Laravel Conventions

Follow standard Laravel conventions whenever practical.

Use:

- Controllers
- Models
- Form Requests
- Policies
- Services when business logic justifies them
- Eloquent relationships
- Middleware
- Blade components
- Migrations
- Seeders
- Feature tests

Do not create unnecessary architectural layers.

---

## 6. Keep Controllers Thin

Controllers should coordinate requests and responses.

Avoid placing large business logic blocks inside controllers.

Preferred structure:

```text
Route
  ↓
Controller
  ↓
Service / Model
  ↓
Database
````

For simple CRUD operations, a Service is not mandatory if it would only wrap one Eloquent call.

---

## 7. Business Logic

Business rules must have a clear and centralized location.

Examples:

* Product availability
* Service-hour logic
* Category visibility
* Product status
* Menu visibility

Do not duplicate the same business rule across multiple controllers or views.

---

## 8. Services

Create a Service when business logic:

* Is reused
* Contains multiple steps
* Requires coordination between multiple models
* Would make a controller difficult to understand
* Represents an important domain operation

Do not create a Service class for every simple CRUD method.

---

## 9. Models

Eloquent Models should represent database entities and relationships.

Use Models for:

* Relationships
* Query scopes
* Simple model-specific behavior
* Database interaction appropriate to the model

Avoid putting unrelated application logic inside Models.

---

## 10. Eloquent Relationships

Define relationships explicitly.

Example:

```php
public function translations()
{
    return $this->hasMany(ProductTranslation::class);
}
```

Use relationships instead of manually repeating database joins when Eloquent relationships are appropriate.

---

## 11. Avoid N+1 Queries

Always consider query efficiency.

Use eager loading when related data is required:

```php
Product::with([
    'translations',
    'images',
])->get();
```

Do not load relationships repeatedly inside Blade loops.

---

## 12. Database Queries

Database queries must be:

* Secure
* Understandable
* Efficient
* Relevant to the actual requirement

Do not execute unnecessary queries.

Avoid raw SQL unless Eloquent or Query Builder is not appropriate.

---

## 13. Raw SQL

Raw SQL is allowed only when there is a clear technical reason.

When raw SQL is necessary:

* Use parameter binding
* Never concatenate user input
* Keep the query maintainable
* Document unusual queries when appropriate

Never construct SQL using untrusted input.

---

## 14. Validation

All user-controlled input must be validated on the server.

Prefer Laravel Form Requests for non-trivial validation.

Frontend validation may improve UX, but it must never replace server-side validation.

---

## 15. Mass Assignment

Protect Eloquent Models against mass assignment.

Use:

```php
protected $fillable = [
    // allowed fields
];
```

or another appropriate Laravel protection mechanism.

Never blindly accept arbitrary request data.

---

## 16. Authorization

Authentication and authorization must be enforced server-side.

Never trust:

* Hidden form fields
* Client-side permissions
* JavaScript conditions
* URL parameters
* Request payload role values

Admin operations must verify that the authenticated user has permission to perform the action.

---

## 17. Authentication

Customer authentication is not part of PONT CAFE V1.

Admin authentication is required for the management area.

Do not add customer accounts or login flows unless the project specification changes.

---

## 18. Blade Rules

Blade templates should primarily handle presentation.

Avoid placing complex business logic inside Blade.

Do not perform database queries directly inside Blade templates.

Bad:

```blade
@php
    $products = DB::table('products')->get();
@endphp
```

Preferred:

```text
Controller
  ↓
Service / Model
  ↓
Blade
```

---

## 19. Blade Components

Use reusable Blade components for repeated UI patterns.

Examples:

* Product card
* Language switcher
* Price display
* Availability state
* Navigation
* Admin form fields
* Buttons
* Alerts

Do not create duplicate implementations of the same UI pattern.

---

## 20. UI Consistency

Follow `DESIGN_SYSTEM.md` and `UX_RULES.md`.

Do not introduce arbitrary:

* Colors
* Font sizes
* Spacing values
* Border radii
* Shadows
* Button styles
* Component styles

when an existing project token or component already exists.

---

## 21. Responsive Design

The customer menu must be mobile-first.

Supported baseline widths include:

```text
320
360
375
390
414
768
1024
1280+
```

Mobile is not simply a smaller desktop layout.

Layouts should adapt intentionally to mobile.

Avoid:

* Horizontal page scrolling
* Tiny text
* Tiny touch targets
* Desktop tables squeezed into mobile
* Oversized UI elements

---

## 22. RTL and LTR

The project supports:

```text
fa
ar
en
```

Persian and Arabic must use RTL.

English must use LTR.

Do not hardcode directional assumptions into reusable components.

Use logical CSS properties where possible.

Prefer:

```css
margin-inline
padding-inline
inset-inline
border-inline
```

instead of unnecessary left/right-specific rules.

---

## 23. Typography

Use the project typography defined in `PROJECT_SPEC.md` and `DESIGN_SYSTEM.md`.

Persian and Arabic:

```text
IranYekan
```

Do not introduce random fonts.

Do not use unnecessarily large typography.

Typography must remain consistent across customer and admin interfaces.

---

## 24. Accessibility

Interactive elements must be accessible.

Use:

* Semantic HTML
* Proper labels
* Keyboard accessibility
* Visible focus states
* Appropriate contrast
* Meaningful alt text
* Accessible buttons
* Accessible form controls

Do not rely only on color to communicate state.

---

## 25. Images

Product images must be optimized.

Preferred format:

```text
WebP
```

Images should have:

* Appropriate dimensions
* Useful alt text
* Lazy loading when appropriate
* No unnecessary full-resolution assets

Do not load huge source images when a smaller version is sufficient.

---

## 26. Loading States

Loading states must follow the project's UX rules.

The customer menu should feel fast and app-like.

Do not add loading indicators when there is no meaningful asynchronous operation.

The global PONT CAFE loading animation may be used only when the application is genuinely loading.

Do not add unnecessary spinners.

---

## 27. Empty States

Every relevant data-driven view should have an intentional empty state.

Examples:

* Empty category
* No available products
* No media
* No search results

Do not leave blank screens without context.

---

## 28. Error States

Errors must be handled intentionally.

User-facing errors should:

* Be understandable
* Avoid technical details
* Provide a useful recovery action when appropriate

Never expose:

* Stack traces
* SQL queries
* File system paths
* Environment variables
* Credentials
* Secrets

in production responses.

---

## 29. Naming

Use clear and descriptive names.

PHP:

```text
PascalCase
```

for classes.

Methods and variables:

```text
camelCase
```

Database:

```text
snake_case
```

Blade files:

```text
kebab-case
```

or the established Laravel project convention.

Follow existing naming patterns consistently.

---

## 30. Comments

Comments should explain why something exists, not simply repeat what the code does.

Bad:

```php
// Get products
$products = Product::all();
```

Good:

```php
// Only active products are shown on the public menu.
$products = Product::where('is_active', true)->get();
```

Do not over-comment obvious code.

---

## 31. Type Safety

Use PHP type declarations whenever practical.

Example:

```php
public function show(Product $product): View
{
    // ...
}
```

Use appropriate return types and parameter types.

Avoid unnecessary mixed or untyped values.

---

## 32. Configuration

Environment-specific values must come from configuration or `.env`.

Never hardcode:

* Database credentials
* API keys
* Secrets
* Production hostnames
* Passwords

`.env` must not be committed to Git.

---

## 33. Security

Follow:

* `SECURITY_RULES.md`
* Laravel security practices
* Server-side validation
* Authorization
* CSRF protection
* Secure file uploads
* Safe database queries

Security must not depend on frontend behavior.

---

## 34. Dependencies

Do not add dependencies without a clear reason.

Before adding a package, consider:

1. Is it actually necessary?
2. Can Laravel already solve the problem?
3. Can a small local implementation solve it?
4. Does it increase maintenance cost?
5. Is it compatible with the hosting environment?
6. Does it affect performance or security?

Avoid unnecessary packages.

---

## 35. JavaScript

JavaScript should be used only when it improves the user experience or enables behavior that cannot reasonably be handled with standard server-rendered HTML.

Prefer:

* Blade
* HTML
* CSS
* Alpine.js

for simple interactions.

Do not build a JavaScript SPA for this project.

---

## 36. Alpine.js

Use Alpine.js only where useful.

Appropriate examples:

* Mobile navigation
* Small interactive controls
* Tabs
* Dropdowns
* Lightweight UI state
* Simple asynchronous interactions

Do not recreate the entire application architecture inside Alpine.js.

---

## 37. Tailwind CSS

Use the project's design tokens and established utility patterns.

Do not create arbitrary one-off visual styles when an existing component or token can be reused.

Avoid excessive class duplication.

Create reusable components when a pattern appears repeatedly.

---

## 38. Routes

Routes should remain clear and intentional.

Avoid unnecessary route duplication.

Use route model binding when appropriate.

Protect Admin routes with the correct authentication and authorization middleware.

---

## 39. Forms

Forms must have:

* Server-side validation
* CSRF protection
* Clear labels
* Error states
* Appropriate input types
* Accessible controls
* Clear success feedback

Do not silently fail submissions.

---

## 40. CRUD

CRUD features must use the real database.

A CRUD feature is not complete if it only changes:

* Frontend state
* JavaScript arrays
* Local storage
* Temporary memory

Production CRUD must persist data correctly.

---

## 41. File Uploads

File uploads must validate:

* File type
* MIME type
* File size
* File extension where appropriate

Use secure generated filenames.

Do not trust the original filename.

---

## 42. Database Migrations

All database schema changes must be represented by migrations.

Do not manually modify production schema without a corresponding migration.

Migrations must be:

* Reproducible
* Ordered
* Safe
* Consistent with Models

---

## 43. Seeders

Seeders may be used for:

* Initial required system data
* Development data
* Controlled default configuration

Do not use fake/demo data as a substitute for the actual production database.

---

## 44. Testing

Important application behavior must have automated tests.

Prioritize:

* Authentication
* Authorization
* Product CRUD
* Category CRUD
* Localization
* Availability
* Service hours
* Public menu visibility
* Validation
* Security-sensitive behavior

Follow `TESTING_RULES.md`.

---

## 45. Refactoring

Refactor when it improves:

* Correctness
* Maintainability
* Reuse
* Performance
* Security

Do not perform large unrelated refactors during a feature implementation.

Keep changes focused on the current phase and feature.

---

## 46. No Duplicate Implementations

Before creating a new:

* Component
* Service
* Helper
* Model method
* UI pattern
* Validation rule

check whether an existing implementation can be reused.

The project should have one clear implementation for each shared responsibility.

---

## 47. No Overengineering

Do not introduce architecture that the project does not need.

Avoid unnecessary:

* Repositories
* Interfaces
* Abstract factories
* Event systems
* Microservices
* APIs
* Queues
* Redis
* Complex state management

unless a real requirement justifies them.

---

## 48. Performance

Performance must be considered during implementation.

Prefer:

* Server-side rendering
* Efficient database queries
* Eager loading
* Image optimization
* Browser caching
* Laravel caching where appropriate
* OPcache in production
* Minimal JavaScript

Do not optimize prematurely without evidence.

---

## 49. Scope Protection

PONT CAFE V1 is a digital menu.

Do not implement:

* Online ordering
* Cart
* Checkout
* Payment
* Delivery
* Reservations
* Customer accounts
* Ratings
* Favorites
* AI assistant
* Push notifications
* Crypto wallet
* Complex analytics

unless the project specification is explicitly changed.

---

## 50. Feature Workflow

Before implementing a feature:

1. Identify the current phase.
2. Read the relevant project rules.
3. Inspect the existing implementation.
4. Reuse existing components and logic.
5. Define the smallest correct implementation.
6. Implement backend/database requirements.
7. Implement frontend/UI requirements.
8. Add validation and authorization where required.
9. Add loading, empty, and error states where relevant.
10. Test the feature.
11. Check responsive behavior.
12. Check RTL/LTR behavior.
13. Perform a focused security and UX review.

---

## 51. Do Not Build Everything at Once

Implementation must be phase-based and feature-based.

Do not give instructions such as:

```text
Build the entire application.
```

Instead implement one defined feature or phase at a time.

Each phase must be integrated and verified before moving to the next phase.

---

## 52. Existing Architecture First

Before creating new files or changing architecture:

* Inspect the current codebase.
* Identify existing patterns.
* Reuse existing components.
* Reuse existing services.
* Reuse existing database structures where appropriate.

Do not replace working architecture without a documented reason.

---

## 53. Change Safety

Do not modify:

* Core architecture
* Database structure
* Authentication
* Design system
* Project rules
* Project specification

as an incidental side effect of implementing an unrelated feature.

If such a change is necessary, identify it explicitly before implementation.

---

## 54. Production Verification

Before considering a feature complete, verify:

* Database persistence
* Server-side validation
* Authorization
* Error handling
* Responsive behavior
* RTL/LTR
* Accessibility
* Performance
* Security
* Real data flow
* No fake/mock implementation
* No console errors
* No unnecessary dependencies

---

## 55. Final Rule

The coding principle for PONT CAFE is:

> Build the simplest correct production implementation that satisfies the project specification.

Do not overengineer.

Do not create fake functionality.

Do not add unnecessary technologies.

Do not duplicate existing logic.

Do not sacrifice security, accessibility, UX, or data integrity for speed.

Every implementation should be real, maintainable, consistent with the project architecture, and appropriate for the actual scope of PONT CAFE.

```

```
