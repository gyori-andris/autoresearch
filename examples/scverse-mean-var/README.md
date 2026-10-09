# Fast-array-utils: sparse mean/variance

Resource gate failed; no accepted speedup.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Explore fused reductions and loop structure.

## Scope and validation

Warm timing does not excuse the reported approximately 30 GiB / 17-minute JIT path. Older bounded candidates need separate replay.

## Evidence

Status: **rejected**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-mean-var/notebook.py`.
