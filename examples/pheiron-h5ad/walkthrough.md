## Request

> Reduce latency and memory for a selected-cell H5AD read. Keep the selected sparse matrix and its annotations correct, and avoid materialising rows that were not requested. Define the remote-read timing boundary before benchmarking.

## Setup

The workload selects 5,000 cells from a remote H5AD file. Latency and memory cover the selected read. An earlier local full-read experiment used a different measurement boundary.

## Change

CSR row pointers identify the selected data interval. Read that interval and its indices, then rebase the row pointers. This avoids loading the full matrix before slicing.

## Evaluation

The recorded validation used aggregate checks. Exact equality of the sparse output and annotations remains unverified.

## Result

Reported latency: **3396 → 465 ms (7.3×)**. Reported memory: **2182 → 997 MiB**.

## Follow-up

Add empty, boundary and noncontiguous selections to the next evaluator. Compare sparse arrays and annotations exactly; aggregate totals can miss indexing errors.
