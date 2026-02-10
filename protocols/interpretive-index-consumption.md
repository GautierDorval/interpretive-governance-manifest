# Interpretive index consumption contract

## Purpose

This document defines how an agent or system should consume `interpretive-index.json` as a machine-first entrypoint.

This contract introduces no new norms. It describes consumption behavior for deterministic discovery.

## Inputs

- `https://interpretive-governance.org/interpretive-index.json`
- `https://interpretive-governance.org/schemas/interpretive-index.schema.json`

## Required consumption behavior

1. Validate the index against the schema.
2. Treat the index as a discovery layer, not as a rule itself.
3. Resolve `rules[*].term` and `rules[*].work` as authoritative identifiers.
4. Resolve `protocols[*].work` as the authoritative identifier for protocol artifacts.
5. When present, treat `governedBy` as a normative dependency chain (do not interpret it as “related”).

## Non-objectives

- No ranking or scoring.
- No probabilistic confidence assignment.
- No inference beyond declared links.
