#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

CRITICAL_LIST = Path("integrity/critical-files.txt")
OUT = Path("integrity/hashes.json")

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    if not CRITICAL_LIST.exists():
        raise SystemExit("Missing integrity/critical-files.txt")

    critical = [
        line.strip()
        for line in CRITICAL_LIST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

    hashes = {}
    for rel in critical:
        p = Path(rel)
        if not p.exists():
            raise SystemExit(f"Missing critical file: {rel}")
        hashes[rel] = sha256(p)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"Wrote {OUT} with {len(hashes)} hash(es).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
