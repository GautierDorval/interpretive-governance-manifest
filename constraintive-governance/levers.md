# Constraintive Governance — levers (runtime)

This document lists runtime levers used to enforce constraintive governance.
They are enforced by configuration and orchestration, **not by prompting**.

## 1) Inference parameters (bounded variability)

Examples:

- temperature (low variability regimes)
- top_p (bounded sampling)
- max_tokens (bounded completion length)
- presence_penalty / frequency_penalty (bounded drift and repetition)

These values must be set in the orchestrator or API wrapper.

## 2) Output constraints (format enforcement)

- strict JSON outputs
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
- schema is invalid,
- confidence thresholds are not met.

Abstention must be enforced by routing and policy, not by “asking the model to abstain”.

## 4) Retrieval boundaries (RAG boundedness)

- allowlist of sources
- deny-by-default retrieval
- canonical priority ordering
- scope-limited retrieval per request type
- refusal when retrieval falls outside boundary

## 5) Orchestration constraints (multi-step systems)

- fixed routing rules and roles
- role separation (generator vs checker vs router)
- no self-validation by the same role
- limited retry strategy (bounded attempts)
- audit logging of each step and decision

## 6) Observability (non-normative)

Implementations may expose descriptive observability surfaces, such as:

- runtime configuration disclosures (what was fixed),
- rejection reasons (schema invalid, scope violation),
- abstention statistics.

These are descriptive only and do not certify correctness or conformance.
