# Constraintive Governance — scope

## Applicable contexts (agentic-closed)

Constraintive Governance is applicable when an organization controls:

- the orchestrator / wrapper calling the model,
- retrieval and source boundaries,
- validation and rejection logic,
- retry and abstention rules,
- logging and audit surfaces.

Typical examples:

- internal agent systems,
- enterprise RAG stacks with strict source policies,
- multi-step pipelines with enforced formats and validators,
- automated decision support where outputs must preserve unknowns.

## Inapplicable contexts (web-open)

Constraintive Governance is **inapplicable** when the execution environment is external:

- public LLMs operated by third parties,
- search engines and AI answer engines,
- external crawlers and summarizers,
- any environment where parameters, orchestration, and validators are not under your control.

In those contexts, only **Interpretive Governance of surfaces** (layer 1) is available.
