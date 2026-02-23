#!/usr/bin/env python3
"""Generate canonical entity-graph artifacts from a YAML source.

This repo uses Git as the single source of truth for the entity graph content.
We keep an editable YAML source and generate:
- entity-graph.jsonld (canonical JSON-LD, stable formatting)
- entity-graph.yaml (human/LLM fallback index, including integrity SHA-256)

Usage:
  python scripts/generate_entity_graph.py
  python scripts/generate_entity_graph.py --check

"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml


DEFAULT_SOURCE = Path("registries/entity-graph/entity-graph.source.yaml")
DEFAULT_OUT_JSONLD = Path("entity-graph.jsonld")
DEFAULT_OUT_YAML = Path("entity-graph.yaml")


def _sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def _read_yaml(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return data


def _validate_graph(doc: Dict[str, Any], source_path: Path) -> None:
    if "@context" not in doc or "@graph" not in doc:
        raise ValueError(f"Missing @context or @graph in {source_path}")
    if doc["@context"] != "https://schema.org":
        raise ValueError(f"@context must be https://schema.org in {source_path}")
    if not isinstance(doc["@graph"], list):
        raise ValueError(f"@graph must be a list in {source_path}")
    # Minimal sanity: each node should be a mapping with @type and @id.
    for i, node in enumerate(doc["@graph"]):
        if not isinstance(node, dict):
            raise ValueError(f"@graph[{i}] must be a mapping in {source_path}")
        if "@type" not in node or "@id" not in node:
            raise ValueError(f"@graph[{i}] must include @type and @id in {source_path}")


def _serialize_jsonld(doc: Dict[str, Any]) -> bytes:
    # Stable formatting for deterministic hashing and diffs.
    return (json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _extract_index(doc: Dict[str, Any], source_path: Path) -> Dict[str, Any]:
    """Build a compact YAML index from the JSON-LD graph.

    This file is *not* the source of truth; it is a fallback encoding for
    quick reading and for systems that prefer YAML.
    """
    graph: List[Dict[str, Any]] = doc.get("@graph", [])
    by_type: Dict[str, List[Dict[str, Any]]] = {}
    for node in graph:
        t = node.get("@type")
        if isinstance(t, list):
            for tt in t:
                by_type.setdefault(str(tt), []).append(node)
        else:
            by_type.setdefault(str(t), []).append(node)

    # Pick the canonical person (prefer /entite/ id)
    persons = by_type.get("Person", [])
    person = None
    for p in persons:
        if isinstance(p.get("@id"), str) and "/entite/" in p["@id"]:
            person = p
            break
    if person is None and persons:
        person = persons[0]

    websites = by_type.get("WebSite", [])
    website = websites[0] if websites else None

    term_sets = by_type.get("DefinedTermSet", [])
    defined_terms = by_type.get("DefinedTerm", [])
    term_by_id = {t.get("@id"): t for t in defined_terms if isinstance(t, dict) and isinstance(t.get("@id"), str)}

    term_sets_out: List[Dict[str, Any]] = []
    for ts in term_sets:
        ts_id = ts.get("@id")
        out: Dict[str, Any] = {
            "id": ts_id,
            "type": "DefinedTermSet",
            "name": ts.get("name"),
            "description": ts.get("description"),
        }
        hdt = ts.get("hasDefinedTerm", [])
        if isinstance(hdt, list):
            term_ids = []
            term_urls = []
            for ref in hdt:
                if isinstance(ref, dict) and "@id" in ref and isinstance(ref["@id"], str):
                    term_ids.append(ref["@id"])
                    term = term_by_id.get(ref["@id"])
                    if isinstance(term, dict) and isinstance(term.get("url"), str):
                        term_urls.append(term["url"])
            if term_ids:
                out["term_ids"] = term_ids
            if term_urls:
                out["term_urls"] = term_urls
        term_sets_out.append(out)

    index: Dict[str, Any] = {
        "schemaVersion": "1.0",
        "type": "yaml-fallback",
        "canonical": "https://gautierdorval.com/entity-graph.jsonld",
        "source_repo": "https://github.com/GautierDorval/interpretive-governance-manifest",
        "source_path": str(source_path).replace("\\", "/"),
        "generated_from": str(source_path).replace("\\", "/"),
    }

    if person:
        index["person"] = {
            "id": person.get("@id"),
            "name": person.get("name"),
            "url": person.get("url"),
            "sameAs": person.get("sameAs"),
        }
    if website:
        index["website"] = {
            "id": website.get("@id"),
            "url": website.get("url"),
            "name": website.get("name"),
            "inLanguage": website.get("inLanguage"),
        }

    if term_sets_out:
        # Stable order: by name then id.
        term_sets_out.sort(key=lambda d: (str(d.get("name") or ""), str(d.get("id") or "")))
        index["definedTermSets"] = term_sets_out

    return index


def _serialize_yaml(doc: Dict[str, Any]) -> bytes:
    # Deterministic YAML dump for diffs.
    return (yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120) + "\n").encode("utf-8")


def _read_bytes_if_exists(path: Path) -> bytes | None:
    if not path.exists():
        return None
    return path.read_bytes()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="YAML source path")
    ap.add_argument("--out-jsonld", type=Path, default=DEFAULT_OUT_JSONLD, help="Output JSON-LD path")
    ap.add_argument("--out-yaml", type=Path, default=DEFAULT_OUT_YAML, help="Output YAML fallback path")
    ap.add_argument("--check", action="store_true", help="Fail if outputs differ from committed files")
    args = ap.parse_args()

    source_path: Path = args.source
    out_jsonld: Path = args.out_jsonld
    out_yaml: Path = args.out_yaml

    doc = _read_yaml(source_path)
    _validate_graph(doc, source_path)

    jsonld_bytes = _serialize_jsonld(doc)
    sha = _sha256_bytes(jsonld_bytes)

    index_doc = _extract_index(doc, source_path)
    index_doc["source_sha256"] = sha
    yaml_bytes = _serialize_yaml(index_doc)

    if args.check:
        existing_jsonld = _read_bytes_if_exists(out_jsonld)
        existing_yaml = _read_bytes_if_exists(out_yaml)
        ok = True
        if existing_jsonld != jsonld_bytes:
            print(f"ERROR: {out_jsonld} is out of date. Re-run generation.")
            ok = False
        if existing_yaml != yaml_bytes:
            print(f"ERROR: {out_yaml} is out of date. Re-run generation.")
            ok = False
        return 0 if ok else 1

    out_jsonld.write_bytes(jsonld_bytes)
    out_yaml.write_bytes(yaml_bytes)

    print(f"Wrote {out_jsonld} (sha256={sha})")
    print(f"Wrote {out_yaml}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
