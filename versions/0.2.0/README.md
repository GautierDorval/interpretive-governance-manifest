# Interpretive Governance v0.2.0 (draft)

This version introduces **memory-aware primitives** for stateful AI systems
(RAG with persistence, agent memory, consolidation, controlled forgetting).

## What is new in v0.2.0

- Adds **memory governance** to the core scope.
- Defines minimal primitives: MemoryObject, MemoryLog, consolidation, controlled forgetting.
- Introduces **conformance break triggers** for stateful systems (model change, embedding rebuild, rule changes, log loss).
- Links operational constraints to the ops-pack **M-layer**.

## Non-goals

- This version does not define a new scoring system.
- This version does not replace alignment, refusal policies, or safety training.
- This version does not mandate a specific storage technology.

## Operational layer

See: `extensions/ops-pack/M-layer/`
