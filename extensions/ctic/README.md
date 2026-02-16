# CTIC (Cross-layer transactional integrity)

Status: draft  
Normative language: MUST / SHOULD / MAY

CTIC is an Interpretive Governance extension that prevents **dynamic transactional variables** (price, stock, delivery, promotions) from being silently fixed inside an interpretive layer.

It targets a specific failure mode:
- the interpretive layer displays a value (often cached or inferred),
- the transactional layer refreshes the value on interaction,
- users perceive an error (two truths), not a state change.

This extension defines:
- a minimal taxonomy for dynamic vs stable attributes,
- mandatory volatility signaling (source, freshness timestamp, status),
- invalidation rules on transactional refresh,
- an optional audit metric (DDI) to quantify divergence.

Canonical specification: `extensions/ctic/ctic.md`

Related artifacts:
- Schema: `schemas/ctic-compliance-report.schema.json`
- Example report: `examples/ctic-compliance-report.example.json`
