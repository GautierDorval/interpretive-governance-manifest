## Summary

Describe what this PR changes and why.

## Change classification (choose one)

- [ ] Normative (changes meaning / enforceable constraints)
- [ ] Non-normative (usability improvements without changing meaning)
- [ ] Editorial (wording / formatting without changing meaning)
- [ ] Operational integrity (hashing discipline, schema validation, workflows, pinning discipline)

## Affected artifacts

List the affected path(s), especially if they are normative or critical.

## Notes for reviewers

Anything that helps reviewers validate non-drift intent, compatibility, or scope boundaries.

## Checklist

- [ ] Linked issue (unless purely editorial)
- [ ] JSON syntax validation passes (CI)
- [ ] JSON Schema validation passes (CI)

### Integrity discipline (required when critical artifacts change)

Critical artifacts are listed in `integrity/critical-files.txt`.

If any of them changed, confirm:

- [ ] `CHANGELOG.md` updated
- [ ] `integrity/hashes.json` updated
- [ ] `python scripts/verify_integrity_hashes.py` passes

### Pinning discipline

- [ ] No `raw.githubusercontent.com/.../main/...` or `.../master/...` URLs introduced
- [ ] `python scripts/verify_pinned_raw_parity.py` passes

### Local quick checks (optional but recommended)

```bash
python scripts/validate_json_syntax.py
python scripts/validate_json_schema.py
python scripts/verify_integrity_hashes.py
python scripts/verify_pinned_raw_parity.py
```
