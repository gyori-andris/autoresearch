# AnnData: historical handover extract

Extract from the Phase 2 handover. Commands refer to the original prepared AnnData
worktree; its scorer is not included in this example folder.

- Contract: native conversion Phase 2; see the adjacent historical CONTRACT extract.
- Objective: minimise paired-ratio `relative_geomean` against the fixed original reference.
- Starting implementation: retained Phase 1 HDF5-row-aligned CSC traversal.
- Initial median score: `0.861417`; maximum observed calibration RSS: `569.141 MB`.
- KEEP: all gates pass and improvement over best prior exceeds `0.02` ratio points.
- Limits: 1536 MB peak RSS; contracted 240-second build/test/evaluation timeout.
- Mutable files: `src/anndata/_io/h5ad.py`, optional `_dense_sparse_native.c`.
- Frozen: contract, build, evaluator, upstream conversion tests, fixtures and scorer.
- Durable records: `autoresearch/results.tsv`, `autoresearch/thesis.md`, committed source.
- Stop signal: `autoresearch/STOP`.
- Execution: an external controller launched fresh workers; each did one experiment and exited.

Scorer command in the prepared worktree:

```sh
.venv/bin/python autoresearch/run.py -m "one change and its hypothesis"
```

It rebuilt the native module, ran upstream tests and then the paired evaluator. It
wrote the attempt record; the worker read the result and restored source on rejection.
It did not launch the coding agent itself.

The initial native backlog was to profile phase costs, establish a correct scalar C
implementation, inspect CPU/compiler/cache capabilities, then compare traversal,
allocation, scalar and instruction-level approaches using the full contracted score.

For a new campaign, generate a handover with your own reference, calibration,
paths, state reconciliation and limits.
