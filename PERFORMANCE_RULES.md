# Performance Rules

## 1. Purpose

This document defines mandatory performance rules for the project.

Performance MUST be considered during:

```text id="p001"
Product Specification
↓
Architecture
↓
Design
↓
Feature Planning
↓
Implementation
↓
Integration
↓
Testing
↓
Audit
↓
Production
```

Performance MUST NOT be treated only as a final optimization step.

---

# 2. Source of Truth

Performance decisions MUST follow:

1. `PROJECT_SPEC.md`
2. `PERFORMANCE_RULES.md`
3. `ARCHITECTURE.md`
4. `UX_RULES.md`
5. `DESIGN_SYSTEM.md`
6. Feature requirements
7. Existing verified implementation

Performance optimization MUST NOT violate security, accessibility, UX, or data integrity requirements.

---

# 3. Performance Principles

The application MUST aim for:

* fast initial loading
* responsive interaction
* stable layout
* efficient network usage
* efficient rendering
* efficient database access
* predictable resource usage
* graceful behavior on slow devices and networks

Do not optimize for benchmark numbers while degrading real user experience.

---

# 4. Performance Budget

Projects SHOULD define measurable budgets where appropriate.

Examples:

| Area               | Budget     |
| ------------------ | ---------- |
| Initial JavaScript | `[TARGET]` |
| Critical CSS       | `[TARGET]` |
| Image payload      | `[TARGET]` |
| API response       | `[TARGET]` |
| Initial page load  | `[TARGET]` |
| Database reads     | `[TARGET]` |

If a project has no explicit budget, AI MUST avoid unnecessary resource growth and SHOULD establish budgets for critical areas.

---

# 5. Core Web Vitals

For public web experiences, AI SHOULD monitor relevant Core Web Vitals:

* Largest Contentful Paint (LCP)
* Interaction to Next Paint (INP)
* Cumulative Layout Shift (CLS)

Where applicable, measurements SHOULD be evaluated using real-user data in addition to synthetic testing.

Passing one synthetic Lighthouse run MUST NOT be treated as proof of production performance.

---

# 6. Rendering Performance

AI MUST avoid unnecessary rendering work.

For React applications:

* keep components appropriately scoped
* avoid unnecessary state updates
* avoid unnecessary parent re-renders
* keep derived state derived
* avoid premature memoization
* use memoization only when it provides measurable or clearly justified value
* avoid expensive calculations during render
* avoid unstable patterns that cause repeated work

React performance techniques MUST NOT make code unnecessarily complex.

---

# 7. Component Performance

Components MUST:

* render only required content
* avoid unnecessary effects
* avoid expensive work on every render
* avoid duplicated data fetching
* clean up subscriptions and listeners
* avoid unnecessary DOM complexity

Large components SHOULD be decomposed when decomposition improves maintainability or rendering behavior.

---

# 8. JavaScript

AI MUST minimize unnecessary JavaScript.

Avoid:

* large unnecessary dependencies
* duplicate libraries
* client-side processing that can be performed more efficiently elsewhere
* loading entire libraries for small utilities
* unnecessary polyfills
* unnecessary global scripts

Dependencies MUST have a clear purpose.

---

# 9. Code Splitting

Large applications SHOULD use appropriate code splitting.

Potential candidates include:

* routes
* large feature modules
* admin areas
* heavy editors
* charts
* maps
* AI interfaces
* rarely used workflows

Code splitting MUST NOT cause poor navigation or excessive loading waterfalls.

---

# 10. Lazy Loading

Non-critical resources SHOULD be loaded only when needed.

Potential candidates:

* below-the-fold images
* heavy components
* large charts
* maps
* secondary dialogs
* optional integrations

Critical content MUST NOT be unnecessarily lazy-loaded.

---

# 11. Images

Images MUST be optimized.

Where applicable:

* use appropriate formats
* provide appropriate dimensions
* avoid unnecessarily large source images
* use responsive image delivery
* define dimensions to reduce layout shift
* lazy-load non-critical images
* prioritize critical visual content

Do not use oversized images when smaller assets provide equivalent visual quality.

---

# 12. Fonts

Font loading MUST be intentional.

AI SHOULD:

* minimize font variants
* load only required weights
* avoid unnecessary font families
* prevent avoidable rendering delays
* use appropriate fallback behavior

Typography MUST remain consistent with `DESIGN_SYSTEM.md`.

---

# 13. Network Requests

AI MUST minimize unnecessary network requests.

Avoid:

* duplicate requests
* sequential requests that could safely run in parallel
* unnecessary polling
* fetching data that is not required
* repeated requests caused by incorrect effect dependencies

Requests SHOULD be:

* cancellable where appropriate
* cacheable where appropriate
* retried only when justified
* bounded in size

---

# 14. Data Fetching

Data fetching MUST be driven by actual Feature requirements.

AI MUST NOT fetch:

* entire collections when a subset is required
* unnecessary fields
* unnecessary related entities
* unbounded result sets

Pagination, filtering, and selective field retrieval SHOULD be used where appropriate.

---

# 15. API Performance

API endpoints SHOULD:

* return only required data
* use pagination for large collections
* avoid unnecessary database queries
* avoid N+1 query patterns
* use appropriate caching
* enforce reasonable request and response limits
* avoid expensive operations on every request

API performance MUST NOT bypass authorization or validation.

---

# 16. Database Performance

Database operations MUST follow `DATABASE_RULES.md`.

AI MUST consider:

* query patterns
* indexes
* document size
* read amplification
* write amplification
* transaction scope
* hot documents
* high-frequency updates
* pagination
* realtime listeners

For Firestore, avoid unnecessary broad collection reads and uncontrolled realtime listeners.

Performance optimization MUST NOT weaken database security.

---

# 17. Firestore Read/Write Efficiency

When Firestore is used, AI MUST evaluate:

* number of document reads
* number of writes
* listener frequency
* query selectivity
* pagination
* index requirements
* transaction retries
* duplicated data

Frequently rendered UI MUST NOT independently create duplicate realtime listeners for the same data without justification.

---

# 18. Caching

Caching SHOULD be used where it provides clear value.

Potential layers:

```text id="p002"
Browser
↓
Application
↓
API
↓
Database / External Service
```

Cached data MUST have an explicit invalidation or freshness strategy.

Sensitive or user-specific data MUST NOT be incorrectly shared through caches.

---

# 19. Search & Filtering

Search and filtering MUST avoid unnecessary full-data downloads.

Prefer:

* server-side filtering for large datasets
* indexed queries
* pagination
* bounded results
* debounced user input where appropriate

Do not debounce actions that should respond immediately unless justified.

---

# 20. Lists & Large Data

Large lists MUST NOT render unlimited items simultaneously.

Where appropriate, use:

* pagination
* cursor pagination
* virtualization
* progressive loading
* server-side filtering

Virtualization SHOULD only be introduced when the data size justifies its complexity.

---

# 21. Mobile Performance

Mobile performance is a first-class requirement.

Test relevant Features on:

* constrained CPU
* constrained memory
* slow network
* small viewport
* touch interaction

Mobile MUST NOT simply receive a reduced desktop experience.

Performance optimizations MUST preserve the mobile UX defined in `UX_RULES.md`.

---

# 22. Loading States

Every asynchronous Feature MUST define appropriate:

* loading state
* success state
* empty state
* error state

Loading UI MUST avoid unnecessary layout shifts.

Skeletons MAY be used where they improve perceived continuity.

Do not use artificial delays to simulate loading.

---

# 23. Layout Stability

AI MUST minimize unexpected layout movement.

Consider:

* image dimensions
* font loading
* dynamic content
* banners
* advertisements where applicable
* async components
* error messages
* loading states

Important content MUST NOT unexpectedly jump during loading.

---

# 24. Background Work

Expensive work SHOULD NOT block critical user interactions.

Where appropriate:

* move expensive processing server-side
* use background jobs
* defer non-critical work
* use Web Workers only when justified

Do not introduce background infrastructure solely for theoretical optimization.

---

# 25. Third-Party Services

Third-party resources MUST be evaluated for:

* network cost
* JavaScript size
* loading behavior
* privacy implications
* reliability
* failure impact

Third-party scripts SHOULD NOT block critical rendering unless required.

A third-party service failure MUST NOT unnecessarily break unrelated application functionality.

---

# 26. Performance & Accessibility

Performance optimization MUST NOT:

* remove keyboard support
* reduce readable text
* remove accessible labels
* disable focus states
* remove semantic structure
* create inaccessible loading states
* sacrifice WCAG requirements

Accessibility remains governed by `UX_RULES.md` and `TESTING_RULES.md`.

---

# 27. Performance & SEO

For public pages, performance MUST be evaluated together with:

* rendering strategy
* crawlability
* content availability
* image optimization
* layout stability

SEO requirements remain governed by `SEO_RULES.md`.

---

# 28. Memory & Resource Management

AI MUST prevent avoidable resource leaks.

Review:

* event listeners
* subscriptions
* timers
* observers
* realtime listeners
* WebSockets
* media resources
* large in-memory datasets

Resources MUST be released when no longer required.

---

# 29. Performance Monitoring

Production systems SHOULD monitor relevant signals such as:

* response latency
* error rate
* request volume
* database usage
* resource usage
* client performance
* Core Web Vitals where applicable

Observability requirements remain governed by `OBSERVABILITY_RULES.md`.

---

# 30. Performance Testing

Relevant Features SHOULD be tested for:

* initial load
* route transitions
* API latency
* database access
* large datasets
* slow network
* slow devices
* repeated interactions
* memory leaks
* rendering performance

Performance testing MUST use realistic data volumes where practical.

A Feature MUST NOT be declared performant solely because it works with a tiny development dataset.

---

# 31. Regression Protection

Performance changes SHOULD be compared against a known baseline when practical.

AI MUST investigate meaningful regressions.

Do not accept significant performance degradation merely because functionality still works.

---

# 32. AI Prohibitions

AI MUST NOT:

* add random memoization everywhere
* add arbitrary caching
* introduce unnecessary state-management libraries
* add unnecessary dependencies
* lazy-load everything
* virtualize every list
* introduce complex infrastructure without justification
* optimize only for Lighthouse
* remove UX/accessibility features for speed
* hide performance problems with artificial delays
* use fake/mock data to demonstrate performance
* claim performance completion without verification

---

# 33. Performance Workflow

For performance-sensitive Features:

```text id="p003"
Identify
↓
Measure / Establish Baseline
↓
Find Bottleneck
↓
Plan
↓
Implement
↓
Measure Again
↓
Regression Check
↓
Audit
```

AI MUST optimize based on evidence whenever practical.

---

# 34. Completion Gate

A performance-relevant Feature is complete only when:

* performance impact is identified
* relevant budgets are considered
* unnecessary work is removed
* network usage is reasonable
* database usage is reasonable
* mobile performance is considered
* loading/error states are stable
* accessibility is preserved
* relevant performance tests pass
* significant regressions are resolved
* performance claims are supported by evidence

Final status:

```text id="p004"
Performance Status: PASS
Feature: [FEATURE_ID]
Baseline: [STATUS]
Network: [STATUS]
Rendering: [STATUS]
Database: [STATUS]
Mobile: [STATUS]
Accessibility: [STATUS]
Regression: [STATUS]
Audit: PASS
```
