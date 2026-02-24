PY ?= python3

.PHONY: all json-syntax json-schema integrity-verify pinning-verify recompute-hashes

all: json-syntax json-schema integrity-verify pinning-verify

json-syntax:
	$(PY) scripts/validate_json_syntax.py

json-schema:
	$(PY) scripts/validate_json_schema.py

integrity-verify:
	$(PY) scripts/verify_integrity_hashes.py

pinning-verify:
	$(PY) scripts/verify_pinned_raw_parity.py

recompute-hashes:
	$(PY) scripts/recompute_integrity_hashes.py
