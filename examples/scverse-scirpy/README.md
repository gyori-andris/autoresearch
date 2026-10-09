# Scirpy: Hamming distances

Frozen small public-call suite: 4.202494 s baseline, 0.224315 s generic C, 0.206812 s AVX-512BW.

[Notebook](notebook.ipynb) · [Setup and experiment](walkthrough.md)

## Mechanism

Remove repeated Numba compilation; compute byte mismatch masks in native code with bounded scratch.

## Scope and validation

20.32× is total gain, not ISA-only. Larger synthetic one-core calls: 1.77–2.39× total, 1.15–1.44× incremental ISA. Validation report and tool records recovered with exact CSR/Hamming checks; complete original run bundle still pending.

## Evidence

Status: **audit-reported**. [Evidence record](evidence/provenance.json).

Edit from the repository root: `uv run marimo edit examples/scverse-scirpy/notebook.py`.
