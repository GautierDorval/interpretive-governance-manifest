# CTIC (Cross-layer transactional integrity)

Status: draft  
Normative language: MUST / SHOULD / MAY

## 1. Purpose

CTIC prevents a common integrity failure in transaction-adjacent systems:

- the interpretive layer states a transactional value early (often cached, stale, or inferred),
- the transactional layer refreshes the value on user interaction,
- the system yields two conflicting values for the same entity,
- the user perceives an error (loss of trust), not a state change.

CTIC does not attempt to guarantee market truth. It constrains how dynamic variables are represented, signaled, refreshed, and audited.

## 2. Scope

CTIC applies when a system includes both:

- an **interpretive layer** (text synthesis, recommendation, justification), and
- a **transactional layer** (shopping cards, checkout, inventory, live quotes, offers).

CTIC is domain-agnostic. It applies to any dynamic variable, including:

- price, taxes, discounts, promotions
- stock, availability
- delivery windows
- exchange rates
- real-time metrics and quotes

## 3. Definitions

- **Interpretive layer**: A surface that produces interpretation, recommendation, or explanation.
- **Transactional layer**: A surface that presents or executes market-state variables (price, stock, delivery, seller) and can refresh them.
- **Dynamic attribute**: A value that can change without changing the identity of the referenced entity.
- **Agent-dependent attribute**: A value that depends on an agent (seller, marketplace, region, account, channel).
- **Volatility signal**: Minimal metadata that makes a dynamic attribute safe to show (source, freshness timestamp, status).
- **Refresh event**: Any action that triggers a transactional recomputation (click, expand, scroll-triggered lazy load, explicit refresh).

## 4. Attribute taxonomy (required)

A system implementing CTIC MUST classify surfaced attributes into at least:

- **A1 stable**: intrinsic properties that do not change across vendors and time (within reasonable tolerance).
- **A2 semi-stable**: properties that may vary by model revision, batch, or jurisdiction, but are not market-state variables.
- **A3 dynamic**: market-state variables that change over time (price, stock, delivery, promotions).
- **A4 agent-dependent**: variables that depend on the seller, marketplace, account, region, or channel.

A3 and A4 are treated as volatile by default.

## 5. Normative rules

### CTIC-1: Non-fixation (MUST)

The interpretive layer MUST NOT present an A3 or A4 value as an intrinsic property of the entity.

Allowed patterns:
- constraints ("under 150 $", "often under 150 $")
- classes ("budget", "mid-range")
- relative comparisons ("cheaper than X")

Disallowed pattern:
- an exact transactional value presented without volatility signaling.

### CTIC-2: Layer separation (MUST)

If a transactional layer exists and is responsible for refresh, the system MUST treat it as the authoritative surface for A3/A4 exact values.

The interpretive layer SHOULD avoid exact A3/A4 values unless the user explicitly requests them.

### CTIC-3: Volatility signaling (MUST)

If an A3/A4 value is displayed anywhere, it MUST carry a volatility signal with at least:

- **source**: where the value comes from (provider, marketplace, seller feed)
- **capturedAt**: an ISO 8601 timestamp
- **status**: one of `indicative`, `estimated`, `real_time`

For monetary values, the system MUST also signal:
- currency (ISO 4217)
- pricing convention when applicable (tax included or excluded, shipping included or excluded)

### CTIC-4: Invalidation on refresh (MUST)

When a refresh event updates an A3/A4 value in the transactional layer, any earlier surfaced value for the same entity MUST be:

- updated, or
- invalidated, or
- explicitly marked as stale/obsolete.

Two conflicting values MUST NOT remain concurrently presented without a clear staleness marker.

### CTIC-5: Anti-anchoring (SHOULD)

The system SHOULD avoid presenting an exact A3/A4 value before:

- an explicit user request ("what is the price") or
- an explicit budget constraint that requires filtering.

Rationale: the first seen number becomes a cognitive anchor and increases interpretive debt.

### CTIC-6: Locale and jurisdiction clarity (MUST)

If the system presents market-state variables, it MUST not silently mix jurisdictions.

Minimum requirement:
- display locale or region context when it affects interpretation
- avoid implicit tax and shipping conventions

## 6. Conformance levels

CTIC defines four incremental conformance levels:

- **CTIC-Info**: CTIC-1 and CTIC-2, plus a user-facing variability note.
- **CTIC-Signal**: CTIC-Info plus CTIC-3.
- **CTIC-Sync**: CTIC-Signal plus CTIC-4.
- **CTIC-Audit**: CTIC-Sync plus reporting under the CTIC compliance report schema and optional divergence metrics.

## 7. DDI (Dynamic Divergence Index)

DDI is an optional audit metric to quantify cross-layer divergence.

Minimum recommended fields:
- `divergence_frequency`: ratio of sessions where divergence occurs
- `divergence_amplitude_pct_mean`: mean divergence amplitude in percent
- `window_days`: observation window in days

DDI is not a truth metric. It is a stability and trust metric.

## 8. Compliance reports

CTIC-Audit implementations SHOULD produce JSON reports conforming to:

- `schemas/ctic-compliance-report.schema.json`

A minimal example is provided in:

- `examples/ctic-compliance-report.example.json`

