## Request

> Reduce cold remote Zarr read latency without caching the converted result. Include metadata access and required startup work in the timing boundary; preserve the returned data and lazy/eager behaviour.

## Setup

The workload is a cold remote read. Startup/import state and metadata requests are part of that boundary. The earlier local experiment had a different contract.

## Change

Consolidate metadata requests and remove an unused cold Dask import. Both reduce startup and access overhead.

## Evaluation

The comparison needs the same cold-start policy for both implementations. Previously materialised outputs cannot be reused; otherwise the test would measure caching rather than the read path.

## Result

Reported latency: **1944 → 551.3 ms (3.5×)**. Candidate observations: **541.8, 551.3 and 561.3 ms**. Only the baseline endpoint is available.

## Follow-up

Measure cold and warm reads separately. Check returned data, metadata and lazy/eager behaviour after changing imports or metadata access.
