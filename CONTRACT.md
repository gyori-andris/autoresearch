# Core experimental contract

Each experiment specifies its reference, objective, correctness checks and resource limits.
The examples report their own conditions and deviations from this protocol.

## Before search

Freeze the reference revision, fixtures, evaluator, dependencies, build command,
correctness oracle, timing boundary and resource ceilings. Name the editable files.
Record CPU model, exposed instruction sets, affinity, thread counts and cache policy.
Calibrate measurement variability before choosing the acceptance threshold.

## One iteration

1. Load the contract, retained source and experiment ledger. Use a fresh worker session
   per experiment when that execution mode is configured; otherwise reload durable state
   between iterations and after context rollover.
2. Choose one hypothesis. Change only the permitted implementation surface.
3. Record the candidate revision; rebuild native code from that revision.
4. Run correctness and resource gates, then paired baseline/candidate measurements.
5. Retain only a passing improvement above the case's declared noise threshold.
6. Record hypothesis, samples, gate results, source revision and retention decision;
   restore the retained implementation if the candidate is rejected, then exit.

The evaluator and controller own measured results and retention records. The worker
may explain findings, but cannot rewrite the frozen oracle or measured ledger.
Interrupted runs must be reconciled before another experiment starts.

## Measurement boundaries

Only one timed experiment may occupy a benchmark machine at once. Memory measurement
must include candidate allocations and required outputs; report scratch separately
where useful. Explicitly distinguish compilation, cold start and steady state.
Warm input/page caches are permitted only when declared; cached output substitution,
benchmark detection and undisclosed extra workers are not.

Native code, cache-aware layouts, compiler optimisation and any instructions exposed
by the target CPU may be in scope. ISA-only gains require a matched native comparison;
Python-to-native or algorithmic gains must not be attributed entirely to ISA changes.
Machine-specific PoCs do not establish portable deployment or upstream acceptance.

## Reporting

Preserve absolute samples, aggregation formula, source/evaluator hashes, environment,
gate results and later validation. Keep historical, retained and replayed results
distinct. Record rejected and incomplete cases. Changed semantics, approximations or
compression-rate trade-offs require explicit labels and their own correctness contract.
