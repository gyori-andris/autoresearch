# Validation report

**NO_CANDIDATE** for a speedup claim. The clean repository contains only the baseline harness; no Scanpy source change, adapter, or candidate measurement exists.

The raw single-core baseline is 108.773 ms for the public graph, with 89.811 ms in scikit-learn’s `fit_transform` and 15.875 ms in Scanpy postprocessing. The dependency owns 82.6% of public graph time. The 473,168 KiB memory figure is peak process RSS, not incremental memory use. CPU ISA support does not establish an optimization opportunity.

The profile led to `STOP_DEPENDENCY_DOMINATED`. A speedup claim requires an authorized, bounded candidate with a portable brute fallback, preserved exact-neighbor and graph semantics, and a locked end-to-end score meeting the contract’s ≥2% improvement and stability gates. No fresh tests were run while another project held the shared benchmark lock.
