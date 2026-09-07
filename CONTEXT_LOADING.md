# Context Loading Strategy

A free account should not send the entire framework to the AI assistant for every request. The framework is intentionally loaded progressively.

## The four levels

| Level | When | What to load |
|---|---|---|
| Bootstrap | Start of a new session | `AGENTS.md`, `config/route-map.json`, and the current project status |
| Phase pack | Start or continuation of a Phase | The four or five files listed by the phase router |
| Feature overlay | Only for the active Feature | One feature route and its two or three Skills |
| Deep rule | Only after a risk is identified | The specific security, Firebase, privacy, SEO, performance, or deployment rule |

Never load all root rules as a default. A deep rule is requested by the phase or feature only when its risk is present.

## Commands

```bash
python3 scripts/framework_route.py --phase 01
python3 scripts/framework_route.py --phase 04 --feature frontend
python3 scripts/framework_route.py --phase 04 --feature ai --json
```

The command prints an ordered reading list. The assistant should read those files in order, summarize the active constraints, and then work only on the current Phase and Feature.

## Session protocol

At the beginning of a session, provide the assistant with the current Phase number, Feature ID, and the last phase report. Do not paste old chat history or every rule file. At the end, save a short phase/feature report so the next session can resume from a small artifact rather than rereading the whole repository.

## Context budget rule

The default Phase pack has at most five canonical files. The Feature overlay has at most three Skills/files. If more material appears necessary, first explain which new risk requires it and load only the matching deep rule. This is a deliberate stop against context explosion, not an optional optimization.

## Recommended prompt

> Current phase: `04`. Current feature: `F-003`. Run `python3 scripts/framework_route.py --phase 04 --feature frontend --json`. Read only the returned files. Summarize constraints, scope, affected files, and unknowns. Do not implement until I approve the plan.
