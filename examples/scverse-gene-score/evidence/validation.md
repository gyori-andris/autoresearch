# Validation report

Verdict: **CONDITIONAL for the frozen benchmark; FAIL for the stated dense-equivalence contract.**

The retained source's recorded objective is **20.9908523 ns/nonzero**, versus the frozen baseline **37.1468614 ns/nonzero**: **1.770× speedup, or 43.49% less time**. Both measurements use the scorer’s geometric objective, which weights isolated kernels and public `score_genes` equally. The retained run passed its 32 local checks and `28` upstream tests; all 32 cases met the 15% robust noise gate. Public-workflow geomean improved only **8.24%**, so the composite gain should not be described as an end-to-end speedup.

A focused independent test exposed a contract violation. For valid noncanonical CSR and CSC matrices containing duplicate coordinates with stored NaNs, `np.nanmean(x.toarray(), axis=...)` returned `[2, 0]` while the retained within-slot reducer returned `[inf, 0]`; the indexed path similarly produced `nan` where the dense reference produced `0`. This occurred on both physical formats. A separate explicit stored-zero check passed. The frozen inputs and scorer omit duplicate-coordinate cases, so their passing gates cannot establish the advertised general equivalence. The upstream baseline has the same duplicate handling assumption, making this a preexisting semantic gap rather than a demonstrated regression.

The campaign’s historical best recorded KEEP was **19.3027676 ns/nonzero** or **1.924×** the frozen baseline. That source is recoverable from Git, but it is not retained at HEAD. Later slower results were still marked KEEP because the scorer compares each result with the original baseline, not the incumbent; rejected experiments were reverted. The historical best is therefore an exact replay candidate, not a performance claim for the current source. The roughly 8% difference between it and the retained score also warrants a controlled paired rerun before ranking them under VM noise.

AVX2 dispatch applies to the contiguous native reducer; the indexed prefetch implementation is scalar C. The aggregate gain cannot be attributed solely to AVX2. Native compilation failure falls back to Numba, but the non-AVX2 path and other architectures were not measured. Peak process RSS in evidence was 448.625 MiB for the retained run versus 534.496 MiB at baseline; this is process-level evidence, not an isolated kernel memory result.

Replay the historical best in an isolated checkout after adding duplicate-coordinate semantics to the gate. Run the frozen tests and paired benchmark under an exclusive benchmark lease.
