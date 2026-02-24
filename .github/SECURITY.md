# Security policy

Interpretive Governance is **non-executable by design**.

This repository contains primarily:
- normative specifications (JSON, JSON-LD, Markdown), and
- minimal helper scripts (validation, hashing discipline) used for integrity checks.

## Reporting a security vulnerability

If you believe you have found a security issue in:
- scripts under `/scripts/`,
- GitHub Actions workflows under `/.github/workflows/`,
- or any other executable automation shipped with this repository,

please report it responsibly.

Preferred channel (if enabled): GitHub private vulnerability reporting / Security Advisories.

If private reporting is not available, contact the normative maintainer via the canonical identity page:
- https://gautierdorval.com/

Avoid publishing exploit details in a public issue before coordinated disclosure.

## Non-security reports

Issues related to:
- schema mismatches,
- hash mismatches,
- broken canonical URLs,
- pinning discipline defects,

should be reported as **integrity defects** via public issues.
