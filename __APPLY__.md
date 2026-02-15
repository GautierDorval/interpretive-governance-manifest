# Apply this patch

This ZIP contains corrected files to prepare the `interpretive-governance-manifest` repository for release 1.4.0.

## What it fixes

1) Avoids a naming collision:
- `ops-pack/M-layer/` is already used for multi-agent coordination.
- Memory governance is therefore renamed to **MEM-layer** under `extensions/ops-pack/`.

2) Fixes schema `$id` fields:
- Replaces `example.org` with `interpretive-governance.org` for memory schemas.

## How to apply

- Extract the ZIP at the root of the repository (overwrite existing files).
- Ensure `extensions/ops-pack/MEM-layer/` exists after extraction.
- The legacy directory `extensions/ops-pack/M-layer/` remains as redirect stubs.

Optional cleanup:
- If you prefer, you may delete the legacy redirect stubs under `extensions/ops-pack/M-layer/` after updating all references.
