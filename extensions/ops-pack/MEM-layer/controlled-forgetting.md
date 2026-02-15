# Controlled forgetting (MEM-layer)

Status: draft

## 1. Principle

Forgetting MUST be a governed operation. Silent deletion breaks auditability.

## 2. Allowed operations

- `invalidate`: mark object as not to be used for factual claims
- `archive`: move object to cold storage while keeping references
- `supersede`: mark object replaced by a newer object

Each operation MUST:
- preserve prior versions
- log an append-only event with reason

## 3. Required reasons

Reasons SHOULD be one of:
- obsolescence
- conflict
- correction
- policy constraint
- user request (with scope and limitations)

## 4. Prohibited operations

- physical deletion without trace
- mutation without version bump
- mutation without MemoryLog entry
