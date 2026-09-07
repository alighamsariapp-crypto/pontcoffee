# CONTENT RULES

## 1. Purpose

Content is part of the product experience.

Content MUST be:

* Accurate
* Clear
* Consistent
* Useful
* Accessible
* Appropriate for the target audience
* Consistent with the project's brand and product requirements

AI MUST NOT treat content as placeholder material when real production content is required.

---

## 2. Source of Truth

Content decisions MUST follow:

1. `PROJECT_SPEC.md`
2. Product/business requirements
3. Brand guidelines, if provided
4. `DESIGN_SYSTEM.md`
5. `UX_RULES.md`
6. `SEO_RULES.md`
7. `PRIVACY_RULES.md`
8. Applicable legal requirements

---

## 3. Real vs Placeholder Content

AI MUST clearly distinguish between:

### Production Content

Approved content intended for real users.

### Placeholder Content

Temporary content used only when final content is unavailable.

Placeholder content MUST NOT be presented as final production content.

Avoid meaningless placeholders such as:

```text
Lorem ipsum
Product 1
Test User
Sample text
Description here
```

when realistic content is required for proper UX evaluation.

---

## 4. Content Structure

Content SHOULD be structured according to its purpose.

Examples:

* Page title
* Section heading
* Supporting description
* Primary action
* Secondary action
* Labels
* Help text
* Validation messages
* Empty states
* Error messages
* Success messages
* Notifications

Do not add text merely to fill visual space.

---

## 5. Clarity

User-facing text SHOULD be:

* Concise
* Direct
* Understandable
* Action-oriented where appropriate

Avoid:

* Unnecessary technical terminology
* Repetitive explanations
* Long paragraphs in interfaces
* Ambiguous actions
* Decorative text that reduces clarity

---

## 6. Consistency

The same concept MUST use consistent terminology throughout the product.

Examples:

Do not alternate between:

```text
Delete
Remove
Erase
```

for the same action unless they intentionally represent different operations.

Shared terminology SHOULD be documented in the project specification when important.

---

## 7. UI Content

Interface content MUST respect the design system.

AI MUST consider:

* Text length
* Component width
* Responsive behavior
* RTL layout
* Mobile readability
* Button width
* Form labels
* Error message length
* Empty states

Content MUST NOT force broken layouts.

---

## 8. Persian / RTL Content

For Persian projects:

* Content MUST be natural Persian.
* RTL direction MUST be respected.
* Persian punctuation SHOULD be used appropriately.
* Persian and Latin text MUST coexist safely.
* Numbers, prices, dates, URLs, SKUs, and technical identifiers MUST remain readable.
* Content MUST NOT rely on manual spaces for alignment.

Use CSS logical properties and appropriate typography from `DESIGN_SYSTEM.md`.

---

## 9. Accessibility

Content MUST support accessibility.

Avoid:

* Meaningful information conveyed only by color
* Unclear link text
* Icon-only actions without accessible labels
* Ambiguous form instructions
* Error messages that do not explain the problem

Important actions and states MUST be understandable to assistive technologies.

Follow `UX_RULES.md` and `TESTING_RULES.md`.

---

## 10. Forms

Forms MUST have clear:

* Labels
* Instructions
* Required/optional indicators
* Validation messages
* Error messages
* Success feedback

Validation messages SHOULD explain:

1. What is wrong
2. How the user can fix it

Do not use vague messages such as:

```text
Invalid input
Something went wrong
Error
```

when a more useful explanation is possible.

---

## 11. Empty States

Every important data-driven view SHOULD define an intentional empty state.

Examples:

* No products
* No orders
* No search results
* No notifications
* Empty cart
* No saved items

An empty state SHOULD explain what happened and, where appropriate, provide a useful next action.

---

## 12. Error Messages

User-facing errors SHOULD:

* Explain the problem simply
* Avoid exposing internal details
* Provide a recovery action when possible

Internal diagnostic information belongs in secure logs/observability, not directly in the UI.

---

## 13. Loading & Progress Content

Loading states MUST communicate meaningful progress when appropriate.

Avoid unnecessary text such as:

```text
Loading...
Please wait...
Processing...
```

when a suitable visual loading state already communicates the status.

For long-running operations, provide useful progress information where possible.

---

## 14. Confirmation & Destructive Actions

Destructive operations SHOULD clearly communicate:

* What will happen
* Whether the action is reversible
* What data may be affected

Confirmation text MUST NOT be misleading.

---

## 15. Notifications & Feedback

Success, warning, and error messages SHOULD be:

* Clear
* Short
* Relevant
* Timely
* Accessible

Do not use notifications as a replacement for important persistent information.

---

## 16. SEO Content

SEO content MUST follow `SEO_RULES.md`.

AI MUST NOT:

* Stuff keywords unnaturally
* Generate duplicate pages only for search traffic
* Create misleading titles/descriptions
* Generate large amounts of low-value content
* Add structured data that does not match visible page content

SEO optimization MUST preserve user value.

---

## 17. Dynamic & User-Generated Content

User-generated content MUST be treated as untrusted input.

The system MUST safely handle:

* HTML
* Markdown
* Links
* Images
* Embedded content
* User names
* Reviews
* Comments
* Product descriptions

Never render untrusted HTML directly without appropriate sanitization and security controls.

Follow `SECURITY_RULES.md`.

---

## 18. AI-Generated Content

AI-generated content MUST be validated before being treated as production content.

Depending on the feature, verify:

* Accuracy
* Relevance
* Safety
* Tone
* Formatting
* Privacy
* Policy compliance
* SEO requirements

AI MUST NOT silently publish high-impact content without the required validation or approval workflow.

---

## 19. E-Commerce Content

For commerce projects, important product content SHOULD clearly define:

* Product name
* Product description
* Price
* Availability
* SKU where applicable
* Specifications
* Variants
* Shipping information where applicable
* Warranty/return information where applicable

The UI MUST NOT invent product facts.

Server-authoritative values such as price, inventory, discount, and order totals MUST come from trusted backend logic.

---

## 20. Localization

If multiple languages are supported:

* Translations MUST preserve meaning.
* UI layouts MUST support text expansion.
* Dates/numbers/currency MUST follow the appropriate locale.
* Language metadata MUST be correct.
* SEO localization MUST follow `SEO_RULES.md`.

Do not use machine-translated text as final production content without appropriate review when quality matters.

---

## 21. Legal / Compliance Content

Legal or regulatory text MUST NOT be invented.

Examples:

* Privacy notices
* Terms
* Refund policies
* Warranty conditions
* Consent notices
* Disclaimers

When authoritative legal text is required but not provided, AI MUST flag the missing source instead of fabricating it.

---

## 22. Content & Design Workflow

Content MUST be considered during:

```text
Discovery
↓
Specification
↓
Design
↓
Implementation
↓
Responsive Review
↓
Accessibility Review
↓
SEO Review
↓
Final Audit
```

Design SHOULD be evaluated with realistic content lengths, not only short placeholder text.

---

## 23. Content Testing

Where applicable, verify:

* Long text
* Short text
* Empty content
* Missing content
* Persian/RTL content
* Mixed Persian/Latin content
* Numbers
* Dates
* Currency
* Error messages
* Validation messages
* Mobile text wrapping
* Button labels
* Accessibility labels

Content MUST NOT create layout failures.

---

## 24. AI Development Rules

AI MUST NOT:

* Invent business facts
* Invent product specifications
* Invent prices
* Invent policies
* Invent legal requirements
* Use fake production content without marking it
* Fill interfaces with meaningless text
* Duplicate content unnecessarily
* Add SEO spam
* Publish unverified AI-generated high-impact content
* Expose private user-generated content
* Render unsafe HTML

---

## 25. Completion Gate

Content is complete when:

* Required content is identified
* Production vs placeholder content is clear
* Terminology is consistent
* UI content is responsive
* RTL/localization requirements are satisfied
* Accessibility requirements are satisfied
* SEO requirements are satisfied where applicable
* User-generated content is safely handled
* AI-generated content is appropriately validated
* Legal content has an authoritative source
* No critical content gap remains

Final status:

```text
COMPLETE
COMPLETE WITH WARNINGS
BLOCKED
```

---

## 26. Core Principle

> Content must serve the user, fit the interface, respect the product's truth, and never be invented merely to make the application look complete.
