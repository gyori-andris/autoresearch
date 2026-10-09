## Request

> Optimise Scanpy gene scoring, measuring both sparse reductions and public score_genes calls. Define whether the oracle is baseline parity or dense mathematical equivalence, including duplicate-coordinate and NaN behaviour.

## Setup

The geometric objective, measured in ns/nonzero, weights isolated kernels and public calls equally. The retained run passed 32 local checks and 28 upstream tests; the audit reports a 15% robust noise gate. Those fixtures did not cover duplicate-coordinate NaNs. A new contract must resolve that omission before launch.

## Change

Reduce sparse reduction overhead with contiguous native reduction and an indexed path. The audit attributes AVX2 dispatch to the contiguous reducer and scalar C to indexed prefetching; the combined score cannot be called an AVX2-only gain.

## Evaluation

The runner scored candidates against the frozen composite objective. The audit found later KEEP decisions compared to the original baseline rather than the incumbent, leaving a faster historical candidate unretained. Retention therefore needs an incumbent-relative check, with public-call timing reported separately.

## Result

Retained composite **37.1468614 → 20.9908523 ns/nonzero (1.770×)**; public-workflow improvement is **8.24%**. Independent duplicate-coordinate/NaN tests fail dense equivalence in both baseline and candidate. Baseline parity therefore does not satisfy the broader advertised oracle. The best recorded candidate was not retained.

## Follow-up

Add duplicate-coordinate/NaN cases to the oracle, fix incumbent-relative retention and replay the historical best against the retained source. Report the public-call result separately from the composite.
