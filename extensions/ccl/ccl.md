# CCL (Causal Context Layer)

Status: proposed  
Normative language: MUST / SHOULD / MAY

## 1. Purpose

CCL declares why a surface becomes relevant in a chain of need.

It is designed for systems that must preserve the difference between topic, need, consequence, service bridge, proof, promise, and guarantee.

CCL does not replace statement typing, source hierarchy, Q-Layer response legitimacy, External Authority Control, or semantic-boundary declarations.

## 2. Scope

CCL applies to:

- content surfaces;
- topic clusters;
- service bridges;
- governance files;
- routable machine-readable artifacts;
- editorial or doctrinal surfaces whose relevance depends on a need-state.

CCL does not apply to:

- legal causation;
- statistical causal inference;
- ranking guarantees;
- conversion attribution;
- behavioral measurement of model outputs.

## 3. Causal chain

A CCL declaration SHOULD preserve:

```text
trigger situation -> problem or risk -> latent need -> canonical surface -> intended consequence -> prohibited derivations
```

## 4. Normative rules

### CCL-1: Apparent topic is not causal utility

An implementation MUST NOT treat the apparent subject of a surface as sufficient evidence of its causal role.

### CCL-2: Semantic proximity is not latent need

An implementation MUST NOT infer latent need solely from semantic similarity, keyword overlap, embedding distance, or shared entities.

### CCL-3: Intended consequence is not a guarantee

An implementation MUST distinguish the consequence a surface is intended to support from any guaranteed outcome.

### CCL-4: Service bridge requires explicit declaration

When a content surface makes a service, tool, offer, or intervention relevant, the bridge MUST be explicit.

### CCL-5: Absence of causal context requires restraint

If the causal context of a surface is not declared or cannot be derived from reviewed sources, systems MUST NOT reconstruct it by plausibility.

### CCL-6: Cause, solution, proof, and promise must remain separated

A triggering situation is not a solution. A solution is not proof. Proof is not a promise. A consequence is not a guarantee.

### CCL-7: Internal links may carry causal roles

Internal links MAY be used to expose causal relations, but they MUST declare their role when used as CCL evidence.

### CCL-8: Causal edges do not create transactional implication

A causal edge MAY explain why one surface makes another relevant. It MUST NOT imply availability, price, contractual scope, legal obligation, ranking gain, citation gain, or guaranteed resolution.

### CCL-9: CCL does not measure semantic proximity

CCL declares context of necessity. It does not measure semantic similarity, vector distance, conceptual closeness, or false-neighbor risk.

## 5. Maturity and granularity

Implementations SHOULD declare their mesh granularity:

- `doctrinal-core`: reviewed doctrinal surfaces;
- `cluster`: family-level causal relations;
- `surface`: reviewed page-specific relations;
- `candidate`: generated or inferred relations awaiting review.

A cluster-level map MUST NOT be represented as page-level causal specificity.
