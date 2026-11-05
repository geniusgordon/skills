---
name: gstack-arena
description: Compare independent candidates for one task, select a base, integrate compatible ideas, and verify the synthesized artifact within an approved budget.
disable-model-invocation: true
license: MIT
---

# Arena

Produce one selected artifact from independent attempts at the same task. Arena chooses an artifact; it does not evaluate whether a workflow improves agent behavior.

Keep the deliverable within the request. Design-only work never becomes production implementation. Use available host facilities and the configured provider. Do not install, commit, publish, switch providers, or launch unapproved calls.

## 1. Frame the comparison

State the task, artifact kind, shared grounding, success conditions, allowed paths, forbidden actions, and output destination. Read the affected context before comparing designs. Define three to five concrete selection criteria before candidate execution.

Record the approved candidate count, provider and models, optional judge, resource limits, and retry allowance. Count judge calls and replacements in the budget. If no bounded grant exists, prepare the brief and proposed run matrix, then pause before calls. Do not claim a cost or token cap the host cannot enforce.

Confirm that the host can start fresh independent workers, isolate their writable state, retain outputs, and enforce the selected limits. Use existing documented capabilities; no specific delegation API is required. A missing capability is a named blocker, not permission to invent isolation.

Read `references/run-record.md` and keep one local coordinator record outside candidate workspaces. Resolve destination ownership before replacing existing artifacts. Keep secrets and unrelated private context out of candidate briefs.

Completion: a shared brief, fixed criteria, permitted workspaces, and an authorized executable run matrix, or a specific blocker.

## 2. Produce independent candidates

Give each worker the same task and grounding, its own output path, and a request for an artifact plus a short rationale. Candidates see the task, not coordinator scores or sibling outputs. Do not give one candidate another's result before it completes.

Use separate git worktrees for code candidates. Separate artifact directories can serve design-only work. Record the starting revision or inputs and control relevant environment differences. Folder separation is not a sandbox; disclose actual access limits and inspect records for contamination.

Each candidate owns only its allowed writable workspace. Run concurrently only when the host supports safe independent work; otherwise use fresh sequential sessions. Require the same scope and evidence from each. Preserve user edits and reject shared-writer setups.

Retain failed, timed-out, and missing-output attempts. Report every approved seat's terminal outcome. Retry only within an explicit allowance; do not silently replace dropouts, relax the task, or change providers. Inspect any partial output, but do not present it as a completed candidate.

Completion: artifacts and terminal records for the authorized attempts, including failures and disclosed isolation limits.

## 3. Inspect and assess

Read every completed candidate end to end. Run applicable direct checks on its exact artifact; inspect assumptions, scope, linked dependencies, and recorded evidence. A build or persuasive rationale cannot override a failed behavior check.

With at least two completed independent candidates, compare them criterion by criterion. A completed but invalid artifact remains visible as a failed alternative, not an eligible base. One survivor is a single-candidate result, not an Arena comparison; zero survivors leaves the task failed or blocked. Continue with a lone artifact only if the request permits that deliverable.

Use an authorized read-only judge only after candidates stop writing. Prefer another model family within the configured provider when available. Give neutral labels, criteria, complete relevant artifacts, unchanged dependencies, and both read-based and executable evidence. Disclose identity leakage, same-family review, or missing evidence.

If judge capability or budget is absent, assess in the coordinator and label the review non-independent. Never simulate a judge. Inspect disagreement against artifacts; do not silently change criteria to justify a preferred result. A materially revised brief requires a new comparison within approved limits.

Completion: an evidence-supported assessment with valid base options, rejected artifacts, judge limitations, and all dropouts accounted for.

## 4. Select and synthesize

Choose a valid base against the fixed criteria. When outcomes tie, prefer clear responsibilities, a smaller exposed interface, and maintainability. Selection belongs to the coordinator, not the judge score alone.

Inspect losing candidates for a few useful compatible ideas. Integrate deliberately under one coherent design; reject incompatible assumptions rather than average them. Convergence needs no graft. Record the base, each adopted idea's source, and rejected alternatives with reasons.

Work only in the authorized synthesis destination, separate from candidate artifacts when possible. Preserve original candidate evidence. Design-only synthesis stays a design. Broad divergence is evidence to reframe, not permission for an unbudgeted rerun.

Completion: one coherent in-scope artifact and a traceable selection/synthesis rationale, or a disclosed lack of a valid base.

## 5. Verify and report

Run the task's direct checks on the final synthesized artifact. Recheck affected invariants after every graft. A passing base does not establish a passing synthesis. Inspect the real surface required by the artifact; a design can pass consistency checks without proving runtime behavior.

Report verified only when all claimed completion conditions pass direct checks. An observed contradiction means failed; missing or blocked evidence without an established product failure means unverified. Preserve partial passes without upgrading the overall result. Never retain a verified verdict after a failing synthesis check.

If verification fails, identify whether the brief, base, or graft caused it. Make only authorized corrections and rerun affected checks. Additional candidates, judge calls, or substantial reframing require remaining budget and permission.

Report the artifact path or revision, base and selection reasons, grafts and rejections, candidate outcomes, judge status, checks actually run, resource use where available, and remaining limits. Stop at the requested deliverable. Clean up only owned resources under the agreed lifecycle; preserve evidence and disclose resources left active.

Completion: a selected artifact with final evidence and an honest verdict, or an explicit failure or blocker. Arena alone proves no general skill improvement.

## Origin

Adapted from Lauren Tan's MIT-licensed pstack [Arena skill](https://github.com/cursor/plugins/blob/main/pstack/skills/arena/SKILL.md). The upstream notice appears in `../../LICENSE`.

This version removes fixed models, implicit replacement calls, and host-specific tools. It adds explicit resource approval, honest single-candidate outcomes, and complete evidence packets.
