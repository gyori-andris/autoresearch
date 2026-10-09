## Request

> Improve sparse mean/variance runtime while preserving correction and numerical behaviour. Include compilation/startup cost and peak memory as gates, rather than measuring only a warmed kernel.

## Setup

The retained candidate improved steady-state timing but exceeded practical resource limits during JIT warm-up. Its scorer omitted nonzero correction and timed small signed integers only. The oracle also needs nonzero correction, adversarial magnitudes, cancellation and overflow cases.

## Change

Fuse reductions and alter loop structure to reduce repeated passes. Excessive specialisation or unrolling can move cost into compilation, so a warmed-kernel win must not bypass startup and memory gates.

## Evaluation

The audit did not rerun the resource-heavy implementation under the 8 GiB limit. It identified an older smaller candidate for a separate, memory-capped replay. That candidate needs a separate measured replay.

## Result

The retained kernel's recorded **1.300×** steady-state result came with **1043.8 s warm-up and 30.0 GiB RSS**: resource-gate failure. An older candidate reportedly achieved 1.276×, 1004.6 MiB RSS and 7.69 s warm-up, but remains conditional until replay. No accepted speedup is claimed here.

## Follow-up

Replay the smaller candidate in a memory-capped worker. Add nonzero correction, cancellation and overflow cases before scoring. Keep compilation time and peak RSS as hard gates.
