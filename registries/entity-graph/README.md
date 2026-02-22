# Entity graph registry (Git source of truth)

This directory contains the **source of truth** for the canonical entity graph served on:

- `https://gautierdorval.com/entity-graph.jsonld`
- `https://gautierdorval.com/entity-graph.yaml` (fallback)

## Files

- `entity-graph.source.yaml`
  - Editable YAML representation of the JSON-LD graph.
  - This is the only file you should edit.
- Generated artifacts (repo root):
  - `entity-graph.jsonld`
  - `entity-graph.yaml`

## Generate artifacts

```bash
python scripts/generate_entity_graph.py
```

To verify committed artifacts are up to date:

```bash
python scripts/generate_entity_graph.py --check
```

## Integrity

If the entity graph is treated as a critical machine-first artifact, update integrity hashes after regeneration:

```bash
python scripts/recompute_integrity_hashes.py
```

