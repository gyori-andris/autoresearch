# Pheiron: TileDB sparse reads

617 → approximately 51 ms for the reported local synthetic full read.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Encode integer positions at write time, avoid redundant coordinate output and sorting during reads.

## Scope and validation

The measured improvement includes a write-time representation change and query-path changes. It is not an isolated ISA gain; the internal implementation is not distributed here.

## Evidence

Status: **reported**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/pheiron-tiledb/notebook.py`.
