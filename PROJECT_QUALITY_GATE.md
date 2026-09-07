# Project Quality Gate

`framework_check.py` validates this reusable framework. It does not claim that an application is correct. Generated projects must add a `.webtow/` state directory and run `scripts/project_gate.py` for Phase and Feature progression.

## Required project state

Copy the templates under `templates/project-state/` into the generated project:

```text
.webtow/
├── phase-status.json
├── phases/PHASE_XX_REPORT.md
└── features/F-000/
    ├── status.json
    ├── FEATURE_SPEC.md
    ├── PHASE_REPORT.md
    └── AUDIT.md
```

A Feature may declare `API_CONTRACT.md`, `DATA_MODEL.md`, or other artifacts in `required_artifacts` when its behavior needs them. This avoids forcing irrelevant files while still making the required evidence machine-checkable.

## Gate rules

A Phase cannot pass while any previous Phase is not `PASS`. A Phase must have a `PASS` status, a report, no blockers, and all declared evidence files. A Feature must have a `PASS` status, belong to a passing Phase, include its declared artifacts, pass every declared check, and have an audit with `PASS` status.

`IN_PROGRESS`, `NOT_RUN`, `WARN`, `BLOCKED`, and missing values never count as `PASS`.

## Commands

```bash
python3 scripts/project_gate.py --phase 03
python3 scripts/project_gate.py --feature F-003
```

The command is intentionally separate from `framework_check.py`: one checks the framework repository, the other gates a real project.
