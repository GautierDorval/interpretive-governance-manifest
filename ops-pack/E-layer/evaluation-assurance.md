# E-Layer — evaluation and assurance

## Purpose

This layer defines a non-normative but structured evaluation discipline for governed systems.
It exists to make governance changes testable, auditable, and regression-resistant.

This layer does not prescribe implementation stacks or execution tooling.

## Evaluation scope

Evaluation must cover:

- correct refusals vs over-refusals
- correct escalation vs unnecessary escalation
- simulation correctness (when simulation-only is required)
- near misses (attempts that would have violated authority rules)
- drift signals after policy changes

## Minimal metrics (recommended)

### Response-side (interpretive)

- rate of "non specified" when information is absent
- rate of canonical citation when required
- rate of legitimate non-response when Q-Layer conditions fail

### Authority-side (act boundary)

- authority decisions by class: allow / deny / escalate / simulate
- rate of policy conflicts (planner vs critic vs policy outcome)
- near-miss rate (tripwire activations)
- rollback coverage (classes requiring rollback plan)

## Regression testing discipline

When governance artifacts change, run regression checks against:

- boundary rule: inference never implies authority
- action taxonomy mapping stability
- policy outcomes for canonical test cases
- logging completeness against the ledger specification

Changes must not silently expand authority.

## Test set (normative structure, non-normative content)

A test set should be versioned and categorized by:

- intent type (instructional, commercial, authority_request, identity_reference)
- action class (read, write, delete, pay, publish, deploy, etc.)
- sensitivity (none, confidential, pii, secret)
- outcome expectation (deny, escalate, simulate, allow)

This repository does not ship executable test harnesses.

## Red-team scenarios (recommended)

Red-team scenarios should include:

- prompt injection and tool injection attempts
- data exfiltration attempts
- authority laundering (trying to convert inference into permission)
- ambiguous identity or relationship baiting
- proxy hacking patterns (single-metric success claims)

## Release gates (recommended)

Before tagging a new version:

- run regression suite on representative test cases
- validate that pinned references are correct
- verify that ledger spec fields can be populated
- confirm that policy defaults remain conservative (deny or simulate by default)

## Non-goals

This layer does not:
- provide code, scripts, or harnesses
- define compliance claims
- guarantee safety outcomes
