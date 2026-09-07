# Performance Skill

## Purpose

Use this Skill when implementing, reviewing, testing, or optimizing a Feature where performance may materially affect user experience, infrastructure cost, scalability, or reliability.

Performance MUST be handled as part of Feature development.

---

# 1. Workflow

Follow this sequence:

```text
IDENTIFY
↓
MEASURE
↓
ANALYZE
↓
PLAN
↓
IMPLEMENT
↓
MEASURE AGAIN
↓
REGRESSION CHECK
↓
AUDIT
↓
REPORT
```

Do not optimize blindly.

---

# 2. Identify

Determine whether the Feature affects:

* initial page loading
* route transitions
* rendering
* JavaScript bundle size
* images
* fonts
* API requests
* database reads/writes
* realtime listeners
* large datasets
* third-party services
* mobile performance
* memory usage
* Core Web Vitals
* infrastructure cost

If performance impact is negligible, document:

`Performance impact: Low / None`

---

# 3. Inspect

Before changing performance-sensitive code, inspect:

* `PROJECT_SPEC.md`
* `PERFORMANCE_RULES.md`
* `ARCHITECTURE.md`
* `UX_RULES.md`
* `DESIGN_SYSTEM.md`
* existing performance utilities
* data-fetching patterns
* API implementation
* database queries
* existing tests
* existing monitoring

Do not introduce a new optimization pattern when an appropriate existing pattern already exists.

---

# 4. Establish a Baseline

Where practical, measure the current state before optimization.

Possible measurements:

* page load
* route transition
* API latency
* database reads
* database writes
* bundle size
* image payload
* rendering time
* memory usage
* Core Web Vitals

Record the baseline when it is relevant to the change.

---

# 5. Analyze

Identify the actual bottleneck.

Potential causes:

```text
Rendering
Network
JavaScript
Images
Fonts
API
Database
Third Party
Memory
Architecture
```

Do not optimize an area without evidence or a clear architectural reason.

---

# 6. Plan

Define:

### Problem

`[PERFORMANCE_PROBLEM]`

### Root Cause

`[ROOT_CAUSE]`

### Proposed Change

`[CHANGE]`

### Expected Result

`[EXPECTED_RESULT]`

### Risk

`[RISK]`

Performance improvements MUST NOT introduce unnecessary complexity.

---

# 7. Frontend Optimization

Evaluate:

* unnecessary renders
* unnecessary state updates
* expensive calculations
* duplicate requests
* large component trees
* unnecessary effects
* large client bundles
* route-level code splitting
* image loading
* font loading

For React:

* preserve component purity
* preserve Rules of Hooks
* avoid unnecessary state
* derive values instead of duplicating state
* use memoization only when justified

Do not add `useMemo`, `useCallback`, or `memo` everywhere without justification.

---

# 8. Data Fetching

Review:

* request count
* request duplication
* request ordering
* payload size
* caching
* pagination
* cancellation
* retry behavior

Avoid:

```text
Component A → Request X
Component B → Request X
Component C → Request X
```

when the architecture can safely share the same data source.

---

# 9. API Analysis

For backend/API Features, inspect:

* response size
* query count
* N+1 patterns
* expensive operations
* pagination
* caching
* external service latency
* serialization cost

API optimization MUST NOT bypass:

* authentication
* authorization
* validation
* rate limiting
* audit requirements

---

# 10. Database Analysis

Inspect:

* query shape
* indexes
* number of reads
* number of writes
* document size
* transaction scope
* listener count
* pagination
* hot documents
* high-frequency writes

For Firestore, pay particular attention to:

* broad collection reads
* unnecessary realtime listeners
* duplicated reads
* large documents
* high-frequency updates

Database performance changes MUST remain compatible with `DATABASE_RULES.md`.

---

# 11. Rendering Strategy

Evaluate whether the Feature requires:

* CSR
* SSR
* SSG
* hybrid rendering
* client-side lazy loading
* server-side data loading

Do not change rendering architecture solely for theoretical performance gains.

Architecture changes require impact analysis.

---

# 12. Images

Verify:

* correct dimensions
* appropriate format
* responsive delivery
* compression
* lazy loading where appropriate
* priority loading for critical images
* layout stability

Do not lazy-load critical above-the-fold content unnecessarily.

---

# 13. JavaScript & Dependencies

Inspect bundle impact before adding large dependencies.

Prefer:

* existing project utilities
* native platform capabilities
* small focused dependencies
* route-level code splitting

Avoid adding libraries for functionality already adequately supported by the project.

---

# 14. Caching

Before introducing caching, define:

* what is cached
* cache key
* freshness
* invalidation
* scope
* security implications

Caching MUST NOT expose user-specific or sensitive data across users.

---

# 15. Large Data

For large collections, evaluate:

* pagination
* cursor pagination
* server-side filtering
* server-side sorting
* virtualization
* incremental loading

Do not load an entire production dataset into the browser when only a subset is required.

---

# 16. Mobile Performance

Test relevant Features on constrained environments.

Consider:

* slower CPU
* slower network
* limited memory
* small viewport
* touch interaction

Mobile performance MUST remain compatible with the independent mobile UX defined in `UX_RULES.md`.

---

# 17. Loading & Error States

Verify:

```text
Loading
↓
Success
↓
Empty
↓
Error
```

Loading states MUST NOT cause unnecessary layout shifts.

Do not add artificial delays.

---

# 18. Third-Party Services

For every new third-party dependency or service evaluate:

* bundle/network cost
* initialization cost
* reliability
* failure behavior
* privacy impact
* caching
* necessity

A third-party failure MUST NOT unnecessarily break unrelated Features.

---

# 19. Measurement After Change

After implementation:

1. repeat the baseline measurement
2. compare results
3. verify the expected improvement
4. check for regressions
5. verify UX and accessibility
6. verify security and data correctness

An optimization is not complete simply because the code looks cleaner.

---

# 20. Regression Testing

Check for regressions in:

* functionality
* responsiveness
* accessibility
* API behavior
* database behavior
* authentication
* authorization
* SEO
* memory usage
* bundle size
* loading behavior

Performance optimization MUST NOT silently break another system.

---

# 21. Performance Audit

Audit the Feature using:

```text
[ ] Bottleneck identified
[ ] Baseline established where practical
[ ] Root cause understood
[ ] Optimization justified
[ ] Network usage reviewed
[ ] Rendering reviewed
[ ] Database usage reviewed
[ ] Mobile reviewed
[ ] Loading states reviewed
[ ] Accessibility preserved
[ ] Security preserved
[ ] Regression checked
[ ] Production impact considered
```

---

# 22. Failure Handling

If performance does not improve:

1. stop unnecessary optimization
2. compare measurements
3. identify the real bottleneck
4. revert ineffective complexity when appropriate
5. select a better approach
6. measure again

Do not accumulate optimizations that provide no meaningful benefit.

---

# 23. Hard Prohibitions

AI MUST NOT:

* optimize without understanding the bottleneck
* add memoization everywhere
* lazy-load everything
* cache everything
* virtualize every list
* add unnecessary dependencies
* introduce complex infrastructure without justification
* optimize only for Lighthouse
* sacrifice accessibility
* sacrifice UX
* bypass security
* bypass validation
* hide performance problems with artificial delays
* use mock data for performance demonstrations
* claim performance completion without verification

---

# 24. Completion Gate

Performance work is complete only when:

```text
Problem Identified
↓
Baseline / Evidence
↓
Root Cause
↓
Optimization
↓
Measurement
↓
Regression Check
↓
Audit PASS
```

Final report:

```text
Performance Status: PASS
Feature: [FEATURE_ID]

Problem:
[DESCRIPTION]

Baseline:
[RESULT]

After:
[RESULT]

Network:
[PASS/FAIL]

Rendering:
[PASS/FAIL]

Database:
[PASS/FAIL]

Mobile:
[PASS/FAIL]

Regression:
[PASS/FAIL]

Audit:
PASS
```
