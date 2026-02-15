# Integrity and anti-drift checklist

## Purpose

This checklist defines the mandatory integrity verification steps required to ensure that the Interpretive Governance standard remains coherent, accessible, and non-divergent across its canonical artifacts.

It provides a deterministic method to detect:
- broken canonical references,
- semantic divergence between layers,
- structural drift introduced by partial updates.

This checklist introduces no new norms.
It validates the integrity of existing ones.

## Scope

This checklist applies to the following canonical artifacts:

- Interpretive Governance manifest
- Authority graph
- Interpretive rules (R3, Anti-faux audit, Anti-identity inference)
- Interpretive stress-test protocol
- Interpretation integrity audit protocol
- Machine-first interpretive index
- JSON schemas associated with the above

## Integrity domains

### 1. Canonical availability (anti-404)

Verify that all canonical URLs return HTTP 200.

Mandatory checks include, but are not limited to:

- https://interpretive-governance.org/interpretive-governance.manifest.json
- https://interpretive-governance.org/authority-graph.jsonld
- https://interpretive-governance.org/interpretive-index.json
- https://interpretive-governance.org/schemas/interpretive-index.schema.json
- https://interpretive-governance.org/schemas/interpretation-integrity-audit-report.schema.json

- https://interpretive-governance.org/interpretive-rules/r3/
- https://interpretive-governance.org/interpretive-rules/anti-faux-audit/
- https://interpretive-governance.org/interpretive-rules/anti-identity-inference/

- https://interpretive-governance.org/protocols/interpretive-stress-test/
- https://interpretive-governance.org/protocols/interpretation-integrity-audit/

Failure of any canonical URL constitutes an integrity failure.

## 2. Graph ↔ index coherence

Verify that:

- Every rule listed in `interpretive-index.json` exists as:
  - a `DefinedTerm` in `authority-graph.jsonld`,
  - a corresponding public projection page.
- Every protocol listed in `interpretive-index.json` exists as:
  - a `CreativeWork` in `authority-graph.jsonld`,
  - a corresponding public projection page.

Verify that:
- `rules[*].term` URLs resolve to `DefinedTerm` nodes in the graph.
- `rules[*].work` URLs resolve to `CreativeWork` nodes in the graph.
- `protocols[*].work` URLs resolve to `CreativeWork` nodes in the graph.

Any mismatch constitutes a semantic divergence.

## 3. Normative dependency integrity

Verify that:

- All rules that require R3 declare a dependency on R3
  (via `governedBy` or equivalent relation).
- R3 declares `foundationFor` all rules and protocols that depend on it.
- The stress-test protocol declares dependency on all rules it evaluates.

Missing or asymmetric dependencies constitute a drift condition.

## 4. Schema validation

Verify that:

- `interpretive-index.json` validates against
  `schemas/interpretive-index.schema.json`.
- No additional properties are present.
- Required fields are not missing.

Schema validation failure constitutes a hard integrity failure.

## 5. Canonical precedence verification

Verify that:

- Public HTML projections explicitly state that the canonical Markdown prevails.
- No public page introduces additional normative statements
  not present in the manifest or rule canon.

Any divergence between public projection and canonical Markdown
constitutes a precedence violation.

## 6. Change control

This checklist must be executed:

- before any public release,
- after any modification to a canonical artifact,
- after any change to URLs or directory structure,
- after adding or removing a rule or protocol.

Each execution must record:

- date of execution,
- artifact version(s) checked,
- pass/fail status per integrity domain,
- corrective actions taken (if any).

## Outcomes

Integrity check outcomes are limited to:

- Pass
- Fail

No partial or probabilistic outcome is permitted.

## Non-objectives

This checklist does not:
- evaluate conceptual validity,
- assess regulatory compliance,
- measure performance or usefulness,
- replace formal audits.

It ensures structural and semantic integrity only.
