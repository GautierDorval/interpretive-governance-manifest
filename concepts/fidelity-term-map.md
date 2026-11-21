# Fidelity term map

**Status:** informative document (non-normative)  
**Version:** 1.1, 2026-11-20  
**Author:** Gautier Dorval  
**Version française :** [Carte des termes de fidélité](carte-des-termes-fidelite.md)

Within this corpus, the fidelity vocabulary covers a concept, its applications, evidence and measurement fields. Reading a claim accurately requires identifying **what is assessed, against which reference, for which task and through which method**.

| Term | Object | Intended reading |
|---|---|---|
| **Interpretive fidelity** | Relationship between a reconstruction and its reference | Preservation of the meaning and boundaries relevant to the task: facts, conditions, exclusions, authority, evidence and claim status. |
| **Reconstruction fidelity** | The same concept, in the context of this corpus's AI-generated answers | Within this corpus, a contextual entry term for interpretive fidelity, with the same conceptual scope. The expression has other published uses outside this corpus. |
| **Applicability fidelity** | Conditions under which information, an offer or a recommendation applies | Preservation of the prerequisites, exclusions and limits that determine applicability to a situation. |
| **Proof of fidelity** | Artifacts supporting examination of the relationship between an output and its reference | A documented set interpreted under a task and protocol: reference, output, criteria, observations and limits. |
| **`sequence_fidelity`** | Access sequences inferred from access logs, under the Q-Metrics contract | A ratio of inferred sessions whose sequence matches an expected pattern, within a declared window. It does not measure an answer's meaning. |
| **`semantic_fidelity`** | A dimension or field defined by a particular instrument | Read its definition and evaluation state in that contract. `NOT_EVALUATED` means that no assessment has been performed, not a score of zero. |

## Reference points

- The [interpretive fidelity definition](https://gautierdorval.com/en/definitions/interpretive-fidelity/) is the author reference for the concept.
- The [reconstruction fidelity entry page](https://gautierdorval.com/en/reconstruction-fidelity/) presents its application to understanding and assessing generated answers.
- The [terminology note](reconstruction-fidelity.md) declares the relationship between reconstruction fidelity and interpretive fidelity within this corpus.
- The [applicability fidelity definition](https://gautierdorval.com/en/definitions/applicability-fidelity/) specifies the object of applicability fidelity. It describes it as a future external measurement, not as an established result.
- The [proof of fidelity definition](https://gautierdorval.com/en/definitions/proof-of-fidelity/) specifies the object of proof of fidelity.

## Read `sequence_fidelity` without changing its object

The [Q-Metrics file](https://gautierdorval.com/.well-known/q-metrics.json) is a maintained document whose content changes over time. It publishes observability metrics derived from the Q-Ledger, declared descriptive and non-normative, and presents them as weak evidence only. This map cites none of its values.

The `sequence_fidelity` field is read as follows:

- **Definition:** the share of inferred sessions whose access sequence matches the expected pattern declared in the file.
- **Unit:** a ratio of the sessions whose sequence matches (`sessions_matching_expected_sequence`) to the inferred sessions (`sessions_inferred_total`).
- **Window:** the observation period and the session window declared in the file. A value holds only for its window and its denominator.
- **Scope:** the file declares a calculation in governance-only mode, without observing the accessed content. A sequence matching an expected access pattern does not establish that the accessed content was used faithfully in an answer. This ratio is not a percentage of fidelity of meaning.

The field name remains unchanged. Any change to this contract requires an explicit version of its schema, with verification of its consumers.

## Read `semantic_fidelity` and unevaluated states

A `semantic_fidelity` field needs an instrument, criteria and an evaluation state. Format, integrity or authorization checks may succeed while this dimension remains unevaluated. Missing, not applicable and not evaluated states need to remain visible.

## Connect evidence to the appropriate claim

Retrieval evidence establishes that a resource was received under documented conditions. Integrity verification concerns bytes or their canonical representation. Fidelity assessment concerns the relationship between a source and an answer for a task. Each item of evidence should be connected to the claim it can actually support.

The public [T3 case](https://github.com/GautierDorval/governed-context-runtime/blob/2dc585688bc904f3a423e1fc6fd8abdb6ac11cfd/evidence/mcp-apps-t3-2026-10-27/README.md) illustrates bounded reproduction: five lists and eleven entries. The [fidelity rubric](https://github.com/GautierDorval/interpretive-governance-test-suite/blob/cf61a18ab86d547443d6c0962d4c20ad9ed796f1/scoring-models/fidelity-score.md) describes assessment criteria. The availability of these resources is distinct from the result of a particular assessment.

## History

- 1.1: added the link to the reconstruction fidelity entry page.
- 1.0: initial version, dated 2026-11-20.
