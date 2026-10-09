# Worked examples

Each notebook covers the request, setup, implementation change, evaluation and result.
Read them directly on GitHub or edit the marimo source in the case folder.

Start with [AnnData](scverse-anndata/notebook.ipynb). It includes
[contract](scverse-anndata/CONTRACT.md) and [handover](scverse-anndata/HANDOVER.md)
extracts, calibration values and raw replay samples. Then read
[how to use the examples](USAGE.md) to prepare a campaign in your own project.

Other setups are reconstructed from case summaries and audits. Requests are adapted
examples. Original candidate/harness bundles are incomplete; see
[evidence availability](../RECOVERY.md). Opening a notebook does not launch a campaign.

| Case notebook | What it teaches |
| --- | --- |
| [AnnData: dense H5AD to CSR/CSC](scverse-anndata/notebook.ipynb) | Full setup: scalar objective, exact output, native search boundary, handover and replay |
| [Pheiron: selected H5AD reads](pheiron-h5ad/notebook.ipynb) | Make selection and remote-read boundaries explicit; avoid unnecessary materialisation |
| [Pheiron: TileDB sparse reads](pheiron-tiledb/notebook.ipynb) | Authorise coupled writer/reader representation changes |
| [Pheiron: Zarr reads](pheiron-zarr/notebook.ipynb) | Include startup and metadata work in a cold-read contract |
| [Scirpy: Hamming distances](scverse-scirpy/notebook.ipynb) | Separate generic native and ISA gains; bound scratch memory |
| [Scanpy: gene scoring](scverse-gene-score/notebook.ipynb) | Distinguish composite scores, public calls and independent semantics |
| [Scanpy: top-expression proportions](scverse-qc-top/notebook.ipynb) | Use edge cases to reject a fast but invalid shortcut |
| [Sparse mean and variance](scverse-mean-var/notebook.ipynb) | Gate compilation/startup resources as well as warmed timing |
| [Scanpy: normalisation](scverse-normalize/notebook.ipynb) | Calibrate noise and reject sub-threshold gains |
| [Sparse-to-dense conversion](scverse-sparse-dense/notebook.ipynb) | Account for allocation, page faults and usable output |
| [Squidpy: co-occurrence](scverse-cooccurrence/notebook.ipynb) | Validate integrated multicore behaviour and isolate memory measurements |
| [Scanpy: sparse scaling](scverse-scaling/notebook.ipynb) | Complete profiling before enrolling a task |
| [Scanpy: exact neighbours](scverse-neighbors/notebook.ipynb) | Stop at a dependency boundary instead of silently enlarging scope |
| [Small language-model decoder](slm-cache/notebook.ipynb) | Define allowable quality trade-offs for algorithm/cache/ISA search |

The Pheiron cases contain approved summaries only; internal source, datasets and run logs
are not included. Rejected and incomplete experiments remain labelled as such.

To edit a marimo source, run `uv sync --locked`, then
`uv run marimo edit examples/<case>/notebook.py` from the repository root.
