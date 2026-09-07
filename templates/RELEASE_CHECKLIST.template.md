# Release Checklist

- Version/commit: `[VERSION]`
- Environment: `[STAGING/PRODUCTION]`
- Release owner: `[OWNER]`

## Scope

- [ ] Included features are listed
- [ ] Out-of-scope changes are excluded
- [ ] Database/API compatibility is checked

## Verification

- [ ] Type check
- [ ] Lint
- [ ] Unit/integration tests
- [ ] E2E critical flows
- [ ] Security checks
- [ ] Accessibility review
- [ ] SEO review where applicable
- [ ] Performance review
- [ ] Production build

## Deployment

- [ ] Correct environment selected
- [ ] Secrets verified
- [ ] Migrations reviewed
- [ ] Deployment completed
- [ ] Health check passed
- [ ] Smoke test passed
- [ ] Monitoring checked
- [ ] Rollback path confirmed

## Result

- Status: `PASS / PASS WITH WARNINGS / BLOCKED`
- Remaining issues: `[ISSUES]`
