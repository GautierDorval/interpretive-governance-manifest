# Memory governance (MEM-layer)

Status: draft  
Normative language: MUST / SHOULD / MAY

## 1. Core invariant

A stateful memory system MUST NOT allow untyped, untraceable, or temporally ambiguous memory to become a durable “fact”.

## 2. Minimum invariants (MUST)

1) MemoryObjects MUST be typed (`statement_type`, `verdict_type`).  
2) MemoryObjects MUST be traceable (`source_refs`) for any high-confidence usage.  
3) MemoryObjects MUST be time-aware (`valid_from` / `valid_to` or explicit unknown).  
4) Memory changes MUST be append-only logged (MemoryLog).  
5) Forgetting MUST be controlled (invalidate/archive, no silent deletion).  
6) Consolidation MUST be gated (see `memory-consolidation-policy.md`).  
7) Conformance breaks MUST be explicit and logged.

## 3. Allowed architectures

This layer is storage-agnostic. It MAY be implemented with:
- vector databases
- relational stores
- graph stores
- hybrid approaches

The invariants still apply.

## 4. Compatibility

This layer is compatible with external audit frameworks (e.g., scoring systems) as long as:
- MemoryObjects and MemoryLogs are available as verifiable inputs,
- model identity/version is recorded,
- conformance breaks are enforced.

## 5. Security note

Memory is a new attack surface. Any change to:
- embedding/index
- consolidation rules
- forgetting rules
without audit trails MUST be treated as a conformance break.
