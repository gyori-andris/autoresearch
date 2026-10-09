## Request

> Accelerate Scirpy's Hamming-distance calls with exact CSR results and bounded scratch memory. Compare the public-call baseline with generic native C and CPU-specific code separately; keep the one-core PoC scope explicit.

## Setup

The frozen small public-call suite compares Numba, generic C and AVX-512BW. Validation covers exact sparse/dense CSR output, upstream Hamming tests and compiler-disabled fallback. The native path is serial and bypasses n_jobs.

## Change

Avoid repeated Numba compilation and perform byte-mismatch counting in native code. Then compare vector mismatch masks with generic optimised C. Tiling bounds scratch space rather than allocating a large intermediate pairwise structure; the final retained-pair output can still be quadratic.

## Evaluation

The recovered implementation underwent a separate correctness and memory audit. It passed 11 upstream Hamming tests in native and compiler-disabled modes, exact CSR checks at 2,048 and 4,096 sparse sequences, and a 512² dense case. This audit is distinct from scoring an attempt in the original protected ledger.

## Result

The archived small suite is **4.202494 s → 0.224315 s generic C → 0.206812 s AVX-512BW**: **20.32× total**, about **1.085× incremental ISA** on that comparison. Larger synthetic one-core calls show **1.77–2.39× total** and **1.15–1.44× incremental ISA**.

At 4,096 sparse sequences, tiling reduced peak RSS **559.1 → 307.0 MiB** and median time **0.17661 → 0.12876 s** versus the recovered wrapper. The bounded branch has audit timings but no new official score.

## Follow-up

Benchmark mixed sequence lengths and neighbour densities, multicore public calls and a CPU without AVX-512. Measure scratch and retained-pair output separately; dense output can still grow quadratically.
