# Validation report

**FAIL for the retained kernel as a production candidate.** Its accepted benchmark shows a 1.300× steady-state speedup (1.52194 versus 1.97790 ns/nonzero), but JIT warm-up took 1043.8 seconds and peaked at 30.0 GiB RSS. I did not rerun it under the 8 GiB limit.

A smaller candidate scored 1.276× at 1004.6 MiB peak RSS with 7.69 seconds of warm-up. Its 185-line source is substantially smaller than the retained 1051-line module. Treat it as **CONDITIONAL** until an isolated, memory-capped replay checks nonzero correction, adversarial cancellation and overflow values, sparse edge cases, and performance beyond this single-core EPYC/AVX2 host.

The scorer’s correctness gate never calls `mean_var` with nonzero `correction`, contrary to its contract. Its timed values are limited to signed integers from 1 to 7, so they do not establish numerical behavior for adversarial magnitudes.
