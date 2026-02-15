# Memory drift audit protocol (draft)

## 1. Goal

Detect and quantify drift introduced by memory persistence and consolidation
between two or more time points (t0, t1, ...).

## 2. Required inputs

- Model identity/version at each time point
- Corpus snapshot or source references
- MemoryObjects (export)
- MemoryLog (append-only export)
- QBank (question set) suitable for drift testing

## 3. Procedure (high-level)

1) Run baseline at t0 with Memory disabled or empty state (if possible).
2) Run stateful system at t0 with Memory enabled.
3) Persist memory state; record MemoryObjects + MemoryLog.
4) Run at t1 with same QBank; record outputs and memory changes.
5) Compare verdict distributions and drift indicators.

## 4. Minimal outputs

- drift summary
- list of conformance breaks (if any)
- evidence pack (memory exports + logs)
