# Validation report

Independent verdict: **NO_CANDIDATE** for a speedup claim. The baseline and profiling evidence pass; no optimization was accepted or retained. All rejected candidates are closed under the current contract. Their timings are research leads, not validated gains.

The baseline is 43.549 ms on one core and 12.052 ms on four cores. The fastest algorithmic run recorded 23.409 ms (1.86× faster on one core), but was discarded. The AVX-512 run recorded 33.870 ms for the kernel (1.29× faster), while the integrated helper showed no gain and its four-core result was slower. Its native source was reverted, so ISA execution cannot now be independently established.

The memory gate needs repair before revisiting any lead: `ru_maxrss` is a process lifetime high water mark taken after all fixture warmups, probes, and core modes. It cannot attribute the reported excess over the original 508.3 MiB baseline to a candidate kernel. Repairing that measurement would require reconstructing candidate source and rerunning correctness, integrated helper, memory, and paired timing checks; it cannot retroactively turn these discarded runs into wins.

Current source and scorer hashes match the baseline, and 13 focused oracle/API tests passed under the benchmark lock.
