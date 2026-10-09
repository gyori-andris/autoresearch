# Validation report

**FAIL for the current retained source; recoverable.** A read-only check under `benchmark.lock` found that CSR and CSC results diverge from dense Scanpy results when stored values are negative and implicit zeros occupy higher ranks. For `[-3, 0, 0, 0]` with ranks `(1, 2, 3, 4)`, dense gives `(0, 0, 0, 1)` while retained CSR and CSC give `(1, 1, 1, 1)`. The shortcuts at `row_nnz <= ns[0]` and `ns[j] >= row_nnz` cause the error.

The retained source's recorded, stable score is `0.459353` relative to baseline, a **2.18× weighted speedup** on the frozen nonnegative datasets; aggregate time was 31.677 ms versus 70.753 ms, with peak RSS 318,544 versus 323,672 KiB. That performance result does not validate signed-value correctness.

An exact repair is to send signed short rows through the baseline’s zero-padded partition and segment-sum path while keeping the current path for nonnegative rows. Then add signed CSR/CSC and public `calculate_qc_metrics` comparisons against dense results, and rerun the sole frozen scorer. A stable KEEP after that replay would permit validation.
