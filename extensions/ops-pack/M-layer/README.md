# M-layer (Memory governance)

The M-layer defines operational constraints for stateful systems that persist memory:
- memory object requirements
- consolidation policy
- controlled forgetting
- temporal integrity
- logging minimums

This layer is designed to extend the core primitives introduced in `versions/0.2.0/`.

## Files

- `memory-governance.md` (overview + invariants)
- `memory-consolidation-policy.md` (gates for consolidation)
- `temporal-integrity.md` (time validity rules)
- `controlled-forgetting.md` (no silent deletion)
- `memory-logging-minimum.md` (append-only log discipline)
- `examples/` (objects, logs, conformance break scenario)
