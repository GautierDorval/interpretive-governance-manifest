# C-Layer — cost and scalability profiles

## Purpose

This layer defines scalability-aware governance profiles to prevent governance from becoming impractical.
It expresses how to trade cost, latency, and assurance while preserving non-negotiable constraints.

This layer is operational in intent but non-prescriptive in implementation.

## Profiles

### Lite

Goal: minimal overhead for low-risk interpretive usage.

- prioritize Q-Layer enforcement
- conservative defaults: deny / non-specified / abstain
- limited logging: pointers only, no payload retention
- sampling-based evaluation (not exhaustive)

### Standard

Goal: balanced assurance for normal governed operation.

- full Q-Layer enforcement
- authority boundary enforced (simulation-only for high-risk classes)
- ledger completeness for all authority decisions (including deny/escalate)
- periodic regression evaluation

### High assurance

Goal: maximum assurance for high-risk environments.

- strict Q-Layer + strict authority governance
- mandatory human oversight gates for high/critical classes
- expanded ledger integrity primitives (tamper-evidence)
- frequent regression evaluation and red-team cadence
- compatibility windows and hotfix procedures enforced

## Cost control levers (non-prescriptive)

- caching of canonical pointers and taxonomy mapping
- policy compilation into static decision tables
- sampling strategies for evaluation
- separating "execution constraint" from "audit depth"
- progressive hardening: start Lite, migrate to Standard/High assurance

## Non-negotiables across profiles

Across all profiles:

- inference never implies authority
- unknowns must remain explicit
- no silent completion for missing evidence
- high-risk actions must not be executed by default

## Non-goals

This layer does not:
- define pricing models
- prescribe infrastructure stacks
- claim performance guarantees
