# Authority ledger specification

## Purpose

This document specifies the minimal, normative audit record for authority decisions.

The ledger must record:
- granted authority
- denied authority
- escalations
- simulations
- rollbacks (when applicable)

## Core rule

If an authority decision exists, a ledger entry must exist.

Ledger absence is a policy violation.

## Ledger entry (minimal fields)

A ledger entry MUST include the following fields.

### Identity and scope

- `entry_id` (unique identifier)
- `timestamp` (UTC)
- `actor_identity` (executable identity)
- `principal_identity` (delegating identity, if any)
- `delegation_ref` (pointer to delegation proof, if any)
- `environment` (e.g., sandbox, staging, production)

### Intent and classification

- `intent_summary` (short natural language summary)
- `action_class` (must match action taxonomy)
- `target` (what system/resource would be affected)
- `surface` (internal/external)
- `data_sensitivity` (none/confidential/pii/secret)

### Policy application

- `taxonomy_version`
- `policy_version`
- `proof_model_version` (or reference)
- `rule_path` (which rule(s) triggered the outcome)
- `decision` (allow | deny | escalate | simulate)

### Evidence pointers (proof references)

- `proof_refs` (list of pointers, each with `type` and `ref`)
  - `type` ∈ {reversibility, auditability, identity, activation, oversight, two_person_rule, quorum, veto, simulation, rollback_plan}
  - `ref` is a URI, hash pointer, or internal identifier

### Outcome and constraints

- `constraints` (any constraints applied, e.g. “read-only”, “simulation-only”, “no external writes”)
- `notes` (short, non-normative explanation)

## Rollback and reversibility

If the action class requires reversibility proof, the ledger entry MUST include:

- `reversibility_class` (reversible | compensable | irreversible)
- `rollback_window` (if applicable)
- `rollback_ref` (pointer to rollback procedure or compensation procedure)

If rollback is executed, an additional ledger entry MUST be recorded:

- `decision` = `rollback`
- `rollback_of` (entry_id of the original execution)
- `rollback_outcome` (success | partial | failed)
- `rollback_notes`

## Integrity (tamper-evidence)

The ledger SHOULD support integrity primitives, such as:
- `entry_hash`
- `previous_entry_hash` (append-only chaining)
- `signature_ref`

This specification does not mandate a specific cryptographic scheme.

## Redaction and privacy

If the ledger contains sensitive data:
- redact content but preserve pointers and hashes
- store sensitive payloads separately with controlled access
- record redaction policy reference where applicable

## Non-goals

This specification does not:
- prescribe a storage engine
- define cryptographic implementation details
- provide orchestrator wiring or code
