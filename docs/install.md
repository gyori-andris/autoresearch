# Use the skills with your agent

Each skill is a folder of Markdown instructions and supporting files. There is no
installation program, background service or mandatory Python dependency.

## Option A: read the files directly

Clone or download this repository. Ask your agent to read
`skills/autoresearch/SKILL.md`, including its linked resources, and prepare an experiment
in your project. After approving the contract and receiving a validated HANDOVER, ask
it to read `skills/autoresearch-runner/SKILL.md` and run the agreed campaign.

This does not depend on auto-discovery or slash-command support. It requires an agent
that can read local files and execute the task. A chat-only interface may help design
the contract but cannot run experiments. Keep the whole skill folder: SKILL.md alone
omits the planner's templates and harness reference.

## Option B: copy into a skill directory

Copy `skills/autoresearch/` and `skills/autoresearch-runner/` into `.agents/skills/`
for Codex or `.claude/skills/` for Claude Code. The resulting layout is:

```text
your-project/
  .agents/skills/                 # .claude/skills/ for Claude Code
    autoresearch/
      SKILL.md
      assets/
      references/
    autoresearch-runner/
      SKILL.md
```

Copy the two skill folders, not the repository root. Examples and notebooks are optional. For account-wide
installation or another client, use its documented skill directory. File-manager copying
works too; a shell is not required for this step.

## Verify without starting an experiment

Open a fresh agent session in the target project and ask:

```text
Read the autoresearch and autoresearch-runner skills. Explain which prepares
the experiment and which runs it, and identify the contract template.
Do not edit files or execute experiments yet.
```

If discovery fails, provide the full skill paths. Installation does not require
authentication beyond your existing agent setup and does not start a campaign.

## Updates and customisation

Compare changes before replacing installed folders, particularly if you customised
them. Keep a backup; do not merge directory trees blindly. A copy is a snapshot and
does not auto-update when this repository changes.

Keep project-specific machines, datasets, thresholds and budgets in the experiment
contract and handover, not in the generic skills. When adapting the workflow, preserve
the planner/runner boundary and make changed acceptance rules explicit.

Client documentation: [Codex skills](https://developers.openai.com/codex/skills),
[Claude Code skills](https://code.claude.com/docs/en/skills).
