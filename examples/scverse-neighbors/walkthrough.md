## Request

> Profile Scanpy exact-neighbour graph construction. Find which implementation owns the runtime before deciding whether a CPU-specific replacement fits the authorised scope.

## Setup

The single-core public graph took 108.773 ms: 89.811 ms in scikit-learn fit_transform and 15.875 ms in Scanpy postprocessing. The dependency owns 82.6% of public runtime. The existing worktree contained only a baseline harness, not a replacement adapter.

## Change

Optimising a Scanpy-owned helper cannot directly remove dependency-owned work. A native exact-neighbour adapter could be a new experiment only with explicit authority, exact graph semantics, a portable brute fallback and a newly validated boundary.

## Evaluation

The task stopped as dependency dominated. No candidate measurement exists. The audit did not run fresh tests while another project held the shared benchmark lock. The contract required at least 2% end-to-end improvement and stability gates for any future candidate.

## Result

**Not enrolled.** Profiling stopped the task at the dependency boundary. Recorded peak RSS is 473,168 KiB for the whole process, not incremental kernel memory.

## Follow-up

A replacement adapter needs a new approved scope, exact-neighbour/graph tests and portable fallback. Rebaseline the public call after establishing that boundary.
