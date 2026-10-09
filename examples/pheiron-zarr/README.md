# Pheiron: Zarr reads

1944 → 551.3 ms; reported candidate trials 541.8, 551.3, 561.3 ms.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Consolidate metadata requests and avoid an unused cold Dask import.

## Scope and validation

Cold-start and metadata effects; do not present as faster arithmetic or cached-result reuse. Early local contract needs phase matching.

## Evidence

Status: **reported**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/pheiron-zarr/notebook.py`.
