# Running, stopping and recovering

## Start with a short campaign

First approve a contract, calibrate the reference and test the harness with `autoresearch`.
Then ask `autoresearch-runner` for a bounded campaign, such as 10 attempts or 30 minutes,
whichever comes first. Run one benchmark at a time per machine. You can explore different
tasks on separate machines, but each needs its own pinned baseline.

The minimum run artifacts are:

```text
experiment/
  CONTRACT.md       Human-approved scope, gates, budgets and measurement protocol
  HANDOVER.md       Exact commands and operator instructions
  run.py            Task-specific scorer; sole measurement/decision writer
  evaluator.py      Frozen correctness oracle and objective
  results.tsv       Every attempt, including failures and rejected candidates
  state.json        Retained revision, score and in-flight transaction
  thesis.md         Hypotheses, interpretation and next ideas
  artifacts/        Raw samples, logs, environment and hashes
```

The mutable source may live elsewhere in the target repository. Its exact paths belong
in the contract; the layout above is illustrative, not a requirement to move source.

## Two execution modes

**Chat controller:** your current agent uses the runner skill to conduct a sequence of
experiments. This is the simplest starting point. It reloads state after interruptions
or context rollover. Do not assume it continues after its process exits.

**Fresh-session controller:** a separate process starts a new agent session for each
experiment, with the same handover and durable state. The worker does one experiment
and exits. The controller checks budget, STOP, exit status and transaction consistency
before starting another. Model cadence belongs here, not in the benchmark evaluator.

The skills support this division of responsibility, but this repository does not yet
provide a tested provider-specific controller. Do not mistake the scorer `run.py` for
an agent launcher. Configure and validate your controller before unattended use.

## Detachment and tmux

tmux can keep an already configured agent/controller process alive after an SSH client
disconnects. It does not create fresh contexts, enforce a campaign budget, prevent CPU
contention or recover a broken scorer. It also does not survive a VM shutdown.

Launch the configured controller in a named tmux session, confirm its process and first
ledger entry, detach, and reattach to check status. The exact launch command is specific
to your chosen agent and must be recorded in HANDOVER; none is invented by these skills.
Do not copy credentials into the repository. Use the agent's supported authentication.

## Stop and resume

Use the stop-file path specified in HANDOVER, or tell the controller to stop. Its scorer
must have a hard timeout, and its controller must stop scheduling new attempts. If a run
is interrupted, keep its in-flight marker and logs rather than pretending it completed.

Before resuming, reconcile candidate revision, ledger record and retained state. A scored
candidate without a recorded retention transition needs reconciliation, not another score.
An unscored interrupted candidate needs a failed/interrupted record under the harness's
recovery protocol. The worker cannot manually invent scores or rewrite the ledger.

## Common problems

| Observation | Action |
| --- | --- |
| Skill is not discovered | Check the target project and installation paths; open a fresh agent session. You can explicitly point the agent at SKILL.md. |
| An older/customised skill already exists | Compare the folders and back up your version before replacing it. |
| Benchmark variation exceeds meaningful gains | Return to measurement design; do not lower the threshold mid-campaign. |
| Correctness passes but candidate is rejected | Compare against the incumbent and threshold, not only the original baseline. |
| Native result survives a source revert suspiciously well | Ensure each score rebuilds native binaries from the exact candidate. |
| Warm result is fast but startup or memory explodes | Check resource gates and the timer boundary; report cold and warm costs separately. |
| Twenty attempts make no progress | Reassess hypothesis families within scope; do not silently broaden the contract. |
| STOP, budget or lease is ignored | Treat it as a controller/harness defect and stop before further experiments. |

## Acceptance and deployment

The contract decides which candidates to retain. A retained candidate still needs
review for its intended deployment, including portability and upstream requirements.
