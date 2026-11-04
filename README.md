# Skills

Portable engineering skills for Claude Code, Codex CLI, and pi agent.

Each skill uses the directory-based Agent Skills format. Instructions use host capabilities rather than fixed tool names, model IDs, or transcript paths.

## Available skills

| Skill | Purpose |
| --- | --- |
| [eval](skills/eval/SKILL.md) | Compare a skill or workflow change against the current baseline before adoption. |
| [verify-result](skills/verify-result/SKILL.md) | Manually verify observable results. Experimental; pilots show no correctness gain over the tested baseline. |
| [bug-fix](skills/bug-fix/SKILL.md) | Manually reproduce, diagnose, fix, and verify a defect. Draft; requires the sibling verify-result skill. |
| [reflect](skills/reflect/SKILL.md) | Extract lessons from real work and propose targeted skill edits. Changes require approval. |

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
       for name in eval verify-result bug-fix reflect; do
         destination="$base/$name"
         if [ -e "$destination" ] || [ -L "$destination" ]; then
           printf 'Already exists: %s\n' "$destination" >&2
           exit 1
         fi
       done
     done
     mkdir -p "$HOME/.claude/skills" "$HOME/.agents/skills"
     for base in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
       for name in eval verify-result bug-fix reflect; do
         ln -s "$(pwd)/skills/$name" "$base/$name"
       done
     done
   )
   ```

   The block checks all destinations before it creates links. Existing entries, including dangling symlinks, stop installation. Inspect the reported entry before you choose another name or replace it. Do not run concurrent installations. Keep the checkout in place while the links are installed.

Claude Code reads `~/.claude/skills/`. Codex CLI and pi read `~/.agents/skills/`. The checkout's `skills/` directory alone is not an automatic discovery location.

Start a new session after installation. In an existing pi session, use `/reload`.

| Host | Eval | Verify Result |
| --- | --- | --- |
| Claude Code | `/eval <request>` | `/verify-result <request>` |
| Codex CLI | `$eval <request>` | `$verify-result <request>` |
| pi agent | `/skill:eval <request>` | `/skill:verify-result <request>` |

All skills require explicit invocation. Invoke Bug Fix with `/bug-fix <request>` in Claude Code, `$bug-fix <request>` in Codex, or `/skill:bug-fix <request>` in pi. It reads `../verify-result/SKILL.md` directly, so install both sibling directories. Resolve relative references from the loaded skill's directory.

Invoke Reflect with `/reflect`, `$reflect`, or `/skill:reflect` respectively. It reviews the current work and proposes changes. It waits for approval before edits and does not publish tickets or changes automatically.

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

## Improve skills through real work

1. Use a workflow in your work project.
2. Invoke Reflect after a correction, failure, or useful result.
3. Review the evidence and exact proposed changes.
4. Approve selected changes in the canonical skill checkout.
5. Run local checks; use Eval when a behavior comparison merits extra model calls.

Reflect can use the visible conversation when the host does not expose its current transcript. It must disclose evidence gaps. Keep private project details in project-local guidance rather than global skills.

## Repository layout

```text
skills/
  eval/
    SKILL.md
    agents/openai.yaml
    references/
      protocol.md
      report-template.md
  verify-result/
    SKILL.md
    agents/openai.yaml
  bug-fix/
    SKILL.md
    agents/openai.yaml
  reflect/
    SKILL.md
    agents/openai.yaml
    references/proposal-template.md
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

The [MIT license](LICENSE) retains the upstream copyright and permission notice. Eval adaptation details appear in [the protocol](skills/eval/references/protocol.md#attribution).
