# Memory consolidation policy (MEM-layer)

Status: draft

Consolidation is a high-risk operation because it can convert inference into durable memory.

## 1. Consolidation gates

A consolidation operation MUST be blocked unless all gates pass:

### Gate A: Typing
- All input MemoryObjects MUST be typed.
- Output MUST be `ConsolidatedStatement`.

### Gate B: Traceability
- Output MUST contain `source_refs` that cover the informational content.
- If any critical fragment has no source, output MUST mark it as derived and MUST NOT elevate confidence.

### Gate C: Temporal validity
- Output MUST carry a temporal scope at least as restrictive as the strictest input.
- If any input is time-bound, output MUST be time-bound unless justified.

### Gate D: Conflict handling
- If inputs conflict, output MUST:
  - either refuse consolidation, or
  - record explicit conflict, with a non-factual verdict for the disputed part.

### Gate E: Audit event
- A MemoryLog event MUST record:
  - input ids
  - output id
  - justification
  - diff or deterministic reconstruction steps

## 2. Prohibited patterns

- “Compression without provenance”: summarizing multiple items into a durable statement without preserving sources.
- “Confidence escalation by rewrite”: rewriting an inference into factual language without source reinforcement.
- “Silent merge”: merging objects without a MemoryLog event.
