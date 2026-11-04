# Skills

Portable engineering skills for Claude Code, Codex CLI, and pi agent.

Each skill uses the directory-based Agent Skills format. Instructions use host capabilities rather than fixed tool names, model IDs, or transcript paths.

## Available skills

| Skill | Purpose |
| --- | --- |
| [eval](skills/eval/SKILL.md) | Compare a skill or workflow change against the current baseline before adoption. |

## Install locally

1. Clone the repository into a directory you choose:

   ```sh
   git clone https://github.com/geniusgordon/skills.git geniusgordon-skills
   cd geniusgordon-skills
   ```

2. From the repository root, link the skill into each host's personal location:

   ```sh
   mkdir -p ~/.claude/skills ~/.agents/skills
   ln -s "$(pwd)/skills/eval" ~/.claude/skills/eval
   ln -s "$(pwd)/skills/eval" ~/.agents/skills/eval
   ```

   These commands create links without replacing existing entries. If either destination exists, inspect it before you choose another name or replace it. Keep the checkout in place while the links are installed.

Claude Code reads `~/.claude/skills/`. Codex CLI and pi read `~/.agents/skills/`. The checkout's `skills/` directory alone is not an automatic discovery location.

Start a new session after installation. In an existing pi session, use `/reload`.

| Host | Explicit invocation |
| --- | --- |
| Claude Code | `/eval <request>` |
| Codex CLI | `$eval <request>`, or select it through `/skills` |
| pi agent | `/skill:eval <request>` |

The skill can also load from its description. A discovery check and a completed evaluation are separate checks.

Official host references:

- [Claude Code skills](https://code.claude.com/docs/en/skills).
- [Codex skills](https://developers.openai.com/codex/skills).
- [pi skills](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).

## Evaluate a change

Ask the agent to use the eval skill and name the change:

```text
Use the eval skill to compare my current bug-fix workflow with this proposed change.
Prepare the cases, rubric, and run budget first. Wait for approval before paid runs.
```

The skill requires independent sessions and matched project state. It uses available native agent facilities or installed CLIs. It reports blocked execution if neither supports the required isolation.

Executable checks take priority over judge scores. Missing execution records limit process claims. A same-family judge or non-blinded review must appear as a limitation.

## Repository layout

```text
skills/
  eval/
    SKILL.md
    references/
      protocol.md
      report-template.md
```

Keep private run records outside version control. The repository ignores `reports/` and `.pi/`.

## Scope

This repository contains instructions, not an execution harness. It does not configure authentication, bypass permissions, or provide an automatic model-routing layer.

Host support covers portable skill discovery and a capability-based execution protocol. It does not imply identical tool APIs or successful end-to-end runs on every host.

The first version passed structural checks and explicit skill-load smoke checks on Claude Code `2.1.251`, Codex CLI `0.161.0`, and pi `1.5.0`. Each host returned the five phases and a sentence from the bundled protocol. Codex and pi execution logs also recorded file reads. The Claude run returned only its final result, so its file-read trace remains unverified.

These checks confirm explicit invocation and reference access, not automatic discovery decisions or a complete evaluation. Matched baseline comparisons, blinding, and adoption decisions remain untested. The official host documentation confirms the locations and commands above.

## Attribution

The eval skill adapts [pstack's Eval playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md) and [Arena skill](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md) by Lauren Tan.

The [MIT license](LICENSE) retains the upstream copyright and permission notice. Adaptation details appear in [the protocol](skills/eval/references/protocol.md#attribution).
