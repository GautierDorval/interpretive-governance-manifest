# Interpretation integrity audit protocol

## Purpose

The interpretation integrity audit protocol defines a reproducible method for producing an opposable audit report that characterizes divergence between:

- a declared canonical corpus snapshot (what is stated),
- machine-generated interpretations under declared test conditions (what is produced),
- and a verifiable evidence chain linking each finding to concrete artifacts (what is traceable).

This protocol does not introduce new norms.  
It operationalizes existing interpretive governance constraints by enforcing traceability, bounded interpretation, and legitimate non-response when verification is not possible.

**Informative label (fr-CA)**  
Audit d’intégrité interprétative

## Scope

This protocol applies to audits of:

- websites or document corpora (domain, subpath, or URL list),
- retrieval-augmented systems consuming that corpus,
- conversational agents producing interpretive outputs about that corpus,
- multi-model or multi-run stability evaluations.

The audit evaluates interpretive integrity, not usefulness or performance.

## Governed by

This protocol is governed by:

- R3 — Interpretive abstention
- Anti-faux audit
- Anti-identity inference

## Principle

An interpretation integrity audit is **snapshot-bound**:

1. **Anchor** the corpus as a snapshot with an explicit boundary and SHA-256 hash.
2. **Probe** the system with a versioned QuerySet.
3. **Record** one or more ModelRuns with declared parameters and timestamps.
4. **Extract** findings as typed items supported by evidence.
5. **Declare** audit validity as conditional on the stability of audit variables.

The audit must prefer abstention, clarification, or referral to canonical evidence over plausible completion.

## Primary unit of audit

### Corpus snapshot (primary)

An audit MUST declare a corpus snapshot:

- `snapshotId`
- `timestamp` (ISO 8601)
- `boundary` (domain, subpath, or URL list)
- `hashAlg` (SHA-256)
- `hash` (hex)

The snapshot is the primary unit of comparability.  
No grade, score, or conclusion is valid outside the declared snapshot boundary.

## Required inputs

An audit SHOULD record the following inputs:

- Corpus snapshot (primary unit)
- QuerySet (`id`, `version`, and questions)
- Model identity (provider, name, version if available)
- Run parameters (temperature, top_p, or explicit `unknown`)
- Raw outputs per question (outputId + content)

## Required output artifact

The audit MUST produce a structured JSON report that validates against:

- `schemas/interpretation-integrity-audit-report.schema.json`

A minimal example is provided under:

- `examples/interpretation-integrity-audit-report.example.json`

## Findings typing (audit layer)

Audit findings MUST be typed using the following categories:

- `Observation` (what was observed in outputs)
- `Evidence` (raw trace anchors: excerpt, log, capture, link)
- `Measurement` (computed or derived metric from observations)
- `NonConformance` (rule-bound deviation with evidence)
- `RiskStatement` (bounded conditional risk statement)
- `Recommendation` (non-normative corrective action suggestion)
- `Limitation` (scope, coverage, or validity constraint)

These types are audit-layer types.  
They do not replace the core statement types (observed / derived / inferred / unknown) required by the Interpretive Governance manifest.

## Conditional validity

Audit validity is **conditional**, not calendrical.

An audit MUST declare a validity status based on:

- corpus snapshot hash
- boundary definition
- QuerySet id + version
- model identity (as declared)
- run parameters (as declared)
- timestamps of runs

Recommended validity states:

- `valid`
- `to_be_refreshed`
- `legacy`
- `invalid`

## Non-objectives

This protocol does not:

- certify regulatory compliance,
- provide legal advice,
- rank systems,
- guarantee absence of hallucination,
- measure SEO performance, traffic, or conversion,
- substitute an organizational audit program.

It produces evidence-anchored interpretive integrity signals only.
