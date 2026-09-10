
# PERFORMANCE RULES — PONT CAFE

Version: 1.0
Status: Active
Project: PONT CAFE Digital Menu

---

## 1. Purpose

This document defines performance requirements for the PONT CAFE application.

The primary performance goals are:

- Fast initial page load
- Fast navigation
- Low bandwidth usage
- Excellent mobile performance
- Efficient database access
- Optimized images
- Minimal JavaScript
- Low hosting resource usage
- Reliable performance on shared Linux hosting

---

## 2. Source of Truth

`PROJECT_SPEC.md` is the primary source of truth.

Performance decisions must remain consistent with:

- `PROJECT_SPEC.md`
- `DESIGN_SYSTEM.md`
- `UX_RULES.md`
- `DATABASE_RULES.md`
- `DEPLOYMENT_RULES.md`

Do not introduce infrastructure or technologies that are unnecessary for the project.

---

## 3. Performance Priority

Performance priorities for PONT CAFE are:

1. Fast first page load
2. Fast menu navigation
3. Fast product list rendering
4. Fast product detail loading
5. Optimized images
6. Efficient database queries
7. Minimal client-side JavaScript
8. Low server resource usage

---

## 4. Server-Side Rendering

The customer menu should primarily use Laravel + Blade server-side rendering.

Preferred architecture:

```text
Browser
   ↓
Web Server
   ↓
Laravel
   ↓
Database
   ↓
Blade
   ↓
HTML Response
````

Do not build a JavaScript SPA for the menu.

---

## 5. Minimize JavaScript

JavaScript should only be used when it provides meaningful functionality.

Prefer:

* HTML
* CSS
* Blade
* Alpine.js

for simple interactions.

Do not add JavaScript libraries for functionality that can be handled by standard HTML/CSS or Laravel.

---

## 6. No Unnecessary API Requests

Do not create API requests for information that can be rendered directly by Blade.

Avoid patterns such as:

```text
Page loads
    ↓
JavaScript request
    ↓
API
    ↓
Database
    ↓
Render menu
```

when the same data can be rendered directly by Laravel.

Preferred:

```text
Request
    ↓
Laravel
    ↓
Database
    ↓
Blade
    ↓
HTML
```

---

## 7. Database Query Efficiency

Every database query should have a clear purpose.

Avoid:

* Repeated identical queries
* Queries inside Blade loops
* Loading unnecessary columns
* Loading unnecessary relationships
* Unbounded large queries

---

## 8. Prevent N+1 Queries

Avoid N+1 query problems.

When related data is required, use eager loading.

Example:

```php
Product::with([
    'translations',
    'images',
])->get();
```

Do not repeatedly query relationships inside a loop.

---

## 9. Select Only Required Data

When appropriate, retrieve only the columns needed by the current operation.

Example:

```php
Product::select([
    'id',
    'category_id',
    'slug',
    'price',
    'is_active',
    'is_sold_out',
])->get();
```

Do not optimize every query prematurely.

Use selective columns when it provides a real benefit.

---

## 10. Pagination

Use pagination for potentially large administrative lists.

Examples:

* Admin products
* Admin categories when necessary
* Media management
* Large datasets

The public menu contains a small, controlled number of products and does not require pagination unless actual content size makes it necessary.

---

## 11. Public Menu Size

PONT CAFE V1 is expected to contain approximately 100 products.

The architecture should handle this size efficiently without introducing unnecessary infrastructure.

Do not build complex data-loading systems for a small menu.

---

## 12. Image Performance

Images are one of the most important performance considerations for the menu.

Product images must be optimized before or during upload.

Preferred format:

```text
WebP
```

Images should use appropriate dimensions and compression.

Do not serve unnecessarily large original images to mobile devices.

---

## 13. Image Dimensions

Images should be sized according to their actual display area.

Do not upload a very large image when a smaller image is sufficient.

Example:

If a product card displays an image at approximately 400px wide, do not serve a multi-megapixel image unnecessarily.

---

## 14. Responsive Images

Where appropriate, use responsive image techniques such as:

```html
srcset
sizes
```

to serve suitable image sizes.

Do not implement complex image processing if the actual hosting environment or project size does not require it.

---

## 15. Lazy Loading Images

Images below the initial viewport should generally use lazy loading.

Example:

```html
<img
    src="..."
    loading="lazy"
    alt="..."
>
```

The primary above-the-fold image should not be unnecessarily lazy-loaded.

---

## 16. Image Alt Text

Images must have meaningful alt text where appropriate.

Decorative images may use an empty alt attribute.

Do not use meaningless alt text such as:

```text
image
photo
product image
```

when the actual product name is available.

---

## 17. Image Upload Processing

Admin image uploads should be validated and optimized.

Where practical:

* Validate MIME type
* Validate file size
* Resize oversized images
* Convert to WebP
* Generate secure filenames
* Remove unnecessary metadata when appropriate

---

## 18. CSS Performance

Keep CSS focused and reusable.

Avoid:

* Large duplicated CSS files
* Unused frameworks
* Repeated custom styles
* Excessive one-off rules

Tailwind CSS should be built for production so unused styles are removed where supported by the build process.

---

## 19. JavaScript Bundle Size

Keep the production JavaScript bundle small.

Do not add large libraries for small interactions.

Examples of interactions that should normally remain lightweight:

* Mobile navigation
* Simple tabs
* Small dropdowns
* Language switching UI
* Simple state changes

---

## 20. Vite Production Build

Production assets must be built using the production Vite build.

Typical command:

```bash
npm run build
```

Do not deploy development assets as the production bundle.

---

## 21. Browser Caching

Static assets should be cacheable where appropriate.

Examples:

* CSS
* JavaScript
* Fonts
* Product images

Use cache-friendly asset filenames generated by the build system when appropriate.

---

## 22. Laravel Cache

Use Laravel caching when it provides a real performance benefit.

Good candidates may include:

* Categories
* Public menu configuration
* Service hours
* Stable public menu data

Cache must be invalidated when the underlying data changes.

---

## 23. Cache Strategy

Do not cache everything.

Caching should not create:

* Stale menu data
* Incorrect availability
* Incorrect prices
* Incorrect product status

Dynamic information must remain accurate.

---

## 24. Availability Accuracy

Performance optimization must never make availability incorrect.

The following states must remain accurate:

```text
Available
Sold Out
Outside Service Hours
```

Do not serve stale availability data merely to improve performance.

---

## 25. Price Accuracy

Prices must always come from the authoritative database state.

Do not rely on long-lived cached prices that may become outdated after an Admin update.

---

## 26. Database Indexes

Important query fields should have appropriate indexes.

Likely candidates include:

```text
categories.slug
categories.parent_id
categories.is_active

products.category_id
products.slug
products.is_active
products.sort_order

product_translations.product_id
product_translations.locale

category_translations.category_id
category_translations.locale
```

Indexes must be based on actual query patterns and schema requirements.

Do not create excessive indexes.

---

## 27. Slug Queries

Public product and category routes should use indexed slug fields.

Example:

```text
/menu/product/{slug}
```

Slug lookups should be efficient.

---

## 28. Eloquent Optimization

Use appropriate Eloquent features:

* Eager loading
* Scopes
* Selective columns
* Pagination
* Query constraints

Do not bypass Eloquent with raw SQL unless there is a clear technical reason.

---

## 29. Avoid Queries in Views

Blade views must not execute database queries.

Bad:

```blade
@foreach(DB::table('products')->get() as $product)
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

## 30. Avoid Repeated Computation

Do not repeatedly perform expensive calculations during rendering.

If a value can be calculated once before rendering, prefer doing so.

This is especially important for:

* Availability
* Translation selection
* Image selection
* Category hierarchy

---

## 31. Translation Performance

Localization must not cause unnecessary database queries.

For a product list, load the required translations efficiently.

Avoid querying translations separately for every product.

---

## 32. Language Handling

The active locale should be determined once per request.

Do not repeatedly calculate locale selection inside loops.

Supported locales:

```text
fa
ar
en
```

---

## 33. Font Performance

Fonts should be loaded efficiently.

The project uses:

```text
IranYekan
```

for Persian and Arabic.

Avoid loading unnecessary font weights.

Only required weights should be included.

---

## 34. Font Loading

Fonts should not unnecessarily block page rendering.

Use appropriate font loading strategies supported by the application.

Do not load multiple large font families when they are not required.

---

## 35. Above-the-Fold Content

The first viewport should load quickly.

Prioritize:

* Logo
* Primary navigation
* Main category choices
* First visible menu content

Do not load large amounts of below-the-fold content before the initial view can render.

---

## 36. Navigation Performance

Navigation between menu sections should feel immediate.

Prefer normal Laravel page navigation for the V1 architecture.

Do not add SPA navigation libraries only to make page changes appear faster.

Use proper caching and optimized server rendering first.

---

## 37. Loading Animation

The PONT CAFE loading animation should only appear when the application is genuinely waiting for an operation.

Do not show a loading animation unnecessarily between normal server-rendered pages.

The loading animation must remain subtle and short.

---

## 38. Perceived Performance

Performance is not only about server response time.

The interface should feel fast through:

* Immediate visual feedback
* Stable layouts
* Correct image dimensions
* No unnecessary spinners
* No layout jumps
* Lightweight interactions

---

## 39. Avoid Layout Shift

Reserve appropriate space for images and major UI elements.

Images should have predictable dimensions.

Avoid content unexpectedly moving after page load.

---

## 40. Mobile Performance

Mobile performance is a primary requirement.

The application should work well on:

```text
320px
360px
375px
390px
414px
```

and common tablet/desktop widths.

Do not assume high-speed desktop internet.

---

## 41. Low Bandwidth

The menu should remain usable on slower mobile connections.

Prioritize:

* Small image sizes
* Minimal JavaScript
* Optimized CSS
* Browser caching
* Server-side rendering
* No unnecessary third-party requests

---

## 42. Third-Party Resources

Minimize external dependencies.

Avoid unnecessary:

* External fonts
* Analytics scripts
* Tracking scripts
* JavaScript CDNs
* External UI libraries
* External image services

Core menu functionality must not depend on third-party resources.

---

## 43. External Service Failure

The customer menu should remain functional if an optional external service becomes unavailable.

Core functionality must depend only on:

```text
Laravel
PHP
MySQL/MariaDB
Local application assets
Local product images
```

---

## 44. Hosting Resource Usage

The application must be efficient enough for standard Linux shared/cloud hosting.

Avoid unnecessary:

* Long-running processes
* Workers
* Queues
* Redis
* Elasticsearch
* Multiple application servers

unless actual requirements justify them.

---

## 45. Memory Usage

Avoid loading unnecessary large datasets into memory.

For administrative operations involving potentially large datasets, use:

* Pagination
* Chunking
* Lazy collections

where appropriate.

---

## 46. Admin Performance

The Admin panel should remain responsive without compromising the existing design.

Admin lists should use:

* Pagination when necessary
* Efficient queries
* Eager loading
* Search/filter only when useful
* Optimized images

Do not load the entire database into the Admin UI.

---

## 47. Product List Performance

The public product list should load only the information needed to display:

* Product image
* Product name
* Product price
* Availability state

Do not load unnecessary product metadata.

---

## 48. Product Detail Performance

The product detail page should load:

* Main product image
* Product name
* Description
* Ingredients when available
* Allergens when available
* Price
* Availability

Do not load unrelated products or administrative information.

---

## 49. Error and Performance Balance

Error handling must not create excessive overhead.

Do not perform multiple fallback queries for every request.

Use clear failure paths and appropriate defaults.

---

## 50. Performance Testing

Before production release, test:

* Homepage
* Category pages
* Product lists
* Product detail
* Language switching
* Admin product list
* Admin product editor
* Image upload
* Mobile layouts

Check both network behavior and server-side behavior.

---

## 51. Query Monitoring

During development and performance audits, inspect database query counts for important pages.

Pay particular attention to:

* Product lists
* Category pages
* Translation loading
* Image loading
* Admin lists

Fix unnecessary queries before production.

---

## 52. Production Optimization

Production should use appropriate Laravel optimizations.

Typical commands include:

```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

Only use caching commands that are compatible with the application's configuration and deployment process.

---

## 53. OPcache

PHP OPcache should be enabled when supported by the hosting environment.

This can improve PHP execution performance without requiring additional application infrastructure.

---

## 54. No Premature Optimization

Do not complicate the codebase for theoretical performance problems.

First prefer:

* Correct database queries
* Proper indexes
* Efficient rendering
* Image optimization
* Minimal JavaScript
* Appropriate caching

Introduce more advanced optimization only when actual performance requirements justify it.

---

## 55. Performance Regression

A feature must not introduce a significant performance regression without a clear reason.

Before adding a large dependency or complex client-side behavior, consider its impact on:

* Bundle size
* Network requests
* Server memory
* Database queries
* Mobile performance

---

## 56. Performance and UX

Performance optimization must not break the approved UX.

Do not remove:

* Required states
* Accessibility
* Useful navigation
* Product information
* Availability indicators

simply to reduce implementation complexity.

---

## 57. Scope Protection

PONT CAFE V1 is a small digital menu.

Do not introduce complex performance infrastructure designed for large-scale applications.

The expected scale does not justify:

* Microservices
* Kubernetes
* CDN architecture
* Redis clusters
* Elasticsearch
* Dedicated queue infrastructure

unless future requirements clearly justify them.

---

## 58. Performance Checklist

Before production:

```text
[ ] Server-side rendering used for primary menu pages
[ ] No unnecessary API requests
[ ] No unnecessary JavaScript
[ ] No N+1 queries
[ ] Required database indexes exist
[ ] Images optimized
[ ] WebP used where appropriate
[ ] Images use appropriate dimensions
[ ] Lazy loading used for below-the-fold images
[ ] Fonts optimized
[ ] Production assets built
[ ] Browser caching configured
[ ] Laravel caching configured where useful
[ ] Availability remains accurate
[ ] Prices remain accurate
[ ] No unnecessary third-party dependencies
[ ] Mobile performance checked
[ ] No significant layout shift
[ ] Production optimization enabled
[ ] No unnecessary infrastructure introduced
```

---

## 59. Final Rule

The performance principle for PONT CAFE is:

> Make the simplest architecture fast before introducing complex optimization infrastructure.

Prioritize:

```text
Server-rendered Laravel
        +
Efficient MySQL queries
        +
Optimized images
        +
Minimal JavaScript
        +
Browser caching
        +
Appropriate Laravel caching
```

The menu should feel fast, lightweight, and reliable on mobile devices and modest hosting resources.

Do not sacrifice correctness, security, accessibility, or UX merely for performance.

```


بعدی: **`UX_RULES.md`** — این یکی مهم‌تره چون قوانین UX اختصاصی PONT CAFE را داخلش تثبیت می‌کنیم.
```
