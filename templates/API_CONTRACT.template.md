# API Contract

- ID: `API-000`
- Feature: `[FEATURE_ID]`
- Status: `DRAFT / APPROVED`

## Endpoint

- Method: `[GET/POST/PATCH/DELETE]`
- Path: `/api/v1/[resource]`
- Purpose: `[PURPOSE]`
- Authentication: `[REQUIRED/N/A]`
- Authorization: `[PERMISSION_OR_N/A]`

## Request

### Path/query parameters

`[PARAMETERS]`

### Body

```json
{}
```

### Validation

`[VALIDATION_RULES]`

## Response

- Success status: `[STATUS]`
- Response schema: `[SCHEMA]`

```json
{}
```

## Errors

| Status | Code | Meaning | Recovery |
|---|---|---|---|
| 400 | `[CODE]` | `[MEANING]` | `[RECOVERY]` |

## Safety

- Rate limit: `[LIMIT]`
- Idempotency: `[REQUIRED/N/A]`
- Side effects: `[SIDE_EFFECTS]`
- Sensitive fields excluded: `[FIELDS]`
- Tests: `[TESTS]`
