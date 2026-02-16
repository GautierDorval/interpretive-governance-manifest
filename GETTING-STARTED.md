# Getting started

This file provides a minimal “hello governance” path for newcomers.

Interpretive Governance is a **machine-first standard**. It constrains what may be asserted and how claims must be typed in probabilistic and agentic systems. It is not a policy framework, and it does not certify implementations.

---

## 1) Hello Governance (minimal path)

### Step 1 — Read the core intent

- `README.md` (purpose and scope boundary)
- `interpretive-governance.manifest.json` (canonical manifest)

### Step 2 — Validate machine-first shape

If you publish a manifest derived from this standard, validate it against the schema:

- `schemas/manifest.schema.json`

This repository includes a non-certifying validation script:

```bash
python -m pip install jsonschema==4.23.0
python scripts/validate_json_schema.py
```

This checks structural validity (schema), not semantic conformance.

### Step 3 — Discover rules and protocols

- `interpretive-index.json` — machine-first registry of rules + protocols
- `interpretive-rules/` — public projections of interpretive rules
- `protocols/` — public projections of evaluation protocols

---

## 2) Persona-based entry paths

### Model vendor

Goal: publish clear claim typing constraints and refusal conditions.

Start with:
- manifest + schema
- interpretive index referencing the rules you support

### Integrator / platform

Goal: expose auditable surfaces and stability boundaries.

Start with:
- interpretive index + protocol projections
- audit report schema examples under `/examples/`

### Auditor / compliance

Goal: interpret evidence artifacts under declared constraints.

Start with:
- `protocols/interpretation-integrity-audit/`
- `schemas/interpretation-integrity-audit-report.schema.json`
- example report: `/examples/interpretation-integrity-audit-report.example.json`

---

## 3) Notes on “non-executable by design”

The standard is non-executable by design.
Validation scripts and schemas are provided as **convenience tooling** and do not constitute certification or compliance claims.

If you need a runnable policy engine, treat it as a separate, non-normative implementation layer.
