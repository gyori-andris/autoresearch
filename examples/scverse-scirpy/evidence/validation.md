# Validation report

CONDITIONAL: the recovered, bounded native implementation is a validated single CPU proof of concept. The evaluated C kernel matches the recovered candidate byte for byte. Frozen scorer, references, fixtures, and incumbent are unchanged from the v2 baseline.

Independent checks passed: frozen v2 correctness at 0.22448 s and 340.6 MiB; compiler-disabled Numba fallback at 4.60534 s and 497.8 MiB; 11 upstream Hamming tests in each mode; exact sparse CSR at 2,048 and 4,096 sequences; and exact dense CSR at 512² entries. At 4,096 sparse sequences, tiling reduced peak RSS from 559.1 to 307.0 MiB and median time from 0.17661 to 0.12876 s versus the original recovered wrapper.

The archived frozen comparison supports 20.32× end-to-end speedup over Numba (4.20249/0.20681 s). It does not establish a 20× AVX-512 instruction gain: fresh optimized generic C versus AVX-512 was 1.10× at 2,048 sequences. The official best retained v2 median is 0.19103 s; the prior recovery score was 0.19459 s and marked `DISCARD`. The bounded branch has no new official score because that scorer appends to the protected ledger.

The native path is serial and bypasses `n_jobs`; multiple blocks can raise aggregate memory. Scratch is bounded to approximately `max(1 MiB, 16 × n_columns)`, while dense output still scales with retained pairs. Broader evaluation needs mixed sequence lengths and neighbour densities, multicore end-to-end comparisons and a host without AVX-512. The recorded checks support a single-CPU proof of concept with reduced scratch memory.
