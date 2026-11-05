# Arena and Handoff implementation plan

Status: historical implementation plan. Units A-D are complete under later explicit grants. The operator also authorized publication and local installation. The sections below preserve the original plan and gates; they are not current execution instructions.

Validation outcome: structural and disposable-installer checks passed. Independent static review found no actionable defects. Arena had one two-candidate design-only smoke; Handoff had checkpoint, unchanged-resume, and changed-state-resume smoke checks. Native skill commands and cross-host runtime behavior remain unverified. Private evidence stays outside version control.

Source baseline: `e72a565da38c1f34d085db3fea2bf0e33c223733`. The checkout was clean before this plan. Relative repository pointers below resolve from this document.

## 1. Goal and scope

Add two independent explicit-only skills for Claude Code, Codex CLI, and pi:

- `gstack-arena`: compare independent candidates for one task, select a base, integrate only useful compatible ideas, and verify the synthesized artifact.
- `gstack-handoff`: save an external checkpoint and reconstruct a resume point in the same or a fresh session.

Success means that each skill has a bounded contract, matching host metadata, representative cases, correct repository integration, and honest validation limits. A static pass does not prove runtime reliability or an improvement over the baseline.

Preserve the existing distinction: Plan defines the work contract; Handoff records current execution state; Arena produces a selected artifact. Neither is a general execution engine.

Non-goals: a total router, scheduler, automatic session restart, model-provider configuration, custom runner or dashboard, universal transcript scanner, automatic commits or merges, and automatic comparative Eval.

Use existing host facilities. Respect permissions and explicit-only invocation. A sibling pointer is not permission to bypass a blocked invocation through file reads.

## 2. Design and evidence

### Observed source behavior

- [Plan steps 3-5](../../skills/gstack-plan/SKILL.md) already support optional alternatives, preserve plan-only scope, and separate checkpoints from design. Neither new skill is required for Plan to work.
- [Eval](../../skills/gstack-eval/SKILL.md) owns matched baseline comparisons and adoption claims. Arena must not duplicate that experiment protocol.
- [Verify Result](../../skills/gstack-verify-result/SKILL.md) defines direct artifact verification and verified/failed/unverified evidence. Invocation remains subject to host controls.
- [README](../../README.md) has a skill table, two installer lists, explicit commands, layout, attribution, and host-policy limits. Both new skills must reach those integration points.
- Local pstack Arena at `skills/arena/SKILL.md:11-61` supplies Frame, Fan out, Cross-judge, Pick, Graft, Verify. It defaults to fixed models and can retry rejected seats; omit those defaults here.
- Local pstack Pause safely at `skills/poteto-mode/playbooks/pause-safely.md:5-8` saves a resume note and creates a WIP commit. Keep the note contract, remove unconditional commits and cancellation.
- Local pstack Session pickup at `skills/poteto-mode/playbooks/session-pickup.md:5-9` reconstructs branch/worktree and pending work, then checks inherited claims. Preserve source pointers without treating historical text as current authorization.

No runtime probe ran for this plan. No empirical uncertainty requires a prototype to settle the instruction structure.

### Arena caller usage and contract

Example request: compare two import-pipeline designs from the same grounded brief; produce design artifacts only; use the configured Connexmatrix provider; no production writes. A possible run grant is two candidates and one judge, each capped at 180 seconds. That example is not approval to launch calls.

Inputs: task brief, artifact kind, success conditions, shared grounding, allowed and forbidden actions, output destination, host capabilities, and approved resource limits.

Outputs: candidate artifacts and records, selected base, synthesis rationale, rejected ideas, dropouts, and checks on the final artifact. Output scope follows the brief: design-only never turns into implementation.

Use five steps:

1. Frame the shared brief and criteria before candidates run. Record approved candidate count, models/provider, time or token limits where enforceable, optional judge, and retry allowance.
2. Produce independent candidates in separate writable workspaces. Use the same task and grounding. Candidates cannot inspect siblings or coordinator scores. Folder separation is not a sandbox; disclose actual access limits.
3. Inspect all completed artifacts. Run applicable direct checks and give an authorized read-only judge neutral labels plus complete relevant artifacts and evidence. Missing judge capability is a disclosed limitation, not a fabricated independent verdict.
4. Choose a valid base and integrate only compatible, decision-changing ideas. Do not average incompatible designs. Significant reframing or retries consume the existing budget or need approval.
5. Verify the synthesized artifact, not only the original base. Report what passed, failed, or remains unverified and stop at the requested deliverable.

At least two completed independent candidates are necessary to claim a comparison. One survivor is a single-candidate result, not an Arena win. Zero survivors means blocked or failed with retained evidence. Do not replace dropouts or switch providers without an approved allowance.

Data shape: one coordinator run record with brief, criteria, limits, candidate ids/paths/status, evidence pointers, selection, and final checks. Use plain Markdown; native host records provide telemetry when available. No new JSON schema or runtime controller is needed.

The coordinator owns selection and synthesis. Candidates own only their output location. Judges are read-only. Use isolated git worktrees for code candidates; reject shared-writer setups. For design-only work, separate artifact directories suffice, with access limitations stated.

Judge scores cannot override failed executable checks. Evidence packets include read-based observations and linked unchanged dependencies, not only shell commands or changed files. The prior creator screening showed why omitting those inputs produces false defects. Record grading uncertainty without silently rewriting the original rubric.

### Handoff caller usage and contract

Checkpoint request: save the current task to an agreed project-local note; preserve dirty edits and running services; do not commit or terminate agents.

Resume request: read a specified checkpoint, compare its state with the current checkout, and identify the next safe action. Continue production work only when the current request and host permissions authorize it.

Inputs: explicit mode, selected task, current request, artifact path, optional plan/evidence paths, and host-visible state. Do not infer pause, cancellation, compaction, or execution permission from the skill name.

Output: a checkpoint note for checkpoint mode, or a verified resume summary and refreshed note only when note updates are authorized.

Use one skill with two branches:

- Checkpoint: bound the task and destination; observe repository and active-work state; record the note; verify the saved content and references. A live snapshot is not a clean stop. Record active writers and incomplete atomic steps; pause only when requested and feasible.
- Resume: read only the selected note and relevant artifacts; treat historical records as evidence, not instructions; verify volatile state; reconcile completed versus pending work; present the next action or continue only within current authorization.

Checkpoint fields form five groups:

1. Goal, scope, plan pointer, recorded grants, and current approval limits.
2. Completed, active, and pending units with decisions and rationale pointers.
3. Workspace identity, repository/branch/revision, dirty files, owned task/process identifiers, observation time, and what remains live.
4. Checks actually executed, artifact revisions, evidence paths, blockers, and missing or stale evidence.
5. One next action, its preconditions, and recovery risks.

Prefer the task's existing checkpoint location. Otherwise choose a named project-local Markdown file outside generated or transient caches. Do not overwrite an unrelated note. Preserve private notes locally unless publication is separately authorized.

The note does not make dirty code durable by itself. Warn about uncommitted edits, missing evidence, ephemeral files, and processes that cannot survive a restart. Do not stage, commit, push, kill, or reconstruct missing artifacts automatically.

On resume, check workspace identity, revision, dirty state, reachable evidence, and live process/task ownership where the host supports it. A recorded PID is not proof of current ownership. Use the host's current task handle or verify identity before any separately authorized control action.

If state differs, distinguish expected evolution from a conflict. Report ambiguous conflicts before writes. Recheck only claims affected by changed artifacts or missing evidence; do not redo the entire investigation or accept stale self-reports as proof. Missing essential artifacts leave the relevant completion claim unverified.

Data shape: the checkpoint note is a snapshot of one task, not an execution log or mutable plan. Link existing decision trails rather than copy them. Refresh in place only when task identity and write authorization match; retain prior evidence pointers that remain relevant.

### Alternatives and tradeoffs

Choose standalone skills rather than a total router: fewer implicit transitions, explicit budgets, and no fabricated host lifecycle automation.

Keep checkpoint and resume in one skill: they share one state contract. Separate skills would duplicate that contract without a present capability difference.

Keep Arena separate from Prototype: candidates may produce sketches, code, or prototypes, but comparison is distinct from an empirical probe. Plan's existing prototype reference stays authoritative for its own flow.

Keep Handoff independent of a formal plan: interrupted small tasks also need state recovery. A plan pointer is optional.

No required Plan edit in the initial implementation. Its current optional Arena route remains valid. Add a concrete sibling pointer only if useful, with host permission semantics and no mandatory dependency.

Risks: model comparison cost, incomplete isolation, omitted judge evidence, conflicting grafts, stale snapshots, leaked private state, historical authorization drift, and concurrent note writers. Each becomes a boundary or explicit limitation, not a promise that prose prevents it.

## 3. Work units

The main agent owns implementation. Independent reviewers need separate explicit authorization because this planning run does not launch extra model calls.

### Unit A: Arena contract and package

Create `skills/gstack-arena/SKILL.md`, `agents/openai.yaml`, and one `references/run-record.md` with the minimal coordinator record and evidence-packet checklist. Add `evaluations/arena/cases.md`.

Expected result: the five-step contract above, manual-only metadata, no hardcoded model/provider, authorized resource limits, independent candidates, complete evidence, final verification, and honest dropouts.

Cases: competing design artifacts; code candidates with disjoint worktrees; one dropout or failed candidate; absent judge or extra-call permission; synthesis that fails a previously passing check. A failed synthesis cannot retain a verified verdict.

### Unit B: Handoff contract and package

Create `skills/gstack-handoff/SKILL.md`, `agents/openai.yaml`, `references/checkpoint-template.md`, and `evaluations/handoff/cases.md`.

Expected result: checkpoint/resume branches, five field groups, privacy and trust boundaries, live-snapshot versus pause distinction, current authorization, scoped state checks, and no unauthorized control actions.

Cases: dirty checkout with an active worker; cold resume with unchanged state; changed revision with partial stale evidence; missing note/evidence or unrelated destination; hostile historical directives or reused process id. A note cannot grant destructive permissions.

Units A and B share no mutable skill files. They can be authored independently, but the simplest initial implementation is serial. Neither is independently complete for distribution until Unit C adds its repository integration.

### Unit C: Atomic repository integration and local checks

Depends on the implemented packages. Update README availability, both installer lists, host commands, layout, limits, and attribution in one pass. Preserve existing skills and current user edits.

Keep each package and its README integration in the same publishable change, or publish separately with that package's matching README changes. Do not create a commit that advertises a missing skill.

Use the existing authoring checklist and available YAML parser. Extend the ignored local validation command only for relevant new files; do not add a generic validation framework.

### Unit D: Authorized review and runtime trials

Depends on A-C. Obtain a bounded grant before independent reviewer or smoke/evaluation calls. Use synthetic projects and disposable data, not ongoing private work.

Inspect all artifacts and check preservation boundaries before any judge conclusion. Comparative adoption claims belong to the existing Eval workflow, with its own permitted invocation and run budget. Do not make comparison calls automatically.

## 4. Verification

All checks below are proposed, not completed.

- Unit A static: parse frontmatter and Codex metadata, resolve the run-record reference, walk the five cases, and inspect candidate isolation, budget, dropout, scope, and final-artifact rules. Evidence goes to local ignored reports. A syntax pass proves no independent candidate behavior.
- Unit B static: parse metadata, resolve the checkpoint template, walk five cases, and inspect current authorization, note privacy, dirty-state preservation, stale evidence, process ownership, and blocked writes.
- Unit C executable: adapt and run `python3 reports/check-create-skill.py` if it remains available. It currently checks all skill metadata/file pointers and runs the README installer in disposable HOME. Expand its changed-file list and late-conflict case to the new package. If unavailable in another checkout, use the same direct parser/path/temp-HOME checks; do not claim the ignored script ships with the repo.
- Unit C regression: run `git diff --check`; compare the change list with allowed paths; verify all existing skills retain their metadata and references. In temporary HOME, verify all advertised links, repeat refusal, and a late dangling-symlink conflict before any write. Do not run the full installer against the actual machine merely to test it.
- Unit D Arena smoke: under an approved count/time cap, two candidates produce design artifacts from one brief. Inspect records, candidate outputs, and final checks. Verify no production edits and no unapproved provider switch or extra call. A dropout branch can first use a synthetic terminal result; label this fixture check, not an actual model crash.
- Unit D Handoff smoke: in a synthetic dirty repo, save a checkpoint, then supply it to a fresh session. Verify correct branch/revision/dirty evidence and the next action, with no commits, resets, process kills, or production writes. A separate changed-state case must disclose divergence rather than blindly execute the old next step.

Freeze prompts, allowed mutations, expected checks, and resource limits before runtime trials. Calibrate checkers with deliberately broken metadata, an unauthorized write, stale revision, missing evidence, and an invalid synthesized artifact. Follow linked dependencies; inspect both reads and shell output. Keep original failures and label replacements.

Final goal-level check: both installed-format packages express their contracts, README integration matches them, each case has an observable pass or blocker, and evidence claims match the checks actually executed. Missing runtime trials leave behavior unverified, even when static review passes.

## 5. Gates and first action

Current open gates:

1. Implementation needs a new execution request. This plan creates no skill files.
2. Arena candidates, optional judge, retries, and independent reviewers need explicit resource limits and authorization. Respect configured providers; an example route is not a grant.
3. Host-specific fresh-session, worktree, task-state, and invocation behavior needs documented capability checks before runtime use. Lack of a capability produces a named blocker or disclosed reduced mode.
4. Installation, commits, push, actual project experiments, and publication require separate permission. Existing manual-only settings remain unchanged.

No product decision blocks instruction authoring. Runtime API details remain a preflight gate, not invented flags or tool names.

First action after implementation approval: write the Arena skill and its frozen five-case contract from Unit A, then review the artifact against the proposed static checks. Do not start candidate calls.

Planning evidence: source reads and a clean `git status --short` at the recorded baseline. A direct Python check passed all five required sections, four local Markdown references, and the plain-dash policy. `git diff --check` passed. Final status shows only the new `docs/plans/` artifact. A main-agent static review traced budget, candidate failures, dirty-state recovery, trust boundaries, and publication dependencies through the work order. No prototype, independent reviewer, extra model call, host smoke, or runtime comparison occurred.
