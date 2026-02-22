# LLM-first JSON-LD profile

This document defines a **compact JSON-LD profile** designed for LLM ingestion (especially via `Accept: text/markdown`).

It is aligned with interpretive governance goals: stable meaning, explicit boundaries, canonical references, and minimized ambiguity.

## Scope

This profile applies to:

- `WebPage` content (definitions, doctrine, frameworks, clarifications),
- `BlogPosting` content (phenomena, case notes, synthesis pivots),
- index pages (`CollectionPage` / `ItemList`) when strictly necessary.

## Design goals

1. **Minimal token overhead**
2. **Stable canonical IDs**
3. **High signal per field**
4. **Reference canonical registries instead of repeating definitions**
5. **Avoid SEO-driven verbosity that harms LLM consumption**

## Budget targets

These are not guarantees, but operational targets:

- Typical page JSON-LD: **300–800 tokens**
- High-density doctrinal page: **800–1 500 tokens**
- Index pages: **as small as possible**, prefer human Markdown lists over JSON-LD `ItemList`

## Graph composition rules

### Required nodes (most pages)

- `WebSite` (publisher context)
- `Person` (author/publisher)
- `ImageObject` for logo (optional but stable)
- One primary node:
  - `WebPage` for most pages
  - `BlogPosting` for articles

### Optional nodes

- `ImageObject` for the featured image
- `DefinedTerm` (only when the page is the definition page)
- `DefinedTermSet` (only when the page is a registry page)

### Avoid by default

- Large `ItemList` enumerations (keep lists in Markdown instead)
- Long `keywords` arrays (cap around ~12)
- `mentions` lists longer than ~10 entities
- Nested objects when an `@id` reference is sufficient
- Duplicating the same entity in multiple shapes

## ID conventions

- Website: `https://gautierdorval.com/#website`
- Canonical person: `https://gautierdorval.com/entite/#person`
- Person alias (legacy compatibility): `https://gautierdorval.com/#person` with `sameAs` → canonical person
- Page anchors:
  - WebPage: `{url}#webpage`
  - BlogPosting: `{url}#blogposting`
  - Primary image: `{imageUrl}#primaryimage`
  - DefinedTerm: `{termUrl}#definedterm`
  - DefinedTermSet: `{registryUrl}#definedtermset`

## Canonical reference strategy

### Entity graph

Publish and maintain a canonical entity graph, and use it as the **single place** where key entities and terms are defined.

- Canonical URL: `https://gautierdorval.com/entity-graph.jsonld`
- Git source of truth: `registries/entity-graph/entity-graph.source.yaml` (this repo)

On pages, prefer referencing entities by `@id` instead of embedding full objects.

### Defined terms

For term-driven doctrine, prefer:

- `about`: primary terms (2–5)
- `mentions`: secondary terms (0–10)

Example:

```json
"about": [
  { "@id": "https://gautierdorval.com/definitions/gouvernance-interpretative/#definedterm" },
  { "@id": "https://gautierdorval.com/definitions/dette-interpretative/#definedterm" }
]
```

## Minimal field set (recommended)

### WebPage

- `@type`: `WebPage`
- `@id`, `url`
- `name`, `headline` (can be same)
- `description`
- `inLanguage`
- `isPartOf` → `WebSite`
- `author` / `publisher` → `Person`
- `primaryImageOfPage` (if relevant)
- `datePublished`, `dateModified` (if available)
- `about` (references to DefinedTerm)
- `mentions` (references to other canonical entities)

### BlogPosting

Same as `WebPage`, plus:

- `mainEntityOfPage` (the WebPage id)
- `image` (featured ImageObject id)
- `articleSection` (category label, 1 string)
- `keywords` (bounded)

## Page-type specific guidance

### Definition pages

Use `DefinedTerm` as the `mainEntity` of the `WebPage`.

- `WebPage.mainEntity` → `DefinedTerm`
- `DefinedTerm.url` must point to the canonical definition URL.
- Include:
  - `name`, `alternateName`, `description`
  - `inDefinedTermSet` (reference)
  - `isRelatedTo` (references)

### Registry pages

Use `DefinedTermSet` as the `mainEntity` of the page, but do not enumerate all terms in JSON-LD unless strictly required.
Prefer human Markdown lists for the full index.

## Implementation notes for WordPress + Cloudflare Markdown

If Cloudflare returns `text/markdown` renditions that include your JSON-LD, the graph should be treated as a first-class payload.
Large SEO graphs can dominate the response and reduce doctrine ingestion.

Operationally:

- keep page JSON-LD compact,
- rely on the canonical entity graph for depth,
- validate token overhead regularly (ex. via `x-markdown-tokens` headers).

