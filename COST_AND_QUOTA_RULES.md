# Cost and Quota Rules

## 1. Purpose

This document defines mandatory rules for controlling infrastructure cost, service quotas, resource consumption, and usage growth.

The goal is to prevent accidental:

* excessive database reads/writes
* uncontrolled AI usage
* unnecessary network traffic
* excessive storage consumption
* runaway background jobs
* quota exhaustion
* unexpected production costs

Cost efficiency MUST be considered part of engineering quality.

---

# 2. Core Principles

The system MUST follow:

* predictable resource usage
* bounded operations
* least-resource design
* quota awareness
* cost visibility
* controlled retries
* efficient data access
* graceful degradation
* production-safe defaults

The cheapest implementation is NOT automatically the correct implementation.

Correctness, security, reliability, and maintainability remain higher priorities.

---

# 3. Cost Awareness

For Features that can materially affect infrastructure cost, AI MUST consider:

```text
Feature
↓
Expected Usage
↓
Resource Consumption
↓
Quota
↓
Estimated Cost
↓
Controls
```

The project SHOULD document important cost assumptions in `PROJECT_SPEC.md`.

---

# 4. AI API Usage

AI Features MUST define reasonable limits for:

* requests
* tokens
* context size
* output size
* tool calls
* execution time
* concurrent requests

AI MUST NOT create unlimited model calls.

---

# 5. AI Request Limits

Where applicable, implement:

* per-user limits
* per-session limits
* per-request token limits
* context limits
* timeout limits
* concurrency limits
* daily/monthly quotas

Limits MUST be enforced server-side when they are security or cost controls.

---

# 6. AI Retry Behavior

AI requests MUST NOT retry indefinitely.

Retries SHOULD use:

* bounded attempts
* exponential backoff where appropriate
* jitter where appropriate
* retryable-error classification

Do NOT retry permanent failures.

---

# 7. AI Tool Calls

Agentic AI systems MUST limit:

* maximum tool calls
* maximum iterations
* execution time
* recursive operations
* generated task chains

An AI agent MUST have a defined termination condition.

---

# 8. AI Cost Amplification

Avoid architectures where one user action can trigger an uncontrolled number of AI operations.

Example:

```text
1 User Request
↓
1 AI Request
✓
```

is preferable to:

```text
1 User Request
↓
AI
↓
10 Tools
↓
50 AI Calls
↓
100 Database Reads
✗
```

unless the behavior is explicitly designed, bounded, and justified.

---

# 9. Firestore Read Efficiency

When using Firestore:

* query only required documents
* avoid unnecessary repeated reads
* use appropriate pagination
* avoid loading entire collections
* avoid client-side filtering of large datasets
* avoid polling when realtime listeners are appropriate
* avoid realtime listeners when realtime data is unnecessary

Firestore access MUST follow `DATABASE_RULES.md` and `FIREBASE_RULES.md`.

---

# 10. Firestore Write Efficiency

Avoid unnecessary writes.

Consider:

* batching
* transactions where required
* debouncing
* write frequency
* duplicate updates
* background synchronization

Do not repeatedly write identical data without a valid reason.

---

# 11. Firestore Query Design

Queries MUST be designed around actual application access patterns.

Consider:

* indexes
* pagination
* result limits
* filtering
* sorting
* document size
* read amplification

Avoid queries that can grow without a practical upper bound.

---

# 12. Large Data Structures

Avoid storing unnecessarily large arrays or frequently changing large documents.

Large frequently updated documents can create:

* excessive write costs
* contention
* inefficient reads
* synchronization problems

Prefer appropriate document decomposition when justified.

---

# 13. Pagination

Large lists MUST use pagination or another bounded retrieval strategy.

Never assume that:

```text
collection.get()
```

is safe simply because it works during development.

Default page sizes SHOULD be reasonable and have an enforced maximum.

---

# 14. Search and Filtering

Search/filter Features MUST avoid unnecessary full-dataset retrieval.

Do not implement:

```text
Download Everything
↓
Filter in Browser
```

for large production datasets.

Use appropriate backend queries or search infrastructure.

---

# 15. Realtime Data

Realtime listeners MUST be used only where they provide meaningful product value.

Each listener SHOULD have:

* defined scope
* appropriate query
* lifecycle management
* unsubscribe behavior

Do not create listeners that remain active after the relevant screen or Feature is gone.

---

# 16. Storage

File uploads MUST have controlled:

* file size
* file type
* upload frequency
* retention
* access
* transformation behavior

Avoid storing multiple unnecessary copies of the same file.

---

# 17. Image Processing

Image workflows SHOULD consider:

* original file size
* generated variants
* compression
* responsive sizes
* caching
* transformation frequency
* storage growth

Do not process or regenerate images unnecessarily.

---

# 18. Network Usage

Frontend and backend systems MUST avoid unnecessary network requests.

Consider:

* request deduplication
* caching
* pagination
* batching
* debouncing
* appropriate polling intervals
* response size
* compression

Do not use aggressive polling as a substitute for proper state synchronization.

---

# 19. API Usage

External APIs MUST have:

* timeout limits
* bounded retries
* rate-limit handling
* caching where appropriate
* request validation
* response size limits

Repeated external requests MUST have a justified reason.

---

# 20. Background Jobs

Background jobs MUST have:

* bounded execution
* retry limits
* failure handling
* idempotency where required
* concurrency limits
* monitoring

Jobs MUST NOT create infinite retry loops.

---

# 21. Scheduled Jobs

Scheduled tasks MUST define:

* frequency
* expected execution time
* maximum workload
* failure behavior
* duplicate-execution handling

Do not schedule high-frequency jobs unless the product requirement justifies them.

---

# 22. Serverless Functions

When using serverless functions, consider:

* invocation frequency
* execution duration
* memory usage
* concurrency
* cold starts
* retries
* triggered loops

A function MUST NOT unintentionally trigger itself repeatedly through data changes.

---

# 23. Caching

Caching SHOULD be used when it safely reduces repeated expensive operations.

Potential cache targets include:

* public API responses
* static assets
* product/catalog data
* expensive computations
* external API results

Caching MUST NOT bypass authorization or expose private data.

---

# 24. Cache Invalidation

When caching is introduced, define:

* cache key
* lifetime
* invalidation strategy
* ownership boundary
* stale-data tolerance

A cache MUST NOT cause unauthorized or dangerously stale data to be served.

---

# 25. Quotas

The project MUST identify relevant quotas for critical services.

Examples:

* AI provider limits
* Firestore limits
* Storage limits
* API limits
* serverless execution limits
* hosting limits
* external service limits

Quota-sensitive Features SHOULD have explicit safeguards.

---

# 26. Quota Exhaustion

The application MUST define safe behavior when quotas are reached.

Possible behavior:

```text
Quota Available
→ Normal Operation

Quota Limited
→ Rate Limited / Degraded Operation

Quota Exhausted
→ Safe Failure / Fallback
```

The system MUST NOT continuously retry a quota-exhausted operation.

---

# 27. Rate Limiting

Public or expensive endpoints SHOULD implement appropriate rate limits.

Rate limits MAY be based on:

* user
* IP
* session
* API key
* Feature
* operation type

Rate limiting MUST NOT be implemented in a way that breaks legitimate critical workflows.

---

# 28. Abuse Protection

Costly operations SHOULD be protected against abuse.

Examples:

* AI generation
* bulk exports
* file processing
* search
* image generation
* email sending
* report generation
* large database operations

Controls MAY include:

* authentication
* quotas
* rate limits
* CAPTCHA / abuse controls where appropriate
* maximum input size
* maximum output size

---

# 29. Cost Monitoring

Production systems SHOULD monitor important usage signals:

* AI requests
* AI tokens
* database reads
* database writes
* storage growth
* bandwidth
* function invocations
* external API requests

Unexpected changes SHOULD trigger investigation.

---

# 30. Cost Alerts

Where supported, configure appropriate alerts for:

* quota thresholds
* spending thresholds
* abnormal usage
* sudden traffic increases
* unusual AI consumption
* storage growth

Alerts MUST be actionable rather than excessively noisy.

---

# 31. Development vs Production

Development environments SHOULD avoid unnecessary production-scale resource consumption.

Use:

* emulators
* test projects
* development Firebase projects
* controlled datasets
* bounded test workloads

where appropriate.

Production resources MUST NOT be used casually for development.

---

# 32. Testing and Cost

Tests MUST NOT accidentally create uncontrolled production costs.

Tests SHOULD:

* use isolated environments
* use bounded datasets
* avoid unnecessary external API calls
* mock external services when appropriate for unit/integration tests
* clean up temporary resources

Production integration tests MUST be explicitly controlled.

---

# 33. Data Retention

Data retention MUST consider:

* storage cost
* business requirements
* privacy requirements
* legal requirements
* backup requirements

Do not retain data indefinitely without a justified reason.

Refer to `PRIVACY_RULES.md` and `DATABASE_RULES.md`.

---

# 34. Cost vs Performance

Cost optimization MUST NOT create unacceptable performance or reliability problems.

For example:

```text
Reduce Database Reads
```

MUST NOT become:

```text
Create Extremely Large Documents
```

if that introduces contention, latency, or data integrity problems.

Optimization MUST consider the complete system.

---

# 35. Cost vs Security

Cost optimization MUST NEVER weaken:

* authentication
* authorization
* encryption
* validation
* auditability
* backups
* security monitoring
* data isolation

Security remains mandatory even when a cheaper implementation exists.

---

# 36. Cost vs User Experience

Cost optimization MUST NOT unnecessarily degrade:

* responsiveness
* accessibility
* reliability
* important realtime behavior
* critical user workflows

Optimize implementation before removing valuable product behavior.

---

# 37. AI Development Behavior

When implementing a Feature, AI MUST consider whether the change introduces:

* new AI calls
* additional database reads
* additional database writes
* additional storage
* additional network traffic
* background processing
* third-party API usage

If material, the impact MUST be reported.

---

# 38. AI Prohibitions

AI MUST NOT:

* create unlimited loops
* create unlimited retries
* create unbounded AI calls
* create unbounded database reads
* create unbounded database writes
* poll aggressively without justification
* download entire production datasets unnecessarily
* create uncontrolled background jobs
* bypass quotas
* disable rate limits to improve UX
* ignore service limits
* assume development usage represents production cost
* introduce expensive infrastructure without justification

---

# 39. Completion Gate

A Feature with material infrastructure or AI usage is complete only when:

```text
Usage Identified
↓
Resource Impact Evaluated
↓
Limits Defined
↓
Retries Bounded
↓
Queries Bounded
↓
Storage Controlled
↓
AI Usage Controlled
↓
Rate Limits Reviewed
↓
Quota Behavior Defined
↓
Monitoring Considered
↓
Cost Risk Reviewed
↓
Tests Passed
```

---

# 40. Final Status

For cost-sensitive Features, the final report SHOULD include:

```text
Cost / Quota Status: PASS

AI Usage:
[CONTROLLED / N/A]

Database Usage:
[CONTROLLED / N/A]

Storage:
[CONTROLLED / N/A]

Network:
[CONTROLLED / N/A]

Background Jobs:
[CONTROLLED / N/A]

Rate Limits:
[VERIFIED / N/A]

Quota Handling:
[VERIFIED / N/A]

Monitoring:
[CONFIGURED / N/A]

Known Cost Risks:
[NONE / LIST]
```

---

# Core Principle

The system MUST be designed so that normal user behavior produces predictable resource consumption.

Every expensive operation MUST have a reason, a boundary, and a failure strategy.

Cost control MUST be proactive, not something added only after the production bill becomes a problem.
