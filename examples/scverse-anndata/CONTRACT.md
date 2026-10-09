# AnnData native conversion: historical contract extract

Extract from the Phase 2 machine-specific conversion contract.
The evaluator, candidate and environment bundle are incomplete; see
[evidence availability](../../RECOVERY.md).

## Objective

Minimise `relative_geomean`: the geometric mean across six workloads of the median
paired candidate/reference latency ratio. `1.0` means parity with the frozen
pre-autoresearch AnnData reference. Peak RSS and per-case ratios were also recorded.
Peak RSS was a hard gate; it was not a second optimisation objective.

## Editable and frozen surfaces

Editable: `src/anndata/_io/h5ad.py` and optional
`src/anndata/_io/_dense_sparse_native.c`. One hypothesis could change both.

Frozen: contract, fixture generation, evaluator, build command, scorer,
upstream conversion tests, data and copied reference. Dependencies could not change.
No benchmark-specific branches, converted-result caches or additional workers.

Native C, compiler vectorisation, intrinsics, inline assembly, cache/layout changes
and exact-output representation changes were allowed. Instructions had to be exposed
by the actual CPU. This was a machine-specific PoC; portable wheels and runtime
dispatch were explicitly outside its acceptance gates.

## Correctness and resource gates

- Build the optional native module with the frozen command.
- Pass unchanged `tests/test_io_conversion.py`.
- Match reference CSR/CSC type, shape, dtype, `indptr`, `indices` and `data` exactly.
- Peak RSS at most 1536 MB, including dense buffers, sparse output and native allocations.
- Contracted build/test/evaluation timeout: 240 seconds.
- No eager whole-file or persistent converted-output cache, benchmark detection or hidden threads.

## Measurement

- Deterministic 7000 × 7000 float32 HDF5 datasets.
- Three density/compression combinations: 0.1% uncompressed, 1% LZF, 10% gzip level 1.
- CSR and CSC for each: six workloads; `axis_chunk=6000`.
- One untimed warm-up, six paired candidate/reference observations per case.
- Deterministically randomised case order; alternating implementation order.
- Warm page cache; conversion from an open HDF5 object, not a remote whole-file read.
- CPU affinity to one core; common BLAS/OpenMP thread counts set to one.
- AMD EPYC 7B12 VM; GCC 11.4.0, CPython 3.13 environment at calibration.
- Frozen native flags: `-O3 -march=native -funroll-loops -fPIC -shared -std=c11`.

AVX2 was exposed; AVX-512 was not. The scope also allowed available non-SIMD features
and cache-aware changes. Changing CPU exposure, compiler, dependencies, fixtures,
evaluation or contention required recalibration.

## Calibration and retention

Phase 2 started from the retained Python/HDF5 implementation, not the original
unoptimised reference. Three initial scores were `0.861417`, `0.858227`, `0.870895`.
Their range was 1.47% of the median, below the 5% launch gate.

KEEP required all gates and `best_prior - candidate > 0.02` ratio points.
That is not a universal 2% relative-time threshold. Otherwise restore the incumbent
implementation and preserve the attempted candidate's record.

The later audit found that a measured passing candidate had been restored despite
missing that keep margin. The paired replay therefore records a measured
comparison, not compliance with the historical retention rule.
