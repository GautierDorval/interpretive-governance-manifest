# Non-objectives (authority governance)

## Purpose

This document defines explicit non-objectives for authority governance artifacts.

These non-objectives are normative and intentional.

## Non-objectives

### 1) No implementation recipes

This repository does not provide:
- production-ready orchestrators
- tool wiring patterns
- deployment playbooks
- configuration kits that can be directly reproduced as an execution system

Only normative contracts, schemas, and specifications are provided.

### 2) No bypass or exploitation guidance

This repository does not provide:
- bypass strategies
- prompt or tool injection techniques
- red-team exploitation instructions
- adversarial playbooks intended to defeat governance controls

### 3) No irreversible authority enablement

This repository does not provide:
- direct enablement for payments, deletions, provisioning, or deployment
- step-by-step instructions to operationalize irreversible actions
- “drop-in” mechanisms for high-risk execution

### 4) No claims of compliance

This repository does not claim:
- legal compliance
- regulatory certification
- safety guarantees

It provides governance primitives that can support auditability and operational controls.

## Rationale

Authority governance defines a normative boundary between inference and action.
Publishing implementation recipes would:
- collapse the boundary into an execution kit
- increase misuse potential
- undermine controlled reference demonstrations

## Allowed publications

The following are acceptable:
- definitions, taxonomies, policies, proof models, ledger specs
- non-normative examples that do not enable production execution
- controlled references that demonstrate separation without providing a full kit
