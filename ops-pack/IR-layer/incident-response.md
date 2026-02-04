# IR-Layer — incident response

## Purpose

This layer defines operational procedures when governance or execution drifts or fails.

## Kill switch

A kill switch MUST exist conceptually:
- disable execution
- force read-only or simulation-only mode
- preserve audit trails

## Degraded modes

- read-only mode
- simulation-only mode
- escalation-only mode (no direct execution)

## Rollback controls

If a policy version causes failures:
- revert to the previous policy version
- record rollback decision in the authority ledger
- log the incident in a post-mortem

## Post-mortem (minimal template)

- incident summary
- scope and impact
- timeline (events)
- root cause hypothesis
- corrective actions (policy change, test additions)
- prevention measures (tripwires, oversight gates)
