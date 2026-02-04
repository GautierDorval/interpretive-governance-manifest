# Authority schemas

This directory contains **normative JSON Schemas** for Authority governance (Layer 3).

These schemas are contracts for validation and maintenance.
They do not provide execution recipes, orchestration patterns, or deployment playbooks.

## Schemas

- `action-taxonomy.schema.json`  
  Validates `authority/action-taxonomy.json`.

- `authority-policy.schema.json`  
  Validates `authority/authority-policy.json`.

- `authority-ledger-entry.schema.json`  
  Validates authority ledger entries produced by implementations, aligned with `authority/authority-ledger-spec.md`.

## Non-goals

This directory does not:
- certify compliance
- guarantee safety outcomes
- define runtime storage engines
- provide executable validators or tooling
