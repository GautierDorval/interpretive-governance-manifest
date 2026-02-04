# Role topology (mono-agent and multi-agent)

## Purpose

This document defines a normative role topology for authority governance.

Roles constrain who can propose, critique, approve, execute, and audit authority decisions.

## Core roles

### Planner

- Produces plans, steps, or recommendations (inference domain)
- May propose an authority request but may not execute

### Executor

- Executes an act only after authority is granted
- Must not override policy outcomes

### Critic

- Challenges assumptions, checks policy alignment, searches for failure modes
- May veto or trigger escalation depending on action class criticality

### Approver (human oversight)

- Provides explicit approval when required by policy
- May enforce two-person rule

### Auditor

- Reviews ledger entries, proofs, and trace completeness
- Does not grant authority in real-time (separation from approval)

## Separation of duties (SoD)

For high or critical action classes:
- Planner and Executor MUST be distinct roles
- Critic MUST be distinct from Planner and Executor
- Approver MUST be human when required by policy
- Auditor MUST be independent from approval and execution

## Veto and quorum (multi-agent)

For multi-agent systems, authority governance MAY require:
- quorum approval for critical actions
- explicit veto capabilities by Critic role

Veto outcomes MUST be recorded in the authority ledger.

## Non-goals

This document does not define:
- specific multi-agent orchestration architectures
- inter-agent messaging protocols
- implementation of quorum/veto systems
