#!/usr/bin/env python3
"""Recompute or verify integrity hashes.

This repository declares a small set of *critical* files in:

  integrity/critical-files.txt

Their SHA-256 fingerprints are stored in:

  integrity/hashes.json

Usage:
  - Recompute (writes integrity/hashes.json):
      python scripts/recompute_integrity_hashes.py

  - Check mode (CI-friendly, does not write):
      python scripts/recompute_integrity_hashes.py --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from typing import Dict, List


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRITICAL_LIST_PATH = os.path.join(ROOT, "integrity", "critical-files.txt")
HASHES_PATH = os.path.join(ROOT, "integrity", "hashes.json")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_critical_files() -> List[str]:
    if not os.path.exists(CRITICAL_LIST_PATH):
        raise FileNotFoundError(f"Missing critical list: {CRITICAL_LIST_PATH}")

    files: List[str] = []
    with open(CRITICAL_LIST_PATH, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            files.append(s)
    return files


def compute_hashes(files: List[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for rel in files:
        abs_path = os.path.join(ROOT, rel)
        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"Critical file not found: {rel}")
        out[rel] = sha256_file(abs_path)
    return out


def read_existing_hashes() -> Dict[str, str]:
    if not os.path.exists(HASHES_PATH):
        return {}
    with open(HASHES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def write_hashes(hashes: Dict[str, str]) -> None:
    os.makedirs(os.path.dirname(HASHES_PATH), exist_ok=True)
    with open(HASHES_PATH, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=2, sort_keys=True)
        f.write("\n")


def diff_hashes(expected: Dict[str, str], computed: Dict[str, str]) -> List[str]:
    lines: List[str] = []
    keys = sorted(set(expected.keys()) | set(computed.keys()))
    for k in keys:
        e = expected.get(k)
        c = computed.get(k)
        if e != c:
            if e is None:
                lines.append(f"+ {k} (missing in hashes.json) -> {c}")
            elif c is None:
                lines.append(f"- {k} (listed in hashes.json but not in critical list) -> {e}")
            else:
                lines.append(
                    "! "
                    + k
                    + "\n    expected: "
                    + str(e)
                    + "\n    computed: "
                    + str(c)
                )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Recompute or verify integrity/hashes.json for integrity/critical-files.txt."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="CI mode: do not write. Exit non-zero if hashes.json is out of date.",
    )
    args = parser.parse_args()

    critical_files = load_critical_files()
    computed = compute_hashes(critical_files)

    if args.check:
        existing = read_existing_hashes()
        diffs = diff_hashes(existing, computed)
        if diffs:
            print("❌ integrity/hashes.json is OUT OF DATE. Recompute and commit.")
            print("\n".join(diffs))
            sys.exit(1)
        print("✅ integrity/hashes.json OK.")
        return

    write_hashes(computed)
    print(f"✅ Updated integrity hashes -> {HASHES_PATH}")


if __name__ == "__main__":
    main()
