#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path


CRITICAL_LIST = Path("integrity/critical-files.txt")


JSON_EXTENSIONS = {".json", ".jsonld"}


def read_critical_list() -> set[str]:
    if not CRITICAL_LIST.exists():
        raise SystemExit("ERROR: integrity/critical-files.txt is missing.")
    critical = set()
    for line in CRITICAL_LIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Only include JSON/JSON-LD files in the required set
        ext = Path(line).suffix.lower()
        if ext in JSON_EXTENSIONS:
            critical.add(line)
    return critical


def git_ls_json_files() -> list[str]:
    files = subprocess.check_output(
        ["git", "ls-files", "*.json", "*.jsonld"],
        text=True,
    ).splitlines()
    return [f.strip() for f in files if f.strip()]


def main() -> int:
    required = read_critical_list()
    files = git_ls_json_files()

    missing = sorted(required - set(files))
    if missing:
        print("Missing required files from JSON validation set:")
        for m in missing:
            print(f" - {m}")
        return 1

    errors: list[tuple[str, str]] = []
    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as fh:
                json.load(fh)
        except Exception as exc:
            errors.append((path, str(exc)))

    if errors:
        print("JSON/JSON-LD syntax validation failed:")
        for path, err in errors:
            print(f" - {path}: {err}")
        return 1

    print(f"Validated {len(files)} JSON/JSON-LD file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
