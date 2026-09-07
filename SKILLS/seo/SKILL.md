# SEO Skill

## Purpose

Use this Skill when implementing or reviewing a Feature that has public, crawlable, or search-discoverable content.

SEO MUST be handled during Feature development, not postponed until the final project audit.

---

# 1. Workflow

Follow this sequence:

```text id="seo01"
IDENTIFY
↓
CLASSIFY
↓
PLAN
↓
IMPLEMENT
↓
VERIFY
↓
AUDIT
↓
REPORT
```

Do not skip stages for SEO-relevant Features.

---

# 2. Identify

Determine whether the Feature affects:

* public pages
* indexable content
* URLs
* metadata
* internal links
* structured data
* sitemap
* robots
* localization
* redirects
* search/filter URLs

If none apply, document:

`SEO impact: None`

---

# 3. Classify

Classify each relevant route as:

```text id="seo02"
Public + Indexable
Public + Non-indexable
Authenticated
Admin
Technical/System
```

Indexability MUST be intentional.

Never assume that every public route should be indexed.

---

# 4. Inspect

Before implementation, inspect:

* `PROJECT_SPEC.md`
* `SEO_RULES.md`
* `UX_RULES.md`
* `DESIGN_SYSTEM.md`
* existing routing
* existing metadata system
* canonical implementation
* sitemap generation
* robots configuration
* localization
* structured data
* existing SEO utilities/components

Reuse existing mechanisms whenever possible.

---

# 5. Plan

For every SEO-relevant Feature, define:

### URL

`[URL STRATEGY]`

### Indexability

`[INDEX / NOINDEX]`

### Canonical

`[CANONICAL STRATEGY]`

### Metadata

* Title
* Description
* Open Graph
* Other required metadata

### Internal Links

`[LINKING STRATEGY]`

### Structured Data

`[REQUIRED / NOT REQUIRED]`

### Sitemap

`[INCLUDE / EXCLUDE / DYNAMIC]`

### Localization

`[LANGUAGE / REGION STRATEGY]`

---

# 6. Implement

Implementation MUST:

* use real production data
* generate accurate metadata
* maintain canonical URLs
* preserve routing consistency
* avoid duplicate indexable URLs
* follow project localization rules
* preserve accessibility
* use the existing design system
* avoid unnecessary architecture changes

Do not create fake SEO content.

---

# 7. Ecommerce Features

For ecommerce Features, verify when applicable:

```text id="seo03"
Category
↓
Subcategory
↓
Product
↓
Variant
↓
Related Products
```

Determine:

* canonical product URL
* variant URL behavior
* availability representation
* pricing representation
* product structured data
* breadcrumbs
* internal linking

All SEO data MUST come from authoritative application data.

---

# 8. Dynamic URLs

For Features containing:

* filters
* search
* sorting
* pagination
* query parameters

analyze crawl/index behavior before implementation.

Prevent uncontrolled combinations from becoming indexable.

---

# 9. Localization

If multiple locales exist:

1. identify supported locales
2. define URL strategy
3. define canonical behavior
4. define alternate-language behavior
5. verify language metadata
6. verify internal links

Do not add `hreflang` when no alternate versions exist.

---

# 10. Technical Verification

Verify the actual rendered behavior where possible.

Check:

* HTTP status
* title
* description
* canonical
* indexability
* headings
* internal links
* structured data
* language metadata
* redirects
* sitemap behavior
* robots behavior

Do not assume implementation is correct because source code looks correct.

---

# 11. Mobile & Performance

SEO verification MUST include:

* mobile rendering
* content availability
* layout stability
* image behavior
* loading performance
* JavaScript-dependent content where relevant

SEO MUST NOT be implemented by sacrificing UX or accessibility.

---

# 12. Testing

Relevant tests SHOULD cover:

* metadata generation
* canonical generation
* route classification
* structured data
* sitemap generation
* localization
* redirect behavior
* indexability behavior

Critical SEO Features SHOULD include automated regression tests where practical.

---

# 13. Audit

Perform an SEO audit before marking the Feature complete.

### Audit Checklist

```text id="seo04"
[ ] URL is correct
[ ] URL is stable
[ ] Indexability is intentional
[ ] Canonical is correct
[ ] Title is correct
[ ] Description is correct
[ ] Heading hierarchy is valid
[ ] Internal links work
[ ] Structured data is accurate
[ ] Sitemap behavior is correct
[ ] Robots behavior is correct
[ ] Localization is correct
[ ] Mobile behavior is correct
[ ] Performance impact is acceptable
[ ] No duplicate indexable URLs
[ ] No fake/generated production SEO data
```

---

# 14. Failure Handling

If SEO implementation fails:

1. identify the failing requirement
2. identify the affected route/Feature
3. determine root cause
4. fix the implementation
5. rerun relevant tests
6. repeat the audit

Do not mark the Feature complete while a relevant SEO blocker remains.

---

# 15. Hard Prohibitions

AI MUST NOT:

* keyword stuff
* create hidden SEO text
* fabricate structured data
* index every filter combination
* create doorway pages
* create fake content for ranking
* expose private content to crawlers
* silently change URL architecture
* create duplicate canonical URLs
* claim SEO completion without verification

---

# 16. Completion Gate

SEO work for a Feature is complete only when:

```text id="seo05"
Requirements Identified
        ↓
SEO Strategy Defined
        ↓
Implementation Complete
        ↓
Real Data Verified
        ↓
Tests Passed
        ↓
SEO Audit Passed
        ↓
No SEO Blocker
```

Then report:

```text id="seo06"
SEO Status: PASS
Feature: [FEATURE_ID]
Routes: [ROUTES]
Indexability: [STATUS]
Canonical: [STATUS]
Metadata: [STATUS]
Structured Data: [STATUS]
Sitemap: [STATUS]
Localization: [STATUS]
Audit: PASS
```
