# Constraintive Governance — levers (runtime)

This document lists **runtime levers**.
They are enforced by configuration and system architecture, not by prompting.

## 1) Inference parameters (bounded variability)

Examples:

- temperature (low variability)
- top_p (bounded sampling)
- max_tokens (bounded completion length)
- penalties (bounded repetition / drift)

These values must be set in the orchestrator or API wrapper, not via instruction text.

## 2) Output constraints (format and structure)

- strict JSON output
- JSON Schema validation
- required fields and types
- refusal on invalid schema
- deterministic templates where applicable

Pattern:

LLM output → validator → accept / reject → retry / abort

## 3) Abstention policies (legitimate non-response)

Abstention is a **system decision**, triggered when:

- evidence is missing,
- sources conflict,
- scope is violated,
- confidence thresholds are not met.

Abstention is enforced by policy and routing, not by “asking the model to abstain”.

## 4) Retrieval boundaries (RAG boundedness)

- allowlist of sources
- denylist of sources
- canonical priority ordering
- scope-limited retrieval per request type
- refusal when retrieval is outside boundary

## 5) Orchestration constraints (multi-step systems)

- fixed routing rules
- role separation (generator vs checker vs router)
- no self-validation by the same role
- controlled retry strategy (limited attempts)
- audit logging of each step and decision
