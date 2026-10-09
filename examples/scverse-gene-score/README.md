# Scanpy: gene scoring

Composite 37.1468614 → 20.9908523 ns/nonzero; public-call improvement reported as 8.24%.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Optimise sparse reductions; distinguish kernel timing from the public API.

## Scope and validation

Duplicate-coordinate NaNs fail dense equivalence in baseline and candidate. This is a pre-existing assumption, not an established new regression. Composite is not public-call speedup.

## Evidence

Status: **qualified**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-gene-score/notebook.py`.
