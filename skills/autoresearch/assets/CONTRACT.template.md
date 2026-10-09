# Experimental contract : <task>

Status: DRAFT. Approval: <person/date>. Version: <id>.

## Objective and scope

- Primary scalar, units, direction and aggregation formula: <exact definition>
- Reference revision: <commit>
- Correctness oracle and tolerances: <definition>
- Hard gates versus diagnostic-only metrics: <distinguish>
- Editable source paths: <explicit list>
- Frozen files/hashes: <contract, evaluator, fixtures, build, dependencies>
- Allowed algorithm, representation and native/ISA changes: <scope>
- Portability requirements: <target-specific or fallback/dispatch>
- Prohibited shortcuts: <semantic changes, output caching, extra workers, etc.>

## Measurement

- Dataset provenance, size, shape, distributions and edge cases: <details>
- Machine, exposed CPU features, compiler and dependencies: <details>
- Affinity and thread counts: <details>
- Timer includes/excludes: <build, startup, I/O, materialisation, output>
- Cache policy, warmup, repetitions and order: <details>
- Memory measurement method and ceiling: <details>
- Baseline samples and variability: <artifact>
- Stability bar and acceptance formula: <measured threshold>
- Per-experiment timeout: <build + test + evaluation>

## Operation

- Authorised working directory and benchmark lease: <paths>
- Scorer command: <exact command>
- Ledger, raw artifacts, retained state and STOP file: <paths>
- Mode: <chat controller or separately configured fresh-session controller>
- Campaign cap: <count and/or wall-clock; spending limit if applicable>
- Interruption and scoped restoration protocol: <implementation>
- Rebaseline triggers: <machine/data/dependency/evaluator/scope changes>
