---
name: eval
description: Evaluate a skill or workflow change against the current baseline with matched tasks, isolated sessions, observable checks, and blinded review. Use when the user asks to evaluate, compare, or validate skill behavior before adoption.
license: MIT
---

# Eval

Evaluate behavior, not how persuasive the instructions sound. Recommend adoption only from observed results.

This skill works with Claude Code, Codex CLI, and pi agent. Use the host's available tools. Read `references/protocol.md` before any execution.

## 1. Frame

Record the target behavior, baseline, proposed change, and whether you evaluate explicit execution or automatic discovery. A manually loaded skill does not prove automatic discovery.

Use the user's existing model, instructions, and skills as the baseline. Change one factor at a time. Freeze the task prompts, fixtures, checks, and decision rule before the first run.

Start with five cases: three target tasks, one blocked-environment case, and one simple task where the full workflow adds no value. Adapt these categories to the skill. Keep separate holdout cases for the adoption decision.

Write three to five observable criteria. Include task correctness, evidence quality, and relevant regressions. Define critical failures as adoption blockers. Use executable checks before subjective scores.

Record the approved run count and resource limits. If the user gave no budget, propose a bounded run matrix and obtain approval before paid agent runs. Document work can proceed without that approval.

Completion: a fixed case set, rubric, decision rule, and authorized run matrix.

## 2. Prepare

Give every version and repetition a fresh session and an isolated copy of the same project state. Keep the model, reasoning effort, tools, permissions, fixtures, and task prompt matched within each pair.

Place only the intended skill variant and natural project context in each workspace. Keep the rubric, version map, other outputs, and orchestration records outside candidate access. Use neutral project-shaped workspace names.

Inspect inherited instructions and skill discovery. A baseline that inherits the proposed skill is contaminated. Isolated folders alone do not isolate global skills or conversation history.

Candidate requests describe ordinary work. Keep evaluation labels and requests for skill self-report out of them. Preserve legitimate project identifiers such as an existing test directory.

Confirm fresh-session and isolation capabilities from the host's documentation or command help. If unavailable, stop execution and report the missing capability. An existing conversation is not a fresh-session substitute.

Completion: matched environments with the intended context and no known baseline contamination.

## 3. Run

Run the fixed matrix. A small initial comparison uses two repetitions per version and case. This is a screening run, not statistical proof of reliability.

Use native agent sessions or existing CLI commands. Run sequentially if parallel execution is unavailable. Give concurrent writers separate workspaces. Keep all runs within the authorized budget.

Record the host and version, model and effort, source revisions, loaded configuration, task, output, checks, elapsed time, and available usage data. Mark unavailable fields explicitly.

Retain local execution records when available. Read only records for these runs. Keep credentials and unrelated conversation history out of artifacts.

Treat a crash or missing output as a failed run. Keep it in the results. Label any replacement separately, and retain the original failure.

Completion: one recorded outcome for every scheduled run, including failures and blockers.

## 4. Assess

Run each case's executable checks against the exact output produced. Record commands, exit status, and relevant output. A build alone proves only a build.

Read every output. Inspect execution records for required actions and skill loads when available. Self-reported compliance is not proof. Mark process compliance unverified when records cannot establish it.

Use neutral labels for a separate judge. Remove version names, model names, revealing paths, and evaluation instructions from its input. Preserve substantive artifacts and task requirements.

One judge applies the same rubric to both versions in one pass. Prefer a different model family when available. Use the same-family judge if necessary and disclose the limitation. If no separate judge is available, report a non-blinded assessment rather than simulate independence.

A judge score cannot override failed executable checks. Resolve disagreements through artifacts or a new check. If you change the rubric, invalidate the affected comparison and rerun both versions.

Completion: per-case results with evidence, process-verification status, and disclosed review limitations.

## 5. Decide

Apply the frozen decision rule. Run untouched holdout cases before recommending adoption. A critical regression blocks adoption. Missing essential evidence makes the result inconclusive.

Compare task outcomes, failures, elapsed time, available usage, and human intervention. Report small-sample uncertainty. Treat mixed gains as tradeoffs, not a universal improvement.

Use one verdict: **adopt**, **revise**, **keep baseline**, or **inconclusive**. State which behavior changed and the evidence behind it. Keep case-level results; an average must not hide a critical failure.

For later edits, rerun affected cases plus the core regression set. Changes to shared workflow rules, model, or host require the full relevant suite and a fresh baseline. Check trigger and non-trigger cases after discovery changes.

## Report

Use `references/report-template.md`. Include the run matrix, case results, evidence, limitations, and one concrete next action. Save reports outside candidate workspaces. Report exact artifact paths.

Do not create a runner, dashboard, or new delegation framework unless the direct host tools show a concrete blocker. This skill defines the experiment; it does not provide an execution harness.
