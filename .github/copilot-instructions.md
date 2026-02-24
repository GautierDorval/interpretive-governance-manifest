# Copilot instructions — interpretive-governance-manifest

This repository is a **normative, machine-first standard** and a **stability surface**.

## Non-negotiable constraints

- Do not modify existing artifacts unless explicitly requested.
- Do not rename, move, or delete files/directories unless explicitly instructed and documented.
- Do not auto-format (prettier, remark, jq -S, etc.).
- Do not introduce unpinned raw URLs (never reference `main`/`master` in `raw.githubusercontent.com` links).
- Treat anything that could plausibly alter meaning as **normative**.

## Allowed change surface (default)

Prefer **add-only** changes under:
- `.github/workflows/`
- `scripts/`
- `integrity/`
- `Makefile`

Any other path is read-only unless explicitly authorized.

## Integrity discipline

Critical artifacts are listed in `integrity/critical-files.txt`.

If any critical artifact changes:
- update `CHANGELOG.md`, and
- update `integrity/hashes.json` (SHA-256).

Keep the repo:
- JSON-valid, and
- JSON Schema-valid.

## Review expectations

When proposing changes, include:
- explicit classification (normative / non-normative / editorial / operational integrity),
- affected artifact paths,
- compatibility and migration considerations (when applicable),
- and the minimal commands to validate.

## Repository philosophy

Prioritize:
- semantic stabilization,
- traceability over plausibility,
- explicit boundaries between observed, derived, inferred, unknown,
- and strict separation between inference and executable authority.

Do not introduce text that:
- blurs facts and inference,
- implies authority not explicitly declared,
- expands scope beyond stated boundaries,
- converts normative text into executable claims.
