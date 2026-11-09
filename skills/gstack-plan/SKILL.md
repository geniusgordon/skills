---
name: gstack-plan
description: Ground a task, settle its design with evidence, and write a scoped, verifiable plan without production implementation.
disable-model-invocation: true
license: MIT
---

# Plan

Deliver a design and an executable plan, not the production change. Use the target project's conventions and available tools.

Write only the agreed plan and evidence artifacts, plus permitted isolated scratch prototypes. Preserve production source, user edits, existing services, and shared data. Do not install dependencies, commit, publish, or launch extra model runs without authorization. A request to plan is not permission to implement.

Keep a short checklist with one active step. This workflow does not require Arena, a specific provider, or a session handoff system.

## 1. Frame the task

Extract the goal, intended users, observable completion conditions, constraints, and non-goals. Separate product choices from facts the repository or a safe experiment can answer.

Inspect enough context to assess scope. For a trivial, obvious change, explain why a formal plan adds no value and stop without implementation. If the user explicitly needs a plan artifact anyway, provide a proportional one.

Choose the artifact location from the user's path or project convention. If neither exists, use a named local Markdown file in a suitable writable location and report its path. Check for existing content before writes; update the same task's plan only within scope. Resolve ambiguous ownership before replacing anything.

Completion: a bounded goal, success conditions, and an artifact destination, or an explicit trivial-task exit or blocker.

## 2. Ground the existing system

Read the affected entry points, callers, data flow, ownership, interfaces, and available checks. Record precise file pointers and relevant constraints rather than source dumps. Inspect prior decisions when a proposed change moves responsibility or layers.

For greenfield work, ground the surrounding integration and platform contracts. State which observations remain unavailable. A list of filenames alone is not a model of how the system works.

Ask only for product decisions, permissions, or missing inputs that available evidence cannot settle. Continue independent analysis when useful, but keep blocked decisions visible.

Completion: a source-supported account of the affected behavior, callers, constraints, and evidence gaps.

## 3. Settle the design

Write the caller's usage or user journey first. Derive the data shape, interfaces, state ownership, validation, and error behavior from it. Keep responsibilities clear and the exposed interface no larger than needed.

Compare structurally different alternatives when the choice matters. Explain rejected alternatives and accepted tradeoffs; do not invent contenders for an obvious design. A local comparison is not independent model agreement.

For an empirical uncertainty that can change the design, read `references/prototype.md` before a small planning probe. Use its observations to decide, or retain the uncertainty as a named execution gate. A broader standalone experiment needs a separate authorized invocation; no Prototype sibling is required for Plan. Scratch probes are optional evidence, not production code.

Multiple candidates or an Arena may help a consequential choice, but require available host capabilities, authorization, and a bounded budget. No absent sibling skill blocks local design. Follow host invocation controls; do not bypass a blocked call through file reads.

Keep reversible recommendations distinct from irreversible or product decisions that require the user. Do not treat silence as approval of a named gate.

Completion: a coherent design with its evidence, rationale, tradeoffs, and unresolved gates, not a claim that untested assumptions are settled.

## 4. Write the plan

Keep design rationale in the plan unless its size warrants a linked document. Keep mutable checkpoints and raw evidence separate. Use concrete content, not unfilled template placeholders.

Include these five sections, scaled to the task:

1. **Goal and scope.** Users, completion conditions, constraints, and non-goals.
2. **Design and evidence.** Caller usage, data shape and responsibilities, chosen approach, alternatives, observed evidence, assumptions, and risks.
3. **Work units.** Small verifiable units with dependencies, allowed file or module scope, expected result, and an accountable owner role when delegation matters. Sequence important unknowns before dependent work.
4. **Verification.** For each unit, name the real surface, command or interaction, preconditions, expected observable result, evidence location, and failure or blocker rule. Separate checks already run from checks proposed for execution. Include regression checks and a final goal-level check; add performance checks only when relevant.
5. **Gates and first action.** Unresolved decisions, permission requirements, review points, and the first bounded execution action after authorization.

Use discoverable project commands and established control tools. If exact selectors, commands, or files remain unknown, name the discovery step and the gate it must satisfy instead of inventing them. Do not call a unit independently landable when it breaks a caller until a later unit; keep those edits atomic or state the dependency.

Completion: each work unit has a bounded result and a reachable check or explicit discovery/blocker gate; the whole plan addresses the original completion conditions.

## 5. Review and hand back

Read the plan end to end. Check its references, dependencies, scope, assumptions, and gates against the actual project. Use existing applicable checks, but do not import a validator that enforces another workflow's ceremony.

Trace the work order through the final result. Confirm that planned evidence is not presented as observed evidence, and that scratch code is not described as shippable. Inspect any UI prototype you create; capture the relevant interaction and resulting state.

Report the plan path, design choice, checks actually performed, open gates, and first execution action. Label the result ready for execution approval or blocked by the named decision or capability. A plan can be complete while execution still requires permission.

Stop after delivery. Do not start implementation, merge, or automatically route to an execution skill. A later authorized request owns execution.

Completion: a checked plan with honest evidence and an explicit stop before production work.

## Origin

Adapted from Lauren Tan's MIT-licensed pstack [design guide](https://github.com/cursor/plugins/blob/main/pstack/docs/guide/04-design.md), [Architect skill](https://github.com/cursor/plugins/blob/main/pstack/skills/architect/SKILL.md), and [Multi-phase plan](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md).

This version removes mandatory multi-model design, fixed plan storage, automatic implementation, and fixed live-verification lanes. The upstream notice appears in `../../LICENSE`.
