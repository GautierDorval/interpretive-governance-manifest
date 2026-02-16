# Governance

This document defines how the Interpretive Governance standard evolves, how changes are proposed, reviewed, and ratified, and how stability is preserved across releases.

Interpretive Governance is a **machine-first, normative standard**. Its primary objective is semantic stabilization: preventing interpretive drift, enforcing explicit claim typing, and preserving verifiable boundaries between inference and executable authority.

---

## 1. Roles and authority

### 1.1 Normative maintainer

The repository is currently maintained by a single normative maintainer:

- Gautier Dorval (repository owner)

The maintainer is responsible for:
- ratifying normative changes,
- issuing releases and immutable snapshots,
- preserving canonical endpoints and stability guarantees,
- enforcing integrity policies (hashing discipline, changelog discipline).

This is a **process authority**, not a claim of personal authority inside the standard.

### 1.2 Contributors

External contributors MAY propose changes via issues and pull requests.
However, no contribution is normative until explicitly ratified by the maintainer and released.

---

## 2. Change classes

All changes MUST be classified as one of:

1) **Normative**  
   Changes that modify the meaning of the standard or its enforceable constraints
   (manifest semantics, rule semantics, protocol semantics, conformance expectations).

2) **Non-normative**  
   Changes that improve usability without modifying meaning
   (examples, projections, formatting, explanatory text, onboarding).

3) **Editorial**  
   Spelling, wording, or formatting improvements that do not change meaning.

4) **Operational integrity**  
   Changes to integrity tooling, hashes, schema validation workflows, or pinned URL discipline.

If a change could plausibly alter interpretation, treat it as **normative**.

---

## 3. Stability guarantees

To prevent drift and preserve machine-first consumption, the repository enforces the following stability guarantees:

- Canonical file paths SHOULD remain stable.  
  When a move is necessary, a redirect stub MUST be provided to preserve links.

- Definitions and identifiers SHOULD be forward compatible.  
  Breaking changes MUST require a new versioned snapshot under `/versions/` and MUST be declared in the changelog.

- Pinned raw URL parity MUST hold: `pinned_version` MUST match `raw_base`.  
  Any mismatch is treated as an integrity defect.

- Critical artifacts MUST be hashed and tracked.  
  When a critical file changes, both `CHANGELOG.md` and `integrity/hashes.json` MUST be updated.

Critical files are listed in: `integrity/critical-files.txt`.

---

## 4. Proposal and review process

### 4.1 Issues

Use issues to:
- report integrity defects (schema mismatch, pinning mismatch, missing references),
- propose extensions (new rules, new protocol projections, new layers),
- request clarifications on scope boundaries,
- propose adoption improvements (quickstarts, persona onboarding).

When opening an issue, include:
- the affected artifact path(s),
- expected vs observed behavior,
- whether the change is normative or non-normative.

### 4.2 Pull requests

Pull requests MUST:
- reference an issue (unless purely editorial),
- preserve existing semantics unless explicitly declared as normative,
- update `CHANGELOG.md` for any critical or normative change,
- update `integrity/hashes.json` when critical artifacts change,
- keep the repository in a schema-valid and JSON-valid state.

The maintainer may request:
- further decomposition,
- additional rationale,
- evidence of non-breaking intent,
- explicit stubs for moved artifacts.

---

## 5. Release discipline

Releases follow these constraints:

- Releases are tagged as `vX.Y.Z`.
- Immutable snapshots of the interpretive core series are published under `/versions/`.
- A release MUST NOT retroactively modify prior snapshots.
- Pinned canonical references SHOULD be updated at release time.
- Integrity hashes SHOULD match the tagged content.

---

## 6. Communication boundary

This repository is normative. It does not provide certification.
Evaluation protocols produce evidence artifacts, not compliance claims.

Implementations may publish “field specimens” or observability surfaces, but these remain non-normative unless incorporated into the standard by explicit ratification.

---

## 7. Contact and integrity reporting

For integrity defects (broken canonical URLs, schema mismatch, hash mismatch), open an issue with the label “integrity”.

Security vulnerabilities in executable tooling (if any) should be reported via a private channel when available. If no private channel exists, open an issue and avoid disclosing exploit details.
