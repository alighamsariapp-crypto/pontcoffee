
````md
# API RULES — PONT CAFE

Version: 1.0
Status: Active
Project: PONT CAFE Digital Menu

---

## 1. Purpose

این فایل قوانین استفاده از API در پروژه PONT CAFE را تعریف می‌کند.

API در این پروژه یک الزام برای همه بخش‌ها نیست.

معماری اصلی پروژه بر پایه:

- Laravel
- PHP 8.3+
- MySQL/MariaDB
- Blade
- Tailwind CSS
- Alpine.js در صورت نیاز

است.

صفحات اصلی منوی مشتری باید در صورت امکان مستقیماً توسط Laravel و Blade رندر شوند.

---

## 2. Source of Truth

مرجع اصلی پروژه:

`PROJECT_SPEC.md`

در صورت تعارض بین این فایل و `PROJECT_SPEC.md`، مشخصات پروژه اولویت دارد.

---

## 3. API Is Optional

برای هر قابلیت نباید به صورت خودکار API ساخته شود.

قبل از ساخت API باید مشخص شود که واقعاً به API نیاز است یا خیر.

API فقط زمانی ساخته شود که یکی از موارد زیر وجود داشته باشد:

- نیاز واقعی Frontend به داده مستقل
- نیاز به ارتباط با سیستم خارجی
- نیاز به AJAX/Asynchronous interaction واقعی
- نیاز احتمالی به مصرف داده توسط کلاینت دیگر
- نیاز به یک integration مشخص

برای صفحات ساده منو، API جداگانه ایجاد نشود.

---

## 4. Server Rendered Menu

صفحات عمومی منو باید ترجیحاً با Laravel + Blade پیاده‌سازی شوند.

نمونه:

```text
Request
   ↓
Laravel Route
   ↓
Controller
   ↓
Service
   ↓
Eloquent
   ↓
Blade View
````

نباید برای نمایش ساده دسته‌بندی یا محصول، API غیرضروری ایجاد شود.

---

## 5. Customer Menu Routes

مسیرهای اصلی مشتری باید مستقیماً توسط Laravel مدیریت شوند.

نمونه:

```text
/
 /menu/cafe
 /menu/cafe/hot-bar
 /menu/cafe/cold-bar
 /menu/cafe/dessert
 /menu/restaurant
 /menu/restaurant/breakfast
 /menu/restaurant/lunch
 /menu/restaurant/dinner
 /menu/product/{slug}
```

این مسیرها در حالت عادی نیازی به REST API جداگانه ندارند.

---

## 6. Admin

پنل مدیریت نیز در V1 می‌تواند با Laravel + Blade پیاده‌سازی شود.

CRUDهای مدیریت باید از طریق:

* Controllers
* Form Requests
* Services
* Eloquent Models
* Blade Views

انجام شوند.

برای عملیات ساده Admin، ساخت API جداگانه ممنوع است مگر اینکه نیاز واقعی وجود داشته باشد.

---

## 7. REST API

اگر API لازم شد، طراحی آن باید RESTful و استاندارد باشد.

اصول:

* استفاده صحیح از HTTP methods
* URLهای قابل فهم
* Response structure ثابت
* HTTP status code صحیح
* Validation
* Authorization
* Error handling
* Logging در موارد لازم

---

## 8. HTTP Methods

در صورت استفاده از API:

```text
GET     Read
POST    Create
PUT     Full Update
PATCH   Partial Update
DELETE  Delete
```

از استفاده اشتباه از HTTP methods خودداری شود.

---

## 9. API Versioning

در صورت ایجاد API عمومی یا قابل توسعه، نسخه‌بندی انجام شود.

نمونه:

```text
/api/v1/...
```

اما برای قابلیت‌های داخلی که صرفاً توسط Blade استفاده می‌شوند، API فقط به دلیل نسخه‌بندی ایجاد نشود.

---

## 10. Request Validation

تمام داده‌های ورودی API باید Validate شوند.

ترجیحاً از Laravel Form Request استفاده شود.

Validation نباید فقط در Frontend انجام شود.

Frontend validation می‌تواند برای UX وجود داشته باشد، اما امنیت و صحت داده باید در Server تضمین شود.

---

## 11. Authorization

Authentication و Authorization باید در Server انجام شود.

هیچ API نباید صرفاً بر اساس داده ارسال‌شده از Client به کاربر اجازه دسترسی بدهد.

برای Admin:

* احراز هویت
* بررسی Role
* بررسی Permission در صورت وجود

الزامی است.

---

## 12. Authentication

در PONT CAFE V1:

* Customer authentication وجود ندارد.
* Customer account وجود ندارد.
* Customer API authentication مورد نیاز نیست.

Admin authentication فقط برای بخش مدیریت مورد نیاز است.

---

## 13. Public Menu Data

داده‌هایی که برای مشتری نمایش داده می‌شوند باید فقط شامل اطلاعات مورد نیاز منو باشند.

اطلاعات داخلی مانند:

* Password
* Internal identifiers در صورت عدم نیاز
* Admin metadata
* Security data
* Internal notes

نباید به Client ارسال شوند.

---

## 14. Product API

اگر در آینده API برای محصولات لازم شد، فقط داده‌های مورد نیاز ارسال شود.

نمونه:

```json
{
  "id": 1,
  "slug": "product-slug",
  "name": "Product Name",
  "description": "Product description",
  "price": 120000,
  "image": "/storage/products/example.webp",
  "is_sold_out": false
}
```

ساختار واقعی باید با نیاز پروژه هماهنگ باشد.

---

## 15. Category API

اگر API دسته‌بندی ایجاد شد، فقط داده‌های لازم برای Navigation و Menu نمایش داده شوند.

داده‌های غیرضروری Database نباید expose شوند.

---

## 16. Localization

API در صورت استفاده باید با سیستم زبان پروژه سازگار باشد.

زبان‌های V1:

```text
fa
ar
en
```

Response باید با Locale معتبر درخواست هماهنگ باشد.

نباید Translationها به شکل غیرضروری و بدون نیاز به Client ارسال شوند.

---

## 17. RTL / LTR

API مسئول Layout نیست.

API فقط داده و metadata لازم را ارائه می‌کند.

تصمیم مربوط به:

* RTL
* LTR
* Typography
* Direction
* Layout

در لایه Presentation انجام می‌شود.

---

## 18. Availability

وضعیت محصول باید از منطق مرکزی پروژه دریافت شود.

وضعیت‌ها شامل:

```text
Available
Sold Out
Outside Service Hours
```

نباید هر Controller یا API منطق متفاوتی برای Availability داشته باشد.

منطق Availability باید در Service مرکزی قرار گیرد.

---

## 19. Error Response

در APIهای مورد استفاده، خطاها باید ساختار قابل پیش‌بینی داشته باشند.

نمونه:

```json
{
  "success": false,
  "message": "Validation failed.",
  "errors": {
    "name": [
      "The name field is required."
    ]
  }
}
```

پیام خطا نباید اطلاعات حساس سیستم را افشا کند.

---

## 20. HTTP Status Codes

از Status Code مناسب استفاده شود.

نمونه:

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Unprocessable Entity
429 Too Many Requests
500 Internal Server Error
```

از `200` برای تمام خطاها استفاده نشود.

---

## 21. Error Handling

Exceptionهای داخلی نباید مستقیماً به Client نمایش داده شوند.

ممنوع:

```text
SQL query
Database credentials
File paths
Stack traces
Environment variables
Internal server details
```

در Production پیام عمومی و امن ارسال شود.

---

## 22. Database Access

API نباید مستقیماً SQL را در Controller پخش کند.

ترجیح:

```text
Controller
    ↓
Service
    ↓
Eloquent
```

در Queryهای پیچیده، Repository فقط در صورت نیاز واقعی ایجاد شود.

Repository برای همه Modelها به صورت اجباری ساخته نشود.

---

## 23. Eloquent

استفاده از Eloquent باید مطابق معماری Laravel باشد.

از:

* Relationships
* Scopes
* Eager Loading
* Query Builder

در جای مناسب استفاده شود.

---

## 24. N+1 Prevention

API و Controllerها نباید باعث N+1 Query شوند.

برای Relations مورد نیاز از:

```php
with()
```

یا روش مناسب دیگر استفاده شود.

نمونه:

```php
Product::with([
    'translations',
    'images'
])->get();
```

---

## 25. Pagination

برای Endpointهایی که ممکن است حجم زیادی از داده برگردانند، Pagination استفاده شود.

برای لیست‌های کوچک و کنترل‌شده، Pagination اجباری نیست.

حدود منطقی باید متناسب با داده واقعی پروژه تعیین شود.

---

## 26. Filtering

اگر API برای لیست محصولات ایجاد شد، Filtering فقط برای نیاز واقعی اضافه شود.

نمونه:

```text
category
status
locale
search
```

فیلترهای غیرضروری ایجاد نشوند.

---

## 27. Sorting

Sorting باید محدود و کنترل‌شده باشد.

Client نباید بتواند نام ستون دلخواه Database را مستقیماً وارد Query کند.

فقط Sort fieldهای مجاز پذیرفته شوند.

---

## 28. Search

اگر Search API ایجاد شد:

* Input validation
* محدودیت طول
* Query امن
* جلوگیری از SQL injection
* Performance مناسب

الزامی است.

---

## 29. Rate Limiting

Endpointهای حساس Admin یا Endpointهای عمومی پرمصرف در صورت نیاز باید Rate Limit داشته باشند.

Rate limiting باید متناسب با کاربرد واقعی تعیین شود.

برای هر Endpoint بدون دلیل Rate Limit شدید اعمال نشود.

---

## 30. CORS

CORS فقط زمانی تنظیم شود که API توسط Origin دیگری مصرف شود.

در معماری معمول Blade + Laravel، CORS غیرضروری ایجاد نشود.

نباید به صورت پیش‌فرض:

```text
Access-Control-Allow-Origin: *
```

برای APIهای حساس فعال شود.

---

## 31. CSRF

برای درخواست‌های Web و Blade از محافظت CSRF استاندارد Laravel استفاده شود.

APIهایی که به Session/CSRF وابسته هستند باید طبق معماری Laravel تنظیم شوند.

CSRF نباید صرفاً به دلیل وجود API غیرفعال شود.

---

## 32. Mass Assignment

Modelها باید در برابر Mass Assignment محافظت شوند.

از:

```php
$fillable
```

یا:

```php
$guarded
```

به شکل صحیح استفاده شود.

---

## 33. Sensitive Data

API نباید اطلاعات حساس را expose کند.

موارد حساس شامل:

* Password
* Tokens
* Secrets
* Database credentials
* Internal server information
* Private admin data

است.

---

## 34. File Upload API

اگر در آینده Upload از طریق API انجام شد:

* MIME type validation
* File size validation
* Extension validation
* Secure filename
* Storage خارج از مسیر اجرای PHP در صورت نیاز
* Image processing
* Authorization

الزامی است.

برای تصاویر محصولات، فایل باید در Storage تعریف‌شده پروژه ذخیره شود.

---

## 35. Image Responses

API نباید تصاویر را Base64 داخل JSON قرار دهد مگر اینکه دلیل فنی مشخصی وجود داشته باشد.

ترجیح:

```text
image URL/path
```

تصاویر باید بهینه باشند.

فرمت ترجیحی پروژه:

```text
WebP
```

---

## 36. Transactions

عملیات چندمرحله‌ای Database که باید به صورت اتمیک انجام شوند، باید داخل Transaction انجام شوند.

نمونه:

```php
DB::transaction(function () {
    // database operations
});
```

---

## 37. API Documentation

اگر API قابل استفاده توسط Client یا سیستم دیگر ایجاد شد، Documentation باید به‌روز باشد.

Documentation باید حداقل شامل:

* Endpoint
* Method
* Authentication
* Parameters
* Request body
* Response
* Error responses

باشد.

OpenAPI/Swagger فقط در صورت نیاز واقعی پروژه اضافه شود.

---

## 38. Logging

خطاهای مهم API باید در Logging استاندارد Laravel ثبت شوند.

اطلاعات حساس نباید در Log نوشته شوند.

ممنوع:

```text
Passwords
Tokens
Secrets
Full sensitive request bodies
```

---

## 39. Performance

API نباید Queryهای غیرضروری ایجاد کند.

موارد مهم:

* Eager Loading
* محدود کردن Columns
* Pagination در داده‌های بزرگ
* Cache در موارد مناسب
* جلوگیری از N+1
* جلوگیری از Responseهای بیش از حد بزرگ

---

## 40. Caching

Cache فقط زمانی استفاده شود که واقعاً به Performance کمک کند.

داده‌های مناسب برای Cache:

* Categories
* Menu configuration
* Service hours
* Public menu data در صورت نیاز

بعد از تغییر داده، Cache مربوطه باید invalidate شود.

---

## 41. No Fake API

هیچ API نباید با:

* Static arrays
* Fake JSON
* Mock products
* Hardcoded orders
* Random generated data

به عنوان Production implementation ساخته شود.

داده واقعی باید از Database بیاید.

---

## 42. No Unnecessary API Layer

این پروژه نباید صرفاً برای رعایت یک الگوی معماری عمومی، بین Blade و Database یک API غیرضروری ایجاد کند.

نمونه نامناسب:

```text
Blade
  ↓
API
  ↓
Controller
  ↓
Service
  ↓
Database
```

برای صفحات ساده منو این ساختار غیرضروری است.

ساختار ترجیحی:

```text
Blade
  ↓
Controller
  ↓
Service
  ↓
Database
```

---

## 43. Scope Protection

API نباید قابلیت‌هایی خارج از Scope پروژه ایجاد کند.

V1 شامل:

* Menu
* Categories
* Products
* Product details
* Languages
* Availability
* Service hours
* Admin management

است.

موارد زیر خارج از Scope هستند:

* Online ordering
* Cart
* Checkout
* Payment
* Delivery
* Customer accounts
* Reservations
* Ratings
* Favorites
* AI assistant
* Push notifications
* Crypto wallet
* Complex analytics

---

## 44. Testing

APIهای واقعی باید تست شوند.

حداقل موارد:

* Successful response
* Validation failure
* Unauthorized request
* Forbidden request
* Not found
* Database integration
* Localization
* Availability
* Security

در صورت نبود API، برای آن تست API ایجاد نشود.

---

## 45. Feature Completion

یک Feature دارای API فقط زمانی Complete محسوب می‌شود که:

* Route درست باشد
* Validation انجام شود
* Authorization درست باشد
* Database واقعی استفاده شود
* Error handling وجود داشته باشد
* Security بررسی شده باشد
* Tests مرتبط وجود داشته باشند
* Response contract پایدار باشد

---

## 46. Production Rule

هیچ API نباید فقط برای Demo ساخته شود.

هر API که وارد Production می‌شود باید:

* واقعی
* قابل نگهداری
* امن
* متصل به Database واقعی
* مستند در صورت نیاز
* تست‌شده
* متناسب با Scope

باشد.

---

## 47. Final Rule

اصل اصلی API در PONT CAFE:

> API only when needed.

Laravel + Blade معماری اصلی V1 است.

برای قابلیت‌هایی که مستقیماً با Server-rendered Blade قابل پیاده‌سازی هستند، API جداگانه ساخته نشود.

هر API جدید باید قبل از Implementation دارای دلیل فنی مشخص و قابل دفاع باشد.

```

**همین فایل را جایگزین `API_RULES.md` کن.**

بعد از اینکه گفتی **انجام شد**، مستقیم می‌ریم سراغ `CODING_RULES.md`.
```
