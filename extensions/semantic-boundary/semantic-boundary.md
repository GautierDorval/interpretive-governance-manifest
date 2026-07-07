# Semantic-boundary

Status: proposed  
Normative language: MUST / SHOULD / MAY

## 1. Purpose

Semantic-boundary declares concepts, claims, entities, or surfaces that are close enough to be confused but not equivalent.

It exists to prevent a machine system from turning semantic, lexical, vector, topical, or entity proximity into equivalence, proof, causality, recommendation, or guarantee.

## 2. Scope

Semantic-boundary applies to:

- false-neighbor declarations;
- semantic proximity separation;
- non-equivalence boundaries;
- proximity-risk documentation;
- behavioral testsets proposed for future measurement.

Semantic-boundary does not define causal relevance. That belongs to CCL when explicitly declared.

## 3. Normative rules

### SB-1: Proximity is not equivalence

An implementation MUST NOT treat semantic, lexical, vector, topical, or entity proximity as equivalence unless an authoritative source declares equivalence.

### SB-2: Neighboring concepts require explicit relation types

When two concepts are close but not identical, the implementation SHOULD declare the relation type.

### SB-3: False neighbors must declare prohibited fusions

A false-neighbor declaration MUST identify the fusion or substitution that is prohibited.

### SB-4: Boundary tests must not pretend to be measurements

A behavioral testset is a proposed instrument until model runs, judge criteria, prompts, dates, and outputs are published.

### SB-5: Semantic-boundary does not define causal relevance

Semantic-boundary may identify proximity risks, but it MUST NOT infer the need-state, trigger, or consequence chain of a surface.
