# Changelog

## Unreleased

- Documentation and consistency improvements under discussion.

> Note: the `/versions/0.x/` directory tracks historical snapshots of the
> Interpretive Governance manifest (core standard).
> `1.x` releases track the stabilization and extension of the layered governance
> architecture beyond the core manifest.

---

## 1.4.1 — Adoption hardening (licensing + governance) + manifest/schema consistency

- Added explicit licensing:
  - Documentation licensed under **CC BY 4.0**
  - Schemas and scripts licensed under **Apache-2.0**
  See: `LICENSE`, `LICENSES/`, `NOTICE`.
- Added governance and onboarding documents:
  - `GOVERNANCE.md`
  - `CONTRIBUTING.md`
  - `GETTING-STARTED.md`
- Fixed canonical manifest / schema consistency:
  - Added `non_negotiables.statement_types_required`
  - Added `non_negotiables.facts_vs_inference_separation` (compatibility alias)
  - Added `canonical.schema`
- Fixed pinned raw URL parity (`pinned_version` ↔ `raw_base`) for repository extensions.
- Fixed legacy JSON redirect stubs under `extensions/ops-pack/M-layer/` to remain link-preserving
  while keeping JSON validation green.
- Updated integrity hashes for critical artifacts.

No changes to the memory governance primitives or MEM-layer semantics introduced in `1.4.0`.

---
## 1.4.0 — Memory governance (MEM-layer) + core memory-aware primitives (v0.2.0)

- Introduced **memory-aware core primitives** for stateful systems (RAG with persistence, agent memory, consolidation, controlled forgetting).
- Added core snapshot `versions/0.2.0/`:
  - `versions/0.2.0/interpretive-governance.manifest.json` (adds `memory_governance` scope and memory-aware conformance triggers)
  - `versions/0.2.0/memory-governance-primitives.md` (normative primitives: MemoryObject, MemoryLog, consolidation, controlled forgetting, temporal integrity)
- Added **MEM-layer** to the ops-pack extensions:
  - `extensions/ops-pack/MEM-layer/memory-governance.md`
  - `extensions/ops-pack/MEM-layer/memory-consolidation-policy.md`
  - `extensions/ops-pack/MEM-layer/temporal-integrity.md`
  - `extensions/ops-pack/MEM-layer/controlled-forgetting.md`
  - `extensions/ops-pack/MEM-layer/memory-logging-minimum.md`
  - `extensions/ops-pack/MEM-layer/examples/` (MemoryObject, MemoryLog, conformance break scenario)
- Renamed the memory governance layer from `extensions/ops-pack/M-layer/` to `extensions/ops-pack/MEM-layer/`
  to avoid collision with the existing `ops-pack/M-layer/` designation (multi-agent coordination).
  The legacy path is retained as a redirect stub.
- Added schemas:
  - `schemas/memory-object.schema.json`
  - `schemas/memory-log.schema.json`
- Reserved a **non-normative** evaluation protocol scaffold for stateful drift analysis:
  - `protocols/memory-drift-audit/` (draft; applies existing primitives, does not introduce new core primitives or scoring)
- No changes to the interpretive core semantics, Q-Layer semantics, or executable authority boundaries.
  This release adds a memory-aware profile and operational invariants for systems that persist state over time.

---

## 1.3.0 — Interpretation integrity audit protocol (IIA)

- Added Interpretation integrity audit protocol (canonical protocol + public projection).
- Added audit report schema and minimal example for interpretation integrity audits.
- Updated `interpretive-index.json` and `authority-graph.jsonld` to reference the new protocol and schema.
- Updated integrity checklist coverage for the new protocol and schema.
- Updated integrity hashes for critical artifacts.
- No changes to the interpretive core, Q-Layer semantics, or executable authority boundaries.

---

## 1.2.0 — Integrity locking (V-Layer extension)

- Introduced **Integrity locking (artifact hashing)** as an optional V-Layer mechanism.
- Added `ops-pack/V-layer/integrity-locks.md`.
- Clarified SHA-256 fingerprinting discipline for critical machine-first artifacts.
- Defined scope boundaries: integrity hashes are drift-control signals, not authority proofs.
- No changes to interpretive core, Q-Layer semantics, or executable authority boundaries.

This release strengthens drift detection and artifact traceability
without redefining the layered governance model.

---

## 1.1.0 — Authority governance (Layer 3) + ops pack (minimal)

- Introduced **Authority governance (Layer 3)**:
  - `authority/inference-vs-authority.md`
  - `authority/action-taxonomy.json`
  - `authority/proof-model.md`
  - `authority/authority-policy.json`
  - `authority/authority-ledger-spec.md`
  - `authority/role-topology.md`
  - `authority/incentive-integrity.md`
  - `authority/non-objectives.md`

- Introduced **Agentic operations pack (minimal)**:
  - `ops-pack/H-layer/human-oversight-protocol.md`
  - `ops-pack/P-layer/privacy-data-lineage.md`
  - `ops-pack/V-layer/versioning-drift-change-control.md`
  - `ops-pack/S-layer/security-abuse-resistance.md`
  - `ops-pack/IR-layer/incident-response.md`

This release formally separates **interpretation** from **executable authority**
and introduces the minimal operational primitives required for real-world
agentic systems, without redefining the interpretive core.

---

## 1.0.0 — Ontology locked — layered governance baseline

- Formalized and locked the layered governance baseline:
  - Layer 0 — Ontology
  - Layer 1 — Interpretive Governance
  - Layer 2 — Constraintive Governance

- No new functional modules introduced.
- This release exists to mark a **semantic and architectural stabilization point**
prior to the introduction of executable authority governance.

---

## 0.1.2 — Response legitimacy compatibility (Q-Layer)

- Introduced explicit response legitimacy concepts in the manifest.
- Clarified compatibility with the SSA-E + A2 **Q-Layer** (response authorization).
- Published immutable snapshot under `/versions/0.1.2/`.

---

## 0.1.1

- Added explicit non-equivalence with the academic field of interpretive governance.
- Introduced formal scope boundaries for machine-first usage.
- Clarified provenance and non-normative context separation.
- Published immutable snapshot under `/versions/0.1.1/`.

---

## 0.1.0

- Initial publication of the Interpretive Governance manifest.
