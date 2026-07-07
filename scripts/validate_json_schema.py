#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

REQUIRED_MAPPINGS = [
    ("interpretive-governance.manifest.json", "schemas/manifest.schema.json"),
    ("interpretive-index.json", "schemas/interpretive-index.schema.json"),
    ("authority/authority-policy.json", "schemas/authority/authority-policy.schema.json"),
    ("examples/ctic-compliance-report.example.json", "schemas/ctic-compliance-report.schema.json"),
    ("examples/causal-context-layer.example.json", "schemas/causal-context-layer.schema.json"),
    ("examples/causal-context-map.example.json", "schemas/causal-context-map.schema.json"),
    ("examples/causal-internal-mesh.example.json", "schemas/causal-internal-mesh.schema.json"),
    ("examples/semantic-proximity-separation.example.json", "schemas/semantic-proximity-separation.schema.json"),
    ("examples/false-neighbors.example.json", "schemas/false-neighbors.schema.json"),
    ("examples/false-neighbor-behavioral-testset.example.json", "schemas/false-neighbor-behavioral-testset.schema.json"),
    ("examples/proximity-causality-protocol.example.json", "schemas/proximity-causality-protocol.schema.json"),
    ("examples/governance-package-manifest.example.json", "schemas/governance-package-manifest.schema.json"),
    ("examples/model-panel-declaration.example.json", "schemas/model-panel-declaration.schema.json"),
    ("examples/judge-panel-declaration.example.json", "schemas/judge-panel-declaration.schema.json"),
    ("examples/false-neighbor-behavioral-run.example.json", "schemas/false-neighbor-behavioral-run.schema.json"),
    ("examples/proximity-causality-evaluation-run.example.json", "schemas/proximity-causality-evaluation-run.schema.json"),
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def validate_pair(data_path: Path, schema_path: Path):
    if not data_path.exists():
        raise FileNotFoundError(f"Missing JSON file: {data_path}")
    if not schema_path.exists():
        raise FileNotFoundError(f"Missing schema file: {schema_path}")

    instance = load_json(data_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    validator.validate(instance)

def main() -> int:
    errors = []
    validated = []

    for data_rel, schema_rel in REQUIRED_MAPPINGS:
        data_path = Path(data_rel)
        schema_path = Path(schema_rel)
        try:
            validate_pair(data_path, schema_path)
            validated.append((data_rel, schema_rel))
        except Exception as exc:
            errors.append(f"Required mapping failed: {data_rel} -> {schema_rel}: {exc}")

    authority_dir = Path("authority")
    authority_schema_dir = Path("schemas/authority")
    if authority_dir.exists() and authority_schema_dir.exists():
        for data_path in sorted(authority_dir.glob("*.json")):
            schema_path = authority_schema_dir / f"{data_path.stem}.schema.json"
            if not schema_path.exists():
                continue

            mapping = (str(data_path), str(schema_path))
            if mapping in validated:
                continue

            try:
                validate_pair(data_path, schema_path)
                validated.append(mapping)
            except Exception as exc:
                errors.append(f"Authority mapping failed: {data_path} -> {schema_path}: {exc}")

    if errors:
        print("JSON Schema validation failed:")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"JSON Schema validation passed for {len(validated)} file(s).")
    for data_rel, schema_rel in validated:
        print(f" - {data_rel} -> {schema_rel}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
