# Interpretive Governance — machine-first standard

This repository hosts the **Interpretive Governance** manifest:  
a machine-first governance standard designed to constrain interpretive,
decision, and agentic outputs in probabilistic systems.

> **Non-equivalence notice**  
> Interpretive Governance, as defined in this repository, **is not** the academic
> field of interpretive governance in political or social sciences.
> It is a technical, machine-first standard for governing interpretation in
> automated and agentic systems.

The validator defined in this repository is **conceptual and non-executable by design**.

---

## Purpose

Interpretive Governance defines non-negotiable constraints that require
explicit separation between:

- **observed** — directly sourced facts
- **derived** — values computed from observed facts
- **inferred** — probabilistic hypotheses
- **unknown** — missing or unverifiable information

The objective is not to eliminate error, but to prevent systems from
presenting hypotheses as facts and to make uncertainty explicit and auditable.

---

## Response legitimacy (Q-Layer compatibility)

Interpretive Governance constrains *what* may be asserted and how statements must be typed.
It is compatible with an additional, transversal discipline: **response legitimacy**.

When interpretive conditions are missing, conflicting, or insufficient, a system may be required to
request clarification or produce a **legitimate non-response** instead of defaulting to plausible completion.

This "response authorization" layer is formalized as the **Q-Layer** in the SSA-E + A2 doctrine
release **v1.2.0**. It is not a replacement for Interpretive Governance; it is a compatible extension
that governs *when* an answer is allowed.

Canonical reference (conceptual, normative):
- https://github.com/GautierDorval/ssa-e-a2-doctrine/blob/v1.2.0/layers/q-layer.md

---

## Scope boundary

This standard applies exclusively to:

- interpretive governance of representations,
- decision outputs in probabilistic systems,
- agentic reasoning and delegation chains.

It does **not** define:
- public policy frameworks,
- institutional governance models,
- social or political theory,
- human organizational governance.

---

## Canonical artifacts

- `/interpretive-governance.manifest.json` — canonical manifest  
- `/.well-known/interpretive-governance.json` — stable entrypoint  
- `/schemas/manifest.schema.json` — JSON Schema  
- `/versions/` — immutable version snapshots  

Status: **draft**.

---

## Provenance

Interpretive Governance was initiated and architected by **Gautier Dorval**
as part of a broader effort on semantic stabilization, interpretive governance,
and agentic constraint systems.

Canonical identity reference:  
https://gautierdorval.com/

This provenance is informative only and does not introduce personal authority
into the normative definition of the standard.
