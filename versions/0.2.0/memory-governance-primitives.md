# Memory-aware primitives (v0.2.0)

Status: draft  
Normative language: MUST / SHOULD / MAY (RFC 2119 style)

This document defines the minimal primitives required to govern **stateful**
systems that persist memory, perform consolidation, or apply controlled forgetting.

## 1. Definitions

### 1.1 MemoryObject

A MemoryObject is a persisted, typed, versioned, traceable unit representing:
- a statement, or
- a consolidation derived from multiple statements, or
- an invalidation/archival record.

A MemoryObject MUST include:
- `statement_type` (see §2)
- `verdict_type` (Factual / Inference / False / Unanswered)
- `source_refs` (0..n; if 0, consolidation MUST be prohibited)
- `timestamp` (creation time)
- `valid_from` / `valid_to` (or an explicit `temporal_scope: unknown`)
- `jurisdiction` (if applicable)
- `applicability_scope`
- `version`
- `integrity_hash` (sha256 over canonical form)

### 1.2 MemoryLog

A MemoryLog is an append-only event log (NDJSON recommended) describing the lifecycle of MemoryObjects.

A MemoryLog event MUST include:
- `event_type` (create | consolidate | invalidate | archive | policy_change | conformance_break)
- `memory_object_id`
- `timestamp`
- `actor` (system / human / policy-engine)
- `prev_hash` (when applicable)
- `new_hash` (when applicable)
- `reason` (mandatory for invalidation/archival)

## 2. Statement typing for memory

If the system persists memory, each MemoryObject MUST declare one of:

- `SourceStatement` (directly grounded in a source)
- `UserProvidedStatement` (input provided by user)
- `SystemGeneratedStatement` (model-generated, not validated)
- `DerivedStatement` (calculation/inference; must remain marked as derived)
- `ConsolidatedStatement` (summary/merge; must preserve traceability)

## 3. Consolidation rules (minimal)

Consolidation MUST be treated as a governed transformation.

A consolidation operation MUST:
1) preserve or reference all relevant sources (`source_refs`)
2) keep the original statement types available for audit
3) declare the transformation as `ConsolidatedStatement`
4) record an append-only MemoryLog event with:
   - inputs, outputs
   - justification
   - diff (or deterministic reconstruction instructions)

If `source_refs` are missing, consolidation MUST NOT occur.

## 4. Controlled forgetting (minimal)

Controlled forgetting MUST be implemented as:
- invalidation or archival with explicit reason
- never silent physical deletion

A MemoryObject MAY be marked invalid due to:
- obsolescence
- conflict with higher-priority sources
- correction after audit
- policy constraints

The invalidation MUST be logged with `event_type: invalidate` and a `reason`.

## 5. Temporal integrity (minimal)

MemoryObjects MUST carry temporal information sufficient to prevent time-drift:

- If a statement is time-bound, `valid_to` MUST be set.
- If time validity is unknown, `temporal_scope: unknown` MUST be explicit.
- Any consolidation MUST preserve the most restrictive temporal scope unless justified otherwise.

## 6. Conformance breaks (stateful systems)

A conformance break MUST be triggered if any of the following occurs without re-audit:

- model weights/version change (including post-training)
- embedding/index rebuild without integrity recalculation and logs
- consolidation/forgetting policy change without versioning and audit trail
- loss or unverifiability of MemoryLog

A conformance break MUST be logged as:
`event_type: conformance_break`.

## 7. Operational guidance

Operational implementation requirements live in:
`extensions/ops-pack/M-layer/`
