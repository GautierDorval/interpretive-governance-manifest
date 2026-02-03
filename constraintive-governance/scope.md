# Constraintive Governance — scope

This document defines where Constraintive Governance can and cannot apply.

## Applicable contexts (agentic-closed)

Constraintive Governance is applicable when an organization controls:

- the orchestrator / wrapper calling the model,
- retrieval scope and source boundaries,
- validation and rejection logic,
- retry policies and abstention thresholds,
- logging surfaces and audit trails.

Examples:

- internal agent systems,
- enterprise RAG stacks with strict source allowlists,
- multi-step pipelines with enforced output schemas,
- automated decision support requiring explicit unknowns,
- systems where “legitimate non-response” must be enforced.

## Inapplicable contexts (web-open)

Constraintive Governance is **inapplicable** when execution is external:

- public LLM interfaces operated by third parties,
- search engines and AI answer engines,
- external crawlers and summarizers,
- any environment where temperature, routing, validation, and refusal logic are not under your authority.

In those contexts, only **Interpretive Governance of surfaces** (layer 1) is available.

## Non-goals

Constraintive Governance does not:

- guarantee correctness,
- certify compliance,
- provide safety claims,
- replace interpretive constraints (layer 1),
- define any specific vendor implementation.
