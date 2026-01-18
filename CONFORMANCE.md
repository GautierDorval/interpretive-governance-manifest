# Conformance to the Interpretive Governance Manifest

This document defines how conformance to the Interpretive Governance Manifest is assessed and declared.

Conformance is **voluntary**, **explicit**, and **self-declared**, but must be **truthful** and **auditable**.

This standard does not provide certification.  
It defines conditions under which a system, process, or implementation may truthfully claim alignment.

---

## 1. Conformance principles

An implementation MUST NOT claim conformance unless it:

- explicitly distinguishes between **observed**, **derived**, **inferred**, and **unknown** statements;
- does not silently complete missing data;
- preserves traceability between claims and sources;
- does not present probabilistic inference as factual assertion;
- respects the agentic constraints defined in the manifest.

Partial implementation does not imply full conformance.

---

## 2. Levels of conformance

Conformance is defined across three non-hierarchical levels.
Each level defines a distinct mode of alignment.  
Higher levels do not imply superiority, but increased enforcement and auditability.

### 2.1 Informative alignment

An implementation may claim **informative alignment** if it:

- references the Interpretive Governance Manifest;
- applies its principles conceptually;
- does not misrepresent inferred content as fact.

This level does not require structural enforcement.

**Label:**  
`interpretive-governance:informative`

---

### 2.2 Structural conformance

An implementation may claim **structural conformance** if it:

- enforces statement typing (observed / derived / inferred / unknown);
- prevents silent data completion;
- exposes uncertainty explicitly;
- documents how interpretive constraints are applied.

**Label:**  
`interpretive-governance:structural`

---

### 2.3 Full conformance

An implementation may claim **full conformance** if it:

- enforces all non-negotiable rules in the manifest;
- applies agentic governance constraints;
- provides auditable traces between claims and sources;
- refuses to produce outputs when conditions are not met.

For full conformance, refusal and non-response MUST be **interpretable and auditable**:
- the system must be able to state which condition failed;
- what evidence was missing or conflicting;
- and what additional input would allow a legitimate answer.

Implementations MAY formalize this requirement as a distinct response-authorization layer
(e.g., a "Q-Layer"), but must not treat naming as certification.

**Label:**  
`interpretive-governance:full`

---

## 3. Declaration of conformance

Any declaration of conformance MUST:

- specify the conformance level;
- identify the scope of application;
- avoid implying certification or endorsement.

Example:

> "This system declares **structural conformance** to the Interpretive Governance Manifest  
> within the scope of search interpretation and AI-generated explanations."

---

## 4. Non-conformance

Failure to meet the requirements of a declared level constitutes **non-conformance**.

The standard does not enforce compliance.  
Misrepresentation of conformance is considered a misuse of the standard.

---

## 5. Relationship to the manifest

This document is normative and complements the manifest.

In case of ambiguity, the manifest takes precedence.

---

## 6. Conceptual validator

Conformance assessment is expected to be performed using the **Interpretive Governance conceptual validator**.

The validator defines:
- required checks per conformance level;
- failure conditions;
- downgrade and refusal logic.

Canonical reference:
https://interpretive-governance.org/VALIDATOR.md

The validator is normative for conformance assessment but does not constitute certification.

