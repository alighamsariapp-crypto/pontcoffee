
# DEPLOYMENT RULES — PONT CAFE

Version: 1.0
Status: Active
Project: PONT CAFE Digital Menu

---

## 1. Purpose

This document defines the deployment standards for PONT CAFE.

The deployment must be:

- Production-ready
- Simple
- Low-cost
- Reliable
- Secure
- Compatible with the selected hosting environment
- Easy to maintain
- Appropriate for a small digital menu application

---

## 2. Source of Truth

`PROJECT_SPEC.md` is the primary source of truth for deployment decisions.

If this document conflicts with `PROJECT_SPEC.md`, the project specification takes priority.

---

## 3. Production Stack

The production application uses:

- Laravel
- PHP 8.3+
- MySQL or MariaDB
- Blade
- Tailwind CSS
- Vite-built assets
- Linux hosting

The production application does not require Node.js as a runtime service.

Node.js/npm may be used during development or asset compilation.

---

## 4. Hosting Strategy

PONT CAFE should use a Linux hosting environment that supports:

- PHP 8.3+
- Laravel
- MySQL/MariaDB
- HTTPS
- Cron jobs when required
- File storage
- PHP extensions required by Laravel

An Iran-based hosting provider is preferred for the production deployment when available and technically suitable.

The application must not depend on foreign cloud infrastructure for core operation unless explicitly approved.

---

## 5. No Firebase Dependency

Firebase is not part of the production architecture.

Do not introduce dependencies on:

- Firebase Authentication
- Firestore
- Firebase Storage
- Firebase Hosting
- Firebase Functions

The application must remain fully functional using the Laravel + MySQL architecture.

---

## 6. No External Database Dependency

The production database must be hosted within the selected infrastructure.

Do not make the application dependent on an external cloud database for normal operation.

Primary application data must be stored in MySQL/MariaDB.

---

## 7. No External Image Storage Dependency

Product images should be stored on the selected hosting infrastructure.

Do not require:

- Firebase Storage
- Cloudinary
- S3
- External image CDN

for normal V1 operation.

External image services may only be introduced later if there is a clear requirement and approval.

---

## 8. Laravel Document Root

The web server must point to Laravel's:

```text
public/
````

directory.

The application root must not be exposed directly as the public document root.

Example:

```text
/home/account/project/
    app/
    bootstrap/
    config/
    database/
    resources/
    routes/
    storage/
    vendor/
    public/
```

The web server should serve:

```text
/home/account/project/public
```

---

## 9. Environment Configuration

Production configuration must be provided through environment variables.

Never commit production secrets to Git.

Important environment values include:

```text
APP_ENV
APP_KEY
APP_DEBUG
APP_URL

DB_CONNECTION
DB_HOST
DB_PORT
DB_DATABASE
DB_USERNAME
DB_PASSWORD
```

---

## 10. APP_ENV

Production must use:

```env
APP_ENV=production
```

Do not deploy with:

```env
APP_ENV=local
```

---

## 11. APP_DEBUG

Production must use:

```env
APP_DEBUG=false
```

Never expose Laravel debug pages to public users.

---

## 12. Application Key

Production must have a valid Laravel `APP_KEY`.

Do not expose the application key.

Do not randomly regenerate the production application key during normal deployments.

Changing the production key can invalidate encrypted application data.

---

## 13. Database Configuration

The production application must use the real MySQL/MariaDB database.

Example:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=pont_cafe
DB_USERNAME=...
DB_PASSWORD=...
```

Actual credentials must remain private.

---

## 14. Database Migrations

Database changes must be implemented through Laravel migrations.

Before production deployment:

1. Review pending migrations.
2. Verify compatibility.
3. Back up the database when appropriate.
4. Run migrations safely.

Do not manually change the production schema without documenting the corresponding migration.

---

## 15. Database Backups

Production database backups are required.

Backups should be:

* Automated when the hosting provider supports it
* Tested periodically
* Retained for an appropriate period
* Protected from public access

A backup that has never been tested should not be considered fully reliable.

---

## 16. File Backups

Important application data includes:

* Database
* Product images
* Uploaded media
* Required configuration

These should be included in the hosting provider's backup strategy where possible.

---

## 17. Storage Permissions

Laravel directories that require write access must be writable by the web server.

Typically:

```text
storage/
bootstrap/cache/
```

Do not make the entire project directory publicly writable.

Avoid unsafe permissions such as:

```text
777
```

unless there is an exceptional and documented hosting requirement.

---

## 18. Public Files

Only files intended for public access should exist under:

```text
public/
```

Do not expose:

* `.env`
* Database backups
* Private documents
* Source configuration
* Internal logs
* Credentials
* Application source code

---

## 19. Storage Links

If Laravel public storage uses the standard symbolic link approach, ensure the production environment supports:

```bash
php artisan storage:link
```

If symbolic links are not supported by the hosting environment, use a deployment-compatible storage strategy that keeps private files protected.

---

## 20. Build Process

Frontend assets should be built before production deployment.

Typical development/build process:

```bash
npm install
npm run build
```

The resulting assets should be deployed with the application.

Node.js does not need to remain running after the build.

---

## 21. Production Runtime

PONT CAFE is primarily a server-rendered Laravel application.

Do not require a persistent Node.js server for normal operation.

The production request flow should be:

```text
Browser
   ↓
Web Server
   ↓
Laravel
   ↓
MySQL
   ↓
Blade Response
```

---

## 22. Composer Dependencies

Production dependencies must be installed using Composer.

Use the production-oriented installation process:

```bash
composer install --no-dev --optimize-autoloader
```

Do not deploy unnecessary development dependencies.

---

## 23. Laravel Optimization

After deployment, apply appropriate Laravel production optimizations.

Examples:

```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

Only cache configuration/routes when the application structure is compatible with those caches.

---

## 24. Cache

The initial production deployment should use a simple supported cache driver.

File or database cache is acceptable.

Redis is not required for V1.

Do not introduce Redis merely because it is commonly used in larger Laravel applications.

---

## 25. Queue Workers

PONT CAFE V1 should not require background queue workers unless a real feature requires them.

Do not introduce:

* Supervisor
* Redis queues
* Horizon

without a concrete requirement.

---

## 26. Scheduler

Laravel Scheduler should only be configured if the application actually requires scheduled tasks.

If required, configure the hosting provider's cron system according to its supported method.

Do not add cron jobs that serve no purpose.

---

## 27. Cron

If Laravel Scheduler is used, the production server should execute the Laravel scheduler at the required interval.

Typical Laravel configuration:

```text
* * * * * php /path/to/project/artisan schedule:run
```

The exact command must match the hosting environment.

---

## 28. HTTPS

Production must use HTTPS.

HTTP requests should redirect to HTTPS when supported by the hosting environment.

Do not transmit authentication credentials or sensitive data over plain HTTP.

---

## 29. SSL

The production domain must have a valid SSL certificate.

The certificate must be:

* Valid
* Not expired
* Correctly configured
* Trusted by modern browsers

---

## 30. Domain Configuration

The production domain must point to the correct hosting environment.

The web server document root must point to Laravel's `public/` directory.

Do not expose the Laravel project root through the domain.

---

## 31. Error Handling

Production errors must not expose internal technical details.

Users should receive an appropriate application error page.

Logs should contain the technical details needed for troubleshooting.

---

## 32. Logging

Laravel logging must be enabled in production.

Logs must not contain:

* Passwords
* API secrets
* Database passwords
* Authentication tokens
* Other sensitive information

Logs should be rotated or managed according to the hosting environment.

---

## 33. Deployment Safety

Before deploying a significant change:

1. Verify the code.
2. Run relevant tests.
3. Review database changes.
4. Back up important production data.
5. Deploy.
6. Run required migrations.
7. Clear/rebuild appropriate caches.
8. Verify the application.

---

## 34. Zero-Downtime Expectations

Full zero-downtime infrastructure is not required for PONT CAFE V1.

The priority is:

* Correct deployment
* Short maintenance windows
* Data safety
* Reliable recovery

Do not introduce complex deployment infrastructure solely to achieve zero downtime.

---

## 35. Git Deployment

Git may be used as the source-control mechanism.

Production deployment may use:

* Git-based deployment
* Hosting control panel deployment
* Manual file deployment
* CI/CD when supported

The chosen method must match the actual hosting capabilities.

---

## 36. CI/CD

CI/CD is optional for V1.

Do not require GitHub Actions or another CI/CD system if the hosting environment does not support automatic deployment.

If CI/CD is introduced, it must:

* Run tests
* Build assets
* Protect secrets
* Avoid exposing credentials
* Deploy predictable versions

---

## 37. Shared Hosting Compatibility

The application must remain compatible with standard Linux shared/cloud hosting.

Avoid dependencies that require:

* Docker
* Kubernetes
* Long-running Node processes
* Complex server daemons
* Redis servers
* Elasticsearch
* Specialized infrastructure

unless explicitly required.

---

## 38. PHP Extensions

Before deployment, verify that the hosting environment provides the PHP extensions required by the selected Laravel version and application dependencies.

Do not assume all extensions are available.

---

## 39. PHP Version

Production PHP must meet the version required by the selected Laravel release and project specification.

The project target is:

```text
PHP 8.3+
```

Do not silently deploy to an unsupported PHP version.

---

## 40. Database Version

The production MySQL/MariaDB version must be compatible with:

* Laravel
* PHP
* Application migrations
* Eloquent queries

Verify compatibility before deployment.

---

## 41. Asset URLs

Production asset URLs must be generated correctly through Laravel/Vite.

Do not hardcode development URLs such as:

```text
localhost
127.0.0.1
```

into production assets or configuration.

---

## 42. APP_URL

Production `APP_URL` must match the actual application URL.

Example:

```env
APP_URL=https://example.com
```

The actual production domain must be configured privately in the deployment environment.

---

## 43. Environment Separation

Development and production environments must remain separate.

Never copy:

* Development database credentials
* Development secrets
* Debug configuration
* Local `.env`
* Test data

into production.

---

## 44. No Demo Data in Production

Production must not contain fake demonstration data unless that data is intentionally approved as actual initial content.

Menu products and categories must represent real PONT CAFE data.

---

## 45. Production Database Seeding

Seeders may be used for controlled initial configuration.

Do not run destructive seeders against production.

Never use commands or scripts that reset/drop production data unless explicitly intended and safely controlled.

---

## 46. Admin Access

The Admin area must be protected.

Production deployment must verify:

* Admin authentication
* Authorization
* Password security
* HTTPS
* Session security

Do not expose Admin functionality publicly without authentication.

---

## 47. Security Headers

Where supported by the application/server configuration, use appropriate security headers.

At minimum consider:

* HTTPS enforcement
* Content-Type protection
* Frame protection
* Referrer policy

Security headers must not break the actual application.

---

## 48. Maintenance Mode

Laravel maintenance mode may be used for deployments requiring temporary downtime.

Example:

```bash
php artisan down
```

After deployment:

```bash
php artisan up
```

Do not leave the application in maintenance mode unintentionally.

---

## 49. Deployment Verification

After every production deployment, verify at minimum:

### Customer

* Homepage loads
* Cafe navigation works
* Restaurant navigation works
* Categories load
* Products load
* Product detail works
* Language switching works
* RTL/LTR works
* Sold-out state works
* Service-hour state works
* Images load

### Admin

* Admin login works
* Dashboard loads
* Category management works
* Product management works
* Image upload works
* Service hours work
* Settings work where implemented

---

## 50. Database Verification

After deployment verify:

* Database connection
* Migrations
* Categories
* Products
* Translations
* Images
* Service hours
* Admin users

No production feature should silently fall back to fake or in-memory data.

---

## 51. Performance Verification

After deployment check:

* Initial page load
* Image loading
* Database query count where relevant
* JavaScript bundle size
* CSS bundle size
* Cache behavior
* Mobile performance

The menu should remain fast on mobile connections.

---

## 52. Mobile Verification

Verify the production site at minimum at:

```text
320px
360px
375px
390px
414px
```

Also verify desktop widths.

No horizontal scrolling should appear because of implementation errors.

---

## 53. Rollback

A deployment process should have a recovery strategy.

If a deployment introduces a critical failure:

1. Identify the failed change.
2. Restore the previous working application version when possible.
3. Restore the database only when necessary.
4. Preserve data created after deployment when possible.
5. Verify the restored application.

Database rollback must be handled carefully because application code and schema must remain compatible.

---

## 54. Monitoring

PONT CAFE V1 does not require complex observability infrastructure.

At minimum, monitor:

* Application availability
* Laravel errors
* Database errors
* Storage failures
* SSL expiration
* Hosting resource usage

Use the hosting provider's monitoring where sufficient.

---

## 55. Cost Control

Deployment should remain appropriate for a small menu application.

Avoid unnecessary infrastructure such as:

* Kubernetes
* Multiple application servers
* Redis clusters
* Dedicated queues
* External databases
* External storage
* Complex monitoring platforms

unless actual traffic or requirements justify them.

---

## 56. Disaster Recovery

The deployment environment should provide a practical recovery path.

Required priorities:

1. Database backup
2. Media backup
3. Source code in Git
4. Environment configuration stored securely
5. Ability to redeploy Laravel
6. Ability to restore database and media

---

## 57. No Infrastructure Lock-In

The application should remain portable.

Core functionality should not depend on a single proprietary cloud platform.

The project should be deployable to another compatible Linux + PHP + MySQL environment with reasonable effort.

---

## 58. Deployment Documentation

The project should maintain a concise deployment procedure covering:

* Server requirements
* PHP version
* Database setup
* Environment variables
* Composer installation
* Asset build
* Migrations
* Storage setup
* Cache setup
* Domain/SSL configuration
* Verification

Do not create unnecessarily complex deployment documentation.

---

## 59. Final Production Checklist

Before declaring production deployment complete:

```text
[ ] PHP version verified
[ ] Database created
[ ] Production .env configured
[ ] APP_KEY configured
[ ] APP_DEBUG=false
[ ] APP_ENV=production
[ ] APP_URL configured
[ ] Composer dependencies installed
[ ] Frontend assets built
[ ] Laravel public/ configured as document root
[ ] Storage configured
[ ] Migrations completed
[ ] Database backup available
[ ] HTTPS active
[ ] Admin authentication verified
[ ] Customer menu verified
[ ] Languages verified
[ ] RTL/LTR verified
[ ] Images verified
[ ] Availability states verified
[ ] Error handling verified
[ ] Mobile layouts verified
[ ] Production logs verified
[ ] No fake production data
```

---

## 60. Final Rule

The deployment principle for PONT CAFE is:

> Keep production simple, secure, portable, reliable, and appropriate for the real size of the project.

Use Laravel + PHP + MySQL on compatible Linux hosting.

Do not introduce unnecessary cloud services or infrastructure.

The application must remain operational without Firebase or another foreign cloud platform being required for its core functionality.

Every deployment must protect production data, application secrets, user access, and the ability to recover from failure.

```


بعدی می‌ریم سراغ **`PERFORMANCE_RULES.md`**.
```
