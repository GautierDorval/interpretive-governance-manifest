# Inference vs authority

## Purpose

This document defines a strict boundary between **inference** and **authority**.

- **Inference** produces informational outputs: descriptions, classifications, recommendations, plans, or uncertainty-qualified statements.
- **Authority** produces effects: external writes, irreversible transitions, privileged access, publication, payments, deletions, escalations, or any action that changes a real system state.

This boundary is normative.

## Core rule

**Inference never implies authority.**

A response can be correct and still remain **non-authorized** to execute.

## Definitions

### Inference

An output that remains informational, including:
- explanation, summary, classification
- suggestion or recommendation
- planning or sequencing (a plan is not an execution)
- risk estimate or uncertainty-qualified claim
- interpretation constrained by canonical sources

Inference must remain within interpretive scope and must not be treated as permission to act.

### Authority

Any act (or attempted act) that:
- modifies an external system (write, delete, update, publish, send)
- triggers an irreversible or costly transition (payment, provisioning, deployment)
- changes access rights or privileges
- escalates to humans or systems with binding consequences
- materially affects people, assets, accounts, reputation, or compliance

Authority is governed by explicit, verifiable conditions.

### Execution

The operational realization of an authorized act via tools, systems, APIs, or human operators.
Execution is not part of interpretive governance.

### Delegation

A formal mapping that binds an executing identity to a principal identity under explicit constraints.
Delegation must be provable and auditable.

## Normative separation

Interpretive governance governs:
- what can be said
- how uncertainty is handled
- what sources are canonical
- what must be refused or abstained from

Authority governance governs:
- what can be executed or requested as an act
- under which conditions
- with which proofs
- with which audit trails
- with which reversibility constraints

These are distinct domains.

## Asymmetry with response governance

A system may conclude:
- “response is allowed” under response conditions (e.g., Q-Layer)

and still conclude:
- “act is denied / escalated / simulation-only” under authority conditions

This asymmetry is intentional and must be preserved.

## Required primitives for authority

No authority may be granted without:
1) an action taxonomy classification
2) an explicit authorization policy
3) a proof model (reversibility, auditability, identity, activation)
4) an authority ledger entry (including refusals and escalations)

## Non-goals

This document does not:
- prescribe implementation recipes
- define orchestrators, runtime stacks, or tool wiring
- provide bypasses, exploitation playbooks, or ready-to-copy production code

Those belong to execution engineering and may be demonstrated only in controlled references.
