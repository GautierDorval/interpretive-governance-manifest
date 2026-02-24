#!/usr/bin/env python3
import json
import re
from pathlib import Path
from typing import Any, Iterable


MANIFEST = Path("interpretive-governance.manifest.json")
WELL_KNOWN = Path(".well-known/interpretive-governance.json")

RAW_GH_RE = re.compile(r"^https://raw\.githubusercontent\.com/[^/]+/[^/]+/([^/]+)/")


def load_json(path: Path) -> Any:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"ERROR: failed to parse {path}: {exc}")


def iter_string_values(node: Any) -> Iterable[str]:
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from iter_string_values(v)
    elif isinstance(node, list):
        for v in node:
            yield from iter_string_values(v)


def find_pinned_blocks(node: Any, path: str = "") -> list[tuple[str, str, str]]:
    """
    Returns list of (json_path, pinned_version, raw_base) for any dict containing both keys.
    """
    found: list[tuple[str, str, str]] = []
    if isinstance(node, dict):
        if "pinned_version" in node and "raw_base" in node:
            pv = node.get("pinned_version")
            rb = node.get("raw_base")
            if isinstance(pv, str) and isinstance(rb, str):
                found.append((path or "$", pv, rb))
        for k, v in node.items():
            child_path = f"{path}.{k}" if path else k
            found.extend(find_pinned_blocks(v, child_path))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            child_path = f"{path}[{i}]"
            found.extend(find_pinned_blocks(v, child_path))
    return found


def main() -> int:
    manifest = load_json(MANIFEST)
    well_known = load_json(WELL_KNOWN)

    errors: list[str] = []

    # 1) raw URL discipline: never reference main/master for raw.githubusercontent.com
    for doc_name, doc in [("manifest", manifest), ("well_known", well_known)]:
        for s in iter_string_values(doc):
            if "https://raw.githubusercontent.com/" in s:
                if "/main/" in s or "/master/" in s:
                    errors.append(f"{doc_name}: unpinned raw URL (main/master): {s}")

    # 2) parity: pinned_version must match raw_base version segment and raw_base must not be main/master
    for doc_name, doc in [("manifest", manifest), ("well_known", well_known)]:
        blocks = find_pinned_blocks(doc)
        for jpath, pinned_version, raw_base in blocks:
            if "/main/" in raw_base or "/master/" in raw_base:
                errors.append(f"{doc_name}: raw_base is unpinned (main/master) at {jpath}: {raw_base}")
                continue

            # Ensure raw_base contains `/{pinned_version}/`
            expected_segment = f"/{pinned_version}/"
            if expected_segment not in raw_base:
                m = RAW_GH_RE.match(raw_base)
                version_seg = m.group(1) if m else "(unknown)"
                errors.append(
                    f"{doc_name}: pinned_version/raw_base mismatch at {jpath}: "
                    f"pinned_version={pinned_version}, raw_base={raw_base} (raw segment={version_seg})"
                )

            # Ensure raw_base ends with a trailing slash for stable concatenation
            if not raw_base.endswith("/"):
                errors.append(f"{doc_name}: raw_base should end with '/': {raw_base} (at {jpath})")

    if errors:
        print("Pinned raw URL discipline verification failed:")
        for e in errors:
            print(f" - {e}")
        return 1

    print("Pinned raw URL discipline verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
