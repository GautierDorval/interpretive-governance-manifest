# Entity graph registry (historical snapshot)

This directory and the generated root files `entity-graph.jsonld` and `entity-graph.yaml` are a **historical snapshot** of the entity graph of gautierdorval.com (last content change: 2026-07-07). They are kept for traceability and are **not** the source of the graph served today on:

- `https://gautierdorval.com/entity-graph.jsonld`
- `https://gautierdorval.com/entity-graph.yaml` (fallback)

The served graph is maintained with the gautierdorval.com governance overlay and prevails for those URLs. Its canonical person identifier is `https://gautierdorval.com/en/entity/#person`; `https://gautierdorval.com/entite/#person`, used in this snapshot, is a legacy alias.

Do not resynchronize this snapshot from the served graph, and do not read it as current identity data.

## Files

- `entity-graph.source.yaml`
  - YAML representation of the snapshot graph.
  - Edit only to maintain the snapshot tooling; identity changes belong to the served graph.
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

