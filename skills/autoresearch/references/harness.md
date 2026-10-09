# Harness requirements

The planner implements and tests these requirements for the approved workload.
Implement the scorer for the approved workload.

## Durable state and ownership

Freeze hashes of the human-owned contract, evaluator, fixtures, oracle, dependencies
and build commands. Workers edit only declared source paths and hypothesis notes.
`run.py` owns measured records and incumbent-relative adjudication.

`results.tsv` (or declared append-only JSONL) records experiment ID, timestamp,
hypothesis, candidate revision, parent retained revision, contract version, objective,
elapsed time, gate status, decision and artifact path. Keep raw samples, resource
diagnostics, logs and source/environment hashes. Preserve failed attempts too.

`state.json` identifies the retained revision/score, baseline and any in-flight operation.
The last passing ledger row need not be the incumbent: correctness is not improvement.

## Scoring transaction

1. Acquire the agreed exclusive benchmark lease across tasks on the host. Check STOP,
   budget and unfinished transactions before editing or measuring.
2. Verify environment, frozen hashes, candidate revision and allowed diff paths. Refuse
   dirty source or undeclared dependency changes. Persist an in-flight experiment ID.
3. Build from the exact candidate in a fresh output directory. Do not reuse a shared
   library left behind by a rejected revision.
4. Enforce correctness and resource gates, then the fixed measurement protocol. Timeout
   covers build, tests and evaluation; terminate child process groups as needed. Account
   for native allocations and required outputs, with fresh matched processes where
   lifetime peak RSS would contaminate comparisons.
5. Compute the contracted objective. Keep only if every gate passes and improvement
   over the incumbent exceeds the threshold. For an absolute minimize rule:
   `incumbent - candidate > threshold`; maximize reverses subtraction. A relative
   threshold requires its own explicit formula. Equal/sub-threshold results reject.
6. Persist raw evidence and exactly one terminal record per ID before atomically
   updating retained state. Crash/timeout is a failed result without a score, not zero.
   Print a machine-readable verdict with incumbent, candidate, gates and decision.
7. On restart reconcile in-flight IDs with records before retrying; no duplicate rows
   or silently dropped interrupted attempts. Missing records are a harness fault, not
   permission for the worker to invent measurements.

Keep rejected candidate commits reachable via experiment refs or isolated worktrees.
Restore only declared mutable paths from the retained revision, accounting for newly
created files, or discard an isolated candidate worktree safely. Do not reset a user's
whole checkout. Track candidate identity separately from checked-out retained state.

## Measurement boundary

Specify inclusion of compilation, startup, allocation, transfer, lazy materialisation
and output consumption. Fix threads, workload order, warmup and caches. Paired/alternating
measurements help expose drift. Forbid output reuse, fixture detection and benchmark-only
shortcuts. Use an independent oracle with relevant public-interface edge cases.

Agent model/cadence can vary as authorised without changing the evaluator. Changes to
hardware, fixtures, semantics or dependencies require a new comparison series and baseline.

## Required tests before handover

- Correct candidate emits a finite score and complete artifacts.
- Deliberately wrong output fails and cannot become retained.
- Timeout, build failure and evaluator exception produce terminal failed records.
- An unchanged candidate is not promoted as an improvement.
- Frozen-file tampering and out-of-scope edits reject before timing.
- Rejection restores retained source while preserving evidence and unrelated work.
- Interruption recovers without duplicating or losing a result.

Verify these properties in the generated harness before handover.
