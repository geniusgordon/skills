# gstack

The `gstack-` skill prefix identifies this collection from `geniusgordon/skills`. It does not use a host-specific plugin namespace.

Portable engineering skills for Claude Code, Codex CLI, and pi agent.

Each skill uses the directory-based Agent Skills format. Instructions use host capabilities rather than fixed tool names, model IDs, or transcript paths.

## Available skills

| Skill | Purpose |
| --- | --- |
| [eval](skills/gstack-eval/SKILL.md) | Compare a skill or workflow change against the current baseline before adoption. |
| [verify-result](skills/gstack-verify-result/SKILL.md) | Manually verify observable results. Experimental; pilots show no correctness gain over the tested baseline. |
| [bug-fix](skills/gstack-bug-fix/SKILL.md) | Manually reproduce, diagnose, fix, and verify a defect. Draft; requires the sibling verify-result skill. |
| [reflect](skills/gstack-reflect/SKILL.md) | Extract lessons from real work and propose targeted skill edits. Changes require approval. |
| [create-skill](skills/gstack-create-skill/SKILL.md) | Create or update a focused skill, check its artifact, and route warranted behavior comparisons to Eval. Draft. |
| [plan](skills/gstack-plan/SKILL.md) | Ground a task, settle its design, and write a verifiable plan. Stops before production implementation. Draft. |
| [arena](skills/gstack-arena/SKILL.md) | Compare independent candidates, select and synthesize an artifact, then verify it within an approved budget. Draft. |
| [handoff](skills/gstack-handoff/SKILL.md) | Save a task checkpoint or reconcile its resume point without implicit execution permission. Draft. |
| [prototype](skills/gstack-prototype/SKILL.md) | Answer a bounded empirical question with a disposable experiment, retained evidence, and scoped cleanup. Draft. |

## Install locally

1. Clone the repository into a directory you choose:

   ```sh
   git clone https://github.com/geniusgordon/skills.git geniusgordon-skills
   cd geniusgordon-skills
   ```

2. From the repository root, link all skills into each host's personal location:

   ```sh
   (
     set -eu
     for base in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
       for name in gstack-eval gstack-verify-result gstack-bug-fix gstack-reflect gstack-create-skill gstack-plan gstack-arena gstack-handoff gstack-prototype; do
         destination="$base/$name"
         if [ -e "$destination" ] || [ -L "$destination" ]; then
           printf 'Already exists: %s\n' "$destination" >&2
           exit 1
         fi
       done
     done
     mkdir -p "$HOME/.claude/skills" "$HOME/.agents/skills"
     for base in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
       for name in gstack-eval gstack-verify-result gstack-bug-fix gstack-reflect gstack-create-skill gstack-plan gstack-arena gstack-handoff gstack-prototype; do
         ln -s "$(pwd)/skills/$name" "$base/$name"
       done
     done
   )
   ```

   The block checks all destinations before it creates links. Existing entries, including dangling symlinks, stop installation. Inspect the reported entry before you choose another name or replace it. Do not run concurrent installations. Keep the checkout in place while the links are installed.

Claude Code reads `~/.claude/skills/`. Codex CLI and pi read `~/.agents/skills/`. The checkout's `skills/` directory alone is not an automatic discovery location.

Start a new session after installation. In an existing pi session, use `/reload`.

After a rename, pi uses the frontmatter name, not an old symlink's basename. An old installed path is not a portable command alias. Use the `gstack-` commands below.

| Host | Eval | Verify Result |
| --- | --- | --- |
| Claude Code | `/gstack-eval <request>` | `/gstack-verify-result <request>` |
| Codex CLI | `$gstack-eval <request>` | `$gstack-verify-result <request>` |
| pi agent | `/skill:gstack-eval <request>` | `/skill:gstack-verify-result <request>` |

All skills require explicit invocation. Invoke Bug Fix with `/gstack-bug-fix <request>` in Claude Code, `$gstack-bug-fix <request>` in Codex, or `/skill:gstack-bug-fix <request>` in pi. It depends on the sibling Verify Result workflow, so install both directories. Resolve relative references from the loaded skill's directory.

Invoke Reflect with `/gstack-reflect`, `$gstack-reflect`, or `/skill:gstack-reflect` respectively. It reviews the current work and proposes changes. It waits for approval before edits and does not publish tickets or changes automatically.

Invoke Create Skill with `/gstack-create-skill <request>`, `$gstack-create-skill <request>`, or `/skill:gstack-create-skill <request>` respectively. Name the purpose or existing target and intended hosts. It reuses an existing skill when appropriate and preserves its invocation policy.

Invoke Plan with `/gstack-plan <request>`, `$gstack-plan <request>`, or `/skill:gstack-plan <request>` respectively. It grounds the project, compares designs when needed, and writes the plan using the project's artifact convention. It does not implement the plan.

Invoke Arena with `/gstack-arena <request>`, `$gstack-arena <request>`, or `/skill:gstack-arena <request>` respectively. Define the artifact and scope. Candidate calls, an optional judge, and retries need an approved bounded budget. Arena selects an artifact; Eval compares workflow behavior.

Invoke Handoff with `/gstack-handoff checkpoint <task and note path>` or `/gstack-handoff resume <note path>` in Claude Code. Use `$gstack-handoff` in Codex or `/skill:gstack-handoff` in pi with the same arguments. Resume-only requests identify the next action without starting implementation. A live checkpoint is not a clean pause or a durable copy of dirty code.

Invoke Prototype with `/gstack-prototype <question and limits>`, `$gstack-prototype <question and limits>`, or `/skill:gstack-prototype <question and limits>` respectively. It operates a scoped scratch experiment and returns observations, limitations, and cleanup state, not production code. It needs no full plan or multiple candidates.

A sibling pointer is a workflow dependency, not portable permission. Claude Code's current documentation blocks autonomous manual-only invocation and prohibits a workaround that reproduces its steps. Follow the host's authorized invocation path. A blocked handoff needs explicit user permission; do not bypass it through file reads. Runtime support for these handoffs remains untested.

Claude Code and pi use `disable-model-invocation: true` in `SKILL.md`. Codex uses `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. These settings restrict automatic selection; they are not permission or sandbox controls.

Official host references:

- [Claude Code skills](https://code.claude.com/docs/en/skills).
- [Codex skills](https://developers.openai.com/codex/skills).
- [pi skills](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).

## Evaluate a change

Use your host's explicit eval command with this request:

```text
Compare my current bug-fix workflow with this proposed change.
Prepare the cases, rubric, and run budget first. Wait for approval before paid runs.
```

The skill requires independent sessions and matched project state. It uses available native agent facilities or installed CLIs. It reports blocked execution if neither supports the required isolation.

Executable checks take priority over judge scores. Missing execution records limit process claims. A same-family judge or non-blinded review must appear as a limitation.

## Conditional methods

Bug Fix reads [hard-debug methods](skills/gstack-bug-fix/references/hard-debug.md) when causes remain uncertain or the trigger is intermittent. Reflect reads [environment-review methods](skills/gstack-reflect/references/environment-review.md) when session evidence points to tooling, navigation, or context friction.

Plan reads a [planning adapter](skills/gstack-plan/references/prototype.md) for small safe empirical probes that can change its design. Standalone Prototype owns the complete experiment method. Plan keeps its bounded local probe capability without a Prototype, Arena, or Handoff dependency; broader experiments require separate permitted invocation. Its [five cases](evaluations/plan/cases.md) define the wider scope; the empirical-fork regression described below ran locally, but no comparative evaluation established Plan's benefit.

Prototype's [five cases](evaluations/prototype/cases.md) cover parser behavior, operated UI, timing limits, unavailable environments, and failed-attempt cleanup. One local Pi parser smoke executed ten synthetic inputs, retained evidence, and removed owned scratch state. A separate Plan regression executed seven inputs without a Prototype sibling and stopped at a plan. Source bytes remained unchanged. UI, failure cleanup, native commands, cross-host behavior, and comparative benefit remain unverified.

Arena uses a [run record](skills/gstack-arena/references/run-record.md) for scope, attempts, selection, and final evidence. Its [five cases](evaluations/arena/cases.md) cover design/code candidates, dropouts, missing grants/judges, and synthesis failures. One local design-only smoke completed two same-model candidates and a main-agent synthesis; no judge, native skill-command trial, dropout, code-worktree trial, or comparative benefit was established.

Handoff uses a [checkpoint contract](skills/gstack-handoff/references/checkpoint-template.md) for task state and evidence. Its [five cases](evaluations/handoff/cases.md) define the broader trial scope. Three local Pi sessions exercised checkpoint creation, unchanged-state resume, and changed-state resume in a synthetic dirty repository. They preserved user edits, identified stale evidence, and rejected historical destructive instructions. Native skill commands, active-worker recovery, process identity conflicts, and cross-host behavior remain untested. It does not automatically commit, terminate workers, restart sessions, or treat historical approvals as current permission. Plan, checkpoint, and raw evidence remain separate artifacts.

The Bug Fix and Reflect references summarize useful methods from Matt Pocock's diagnosing-bugs and retro skills. Small local comparisons confirmed reference access, but showed no correctness gain. They do not require the original skills to be installed.

## Improve skills through real work

1. Use a workflow in your work project.
2. Invoke Reflect after a correction, failure, or useful result.
3. Review the evidence and exact proposed changes.
4. Approve selected changes in the canonical skill checkout.
5. Run local checks; use Eval when a behavior comparison merits extra model calls.

Reflect can use the visible conversation when the host does not expose its current transcript. It must disclose evidence gaps. Keep private project details in project-local guidance rather than global skills.

For approved substantive skill edits, Reflect hands the proposal to Create Skill when the host permits it. Create Skill handles authoring and local checks, then prepares an Eval comparison when warranted. Approved scope, host permission, and an existing run budget let the workflow continue without a duplicate approval request. Small wording corrections remain direct.

The [authoring survey](docs/skill-authoring-survey.md) compares Cursor, Matt Pocock, Anthropic, and OpenAI guidance. Cursor's installed built-in source was unavailable. The creator is an original synthesis, not a recovered vendor implementation. Its [cases](evaluations/create-skill/cases.md) define initial static walkthroughs. A later local ten-candidate screening plus one blind judge was inconclusive: no correctness improvement was established, and measurement defects limit the comparison. Private records remain under ignored `reports/`.

## Repository layout

```text
skills/
  gstack-eval/
    SKILL.md
    agents/openai.yaml
    references/
      protocol.md
      report-template.md
  gstack-verify-result/
    SKILL.md
    agents/openai.yaml
  gstack-bug-fix/
    SKILL.md
    agents/openai.yaml
  gstack-reflect/
    SKILL.md
    agents/openai.yaml
    references/proposal-template.md
  gstack-create-skill/
    SKILL.md
    agents/openai.yaml
    references/authoring-checks.md
  gstack-plan/
    SKILL.md
    agents/openai.yaml
    references/prototype.md
  gstack-arena/
    SKILL.md
    agents/openai.yaml
    references/run-record.md
  gstack-handoff/
    SKILL.md
    agents/openai.yaml
    references/checkpoint-template.md
  gstack-prototype/
    SKILL.md
    agents/openai.yaml
docs/
  skill-authoring-survey.md
evaluations/create-skill/
  cases.md
evaluations/plan/
  cases.md
evaluations/arena/
  cases.md
evaluations/handoff/
  cases.md
evaluations/prototype/
  cases.md
evaluations/verify-result/
  plan.md
  checks.py
  calibrate.py
  fixtures/
```

Keep private run records outside version control. The repository ignores `reports/` and `.pi/`.

The [verify-result comparison plan](evaluations/verify-result/plan.md) uses local cases rather than ongoing product work. The [pilot summary](evaluations/verify-result/pilot-summary.md) records the observed limits. Manual installation supports further trials, not a claim of proven benefit. Exclude the proposed skill from baseline runs, even after installation.

The [Bug Fix comparison plan](evaluations/bug-fix/plan.md) adds a calibrated lost-response/retry case. Run `python3 evaluations/bug-fix/calibrate.py` to check the fixture. No agent behavior comparison has run for Bug Fix.

## Scope

This repository contains instructions, not an execution harness. It does not configure authentication, bypass permissions, or provide an automatic model-routing layer.

Host support covers portable skill discovery and a capability-based execution protocol. It does not imply identical tool APIs or successful end-to-end runs on every host.

The first version passed structural checks and explicit skill-load smoke checks on Claude Code `2.1.251`, Codex CLI `0.161.0`, and pi `1.5.0`. Each host returned the five phases and a sentence from the bundled protocol. Codex and pi execution logs also recorded file reads. The Claude run returned only its final result, so its file-read trace remains unverified.

Those smoke checks preceded the manual-only settings. They do not establish the current command behavior on every host. Five controlled A/B pilots used Connexmatrix through pi; no cross-host behavior comparison, holdouts, or blinded judge ran. The official host documentation confirms the locations and commands above.

## Attribution

The eval skill adapts [pstack's Eval playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md) and [Arena skill](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) by Lauren Tan.

Verify Result adapts pstack's [Prove It Works principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-prove-it-works/SKILL.md). Bug Fix adapts its [Bug fix playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/bug-fix.md). Reflect adapts its [Reflect skill](https://github.com/cursor/plugins/blob/main/pstack/skills/reflect/SKILL.md).

Plan adapts pstack's [design guide](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/04-design.md), [Architect skill](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md), [Multi-phase plan](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md), and [Prototype playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md). It removes automatic implementation, mandatory multi-model design, and fixed verification lanes.

Arena adapts pstack's [Arena skill](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md). Handoff adapts its [Pause safely](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/pause-safely.md) and [Session pickup](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/session-pickup.md) playbooks. They retain evidence-based selection and state recovery without fixed models or automatic lifecycle actions.

Standalone Prototype also adapts pstack's [Prototype playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md). It owns the full experiment method, while Plan retains a small planning-specific adapter. Neither automatically promotes scratch code to production.

The [MIT license](LICENSE) retains the upstream copyright and permission notice. Eval adaptation details appear in [the protocol](skills/gstack-eval/references/protocol.md#attribution).
