---
name: autoresearch-runner
description: Execute an authorised optimisation campaign from an autoresearch HANDOVER. Propose one hypothesis per experiment, score with the frozen harness, retain or reject by its verdict, and preserve resumable state. Use to start or resume a prepared loop, not to design its evaluator.
---

# Autoresearch: run the experiment

Run the prepared task. All task-specific scope, authority and commands come from its
approved contract and handover. Do not improvise a different benchmark.

## Load before starting or resuming

Read HANDOVER, CONTRACT, thesis notes, retained state, recent ledger and Git history.
Verify machine, mutable/frozen paths, baseline, threshold, limits, lease, stop signal
and remaining campaign budget. Missing handover/calibration routes to `autoresearch`.
Missing budget/launch authority requires clarification. Launch only with an approved campaign budget.

Respect execution mode. In chat-controller mode, iterate here within the authorised
budget. In externally managed fresh-session mode, do exactly one experiment and exit;
the external controller starts the next worker. Do not spawn another controller or
claim detachment merely because a skill is installed.

## One experiment

1. Check STOP, lease and budget. Reconcile in-flight state against durable records before
   editing. Do not rescore a completed attempt under the same ID.
2. Orient from results and notes. Propose one concrete hypothesis. Coupled edits are
   allowed within the declared surface, not arbitrary extra scope or versioned copies.
3. Record the incumbent. Edit permitted source and commit the candidate as prescribed.
   Preserve unrelated user changes; use an isolated worktree if necessary.
4. Run the exact scorer command. It owns build, tests, timeout, resource gates, objective,
   ledger and decision. Do not run competing timed work on the same machine.
5. Read the terminal record. Passing correctness is not KEEP; follow the scorer's
   incumbent-relative, noise-aware verdict. Preserve evidence and candidate identity.
6. On rejection use the handover's scoped restoration protocol. No broad hard resets or
   deletion of unrelated files. Verify source matches retained state.
7. Record hypothesis, outcome, interpretation and next idea in notes. Never hand-edit
   measurements or promote a rejected score. Continue or exit according to mode/budget.

Ordinary candidate failures do not end the campaign: record, restore, try the next idea.
A trivial fix is a new attempt with its own revision and record. Missing records, frozen
file violations, unsafe recovery, resource exhaustion or unresolved state conflicts are
harness faults: stop experimentation and report the condition rather than loop blindly.

## Reflection and search

Profiling and microbenchmarks inform hypotheses; the contracted score decides retention.
Explore algorithms, representation, allocation, cache layout and available instructions
where allowed. Do not force SIMD onto dependency- or I/O-dominated work.

After 20 consecutive sub-threshold attempts (or the configured interval), explain what
failed, retire unproductive hypothesis families and reorder the backlog. After a second
interval, flag the plateau clearly. Continue only with remaining authorised budget and
a meaningful in-scope hypothesis. Scope/metric changes require review and recalibration.

## Stop and recovery

Stop on user request, STOP file, campaign limit or unsafe/invalid execution. Flush notes;
report retained revision/score, attempts, failures, known budget use and resume instructions.
Before context rollover finish or mark the transaction and checkpoint durable state.
Reload the durable records in the next session. Do not invent compaction
commands, token counts or surviving background processes.

Optimisation permission does not imply permission to push, deploy, provision machines,
install new dependencies or enlarge budgets. Follow the contract and user authority.
