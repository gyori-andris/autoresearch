# Scanpy: top-expression proportions

Historical 2.18× fixture result is not an accepted general-purpose win.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Shortcut for rows with few stored values avoids selection work.

## Scope and validation

Signed data breaks the shortcut when implicit zeros outrank negative stored entries.

## Evidence

Status: **rejected**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-qc-top/notebook.py`.
