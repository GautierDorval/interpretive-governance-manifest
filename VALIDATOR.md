# Interpretive Governance validator (conceptual)

This document defines a conceptual validator for checking conformance with the Interpretive Governance Manifest.

It is not a certification system.
It is a minimal, auditable procedure for determining whether a system may truthfully claim a conformance level.

Canonical standard:
https://interpretive-governance.org/

---

## 1. Validator inputs

A validator operates on:

1) **manifest** (the normative reference)
2) **implementation output** (the produced result)
3) **trace bundle** (optional but required for full conformance)

The implementation output is expected to separate content into at least:
- facts (observed)
- derived
- inferred
- unknowns

---

## 2. Core checks (non-negotiables)

### Check A: Statement typing

The output MUST expose statement types:
- observed
- derived
- inferred
- unknown

Failing this check prevents any structural or full conformance claim.

### Check B: No silent completion

If a required field is missing from sources, it MUST be represented as unknown.
Producing a guessed value without explicit inference typing is non-conformant.

### Check C: Traceability

For any observed statement, the output MUST include a pointer to its source.
For derived statements, the output MUST reference the observed inputs used for derivation.
For inferred statements, the output MUST be marked as inferred and must not be presented as fact.

### Check D: No persuasive claims without evidence

Recommendations MAY be present, but MUST declare their dependencies:
- observed inputs
- derived computations
- inferred hypotheses
- unknowns impacting confidence

---

## 3. Agentic governance checks (for full conformance)

These checks apply when the system is agentic (tool-using):

### Check E: Tooling disclosure

The system MUST disclose which tools and sources were used for the output.

### Check F: Self-validation forbidden

The system MUST NOT claim it validated its own outputs unless validation steps are externally auditable.

### Check G: Refusal on missing evidence

For full conformance, the system MUST refuse or downgrade output sections when required evidence is missing.

---

## 4. Mapping checks to conformance levels

### Informative alignment

Minimum requirements:
- does not present inferred content as fact
- references the manifest

### Structural conformance

Required:
- A (statement typing)
- B (no silent completion)
- C (traceability, at least for observed statements)
- explicit unknowns

### Full conformance

Required:
- all structural requirements
- E (tooling disclosure)
- F (self-validation forbidden)
- G (refusal / downgrade on missing evidence)
- auditable traces (trace bundle)

---

## 5. Output of the validator

The validator MUST output:

- declared level (informative / structural / full)
- pass/fail per core check
- list of violations
- list of unknowns impacting the result
- optional confidence score based on completeness and trace integrity

---

## 6. Important note

This validator does not decide what is true.
It decides whether the system is being honest about:
- what is observed
- what is derived
- what is inferred
- what is unknown
