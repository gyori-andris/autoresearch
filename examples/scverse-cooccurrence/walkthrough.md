## Request

> Optimise Squidpy co-occurrence while preserving outputs and performance in the contracted one-core and multicore modes. Measure memory in an isolated candidate worker.

## Setup

The baselines were 43.549 ms on one core and 12.052 ms on four cores. One-core speedups did not satisfy the complete contract. The audit found process-lifetime ru_maxrss collected after mixed warmups and core modes could not attribute memory to a specific candidate.

## Change

Reduce pairwise counting overhead, then separately test available ISA acceleration. A kernel result is only a lead until its integrated helper and contracted core modes improve without gate failures.

## Evaluation

An algorithmic run reached 23.409 ms on one core but was discarded. An AVX-512 run reported 33.870 ms kernel timing while the integrated helper did not improve and four-core behaviour regressed. Its source was reverted, so later ISA execution could not be independently established.

## Result

Reported **1.86× one-core** and **1.29× kernel** leads are **not accepted gains**. The retained source and scorer match baseline; 13 focused oracle/API tests passed. The memory gate must be repaired and candidates reconstructed before any renewed claim.

## Follow-up

Measure RSS in separate candidate workers, reconstruct the rejected source and rerun correctness, integrated-helper and paired one-/four-core timings. The old discarded measurements remain discarded.
