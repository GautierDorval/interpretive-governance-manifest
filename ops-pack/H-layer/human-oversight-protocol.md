# H-Layer — human oversight protocol

## Purpose

This protocol defines when authority decisions must escalate to humans and how approvals are recorded.

This layer does not define what is true; it defines when to stop and escalate.

## Gates

### 1) Impact gates

If an action class is high or critical, require:
- escalation to human approver, or
- two-person rule (when policy requires)

### 2) Irreversibility gates

If reversibility_class is `irreversible` or rollback is undefined:
- authority MUST be denied or escalated
- simulation-only may be used for evaluation

### 3) Confidence / uncertainty gates

If uncertainty is material to the decision:
- escalate to human approver
- record uncertainty and missing proofs in the ledger

## Approval requirements

When human approval is required:
- approver identity must be recorded
- approval timestamp must be recorded
- scope of approval must be explicit (action class + target)

## Two-person rule

For critical classes (e.g., pay, deploy, delete):
- two distinct humans must approve
- both identities must be recorded in the ledger

## Non-goals

This protocol does not prescribe:
- UI flows
- ticketing systems
- identity provider integration
