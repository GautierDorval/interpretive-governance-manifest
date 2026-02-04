# M-Layer — multi-agent coordination

## Purpose

This layer defines minimal coordination constraints for systems composed of multiple agents or roles.
It exists to prevent contradiction loops, uncontrolled action duplication, and authority drift.

This layer is compatible with the authority role topology (planner / executor / critic / approver / auditor).

## Core constraints

### Role separation

For high and critical action classes:

- planning must be separated from execution
- critique must be independent from planning and execution
- approval must be human when required by policy
- audit must be independent from approval and execution

### Shared state and hypothesis logging

Multi-agent systems should maintain a shared, append-only record of:

- the current goal (informational only)
- hypotheses (typed as inferred unless proven)
- decisions and their justification pointers
- disagreements and veto outcomes

This shared record is non-normative in implementation but normative in intent.

### Conflict handling

When agents disagree:

- the critic role may veto or trigger escalation
- tie-breakers must be explicit (policy-based, not persuasive)
- unresolved conflicts must downgrade to simulation-only or escalation

Conflict outcomes must be recorded in the authority ledger.

### Loop detection (recommended)

Multi-agent coordination should detect:

- repeated attempts to re-justify a denied action
- repeated target mutation across retries
- repeated contradiction between planner and critic

On loop detection:
- stop and escalate
- or degrade to simulation-only

### Duplicate action prevention

The system must prevent duplicated executions by:

- requiring idempotency markers (conceptual requirement)
- requiring a unique intent/target correlation id
- refusing identical high-risk executions without explicit human approval

## Non-goals

This layer does not:
- prescribe a specific agent architecture (planner-critic-executor, swarm, etc.)
- define messaging protocols
- ship reference orchestration code
