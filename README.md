# Skills

Portable engineering skills for Claude Code, Codex CLI, and pi agent.

Each skill uses the directory-based Agent Skills format. Instructions use host capabilities rather than fixed tool names, model IDs, or transcript paths.

## Available skills

| Skill | Purpose |
| --- | --- |
| [eval](skills/eval/SKILL.md) | Compare a skill or workflow change against the current baseline before adoption. |
| [verify-result](skills/verify-result/SKILL.md) | Manually verify observable results. Experimental; pilots show no correctness gain over the tested baseline. |

## Install locally

1. Clone the repository into a directory you choose:

   ```sh
   git clone https://github.com/geniusgordon/skills.git geniusgordon-skills
   cd geniusgordon-skills
   ```

2. From the repository root, link both skills into each host's personal location:

   ```sh
   mkdir -p ~/.claude/skills ~/.agents/skills
   for name in eval verify-result; do
     ln -s "$(pwd)/skills/$name" "$HOME/.claude/skills/$name"
     ln -s "$(pwd)/skills/$name" "$HOME/.agents/skills/$name"
   done
   ```

   These commands create links without replacing existing entries. If either destination exists, inspect it before you choose another name or replace it. Keep the checkout in place while the links are installed.

Claude Code reads `~/.claude/skills/`. Codex CLI and pi read `~/.agents/skills/`. The checkout's `skills/` directory alone is not an automatic discovery location.

Start a new session after installation. In an existing pi session, use `/reload`.

| Host | Eval | Verify Result |
| --- | --- | --- |
| Claude Code | `/eval <request>` | `/verify-result <request>` |
| Codex CLI | `$eval <request>` | `$verify-result <request>` |
| pi agent | `/skill:eval <request>` | `/skill:verify-result <request>` |

Both skills require explicit invocation. Claude Code and pi use `disable-model-invocation: true` in `SKILL.md`. Codex uses `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. These settings restrict automatic selection; they are not permission or sandbox controls.

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
evaluations/verify-result/
  plan.md
  checks.py
  calibrate.py
  fixtures/
```

Keep private run records outside version control. The repository ignores `reports/` and `.pi/`.

The [verify-result comparison plan](evaluations/verify-result/plan.md) uses local cases rather than ongoing product work. The [pilot summary](evaluations/verify-result/pilot-summary.md) records the observed limits. Manual installation supports further trials, not a claim of proven benefit. Exclude the proposed skill from baseline runs, even after installation.

## Scope

This repository contains instructions, not an execution harness. It does not configure authentication, bypass permissions, or provide an automatic model-routing layer.

Host support covers portable skill discovery and a capability-based execution protocol. It does not imply identical tool APIs or successful end-to-end runs on every host.

The first version passed structural checks and explicit skill-load smoke checks on Claude Code `2.1.251`, Codex CLI `0.161.0`, and pi `1.5.0`. Each host returned the five phases and a sentence from the bundled protocol. Codex and pi execution logs also recorded file reads. The Claude run returned only its final result, so its file-read trace remains unverified.

Those smoke checks preceded the manual-only settings. They do not establish the current command behavior on every host. Five controlled A/B pilots used Connexmatrix through pi; no cross-host behavior comparison, holdouts, or blinded judge ran. The official host documentation confirms the locations and commands above.

## Attribution

The eval skill adapts [pstack's Eval playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md) and [Arena skill](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) by Lauren Tan.

Verify Result adapts pstack's [Prove It Works principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-prove-it-works/SKILL.md).

The [MIT license](LICENSE) retains the upstream copyright and permission notice. Eval adaptation details appear in [the protocol](skills/eval/references/protocol.md#attribution).
