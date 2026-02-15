# Memory logging minimum (M-layer)

Status: draft

## 1. Logging format

NDJSON is recommended (one JSON object per line).

## 2. Mandatory event types

- create
- consolidate
- invalidate
- archive
- policy_change
- conformance_break

## 3. Mandatory fields (all events)

- event_id
- event_type
- memory_object_id
- timestamp
- actor
- reason (required for invalidate/archive/conformance_break)
- prev_hash (when applicable)
- new_hash (when applicable)

## 4. Integrity

The system SHOULD:
- hash MemoryObjects (sha256)
- include hashes in an integrity lock artifact (if V-layer is used)
- log hash changes as part of events

If integrity artifacts are missing, high conformance claims SHOULD be refused.
