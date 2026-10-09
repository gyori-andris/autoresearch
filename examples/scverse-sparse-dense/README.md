# Fast-array-utils: sparse to dense

Approximately 1.019× near miss, below acceptance threshold.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Unroll scatter loops and investigate vectorised stores.

## Scope and validation

Allocation, zeroing and page faults need matched accounting; no accepted result.

## Evidence

Status: **no-accepted-win**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-sparse-dense/notebook.py`.
