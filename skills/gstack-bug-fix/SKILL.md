---
name: gstack-bug-fix
description: Reproduce a reported defect, establish its cause, apply the smallest supported fix, and verify the original behavior.
disable-model-invocation: true
license: MIT
---

# Bug Fix

Own the diagnosis, change, and evidence. Use the host's available tools. This workflow requires the sibling `gstack-verify-result` skill; read `../gstack-verify-result/SKILL.md` directly in step 4. Manual-only settings do not prevent ordinary file reads.

Keep a short checklist with one active step. Use disposable data and the current project surface. Ask before production writes, destructive operations, or extra paid services. Redact secrets in evidence.

## 1. Reproduce

Translate the report into expected and observed behavior. Inspect enough project context to find the real entry point and a runnable check.

Run the reported path before a product fix. Prefer an existing test, real command, app interaction, or replay. Observe the exact symptom and save the command or interaction steps and output. A check must detect the symptom, not merely process failure.

If the defect is intermittent, record the trigger, conditions, attempts, and observed failure rate. Narrow the reproduction where useful without changing the reported failure.

If the path is unreachable, report attempts and the specific missing access or input. Ask only for what the tools cannot obtain. Do not invent a reproduction or ship a speculative fix. Read-only investigation can continue, but the reproduction gate remains open.

Completion: observed failure on the reported path, or an explicit blocker.

## 2. Establish the cause

Trace the failing path through relevant callers, state, and boundaries. If the trigger is intermittent, multiple causes remain plausible, or the first probe is inconclusive, read `references/hard-debug.md` before the next probe. Otherwise proceed with a focused check. Change one experimental condition at a time; inspect runtime state when source alone is insufficient.

Identify the first incorrect operation and explain how it produces the symptom. For a lost response or retry, distinguish the operation's committed state from the caller's knowledge of it. Treat distinct operations and repeated attempts according to the project's contract.

When evidence refutes a hypothesis, remove changes justified only by that hypothesis. If repeated fixes fail the same check, test their shared assumption before another fix.

Completion: execution evidence supports the causal mechanism and rules out the relevant alternative explanation. A code location alone is not a causal proof.

## 3. Apply the smallest supported fix

Name the intended behavior and affected callers before the edit. Fix the established cause within the requested scope. Preserve valid behavior and boundary error handling. Add no unrelated hardening or abstractions.

If a cheap test seam reaches the real failure, create the regression check first and observe it fail before the product edit. Otherwise retain a repeatable reproduction and explain the test limitation. Test behavior rather than internal structure.

Check relevant variations that could expose a symptom-only fix, such as a distinct request, an incompatible retry, or an unchanged path. Select variations from the actual contract rather than a fixed universal list.

Remove temporary instrumentation and rejected experiments. Preserve user changes. This skill does not authorize commits, PRs, or merges.

Completion: a scoped patch tied to the observed cause, with a failing-before check or a documented limitation.

## 4. Verify and report

Read `../gstack-verify-result/SKILL.md` and follow its verification and verdict rules. If that file is unavailable, stop before declaring success and report the missing dependency.

Rerun the original reproduction against the final artifact on the same surface. Run the regression check and relevant unchanged-behavior checks. A lower-level test supplements the original reproduction; it does not silently replace it.

Report the user-visible result, root cause, smallest fix, exact checks and relevant failing-before/passing-after output, and uncovered conditions. Keep evidence from before the final edit separate. Use **verified**, **failed**, or **unverified** as that skill defines them.

For an intermittent defect, report attempts and remaining uncertainty. A finite run without the symptom does not prove absence.

Completion: final-artifact evidence establishes the result, or the report explicitly states failure or missing evidence.

## Origin

Adapted from Lauren Tan's MIT-licensed [pstack Bug fix playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/bug-fix.md). The upstream notice appears in `../../LICENSE`.

This version removes mandatory delegation, model routing, Cursor controls, and automatic PR creation. It retains reproduction, causal evidence, scoped fixes, and direct verification.
