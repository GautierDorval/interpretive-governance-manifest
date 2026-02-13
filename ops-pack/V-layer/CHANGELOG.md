# CHANGELOG — ops-pack (V-Layer)

## 1.2.0 — Integrity locking (V-Layer extension)

- Introduced **Integrity locking (artifact hashing)** as an optional V-Layer mechanism.
- Added `ops-pack/V-layer/integrity-locks.md`.
- Clarified SHA-256 fingerprinting discipline for critical machine-first artifacts.
- Defined scope boundaries: integrity hashes are drift-control signals, not authority proofs.
- No changes to interpretive core, Q-Layer semantics, or executable authority boundaries.

Integrity lock (reference implementation surface):
- entity-graph.jsonld (raw bytes): https://gautierdorval.com/entity-graph.jsonld
- SHA-256: 84ebf95a30e60335f265e0fa89f0592717c20fc5527831bfff8fc5e5121e0681

## 1.1.0

- Added Integrity locking (artifact hashing) as an optional V-Layer mechanism.
- Introduced SHA-256 fingerprinting guidance for critical machine-first artifacts.
- Clarified scope: integrity hashes are drift-control signals, not authority proofs.
- Added integrity-locks.md to formalize artifact fingerprint discipline.

## 1.0.0

- Initial publication of V-Layer: versioning, drift, and change control.
