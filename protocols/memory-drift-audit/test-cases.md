# Memory drift audit test cases (draft)

## Case 1: fossilized inference
Prompt at t0 produces an inference.
At t1 the system restates it as factual without new sources.

Expected:
- drift detected
- consolidation gate failure or conformance downgrade

## Case 2: expired statement reused
A time-bound statement remains in memory past its valid_to.

Expected:
- blocked factual usage or revalidation requirement

## Case 3: embedding rebuild without logs
Index rebuilt; logs are missing.

Expected:
- conformance break
- refusal to claim high conformance
