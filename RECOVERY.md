# Evidence availability

The examples include three Pheiron engineering cases, ten scverse targets and one
small language-model decoder. Each evidence record lists the available measurements
and missing reproduction artifacts.

## Available records

- AnnData: six workloads with six paired observations each, timing conditions and
  resource measurements.
- Ten scverse validation summaries covering correctness, performance and resource gates.
- AnnData contract and handover extracts with baseline calibration.
- Case notebooks describing the request, setup, implementation change and result.

The validation summaries describe recorded checks; they are not fresh benchmark runs.
Requests are adapted examples. AnnData's setup documents are recovered extracts;
the other setup descriptions are reconstructed from case records.

## Pheiron cases

H5AD, TileDB and Zarr include reported timings, workload boundaries and explanations.
Internal implementations, datasets and run logs remain private.

The H5AD selection and Zarr cold-read results use remote storage. Earlier local
full-read experiments used different boundaries. TileDB's result includes a
write-time representation change.

## Missing reproduction artifacts

- Complete scverse candidate source, environments and evaluator bundles.
- Full ledgers linking attempted, retained and replayed implementations.
- Public Pheiron fixtures and exact-output validation.
- Matched decoder checkpoints and weights for the throughput/compression comparison.

The decoder's full-file time remains a projection. The notebooks analyse saved
measurements; reproducing the native benchmarks requires the missing run artifacts.
