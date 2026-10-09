# Autoresearch

**Two skills for turning an engineering objective into a measured optimisation loop.**

You define what matters and approve the experimental contract. The agent proposes
changes, evaluates them, keeps improvements and records failures. The same workflow
can explore Python algorithms, storage access, native kernels or CPU-specific code:
the contract defines the search space.

```text
Your objective / existing contract
                ↓
     autoresearch                 Prepare and validate the experiment
                ↓
     approved contract + evaluator + baseline + HANDOVER
                ↓
     autoresearch-runner          Propose → test → measure → keep/discard
                ↖______________________________|
                ↓
     retained implementation + experiment history
```

## Start here

These are plain Markdown skill folders. Use them with a coding agent that can read
files, edit code and run commands. No installer, Python environment, API key or
particular model is required by the skills themselves. Running an experiment requires
the tools and dependencies of your target project, plus your agent's usual access.

### 1. Get the skills

```sh
git clone https://github.com/gyori-andris/autoresearch.git
```

Or download and extract the repository ZIP. Then point your agent at the skill:

```text
Read /path/to/autoresearch/skills/autoresearch/SKILL.md and follow it
to prepare an optimisation experiment in my project. Read its linked resources
as needed. Present the contract for approval before running anything.
```

Keep each skill's entire folder, including its templates and references. A chat-only assistant can help design a contract, but cannot run the
experiment without access to your project and execution environment.

For automatic discovery and named invocation, copy both folders into your client's
skill directory:

| Client | Project-local destination | Invocation |
| --- | --- | --- |
| Codex | `.agents/skills/` | `$autoresearch`, `$autoresearch-runner` |
| Claude Code | `.claude/skills/` | `/autoresearch`, `/autoresearch-runner` |
| Other agents | Their documented skill directory, or read the files directly | Ask to use the skill by name or path |

For example, from the **target project's root**, for Codex:

```sh
mkdir -p .agents/skills
cp -R /path/to/autoresearch/skills/autoresearch .agents/skills/
cp -R /path/to/autoresearch/skills/autoresearch-runner .agents/skills/
```

For Claude Code, replace `.agents/skills` with `.claude/skills`. You can also copy
the folders in your file manager. If either destination already exists, compare it
before replacing a customised skill. See [installation](docs/install.md)
for folder layout, updates and verification.

### 2. Prepare the experiment with `autoresearch`

Ask your agent:

```text
Use autoresearch to make this parser faster without changing its outputs.
Use representative fixtures and the current implementation as the reference.
Propose the contract for my review before running baseline calibration.
```

If installed, use `$autoresearch` in Codex or `/autoresearch` in Claude Code.

Already have a contract? Say:

```text
Use autoresearch with ./experiment/CONTRACT.md.
Keep the agreed scope. Check what is missing, calibrate the baseline after approval,
and create the evaluator, scorer and HANDOVER. Do not start search yet.
```

The planner establishes one objective, correctness/resource gates, editable files,
measurement conditions, a noise threshold and budgets. It builds the task-specific
harness, checks its failure paths, and stops after handover.

### 3. Run with `autoresearch-runner`

```text
Use autoresearch-runner with ./experiment/HANDOVER.md.
Run up to 10 experiments, with a total wall-clock limit of 30 minutes.
Keep the machine and evaluator fixed. Report the retained result and failures.
```

If using the files directly, point to `skills/autoresearch-runner/SKILL.md` as well.
Choose limits appropriate to your task;
agent inference and benchmark time both consume the campaign budget.

The runner reads durable state, tests one hypothesis at a time, and uses the scorer's
verdict to keep or reject changes. It never changes the contract to make a candidate pass.

## Where you can use it

- **Software performance:** reduce parser latency, allocation overhead or query time
  while preserving behaviour.
- **Machine learning:** improve a validation metric under a fixed training budget,
  with evaluation data held separate from search.
- **Algorithms and native code:** explore data structures, compiler options or CPU-specific
  kernels under an explicit correctness and portability contract.

The target can be your laptop, an existing remote machine or a controlled build
environment. Hardware, models, language, dataset, budget and allowed changes are choices
for each experiment. The skills leave these choices to the contract. The method needs an
executable evaluator; it does not establish whether the objective itself is worthwhile.

## The two skills

| Skill | Responsibility | Produces |
| --- | --- | --- |
| [autoresearch](skills/autoresearch/SKILL.md) | Prepare an approved contract or help design one | Frozen evaluator, calibrated baseline, scorer, handover |
| [autoresearch-runner](skills/autoresearch-runner/SKILL.md) | Execute the authorised search | Candidate records, retained implementation, findings |

Your coding agent follows these instructions during a session. A task's
generated `run.py` scores candidates; it does not itself launch a coding agent.
For fresh-session workers or operation after SSH disconnects, see
[execution modes](docs/running.md). A provider-specific detached controller is not included.

## Choosing models

The runner does not need your most capable model. In our experiments, **Sonnet- and
Luna-class models worked for running the loop** once the contract and evaluator were
established. We used **Sol/Opus for experiment design**: defining the objective, choosing
the search boundary, anticipating edge cases and making the measurements meaningful.

These model choices reflect our experience; we did not run a controlled comparison. Use the models available to you; keep the evaluation and
acceptance rules unchanged when switching runners.

## What does a contract look like?

Start from the [contract template](skills/autoresearch/assets/CONTRACT.template.md).
It names the objective, editable surface, reference, gates and measurement protocol.
The [core principles](CONTRACT.md) explain the invariants; the
[harness requirements](skills/autoresearch/references/harness.md) make them executable.

“Faster sparse conversion” is incomplete. A usable contract also specifies output
equivalence, what is timed, cache conditions, memory limits, permitted CPU features
and the improvement required to retain a candidate. Portable deployment and a
machine-specific proof of concept are different contracts; both are valid choices.

## Stop, resume, inspect

- Ask the runner to stop, or create the `STOP` file at the location in its HANDOVER.
- Inspect `results.tsv` for attempts, `state.json` for the retained revision, and
  `thesis.md` for interpretation. Failed experiments remain in the history.
- Resume by invoking `autoresearch-runner` on the same HANDOVER with a renewed budget.
- Changing scope, machine or evaluator starts a new contract version and baseline.

See [running and troubleshooting](docs/running.md) for interrupted experiments,
plateaus, noisy benchmarks and safe restoration.

## Examples and results

Each of the [14 examples](examples/README.md) has its own notebook: request, setup,
change, evaluation and result. Start with [AnnData](examples/scverse-anndata/notebook.ipynb)
for the contract, handover, calibration and paired measurements.
The [usage guide](examples/USAGE.md) covers preparing and running your own campaign.

No setup is needed to read them. For interactive editing, the same notebooks are
also available as marimo Python files:

```sh
uv sync --locked
uv run marimo edit examples/scverse-anndata/notebook.py
```

These analyse saved measurements; they do not run the original benchmarks. See
[evidence availability](RECOVERY.md) for reproduction gaps. The three Pheiron cases
publish reported results, measurement context and explanations. Their internal source,
datasets and run logs are not distributed.

## References

1. Karpathy, A. [autoresearch](https://github.com/karpathy/autoresearch).
2. Agrawal, L. et al. (2025). [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457).
3. [Fast Gemma Challenge](https://huggingface.co/spaces/gemma-challenge/gemma-dashboard).
4. Virshup, I. et al. (2024). [anndata: Access and store annotated data matrices](https://doi.org/10.21105/joss.04371). *Journal of Open Source Software*.
5. Wolf, F. A. et al. (2018). [SCANPY: large-scale single-cell gene expression data analysis](https://doi.org/10.1186/s13059-017-1382-0). *Genome Biology*.
6. Sturm, G. et al. (2020). [Scirpy](https://doi.org/10.1093/bioinformatics/btaa611). *Bioinformatics*.
7. Palla, G. et al. (2022). [Squidpy](https://doi.org/10.1038/s41592-021-01358-2). *Nature Methods*.
8. scverse/anndata issue #454: [speed up read_dense_as_sparse](https://github.com/scverse/anndata/issues/454).
9. [TileDB-SOMA](https://github.com/single-cell-data/TileDB-SOMA).
10. [Hutter Prize](https://prize.hutter1.net/).
