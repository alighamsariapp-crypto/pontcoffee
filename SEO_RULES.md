# SEO Rules

## 1. Purpose

This document defines the mandatory SEO rules for projects that contain public, crawlable, or search-discoverable content.

SEO MUST be considered during Feature Definition, Design, Implementation, Integration, and Audit.

SEO MUST NOT be treated only as a final optimization step.

---

# 2. Source of Truth

SEO implementation MUST follow this priority:

1. `PROJECT_SPEC.md`
2. `SEO_RULES.md`
3. `ARCHITECTURE.md`
4. `UX_RULES.md`
5. Feature requirements
6. Existing verified implementation

Project-specific SEO requirements in `PROJECT_SPEC.md` override generic SEO assumptions.

---

# 3. SEO Scope

For every Feature, AI MUST determine whether it is:

```text
Public + Indexable
Public + Non-indexable
Authenticated
Admin
System / Technical
```

Only relevant public content should normally be indexable.

Admin, authenticated, internal, temporary, utility, and sensitive pages MUST NOT accidentally become indexable.

---

# 4. URL Architecture

URLs MUST be:

* stable
* meaningful
* predictable
* canonical
* unique
* compatible with the project's localization strategy

Avoid unnecessary:

* tracking parameters in canonical URLs
* duplicate URL patterns
* meaningless IDs when a readable identifier is appropriate
* temporary URLs
* unnecessary query-string variations

URL structure MUST be defined at feature level when SEO relevance exists.

AI MUST NOT change established URL architecture without impact analysis.

---

# 5. Canonical URLs

Every indexable page MUST have a deterministic canonical URL.

Canonical URLs MUST:

* represent the preferred version of the page
* use the correct protocol and host
* avoid unnecessary parameters
* remain stable
* be consistent with redirects and internal links

Canonicalization MUST NOT be used to hide genuinely different indexable pages.

---

# 6. Metadata

Indexable pages MUST provide appropriate:

* `<title>`
* meta description
* canonical URL
* language information
* Open Graph metadata where relevant
* social sharing metadata where relevant

Metadata MUST be:

* unique where page content is unique
* relevant to the page
* generated from real data when dynamic
* protected against accidental duplication

AI MUST NOT generate identical generic metadata for an entire catalog.

---

# 7. Heading Structure

Pages MUST use meaningful semantic heading hierarchy.

Rules:

* one clear primary page heading where appropriate
* headings describe actual content
* hierarchy MUST be logical
* headings MUST NOT exist only for visual styling
* visual typography MUST remain controlled by `DESIGN_SYSTEM.md`

SEO MUST NOT be used as a reason to add artificial or hidden keyword content.

---

# 8. Crawlability

Public pages intended for search engines MUST be reachable through valid internal navigation or other intentional discovery mechanisms.

Avoid:

* orphaned important pages
* broken internal links
* accidental authentication requirements
* client-only navigation that prevents meaningful discovery
* infinite URL variations
* duplicate crawl paths

Important public pages MUST have a deliberate crawl/discovery strategy.

---

# 9. Robots.txt

Projects with public crawlable content SHOULD provide an appropriate `robots.txt`.

It MUST NOT accidentally block:

* important public pages
* required assets
* important product/category routes

It SHOULD prevent crawling of clearly unnecessary technical areas where appropriate.

`robots.txt` MUST NOT be treated as a substitute for authentication or authorization.

Sensitive content MUST be protected by application security.

---

# 10. XML Sitemap

Projects with meaningful public content SHOULD provide an XML sitemap.

The sitemap SHOULD contain only appropriate canonical URLs.

It MUST NOT intentionally contain:

* authenticated URLs
* admin URLs
* duplicate URLs
* redirected URLs
* obvious error pages
* non-canonical variants

Dynamic content systems MUST define how sitemap entries are generated and updated.

---

# 11. Indexing Control

The project MUST explicitly determine indexing behavior for:

* public pages
* search results
* filter combinations
* sorting URLs
* pagination
* temporary pages
* checkout
* account pages
* admin pages
* error pages

Do not allow every generated URL to become indexable by default.

---

# 12. Internal Linking

Important public content MUST have intentional internal links.

Internal linking SHOULD support:

* discovery
* navigation
* related content
* category → item relationships
* item → related item relationships
* contextual content relationships

Avoid artificial keyword-heavy links.

---

# 13. JavaScript & Rendering

SEO requirements MUST be considered together with the selected rendering architecture.

The project MAY use:

* CSR
* SSR
* SSG
* hybrid rendering
* framework-specific rendering strategies

AI MUST NOT automatically introduce SSR or another rendering architecture solely because it is commonly recommended for SEO.

The chosen architecture MUST be evaluated against:

* crawlability
* content availability
* performance
* hosting
* complexity
* project requirements

---

# 14. Ecommerce SEO

For ecommerce projects, AI MUST consider SEO for:

* category pages
* product pages
* brand pages where applicable
* collection pages
* useful landing pages
* product availability
* pricing information
* product images
* variants

Product pages SHOULD expose accurate, current information.

Structured data MUST reflect the actual visible page content.

---

# 15. Product Variants

Variant handling MUST be explicitly defined.

AI MUST determine whether variants should:

* share one canonical URL
* have independent URLs
* use query parameters
* use path-based URLs

This decision MUST be consistent with the project's product model and SEO strategy.

AI MUST NOT create indexable duplicate URLs for variants without a deliberate requirement.

---

# 16. Structured Data

Structured data MAY be used when it accurately represents the page.

Potential types include:

* Organization
* WebSite
* BreadcrumbList
* Product
* Offer
* Article
* FAQPage
* LocalBusiness
* other applicable schema types

Structured data MUST:

* describe visible or legitimately represented content
* remain synchronized with actual data
* avoid misleading search engines
* be validated during SEO testing

Do not add structured data merely to increase the amount of schema markup.

---

# 17. Breadcrumbs

Where hierarchical content exists, breadcrumbs SHOULD be implemented.

Examples:

```text
Home
  ↓
Category
  ↓
Subcategory
  ↓
Product
```

Breadcrumbs MUST represent the actual information architecture.

---

# 18. Localization & International SEO

If multiple languages or regions exist, the project MUST define:

* supported languages
* locale structure
* URL strategy
* canonical strategy
* `hreflang` requirements
* language metadata

`hreflang` MUST only be implemented when the project actually has alternate language or regional versions.

RTL and language behavior remain governed by `UX_RULES.md`.

---

# 19. Images

Important images MUST have:

* meaningful filenames where practical
* appropriate `alt` text
* correct dimensions
* optimized delivery
* stable URLs where possible

`alt` text MUST describe the image's actual purpose.

Do not keyword-stuff `alt` attributes.

Decorative images SHOULD use the appropriate accessibility treatment.

---

# 20. SEO & Accessibility

SEO implementation MUST NOT damage accessibility.

AI MUST NOT:

* hide keyword content from users
* create invisible SEO text
* misuse headings
* remove meaningful accessible labels
* sacrifice semantic HTML for SEO hacks

SEO and accessibility MUST work together.

---

# 21. Performance & SEO

SEO-sensitive pages SHOULD meet the project's performance requirements.

AI MUST consider:

* loading performance
* image optimization
* layout stability
* JavaScript cost
* rendering strategy
* caching
* Core Web Vitals where applicable

Performance requirements remain governed by `PERFORMANCE_RULES.md`.

---

# 22. Redirects

URL changes MUST have an explicit redirect strategy.

When an important public URL changes, AI MUST evaluate whether a redirect is required.

Avoid redirect chains.

Redirect rules MUST NOT create loops.

---

# 23. 404 & Error Pages

The project MUST provide an intentional not-found experience.

404 pages SHOULD:

* clearly communicate the missing resource
* provide useful navigation
* preserve the site's design system
* avoid pretending the resource exists

Error pages MUST NOT accidentally return successful status semantics for missing resources when the architecture supports correct HTTP status handling.

---

# 24. Search & Filter Pages

Internal search and filter systems require deliberate indexing rules.

AI MUST evaluate:

```text
Search URL
Filter URL
Sort URL
Pagination URL
Query Parameters
Combination URLs
```

Do not automatically make every combination indexable.

Large combinations of filters MUST NOT create uncontrolled crawlable URL spaces.

---

# 25. Dynamic Content

SEO metadata and structured data generated from databases MUST use validated, real production data.

AI MUST NOT use:

* fake product names
* fake prices
* placeholder descriptions
* fabricated ratings
* mock inventory
* invented structured-data values

for production SEO.

---

# 26. AI-Generated Content

If AI generates content, the project MUST define:

* source of truth
* approval workflow
* factual validation
* duplication control
* update strategy
* editorial responsibility

AI-generated content MUST NOT automatically become production content merely because it was generated successfully.

---

# 27. Technical SEO Validation

Relevant Features MUST be tested for:

* correct title
* correct description
* canonical URL
* indexability
* robots behavior
* sitemap inclusion where applicable
* internal links
* HTTP status
* redirects
* structured data
* language metadata
* duplicate URL behavior
* mobile rendering
* important content availability

SEO testing MUST be part of Feature verification when the Feature is SEO-relevant.

---

# 28. SEO Audit

Before production release, applicable public pages MUST be audited.

The audit SHOULD verify:

```text
URL
↓
HTTP Status
↓
Indexability
↓
Canonical
↓
Metadata
↓
Content
↓
Internal Links
↓
Structured Data
↓
Mobile UX
↓
Performance
↓
Sitemap
↓
Robots
```

---

# 29. AI Prohibitions

AI MUST NOT:

* generate hidden keyword content
* keyword-stuff pages
* create fake backlinks
* create doorway pages
* duplicate pages solely for ranking
* fabricate structured data
* expose private/admin content to crawlers
* index every filter combination automatically
* create duplicate canonical URLs
* block important public content accidentally
* change URL architecture without impact analysis
* claim SEO completion without verification

---

# 30. Completion Gate

An SEO-relevant Feature is complete only when:

* SEO requirements are identified
* URL strategy is defined
* indexability is intentional
* metadata is implemented
* canonical behavior is correct
* internal linking is considered
* structured data is correct where applicable
* mobile behavior is verified
* performance requirements are considered
* relevant tests pass
* SEO audit findings are resolved
* no SEO blocker remains

SEO completion MUST be evidence-based, not assumed from page rendering alone.
