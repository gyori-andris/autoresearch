# Autoresearch handover : <task>

- Contract: <path, version, approval>
- Execution target: <host, workdir, environment; no credentials>
- Scorer command: <copy-pasteable command>
- Objective, direction, baseline: <values>
- Measured variability, threshold, acceptance formula: <values>
- Mutable paths / frozen paths and hashes: <lists>
- Ledger, raw evidence, retained state: <paths>
- Retained revision: <commit; reconcile on startup>
- Per-experiment timeout and resource limits: <values>
- Campaign limits and execution mode: <values>
- Benchmark lease / STOP file: <paths/mechanisms>
- Safe restore and interruption recovery: <commands/procedure>
- Harness verification results: <test artifacts>

## Initial hypotheses

<Ordered, distinct hypotheses tied to observations, not promises of speedup.>

## Operator instructions

Invoke autoresearch-runner on this handover. Stop at the campaign limit or STOP signal.
Resume with renewed authority/budget and reconciled state. The worker cannot edit the
contract; scope changes require review and recalibration.
