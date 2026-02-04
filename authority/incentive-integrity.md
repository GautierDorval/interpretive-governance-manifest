# Incentive integrity (anti proxy hacking)

## Purpose

This document defines minimal constraints to prevent authority decisions from being granted on weak proxies.

Authority must not be granted solely because a single metric appears optimized.

## Core constraints

### 1) No single-metric authority

For high and critical action classes:
- authority decisions MUST not rely on a single metric or objective
- at least two independent criteria MUST be satisfied (multi-criteria)

Examples:
- correctness + safety
- usefulness + reversibility proof
- business intent match + privacy constraints

### 2) Proxy drift detection

If proxy behavior diverges from intended outcomes, the system MUST:
- escalate, or
- degrade to simulation-only, or
- deny authority for that action class until policy update

### 3) Tripwires (stop conditions)

Authority decisions MUST support stop conditions such as:
- unexpected target changes
- repeated near-miss patterns
- inconsistent evidence pointers
- conflicting role outputs (planner vs critic)

Tripwire activation MUST be recorded in the ledger.

### 4) Trade-off logging

When objectives conflict, the decision MUST:
- record the chosen trade-off rationale
- record which constraints dominated
- include references to the applied policy rules

## Non-goals

This document does not:
- define optimal objective functions
- prescribe RL methods or reward shaping
- provide implementation recipes for detection systems
