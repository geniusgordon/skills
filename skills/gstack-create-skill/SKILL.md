---
name: gstack-create-skill
description: Create or update a focused skill with explicit scope, portable instructions, structural checks, and evidence-based evaluation when warranted.
disable-model-invocation: true
license: MIT
---

# Create Skill

Create or update the smallest skill that owns the requested behavior. Use the host's available tools and the target repository's conventions.

A request to create or modify a skill authorizes that scope. A reflection proposal alone does not authorize edits. Keep installation, publication, and extra paid model runs separate.

## 1. Establish the target

Extract the purpose, intended users and hosts, inputs, output, and success conditions from the request and current evidence. Ask only for decisions the evidence cannot settle.

Inspect relevant existing skills before creating a new one. Update an existing owner when it fits. Use project-local guidance for project facts and structural enforcement for deterministic constraints.

Resolve installed symlinks to the canonical source. Read the target, directly used resources, invocation metadata, and affected callers. Preserve unrelated user edits and license notices. If the destination is ambiguous or read-only, resolve it before writes; never edit a generated copy or plugin cache.

For a new gstack skill, use a matching `gstack-<name>` directory and frontmatter name. Keep existing names unless a rename is authorized.

Completion: one canonical destination, authorized scope, intended hosts, and observable success conditions.

## 2. Define the behavior

Choose a short ordered workflow or focused reference. Give workflow steps observable completion conditions. State inputs, outputs, scope limits, failure paths, and permission gates where they change an action.

Choose explicit or automatic invocation for the target separately from this creator's policy. New gstack skills default to explicit invocation. For automatic targets, describe concrete use conditions and near-misses.

Prepare representative requests and expected checks: an ordinary case, a meaningful edge or blocked case, and an adjacent out-of-scope case. Reuse existing cases when they cover the change. For updates, retain the original artifact or revision as a baseline before edits.

Completion: a bounded behavior contract and cases that distinguish success, failure, and out-of-scope work.

## 3. Write the skill

Write YAML frontmatter with a nonempty `name` and `description`, followed by concise Markdown instructions. Match the directory name and portable name rules.

Keep common steps in `SKILL.md`. Put conditional detail in directly linked references with an explicit read condition. Keep each rule in one authoritative place. Prefer a body below 500 lines; split by a real branch rather than an arbitrary size target.

Add scripts only for repeated or fragile deterministic work. Add assets only when the output needs them. Reuse existing tools; omit empty directories, template TODOs, and speculative helpers.

Use skill-root-relative paths and tool-neutral instructions. Name runtime dependencies and alternatives honestly. Keep private examples and machine-specific paths out of shared skills.

Preserve existing host metadata during updates. For explicit-only gstack skills, set `disable-model-invocation: true` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.

A sibling pointer names a dependency, not permission to execute it. Follow the host's invocation controls. Never bypass a blocked skill call through file reads. Use an authorized invocation or report the blocked handoff.

Completion: the requested artifact and affected callers express one consistent behavior without unrelated changes.

## 4. Check the artifact

Read and apply `references/authoring-checks.md`. Run available local checks against the final artifact. Execute added or changed scripts with disposable inputs, including a relevant failure case.

Walk each prepared case through the instructions and inspect its expected path. Label this as a static walkthrough unless an agent actually executes the case. A validator pass proves only the checks that validator implements.

When an authorized host smoke check is available, verify discovery, explicit loading, and reference access. Record the host version and actual evidence. Manual loading does not prove automatic discovery or improved behavior.

Completion: structural checks pass, executable resources have observed results, and missing runtime evidence remains explicit.

## 5. Evaluate when warranted and report

For substantive changes to decisions, failure handling, invocation, or workflow order, prepare a handoff to `../gstack-eval/SKILL.md`. Include the baseline, proposed artifact, behavioral question, cases, checks, and available host capabilities.

Read and follow Eval only when the host permits this handoff. If Eval is missing or invocation is blocked, report the dependency or permission gap. Do not copy its experiment protocol here.

Obtain a run budget before extra paid model calls. If scope, host permission, and budget already cover the comparison, continue without a redundant approval request. Otherwise prepare the plan and pause before execution.

Revise only within authorized scope after observed failures. Keep structural correctness, smoke results, and comparative behavior evidence separate. Clearer wording alone proves no improvement.

Report the created or updated skill, canonical paths, design choices, checks actually run, remaining uncertainty, and one next action when needed. Do not install, commit, push, or publish without authorization.

Completion: a checked artifact with honest evidence, or a specific blocker; any comparative claim follows Eval's evidence rules.

## Sources

This original synthesis uses [the source survey](../../docs/skill-authoring-survey.md). It does not reproduce Cursor's unavailable built-in implementation or require vendor creator scripts.
