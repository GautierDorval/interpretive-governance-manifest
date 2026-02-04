# Proof model

## Purpose

This document defines the minimal proof primitives required to grant or deny **authority**.

Authority may not be granted without explicit proof references, recorded in the authority ledger.

## Proof primitives

### 1) Reversibility proof

A reversibility proof must declare:
- whether the act is reversible, compensable, or irreversible
- the rollback window (if applicable)
- the rollback procedure or compensation procedure
- limits and failure modes

If reversibility is required by policy and no acceptable proof is provided, the authority decision must be **deny** or **escalate**.

### 2) Auditability proof

An auditability proof must ensure:
- the decision and its basis can be reconstructed
- the applied policy and versions are recorded
- evidence pointers exist (inputs, constraints, approvals)
- integrity primitives can be applied (hashes, signatures, tamper-evidence)

Auditability applies to:
- granted authority
- denied authority
- escalations
- simulations

### 3) Executable identity proof

An identity proof must bind:
- an executing identity (system or human operator)
- a principal identity (who delegates authority)
- the scope and limits of delegation
- the time window and revocation conditions

If identity is unknown or unverifiable for the action class, authority must be **deny** or **escalate**.

### 4) Activation proof

An activation proof must declare which gates were satisfied, such as:
- human oversight approval
- two-person rule approval
- quorum / veto outcome (multi-agent)
- sandbox or simulation outcome
- confidence / impact / irreversibility gates

If activation is required and not satisfied, authority must not be granted.

## Normative rule

Proof absence is not neutral.

If policy requires a proof primitive and the primitive is missing, invalid, or unverifiable, the authority decision must be:
- deny, or
- escalate (if the policy allows escalation)

## Non-goals

This document does not prescribe:
- technical implementations (signatures, logging stacks, identity providers)
- orchestrator architectures
- tool wiring or deployment patterns
