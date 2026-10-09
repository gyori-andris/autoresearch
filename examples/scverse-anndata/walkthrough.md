## Request

> Make AnnData's dense H5AD-to-CSR/CSC conversion faster. Preserve exact sparse outputs. Allow Python and native C changes on the pinned CPU, with one-core execution and bounded memory. Propose the contract before preparing the evaluator.

## Setup

Six 7000 × 7000 float32 workloads cover CSR/CSC and three density/compression combinations. The reference is the copied pre-autoresearch implementation; the Phase 2 incumbent already includes Python/HDF5 improvements. The [contract](CONTRACT.md) and [handover](HANDOVER.md) give the full setup.

The score is the geometric mean of per-case medians of paired latency ratios. Exact CSR/CSC arrays, unchanged upstream tests, a 1536 MB RSS ceiling and a contracted 240-second timeout gate scoring. One CPU core, warm page cache, fixture data, dependencies, evaluator and build flags are frozen. Only the Python I/O module and optional native conversion file can change.

## Change

The initial notes identify dense slabs, intermediate SciPy sparse objects and a final stack/copy as possible overhead. The search can test chunk/layout-aware traversal, direct sparse construction and bounded allocation before or alongside available ISA features. A scalar C correctness port is a distinct hypothesis from SIMD acceleration; both must pass the same complete score.

## Evaluation

The external controller started a fresh worker for one experiment. It read the contract, handover, notes, recent ledger and source history, checked STOP, committed one in-scope candidate and called the single scorer shown in HANDOVER. The scorer rebuilt native code, tested outputs, measured paired timings and recorded the attempt. The worker then kept or restored source and wrote its interpretation before exiting.

Phase 2 calibration scores: 0.861417, 0.858227 and 0.870895. KEEP required an improvement over best prior greater than 0.02 ratio points.

## Result

The paired replay gives **2.151×** from 36 paired observations, with peak RSS **569.734 MB**. The measured boundary is conversion from open HDF5 objects, not remote `read_h5ad`.

The Validation report reports 19 passing upstream conversion tests and exact sparse checks. It also found that the source had been restored despite missing the KEEP margin. The replay validates the comparison, not that retention decision.

## Follow-up

Resolve the historical retention exception before calling the replayed source a rule-compliant winner. Portable deployment also needs fallback/dispatch tests and measurements on other CPUs.
