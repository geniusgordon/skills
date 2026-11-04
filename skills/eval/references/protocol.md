# Execution protocol

## Host-neutral contract

Use ordinary file tools, shell commands, and the host's available agent facilities. No specific subagent API, model slug, transcript directory, or external skill is required.

Before execution, establish these capabilities:

1. Start an independent session with controlled instructions and the intended skill variant.
2. Give that session an isolated project state and appropriate permissions.
3. Capture its output and run checks against the resulting artifact.
4. Retain execution records if the host exposes them.
5. Start a separate judge, or disclose that review is not blinded.

A shell with an installed agent CLI can provide independent sessions even when native subagents are absent. Check current command help before choosing flags. Respect the user's authentication, approval, and sandbox configuration. Keep safety checks enabled.

If no independent execution path exists, produce the experiment plan and mark execution blocked. Ask the user only for the specific missing permission or capability.

## Match the comparison

Compare baseline and proposed change on the same model first. To assess several models or hosts, repeat the matched comparison within each one. A cross-model difference alone does not measure the skill's effect.

Use the same repository revision, fixtures, task prompt, tool access, and effort within a pair. Counterbalance execution order where practical. Record unavoidable environment differences.

Freeze the rubric and promotion rule before execution. A useful screening rule requires no critical regression, an observed target improvement, and cost within the approved limit. Choose the actual thresholds for the task before you see outputs.

Keep holdout cases separate from instruction edits. If a holdout becomes part of the edit loop, replace it before the next adoption decision.

## Separate candidate and coordinator material

The coordinator owns the version map, rubric, run matrix, and reports. Candidates receive only natural project context, the intended variant, and the ordinary user task.

Neutral workspace names hide experimental labels; they do not establish a security boundary. Check ancestor instructions, user-level skills, shared configuration, environment variables, and accessible report paths. Use actual access restrictions where the host supports them. Disclose residual exposure.

Do not place evaluation labels in candidate prompts or workspace names. Do not rename legitimate source identifiers merely because they contain words such as `test` or `benchmark`. Preserve the real task.

Skill evaluation differs from instruction-following self-report. Inspect which files the agent actually read and what it actually executed. A claimed skill load is not enough.

## Records and privacy

Locate records through the host's documented facilities or explicit run output. Inspect only the sessions created for this comparison. Never search unrelated user chats for evidence.

Keep raw records local unless the user approves publication. Redact secrets, private inputs, and unrelated information before sharing. Give the judge sanitized artifact copies rather than raw metadata when metadata reveals model or variant identity.

Usage and transcript formats differ by host. Record unknown values as unavailable. A missing transcript limits process claims; it does not erase executable outcome evidence.

## Attribution

Adapted from pstack's Eval playbook by Lauren Tan, licensed under MIT:

- https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/eval.md
- https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md

The adaptation removes Cursor-specific delegation, model defaults, and transcript paths. It adds matched baseline comparisons, resource approval, host capability checks, holdouts, and explicit inconclusive outcomes.

The upstream copyright and license notice live in `../../../LICENSE`, relative to this file.
