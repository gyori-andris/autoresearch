## Request

> Make a TileDB-backed sparse read faster while preserving the logical matrix and coordinate mapping. Consider representation changes only if the contract explicitly permits changes to the writer and reader together.

## Setup

The workload is a full read of local synthetic data. Both the stored representation and the query path can change; the logical matrix and coordinate mapping must be preserved.

## Change

Encode integer positions at write time. The read path can then skip redundant coordinate output and sorting. This changes the writer and reader together.

## Evaluation

The measured quantity is full-read latency. Write/encoding costs and compatibility with existing files need separate checks when changing the representation.

## Result

Reported full-read latency: **617 → approximately 51 ms (12×)**. The gain combines representation and query changes; it is not an isolated ISA comparison.

## Follow-up

Before deployment, test coordinate identity, duplicates, ordering and writer/reader round trips. Decide how existing files will be read, and account for the extra work at write time.
