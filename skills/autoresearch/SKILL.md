---
name: autoresearch
description: Design or prepare an experimental contract for agent-guided optimisation. Calibrate a baseline and scaffold the frozen evaluator, scorer and handover before search. Use when setting up an autoresearch task; use autoresearch-runner to execute an existing handover.
---

# Autoresearch: prepare the experiment

Turn an objective or existing contract into a loop-ready task. Prepare the experiment;
do not run the optimisation campaign.

## Establish the contract

Read the supplied contract and project instructions first. Preserve agreed decisions;
ask only about missing or conflicting choices. When starting from a goal, use
[the contract template](assets/CONTRACT.template.md) to propose:

- One objective scalar and direction; other measurements are diagnostics or explicit gates.
- Reference implementation, representative fixtures and independent correctness oracle.
- Explicit editable surface and frozen set. Prefer a small surface, but coupled
  Python/native files and architecture changes are allowed when approved and testable.
- Build/test/measurement timeout, memory ceiling and campaign limits.
- Pinned environment, dependencies, threads, timing boundary and cache policy.
- A stability criterion and a keep threshold calibrated from baseline measurements.

CPU-specific work is not limited to AVX2 or SIMD. Inspect exposed CPU features and
cache/memory topology. Distinguish algorithm, layout, language and ISA gains. Require
dispatch/fallback only when portability belongs to this contract. Do not infer new
machine, dependency or spending authority.

Present the contract for approval before calibration or scaffolding. An already approved
contract needs review only for changes or missing choices. Preserve existing artifacts.

## Calibrate and freeze

Measure the unchanged reference repeatedly under the agreed protocol (at least twice;
enough samples for the chosen stability criterion). Record raw samples and variability.
Do not invent a noise floor or claim two runs prove stability. If noise masks meaningful
wins, revise the measurement plan with the user rather than handing over a noisy score.
Record the calibrated threshold and approved contract version.

## Build the task-specific harness

Read [harness requirements](references/harness.md) completely before implementing the
scorer. Scaffold contract, evaluator, canonical implementation surface, `run.py`, ledger,
retained-state record, notes and handover in a dedicated worktree or clean run branch.
Use [the handover template](assets/HANDOVER.template.md). Reuse validated harness parts;
do not substitute example-specific checks for the task's correctness oracle.

Test normal scoring, wrong output, timeout/crash reporting, unchanged-baseline behaviour,
frozen-file tampering and interruption recovery in an isolated test copy. These are
harness checks, not a candidate search. Report which checks actually passed.

## Handover and stop

Commit the scaffold only within authorised scope. Supply the scorer command, baseline,
noise threshold, mutable/frozen paths, limits, machine, stop-file path, recovery rules,
starting hypotheses and execution mode. Tell the user to invoke `autoresearch-runner`
on HANDOVER. Do not claim the loop is running because its scaffold exists.
