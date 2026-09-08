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

## State machine and gate rules

The state machine uses `LOCKED`, `READY`, `IN_PROGRESS`, `PASS`, `PASS_WITH_WARNINGS`, and `BLOCKED`.

An **Entry Gate** starts work. It checks only that the previous Phase is `PASS` or `PASS_WITH_WARNINGS`, `current_phase` points to that previous Phase, the target Phase is `LOCKED` or `READY`, and Feature dependencies are complete. It does not require the target to be `PASS` yet.

```bash
python3 scripts/project_gate.py --enter-phase 03
python3 scripts/project_gate.py --enter-phase 03 --apply
python3 scripts/project_gate.py --enter-feature F-003
```

A **Completion Gate** ends work. A Phase must have a passing status, a report, no blockers, all declared evidence, and all required Features complete. A Feature must have a passing status, its specification/report/audit artifacts, passing declared checks, and a passing audit.

```bash
python3 scripts/project_gate.py --check-phase 03
python3 scripts/project_gate.py --check-feature F-003
```

`current_phase` is authoritative: it prevents entering or completing a Phase that is not the active Phase. After a Phase completion, update `current_phase` to the next Phase and set that next Phase to `READY`.

`IN_PROGRESS`, `NOT_RUN`, `WARN`, `BLOCKED`, and missing values never count as `PASS`.

## Commands

The old aliases `--phase` and `--feature` remain available as completion checks.

The pre-commit hook always runs the structural Framework check. In a generated project it runs an explicit completion gate when `WEBTOW_GATE_TARGET` is supplied:

```bash
WEBTOW_GATE_TARGET=phase:03 git commit
WEBTOW_GATE_TARGET=feature:F-003 git commit
```

The command is intentionally separate from `framework_check.py`: one checks the framework repository, the other gates a real project.
