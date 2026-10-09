## Request

> Improve a small language-model CPU decoder on one Ryzen 3700X core. Separate unchanged numerical behaviour from compression-preserving encoder/decoder changes, and measure compression rate alongside throughput.

## Setup

The documented track combines algorithm, attention windows, KV-cache representation, quantisation and instruction-level changes. Decode throughput alone is not a complete objective when model changes affect compressed size. The exact matched checkpoint, complete original contract and run bundle are not attached.

## Change

Reduce cache traffic with compact KV storage, use per-head attention windows, vectorise transcendentals and pack integer GEMV. The throughput result combines these changes. Each fresh hypothesis should be measured against the applicable incumbent.

## Evaluation

The evaluation has to distinguish numerical equivalence from exact compression round trips. If predictions can change, matched encoder/decoder checks and a compression-rate gate are needed alongside throughput.

## Result

Documented throughput is approximately **100 → 1950 tokens/s (19.5×)** on one core. The full-span setting is approximately **1540 tokens/s**; the final span cap adds approximately **0.04 bits/byte**. Matching encoder/decoder behaviour may remain lossless while model predictions change. The full-file decode time remains a projection.

## Follow-up

Recover matched checkpoint/weight provenance and run the complete encode/decode comparison. Report throughput, compression rate and exact round-trip checks together; complete the full-file run before quoting elapsed time.
