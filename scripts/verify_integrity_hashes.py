#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path


CRITICAL_LIST = Path("integrity/critical-files.txt")
HASHES = Path("integrity/hashes.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_critical_list() -> list[str]:
    if not CRITICAL_LIST.exists():
        raise SystemExit("ERROR: integrity/critical-files.txt is missing.")
    critical: list[str] = []
    for line in CRITICAL_LIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        critical.append(line)
    return critical


def load_hashes() -> dict[str, str]:
    if not HASHES.exists():
        raise SystemExit("ERROR: integrity/hashes.json is missing.")
    try:
        return json.loads(HASHES.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"ERROR: failed to parse integrity/hashes.json: {exc}")


def main() -> int:
    critical = load_critical_list()
    expected = load_hashes()

    errors: list[str] = []

    critical_set = set(critical)
    expected_set = set(expected.keys())

    missing_keys = sorted(critical_set - expected_set)
    extra_keys = sorted(expected_set - critical_set)

    if missing_keys:
        errors.append("hashes.json is missing critical file entries:")
        for k in missing_keys:
            errors.append(f" - {k}")

    if extra_keys:
        errors.append("hashes.json contains entries not listed as critical:")
        for k in extra_keys:
            errors.append(f" - {k}")

    for rel in critical:
        path = Path(rel)
        if not path.exists():
            errors.append(f"Missing critical file on disk: {rel}")
            continue
        if rel not in expected:
            continue
        actual = sha256(path)
        if actual != expected[rel]:
            errors.append(f"Hash mismatch: {rel}")
            errors.append(f" - expected: {expected[rel]}")
            errors.append(f" - actual:   {actual}")

    if errors:
        print("Integrity hash verification failed:")
        for e in errors:
            print(e)
        print()
        print("Hint: to recompute hashes.json, run:")
        print("  python scripts/recompute_integrity_hashes.py")
        return 1

    print("Integrity hash verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
