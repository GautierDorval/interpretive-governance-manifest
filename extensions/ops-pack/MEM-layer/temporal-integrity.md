# Temporal integrity (MEM-layer)

Status: draft

## 1. Requirement

A memory-aware system MUST prevent time drift from turning past-valid statements into present-valid claims.

## 2. Temporal fields

Each MemoryObject MUST include:
- `valid_from` (or explicit unknown)
- `valid_to` (or explicit unknown)
- `timestamp` (creation time)

## 3. Rules

- If the domain is time-sensitive (laws, prices, policies), `valid_to` SHOULD be required.
- If time validity is unknown, it MUST be explicit (`temporal_scope: unknown`).
- Consolidation MUST NOT widen temporal validity unless justified and logged.
- A MemoryObject past `valid_to` MUST NOT be used for factual outputs without revalidation.

## 4. Drift detection hooks (optional)

A system MAY periodically:
- re-check a subset of MemoryObjects against sources,
- invalidate/refresh items that are time-bound,
- log refresh events.
