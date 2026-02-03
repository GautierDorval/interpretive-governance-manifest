# Constraintive Governance (layer 2) — definition

Constraintive Governance is a **structural, runtime-only governance layer** applicable
exclusively in **agentic-closed** environments.

It is best understood as:

> a normative configuration of execution that bounds what a system is permitted to compute and emit.

It is:

- not interpretive,
- not cognitive,
- not adaptive by itself,
- and not applicable to web-open environments.

## What it governs

Constraintive Governance governs three domains:

1. **Input space**  
   What the system is allowed to see:
   - retrieval scope,
   - source allowlists,
   - exclusions and deny-by-default boundaries.

2. **Output space**  
   What the system is allowed to emit:
   - formats,
   - schemas,
   - prohibited content classes,
   - bounded variability.

3. **Execution conditions**  
   How the system executes:
   - inference parameters (temperature, top_p, max tokens),
   - validation and rejection logic,
   - retry limits,
   - abstention thresholds,
   - routing and orchestration constraints.

## Why it exists

Models do not self-stabilize.
Therefore, coherence, safety, and non-extrapolation must be imposed externally.

Constraintive Governance is the **runtime enforcement substrate** that makes those external constraints real
in environments where execution can be controlled.

## Relationship to Interpretive Governance

- **Interpretive Governance (layer 1)** governs claim legitimacy and typing:
  - observed / derived / inferred / unknown,
  - traceability over plausibility,
  - legitimate non-response when conditions are missing.

- **Constraintive Governance (layer 2)** governs execution bounds:
  - what may be retrieved,
  - how inference is configured,
  - what formats are accepted,
  - when abstention is triggered.

Layer 2 does not replace layer 1.
In **agentic-closed** systems, layer 2 becomes the **technical substrate** that enables layer 1 enforcement at runtime.

## Regime boundary (canonical)

- **Web-open**: layer 2 is inapplicable (no control over runtime).  
  Only layer 1 can govern surfaces and interpretation conditions.

- **Agentic-closed**: layer 2 is applicable and supports layer 1  
  by adding control of execution to control of surfaces.

## Reference implementations (non-normative)

This repository is a specification.
Reference implementations may exist in separate repositories.

These references are:

- descriptive only,
- non-normative,
- not certification,
- not endorsement,
- and must not be interpreted as conformance claims.

Reference:
- https://github.com/GautierDorval/interpretive-agentic-reference
