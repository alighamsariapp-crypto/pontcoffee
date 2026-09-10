DATABASE RULES — PONT CAFE

1. PURPOSE

Mandatory database rules for PONT CAFE Digital Menu.

Production database:

MySQL or MariaDB

Laravel Eloquent / Query Builder

Laravel migrations

Linux hosting

These rules cover data modeling, relationships, validation, queries, indexes, transactions, security, migrations, integrity, performance, backups, and testing.

2. CORE PRINCIPLE

The database is the authoritative source of persistent application data.

Production flow:

UI
↓
Laravel Controller / Service
↓
Validation
↓
Authorization
↓
Eloquent / Query Builder
↓
MySQL / MariaDB
↓
Persistence
↓
Blade Response

A feature is NOT complete when only its UI or mock data exists.

3. NO MOCK DATABASE IN PRODUCTION

Prohibited in production:

In-memory arrays as persistent storage

Hardcoded products/categories as the source of truth

Fake CRUD

Fake persistence

Fake success responses

Browser-only authoritative storage

Mocks, factories, and fixtures are allowed only for tests/development.

4. DATABASE SOURCE OF TRUTH

PONT CAFE persistent data MUST have one authoritative source in MySQL/MariaDB.

users                  → Users
categories             → Categories
category_translations  → Localized categories
products               → Products
product_translations   → Localized products
product_images         → Product images
service_hours          → Service hours
settings               → Settings
menu_settings          → Menu settings

Caching must never replace the database as the source of truth.

5. DATABASE TECHNOLOGY

PONT CAFE V1 uses:

Laravel
PHP 8.3+
MySQL / MariaDB
Laravel Eloquent
Laravel Migrations
Blade

Firebase and Cloud Firestore are NOT part of the PONT CAFE V1 database architecture.

Do not introduce another database technology without an approved project specification change.

6. APPROVED DATABASE ENTITIES

Primary entities:

users

categories

category_translations

products

product_translations

product_images

service_hours

settings

menu_settings

Do not add unrelated commerce entities.

PONT CAFE V1 does NOT require:

orders

order_items

payments

carts

coupons

delivery

customer accounts

inventory management

unless the project specification is explicitly changed.

7. IDENTIFIERS

Every persistent entity MUST have a stable unique primary key.

IDs MUST NOT depend on display names.

Slugs are for readable URLs/routing and are not a replacement for primary keys.

8. DATABASE NAMING

Database tables and columns MUST use snake_case.

Examples:

product_id
category_id
created_at
updated_at
is_active
is_sold_out
sort_order

Do not mix naming conventions.

9. PRIMARY AND FOREIGN KEYS

Every table MUST have an intentional primary key.

Relationships MUST use proper foreign keys where appropriate.

Examples:

categories.id
    ↓
products.category_id

products.id
    ↓
product_translations.product_id

products.id
    ↓
product_images.product_id

Foreign-key delete/update behavior MUST be intentional.

10. ELOQUENT RELATIONSHIPS

Laravel models MUST accurately represent database relationships.

Category
├── translations
├── products
└── serviceHours

Product
├── category
├── translations
└── images

Do not create undocumented relationships through arbitrary fields.

11. MIGRATIONS

Every production schema change MUST be represented by a Laravel migration.

Prohibited:

Manual schema changes without a migration

Silent schema changes

Destructive changes without review

Migrations that do not reproduce the intended schema

Migrations MUST work on a fresh database.

12. SEEDERS AND FACTORIES

Seeders may create required initial categories, settings, admin accounts, or controlled development menu data.

Factories are for tests/development.

Production functionality MUST NOT depend on fake seed data.

13. VALIDATION

All admin input MUST be validated before persistence.

Validate as applicable:

IDs

Names

Slugs

Prices

Booleans

Status values

Translation data

Image uploads/metadata

Service hours

Sort order

Use Laravel Form Request classes where appropriate.

14. AUTHORIZATION

Authorization MUST be enforced server-side.

Hiding an admin control is NOT security.

Create, edit, delete, publish/unpublish, price, availability, image, and settings changes MUST be authorized by Laravel before database writes.

15. CATEGORIES

Approved PONT CAFE structure:

Cafe
├── Hot Bar
├── Cold Bar
└── Dessert

Restaurant
├── Breakfast
├── Lunch
└── Dinner

Do not introduce arbitrary category levels without an approved specification change.

16. CATEGORY TRANSLATIONS

Supported locales:

fa
ar
en

Localized category names belong in category_translations.

When one translation per language is intended, enforce:

UNIQUE(category_id, locale)

Do not create separate category records only because the language changes.

17. PRODUCTS

A product record contains authoritative product data defined by PROJECT_SPEC.md.

Typical fields:

id
category_id
slug
price
is_active
is_sold_out
sort_order
created_at
updated_at

Do not add ordering, payment, or inventory fields unless explicitly required by a future approved scope.

18. PRODUCT TRANSLATIONS

Localized product content belongs in product_translations.

Supported locales:

fa
ar
en

Typical fields:

name
description
ingredients
allergens

When one translation per language is intended, enforce:

UNIQUE(product_id, locale)

19. PRODUCT IMAGES

Images MUST be stored on the configured project hosting/storage system, not as MySQL binary data unless explicitly approved.

Database metadata may include:

product_id
path
alt_text
sort_order
is_primary

Uploads MUST be validated server-side.

Images SHOULD be optimized for web delivery, preferably WebP where supported.

20. SERVICE HOURS

Service-hour data belongs in service_hours.

Availability MUST use authoritative database settings and server-side time logic.

Do not rely on the browser clock for authoritative availability decisions.

21. PRODUCT AVAILABILITY

The application MUST distinguish:

Active
Sold Out
Outside Service Hours

These are separate states.

is_sold_out MUST NOT represent service-hour closure.

Availability logic SHOULD be centralized, for example in AvailabilityService.

22. SERVER-AUTHORITATIVE DATA

The server/database is authoritative for:

Product price

Product status

Category status

Sort order

Translations

Image metadata

Service hours

Admin roles

Menu settings

The browser MUST NOT establish persistent truth.

23. UNIQUE CONSTRAINTS

Values that must be unique SHOULD be protected by database constraints.

Likely examples:

categories.slug
products.slug
category_translations(category_id, locale)
product_translations(product_id, locale)

Application validation does not replace database constraints.

24. INDEXES

Indexes MUST be based on actual query patterns.

Likely useful indexes:

categories.parent_id
categories.slug

products.category_id
products.slug
products.is_active
products.sort_order

category_translations.category_id
category_translations.locale

product_translations.product_id
product_translations.locale

product_images.product_id

Do not create indexes blindly.

25. QUERY DESIGN

Queries MUST retrieve only data required by the operation.

Public menu:

Requested category
↓
Required products
↓
Required translations/images

Do not load the entire catalog on every request without a real reason.

Database filtering SHOULD be used instead of unnecessary browser-side filtering.

26. N+1 PREVENTION

Avoid one database query per displayed product.

Use intentional Eloquent eager loading such as:

with(...)

Verify collection queries involving categories, translations, and images.

27. PAGINATION

Admin lists that can grow SHOULD use pagination.

The current public menu is intentionally small, so pagination is not mandatory for every customer-facing list.

Do not add pagination solely for architectural complexity.

28. TRANSACTIONS

Use Laravel database transactions when multiple related writes must succeed or fail together.

Example:

Product
+
Translations
+
Image metadata

when the operation is intentionally atomic.

Do not use transactions unnecessarily for simple reads.

29. DELETE STRATEGY

Deletion behavior MUST be intentional.

For owned records such as:

product_translations
product_images

define whether they are:

Cascade deleted

Deleted by application logic

Retained

Soft deleted

Do not rely on undocumented behavior.

30. SOFT DELETE

Soft delete is NOT required by default for PONT CAFE V1.

For menu visibility, prefer:

is_active

when the record should remain in the database.

Use Laravel SoftDeletes only when there is a real historical/recovery requirement.

31. CACHE

Caching is optional.

The database remains authoritative.

If menu data is cached:

Cache keys MUST be predictable.

Invalidation MUST be defined.

Admin changes MUST invalidate affected cache.

Acceptable stale-data behavior MUST be understood.

File/database cache is sufficient initially.

Redis is NOT required for this project.

32. FRONTEND DATABASE BOUNDARY

The browser MUST NOT connect directly to MySQL/MariaDB.

Correct architecture:

Browser
↓
Laravel
↓
Eloquent
↓
MySQL / MariaDB

33. API BOUNDARY

PONT CAFE does NOT require an API for every page.

Server-rendered Blade pages may obtain data through Laravel controllers/services.

Create an API only when a real integration or interaction requires it.

Do not create unnecessary REST endpoints for a simple menu.

34. SQL INJECTION PROTECTION

Use:

Eloquent

Laravel Query Builder

Parameterized queries

Never concatenate untrusted input directly into SQL.

Raw SQL is allowed only when necessary and MUST use parameter binding.

35. MASS ASSIGNMENT

Laravel mass assignment MUST be controlled.

Use appropriate:

$fillable

or:

$guarded

and always pass validated data.

Never pass arbitrary request payloads directly into model updates.

36. DATABASE SECURITY

Database credentials MUST come from environment configuration.

Never commit:

DB_PASSWORD
DB credentials
application secrets
private keys

to GitHub.

Production database access should use the least privilege supported by the hosting environment.

37. DATABASE ERRORS

Production responses MUST NOT expose:

SQL queries

Stack traces

Database credentials

Internal schema details

Connection details

Database errors should be logged securely and converted into appropriate application error states.

38. BACKUPS

Production database backups MUST be part of the hosting/deployment strategy.

Define:

Backup frequency

Retention

Restoration procedure

A backup should be considered reliable only when restoration can be verified.

39. PERFORMANCE

PONT CAFE has a small menu and does NOT require premature database infrastructure.

Do NOT introduce:

Database sharding

Read replicas

Redis clusters

Complex event-driven storage

Unnecessary microservices

Priorities:

Correct schema

Proper indexes

Targeted queries

N+1 prevention

Appropriate caching

Simple maintainable architecture

40. TESTING

Database-related features MUST be tested through the real Laravel database layer.

Tests should cover, where applicable:

Migrations

Relationships

Validation

Authorization

CRUD persistence

Translation persistence

Image metadata

Category/product filtering

Availability

Service hours

Unique constraints

A test is NOT valid merely because a mock array changed.

41. PRODUCTION DATA INTEGRITY

Before a database feature is complete, verify:

Migration
↓
Schema
↓
Model
↓
Relationship
↓
Validation
↓
Authorization
↓
Persistence
↓
Read-back
↓
Blade UI
↓
Tests

All relevant layers MUST operate against the real MySQL/MariaDB implementation.

42. SCOPE PROTECTION

PONT CAFE V1 is a digital menu, not an ordering platform.

Do NOT add database entities for:

Orders

Cart

Checkout

Payments

Delivery

Reservations

Customer accounts

Ratings

Favorites

AI assistant

Push notifications

Crypto wallets

Firebase

Firestore

Required external cloud database

Any future feature requires an explicit project specification change before database implementation.

43. SOURCE OF TRUTH

When database implementation rules conflict with project-specific requirements:

AGENTS.md
↓
PROJECT_SPEC.md
↓
DATABASE_RULES.md
↓
Implementation

PROJECT_SPEC.md is the project-specific source of truth.

Changes to the approved database technol
