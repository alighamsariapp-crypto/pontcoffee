# Data Model

- Feature: `[FEATURE_ID]`
- Storage: `[FIRESTORE/SQL/OTHER]`
- Status: `DRAFT / APPROVED`

## Entity / collection

- Name: `[NAME]`
- Purpose: `[PURPOSE]`
- Owner: `[USER_OR_SYSTEM]`
- Retention: `[RETENTION]`

| Field | Type | Required | Client writable | Sensitive | Validation |
|---|---|---:|---:|---:|---|
| `id` | `[TYPE]` | yes | no | no | `[RULE]` |

## Access patterns

| Operation | Actor | Query/filter | Authorization | Index |
|---|---|---|---|---|
| Read | `[ACTOR]` | `[QUERY]` | `[RULE]` | `[INDEX]` |

## Integrity and lifecycle

- Transaction requirements: `[REQUIREMENTS]`
- Idempotency: `[REQUIREMENTS]`
- Migration plan: `[LINK_OR_N/A]`
- Backup/recovery: `[REQUIREMENTS]`
- Security Rules/tests: `[LINK]`
