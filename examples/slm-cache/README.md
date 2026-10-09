# Small language model: CPU decoder

Approximately 100 → 1950 tokens/s on one Ryzen 3700X core; full-span reference approximately 1540 tokens/s.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Per-head attention windows, vectorised transcendentals, compact KV cache and packed integer GEMV.

## Scope and validation

Final span cap trades approximately +0.04 bits/byte for speed. Combined algorithm/cache/quantisation/ISA gain. Full-file decode time is a projection, not a completed run.

## Evidence

Status: **documented**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/slm-cache/notebook.py`.
