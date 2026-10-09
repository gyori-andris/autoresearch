# AnnData: dense H5AD to CSR/CSC

The replay supplies six paired samples for each of six cases. A separate independent audit reports approximately 2.19×.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

HDF5-aware traversal, direct sparse construction and native implementation reduce allocation and conversion overhead.

## Scope and validation

Warm page cache, one EPYC 7B12 core; conversion from open HDF5, not full public read_h5ad or remote I/O. Replay is not proof of historical retention compliance.

## Evidence

Status: **replayed**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-anndata/notebook.py`.
