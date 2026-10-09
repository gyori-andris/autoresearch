# Pheiron: selected H5AD reads

3396 → 465 ms for a 5,000-cell selection; 2182 → 997 MiB reported.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Read only the selected CSR data interval and rebase row pointers.

## Scope and validation

Later remote-read result is not the early local full-read contract. Aggregate checks are not full sparse-output equality.

## Evidence

Status: **reported**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/pheiron-h5ad/notebook.py`.
