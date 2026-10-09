# Workflow origins

The planner/runner split is inspired by
[karpathy/autoresearch](https://github.com/karpathy/autoresearch).
The planner prepares the contract, evaluator and baseline. The runner tests one
hypothesis at a time and records the result.

The skills support existing contracts, coupled Python/native changes and approved
architectural changes. Each campaign has a budget, stop signal and scoped recovery
procedure. Candidate revisions remain available while retained state is tracked
separately.

Tasks can run in one chat session or under a separately configured fresh-session
controller. Both modes read the same durable records. The repository supplies
instructions and harness requirements; each target needs its own tested scorer
and any controller required for unattended operation.
