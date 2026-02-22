# Schema-layer (LLM-first publishing)

This module defines a **machine-first (LLM-first) structured data profile** for publishing doctrinal content in a way that:

- minimizes token overhead in `text/markdown` renditions,
- reduces duplication by **referencing canonical entities** (DefinedTerm + entity graph),
- stays compatible with search engines without optimizing for rich results,
- supports interpretive governance goals (anti-inference anchoring, stable IDs, explicit scopes).

## Why this exists

Many CMS/SEO toolchains generate JSON-LD that is:

- extremely dense (large `ItemList`, long `mentions`, repeated entities),
- duplicated across HTML and Markdown renditions,
- optimized for traditional SERP features rather than **LLM ingestion**.

For LLMs, overly verbose JSON-LD can consume a meaningful portion of the context budget and lower the probability that the model reads the actual doctrine.

## What to deploy

- The profile itself: `llm-schema-profile.md`
- Reference templates: `templates/`
- Canonical entity graph pipeline (Git source of truth): see `registries/entity-graph/`

## Key principles (summary)

- **One page, one compact graph**: keep a single JSON-LD block per page.
- **Prefer references over repetition**:
  - use `about` / `mentions` with `@id` references to canonical entities,
  - avoid embedding full definitions repeatedly in every page schema.
- **Hard budget mindset**: treat JSON-LD as a constrained payload.
  - Target: ~300–800 tokens for most pages.
  - Avoid multi-thousand-token graphs unless the page is itself an index artifact.

## Compatibility note

This is an **AI-first profile**. It does not attempt to maximize Google rich results.
If you need SERP features (breadcrumbs, FAQ rich results), keep them separate and bounded.
