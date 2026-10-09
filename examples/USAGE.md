# Run a campaign from an example

## Prepare the task

Choose an example with a similar workload. Identify the function to change, the
caller to measure and the reference behaviour to preserve. Work in an isolated
worktree with your own fixtures and pinned reference revision.

Give the case's request to `skills/autoresearch/SKILL.md`. Review the proposed
objective, correctness oracle, editable files, memory/time limits, portability
requirements and campaign budget.

After approval, the planner calibrates the reference, builds the task-specific
scorer and checks rejection of wrong outputs, timeouts and frozen-file changes.
It writes CONTRACT, HANDOVER, retained state and an experiment ledger. Resolve
unstable measurements or failed harness checks before starting search.

## Run the prepared experiment

For example:

```text
Read /path/to/autoresearch/skills/autoresearch-runner/SKILL.md.
Use ./experiment/HANDOVER.md in chat-controller mode.
Run at most 10 experiments or 30 minutes, whichever comes first.
Test one hypothesis per experiment using the approved scorer.
Report the retained result and rejected attempts.
```

Choose limits for your task. In fresh-session mode, each worker runs one experiment
and exits; a separately configured controller checks the budget and launches the next.

The runner changes permitted implementation files and invokes the handover's scorer.
The scorer checks correctness and resource limits, then compares the objective with
the incumbent using the calibrated threshold. On rejection, restore source and keep
the attempt record.

## Read the result

Compare matched workloads and timing boundaries. Report public-call and kernel
timings separately. An instruction-level gain needs a comparison against equivalent
generic native code. A baseline-parity check and an independent mathematical oracle
can expose different errors.

The examples have incomplete original run bundles. See
[evidence availability](../RECOVERY.md) for those gaps.
