---
name: gstack-verify-result
description: Verify a task's observable result with direct checks and report verified, failed, or unverified evidence.
disable-model-invocation: true
license: MIT
---

# Verify Result

Check the result the user needs, on the current artifact. Prefer existing commands and tools. This skill verifies work; it does not authorize new scope or unsafe actions.

## 1. Define the result

Derive observable completion conditions from the request and affected behavior. Name the artifact or revision under check. Use existing acceptance criteria when available.

For a bug fix, include the original reproduction. For a behavior-preserving change, include the behavior that must stay unchanged. Keep checks proportional to the change.

Completion: each claimed result has an observable condition.

## 2. Choose a direct check

Find an existing test, command, or control interface that observes the condition. Match the user's surface:

- CLI output: run the command and inspect its actual output and exit status.
- UI behavior: operate the current app and inspect the resulting state.
- Persistence: write through the real interface, then read back through a fresh read path.
- Bug fix: rerun the original reproduction and relevant regression checks.
- Documentation or a static artifact: inspect the current content and its references.

A build proves compilation, not runtime behavior. A cached screenshot or another agent's report does not establish the current result. If a check observes only part of a condition, record the gap.

Add a small repeatable check only when existing tools cannot establish the result. Do not build a new harness for a one-off check. Respect permissions and use disposable data. Ask before destructive verification, production writes, or extra paid services.

Completion: a reachable check for each condition, or a specific blocker.

## 3. Execute and inspect

Run the checks against the current artifact. Inspect actual values, output, and exit status. Confirm that the check exercised the intended path. Record relevant commands or interaction steps and their evidence.

When a check fails, distinguish a product failure from a failed observation or environment setup. Report the evidence; do not dismiss a failure merely because the check might be wrong. Fix only within the authorized task scope, then rerun affected checks after the final change.

If execution is unavailable, state the exact blocker and what remains unknown. A suggested command is not an executed check. Keep evidence from before the final change separate from final verification.

Completion: an observed result or blocker for each condition on the final artifact.

## 4. Report the verdict

Use one overall verdict:

- **verified**: every completion condition passed a direct check.
- **failed**: an observed result contradicts a completion condition.
- **unverified**: evidence is missing, partial, stale, or blocked, and no product failure is established.

An established failure takes precedence over missing evidence. Keep partial passes visible without calling the whole task verified.

Report the user-visible result first. Include the artifact or revision, checks actually executed, expected and observed results, evidence paths when available, and uncovered conditions. Separate build, test, and live-behavior evidence.

Keep a small check's evidence in the reply. Save larger evidence in a local artifact and give its path. Redact secrets and private data. Commit evidence only when the task needs a durable audit trail.

If anything remains open, give one concrete next action. Never claim completion from confidence or self-report alone.

## Origin

Adapted from Lauren Tan's MIT-licensed [pstack Prove It Works principle](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-prove-it-works/SKILL.md). The upstream notice appears in `../../LICENSE`.
