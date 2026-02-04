# V-Layer — versioning, drift, and change control

## Purpose

This layer makes governance maintainable over time.

Every authority decision must cite active governance versions.

## Semantic versioning

Governance artifacts SHOULD follow semver:
- MAJOR: breaking policy meaning
- MINOR: new rules or action classes
- PATCH: clarifications or fixes without semantic change

## Changelog discipline

A normative CHANGELOG must exist and record:
- what changed
- why it changed
- effective date
- compatibility notes

## Drift detection

Drift signals may include:
- rising near-miss rate
- increasing escalations for one action class
- repeated policy conflicts
- repeated tripwire activation

When drift is detected:
- degrade to simulation-only for affected classes, or
- escalate, or
- apply a controlled hotfix

## Compatibility mode

When policy changes, a compatibility period MAY be defined:
- older rules tolerated for a limited window
- window must be explicit
- decisions must cite which mode applied

## Hotfix procedure

A hotfix is an urgent policy change that must:
- be versioned
- be logged in CHANGELOG
- be referenced by subsequent ledger entries
