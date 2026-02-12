# AGENTS.md

## Agent operating rules — interpretive-governance-manifest

This repository contains normative, machine-first governance artifacts.  
It is **non-executable by design**. Stability, traceability, and non-drift are primary constraints.

---

## Operating mode

Agents MUST operate in **suggest mode** by default.

No autonomous commits.  
No direct writes to `main`.  
All changes must go through pull requests.

---

## Non-negotiable constraints

1. **No modification of existing files** (not even formatting) unless explicitly authorized.
2. **No renaming, moving, or deleting files or directories.**
3. **No auto-formatting** (prettier, remark, jq -S, etc.).
4. No dependency upgrades or structural refactors without explicit instruction.
5. No normalization or stylistic “improvements”.

This repository prioritizes semantic stability over stylistic consistency.

---

## Allowed modification surface (add-only unless authorized)

Agents may add files only under:

- `.github/workflows/`
- `integrity/`
- `scripts/`
- `Makefile`

Any other path is read-only unless explicitly authorized.

---

## Integrity & drift policy

Critical normative files are subject to drift control.

If modifying any file listed in `integrity/critical-files.txt`, the PR must:

1. Update `CHANGELOG.md`
2. Update `integrity/hashes.json`

Otherwise the change is considered invalid.

---

## Versioning model

- `0.1.x` → snapshot versions stored under `/versions/`
- `1.x` → extension series versioned by tags/releases
- Raw URLs must be **pinned** to tagged versions, not `main` or `master`.

Agents must not introduce non-pinned raw URLs in normative artifacts.

---

## Schema authority

If JSON artifacts are modified:

- They must validate against their corresponding schema under `/schemas/`
- Schema violations are blocking

No schema loosening without explicit instruction.

---

## Interpretive constraints (do not violate)

This repository enforces:

- Explicit statement typing
- Facts vs inference separation
- Traceability over plausibility
- Bounded interpretation
- Legitimate non-response

Agents must not introduce content that:

- Implies authority not explicitly declared
- Blurs inference and fact
- Expands scope beyond declared boundaries
- Converts normative text into executable claims

---

## Escalation rule

If uncertain whether a change:

- Alters semantic meaning,
- Expands scope,
- Affects canonical references,
- Or modifies authority boundaries,

Stop and request clarification.

No assumption-based edits.

---

## Design philosophy

This repository is a **stability surface**, not a feature surface.

The goal is not to optimize code.
The goal is to preserve interpretive determinism and canonical traceability.
