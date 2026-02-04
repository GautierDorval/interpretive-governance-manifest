# P-Layer — privacy and data lineage

## Purpose

This layer defines minimal operational rules for data sensitivity, consent, lineage, retention, and redaction.

## Data classes

- none
- confidential
- pii
- secret

## Core rules

### Minimization

Collect, use, and log only what is necessary for the authority decision.

### Consent

When personal data is involved:
- consent must be explicit when required
- consent must be revocable when applicable
- consent status must be recorded (as a pointer, not raw data)

### Lineage

For sensitive decisions, record pointers to:
- data source
- transformation steps (if any)
- access scope

### Retention and purge

Define retention windows for:
- raw payloads
- redacted ledger entries
- proof artifacts

### No-log / no-train

For classes `pii` and `secret`, default to:
- no training use
- minimized logging (pointers + hashes only)

## Non-goals

This layer does not define legal compliance.
It defines operational primitives that support audits and controls.
