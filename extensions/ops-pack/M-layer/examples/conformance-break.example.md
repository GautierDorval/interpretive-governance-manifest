# Example: conformance break (stateful system)

## Scenario

A stateful RAG system persists MemoryObjects and uses consolidation.
The underlying model weights are changed (post-training or model upgrade).

## Why this is a conformance break

The system’s refusal behavior and interpretation invariants may not be preserved.
Previously audited behavior is no longer valid.

## Required actions

1) Log `event_type: conformance_break` with reason.
2) Freeze high-confidence outputs until re-audit.
3) Record new model identity/version in audit metadata.
4) Re-run the applicable audit process for stateful systems (including drift checks).

## What must NOT happen

- silently continuing operation while claiming prior conformance level
- mutating memory rules or embeddings without trace
