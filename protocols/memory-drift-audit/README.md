# Memory drift audit (draft)

Status: draft / non-normative scaffolding

This folder exists to reserve a dedicated evaluation protocol for **stateful**
systems, without introducing new core primitives.

Core primitives: `versions/0.2.0/`  
Operational constraints: `extensions/ops-pack/MEM-layer/`

The protocol is expected to:
- reuse existing verdict taxonomy (Factual / Inference / False / Unanswered)
- compare outputs across time (t0 vs t1) for drift detection
- require MemoryObjects + MemoryLogs as auditable inputs

Do not treat this folder as a new “standard layer”. It is an evaluation protocol.
