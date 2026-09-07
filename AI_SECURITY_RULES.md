# AI Security Rules

## 1. Purpose

This document defines mandatory security rules for applications that use AI models, AI APIs, AI agents, generated content, tool calling, retrieval systems, or automated AI-driven actions.

AI MUST be treated as an untrusted computational component.

AI output MUST NOT automatically be considered trusted, correct, safe, authorized, or executable.

---

# 2. Core Principles

AI-enabled systems MUST follow:

* Zero Trust
* Least Privilege
* Explicit Authorization
* Server-Side Validation
* Data Minimization
* Human Oversight for High-Risk Actions
* Defense in Depth
* Safe Failure
* Explicit Tool Boundaries

---

# 3. AI Is Not an Authority

The AI MUST NOT be the final authority for:

* authentication
* authorization
* user identity
* permissions
* ownership
* payment amounts
* inventory quantities
* financial transactions
* security decisions
* access-control decisions
* irreversible operations

These MUST be enforced by deterministic server-side logic.

---

# 4. Prompt Injection

All AI inputs MUST be considered potentially malicious.

Potential injection sources include:

* user messages
* uploaded documents
* web pages
* product descriptions
* database records
* emails
* third-party APIs
* retrieved documents
* search results
* tool output
* generated content

Retrieved or external content MUST NOT automatically become trusted instructions.

---

# 5. Instruction Hierarchy

The application MUST clearly separate:

```text id="a001"
System / Application Rules
↓
Developer Rules
↓
Feature Rules
↓
User Input
↓
External / Retrieved Content
```

Lower-trust content MUST NOT override higher-trust application instructions.

---

# 6. Retrieved Content

RAG or retrieval systems MUST distinguish between:

```text id="a002"
Instructions
```

and:

```text id="a003"
Data
```

Documents retrieved from external or user-controlled sources MUST be treated as data unless explicitly trusted.

The AI MUST NOT blindly execute instructions found inside retrieved content.

---

# 7. Tool Calling

AI tools MUST use explicit allowlists.

For every tool define:

* purpose
* input schema
* authorization requirements
* allowed caller
* allowed parameters
* side effects
* error behavior
* logging requirements

AI MUST NOT dynamically discover or execute arbitrary server capabilities.

---

# 8. Tool Least Privilege

AI tools MUST have the minimum permissions required.

Example:

```text id="a004"
AI Assistant
    ↓
Search Products
    ✓

AI Assistant
    ↓
Delete Production Database
    ✗
```

A tool MUST NOT receive broader permissions simply because the AI may need them later.

---

# 9. High-Risk Actions

The following actions require deterministic server-side authorization and SHOULD require explicit user confirmation where appropriate:

* payments
* refunds
* account deletion
* permission changes
* destructive database operations
* sending external messages
* publishing content
* changing production configuration
* deleting files
* modifying security settings

AI confirmation alone MUST NOT satisfy authorization requirements.

---

# 10. Human-in-the-Loop

For high-impact or irreversible actions, the system SHOULD use:

```text id="a005"
AI Recommendation
↓
Validation
↓
User Confirmation
↓
Server Authorization
↓
Execution
↓
Audit Log
```

The exact approval model depends on the risk level.

---

# 11. Structured AI Output

When AI output controls application behavior, prefer structured schemas.

Example:

```text id="a006"
AI
↓
Structured Output
↓
Runtime Validation
↓
Business Rules
↓
Authorization
↓
Execution
```

Never execute raw AI-generated code, SQL, shell commands, database operations, or API requests without strict controls.

---

# 12. Runtime Validation

AI-generated values MUST be validated at runtime.

Validation MUST cover:

* type
* format
* allowed values
* ranges
* required fields
* relationships
* authorization
* business rules

TypeScript types alone are NOT sufficient for untrusted AI output.

---

# 13. AI-Generated Code

Production systems MUST NOT execute AI-generated code directly unless a deliberately isolated and secured execution architecture exists.

Never allow unrestricted AI-generated:

* shell commands
* JavaScript execution
* SQL
* Firestore queries
* filesystem operations
* infrastructure commands

---

# 14. SQL / Database Safety

AI MUST NOT directly generate unrestricted database queries against production data.

Use:

* parameterized queries
* query builders
* allowlists
* restricted repositories
* server-side authorization
* row/object-level access control

For Firestore, AI-generated filters and paths MUST be validated against allowed collections, fields, operators, and ownership rules.

---

# 15. Sensitive Data

AI systems MUST minimize sensitive data exposure.

Do not send unnecessary:

* passwords
* authentication tokens
* session identifiers
* payment information
* private keys
* secrets
* personal data
* internal security information

to AI providers.

---

# 16. Secrets

Secrets MUST NEVER be placed inside:

* prompts
* system messages
* client-side AI requests
* generated content
* logs
* analytics events
* AI tool responses

AI MUST NOT be given unrestricted access to environment variables.

---

# 17. Personal Data

AI processing of personal data MUST follow the project's privacy requirements.

Before sending data to an external AI provider determine:

* what data is sent
* why it is needed
* where it is processed
* retention implications
* provider requirements
* user expectations
* applicable legal requirements

Refer to `PRIVACY_RULES.md`.

---

# 18. Data Exfiltration

AI features MUST defend against attempts to expose:

* system prompts
* internal instructions
* secrets
* private documents
* other users' data
* internal APIs
* hidden configuration
* privileged tool information

Authorization MUST be enforced outside the model.

---

# 19. Cross-User Data Isolation

An AI assistant MUST NOT access another user's data merely because:

* the user asks
* the model infers it
* retrieval returns it
* a prompt contains another user's identifier

Every data access MUST pass server-side authorization and ownership checks.

---

# 20. Context Isolation

AI context SHOULD be limited to information required for the current task.

Avoid unnecessarily combining:

```text
User A Data
+
User B Data
+
Internal Admin Data
+
System Secrets
```

inside one model context.

---

# 21. Memory

If an AI feature stores conversational or user memory:

* define what is stored
* define retention
* define ownership
* define deletion behavior
* define access control
* define whether users can review it
* prevent cross-user leakage

Memory MUST NOT become an unrestricted data store.

---

# 22. File Uploads

AI processing of uploaded files MUST treat files as untrusted.

Verify:

* file type
* file size
* parsing safety
* malicious content
* prompt injection
* embedded instructions
* access permissions

Uploaded documents MUST NOT automatically become trusted AI instructions.

---

# 23. Web Browsing / External Data

If AI can browse or consume external content:

* external content is untrusted
* URLs MUST be validated
* SSRF protections MUST apply
* sensitive internal endpoints MUST be blocked
* fetched content MUST NOT override application instructions
* external instructions MUST NOT automatically trigger privileged tools

---

# 24. Rate Limiting

AI endpoints SHOULD have appropriate limits for:

* requests
* tokens
* file size
* context size
* tool calls
* execution time
* concurrent requests

Limits MUST consider abuse and cost amplification.

---

# 25. Cost Abuse

AI systems MUST defend against uncontrolled consumption.

Controls MAY include:

* per-user quotas
* per-request token limits
* maximum context size
* maximum tool calls
* timeout limits
* daily/monthly limits
* budget alerts
* abuse detection

See `COST_AND_QUOTA_RULES.md`.

---

# 26. Model Output Safety

AI-generated content MUST be handled according to its destination.

Never assume generated content is safe for:

* HTML
* SQL
* shell
* URLs
* HTTP headers
* database fields
* executable code

Apply appropriate validation and output encoding.

---

# 27. XSS Protection

AI-generated HTML or rich text MUST NOT be inserted into the DOM as trusted HTML without sanitization and an explicit safe rendering strategy.

Prefer rendering structured data rather than arbitrary generated HTML.

---

# 28. Authorization After AI

When AI recommends an action:

```text id="a007"
AI Output
↓
Server Validation
↓
Authorization
↓
Business Rules
↓
Execution
```

Never:

```text id="a008"
AI Output
↓
Execution
```

---

# 29. AI Agents

Agentic systems MUST have:

* explicit tool registry
* tool permissions
* execution limits
* timeouts
* maximum iteration count
* context limits
* approval boundaries
* audit logging
* failure handling

Agents MUST NOT operate indefinitely.

---

# 30. Autonomous Actions

Autonomous AI actions MUST be classified by risk.

Example:

```text id="a009"
Low Risk
Read/Search
    ↓
May be automatic

Medium Risk
Create/Draft
    ↓
Validation required

High Risk
Financial/Destructive/Privileged
    ↓
Explicit authorization / approval
```

---

# 31. Logging

AI security events SHOULD be logged where appropriate.

Examples:

* rejected tool calls
* authorization failures
* suspicious prompt-injection attempts
* unusual token consumption
* repeated tool failures
* high-risk action approvals
* security policy violations

Logs MUST NOT contain secrets or unnecessary sensitive content.

---

# 32. Monitoring

Monitor AI-specific signals such as:

* request volume
* token usage
* latency
* failure rate
* tool-call frequency
* rejected actions
* abuse patterns
* cost anomalies
* model/provider errors

---

# 33. Provider Security

Before integrating an AI provider, evaluate:

* authentication
* API key protection
* data handling
* retention
* logging
* regional processing where relevant
* rate limits
* failure behavior
* model/version stability
* provider security documentation

Provider-specific assumptions MUST be documented.

---

# 34. AI Dependency Failure

AI services are external dependencies.

The application MUST define behavior for:

* timeout
* provider outage
* rate limit
* malformed output
* unavailable model
* partial response
* network failure
* provider policy rejection

AI failure MUST NOT corrupt application state.

---

# 35. Deterministic Fallbacks

Critical business functionality MUST NOT depend exclusively on AI unless the project explicitly requires it and has a safe fallback strategy.

Where practical:

```text id="a010"
AI Available
→ Enhanced Experience

AI Unavailable
→ Safe Degraded Experience
```

---

# 36. Security Testing

AI features MUST be tested against:

* prompt injection
* indirect prompt injection
* tool abuse
* privilege escalation
* cross-user data access
* data exfiltration
* malicious file content
* malformed structured output
* excessive requests
* excessive token usage
* unauthorized high-risk actions
* model/provider failure

---

# 37. AI Red-Team Testing

High-risk AI features SHOULD undergo adversarial testing before production.

Tests SHOULD attempt to:

* override instructions
* access unauthorized data
* invoke forbidden tools
* bypass approval
* manipulate structured output
* trigger excessive resource usage
* extract hidden information

---

# 38. AI Security Architecture

The preferred architecture is:

```text id="a011"
User
↓
Application
↓
Authentication
↓
Authorization
↓
Input Validation
↓
AI Layer
↓
Output Validation
↓
Business Rules
↓
Authorization Again
↓
Tool / Database / API
↓
Audit / Monitoring
```

The AI layer MUST NOT bypass application security boundaries.

---

# 39. AI Development Rules

During development AI MUST:

* inspect existing security architecture
* reuse existing authorization
* reuse existing validation
* reuse existing data-access boundaries
* avoid creating parallel auth systems
* avoid duplicating security logic
* avoid storing secrets
* avoid weakening existing controls
* add tests for new AI attack surfaces

---

# 40. AI Prohibitions

AI MUST NOT:

* treat user prompts as trusted instructions
* treat retrieved content as trusted instructions
* expose system prompts or secrets
* bypass authorization
* make itself an authorization layer
* execute arbitrary generated code
* execute unrestricted generated SQL
* access arbitrary files
* access arbitrary URLs
* call unrestricted tools
* modify production infrastructure autonomously
* perform destructive actions without required authorization
* expose another user's data
* log secrets
* disable security controls to make an AI feature work
* claim an AI security feature is safe without testing

---

# 41. Completion Gate

An AI feature is complete only when:

```text id="a012"
AI Requirement Defined
↓
Threat Model Reviewed
↓
Trust Boundaries Defined
↓
Data Access Controlled
↓
Tool Permissions Defined
↓
Input Validation Implemented
↓
Output Validation Implemented
↓
Authorization Verified
↓
Failure Handling Implemented
↓
Rate / Cost Controls Verified
↓
Security Tests Passed
↓
Prompt Injection Tests Passed
↓
Cross-User Isolation Verified
↓
Monitoring Implemented
↓
Security Audit Passed
```

Final status:

```text id="a013"
AI Security Status: PASS

Threat Model:
PASS

Authorization:
PASS

Input Validation:
PASS

Output Validation:
PASS

Tool Security:
PASS

Data Isolation:
PASS

Prompt Injection:
PASS

Rate / Cost Controls:
PASS

Failure Handling:
PASS

Security Tests:
PASS

Audit:
PASS
```

---

# 42. Authority Rule

When this document conflicts with an AI model's suggestion, the application security architecture and explicit project security rules take precedence.

AI MUST adapt to the security architecture.

The security architecture MUST NOT be weakened to accommodate the AI.
