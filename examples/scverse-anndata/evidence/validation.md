# Validation report

**Conditional performance result.** The current source supports a scoped “2× end-to-end” result on the frozen six-case, single-core AMD EPYC benchmark. An isolated replay scored 0.455972, or **2.193× faster** than the copied pre-autoresearch AnnData reference. All 19 upstream conversion tests and exact sparse-output checks passed; peak RSS was 584.93 MB, below the 1536 MB gate.

The evaluated source's official ledger score was 0.447641 (**2.234×**, 537.66 MB RSS). That experiment was initially *discarded* because its improvement over the prior best missed the frozen 0.02 keep margin, then restored without a new score. It is the active and best passing source, but calling it retained *under the original keep rule* needs an explicit exception or reconciliation.

The measured gain combines HDF5 traversal and native conversion. AVX2 code is built with `-march=native`; there is no runtime ISA dispatch. The restored candidate needs reconciliation with the retention rule.
