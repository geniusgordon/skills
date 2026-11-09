# Prototype skill implementation plan

Status: historical implementation plan. Units A-B and the authorized review/parser/Plan-regression trials are complete. The operator authorized publication and local installation. The sections below preserve the original plan, not current execution instructions.

Observed validation: static review had no actionable findings; local structure/installer checks passed; Prototype exercised ten parser inputs and Plan exercised seven without a sibling. Source bytes remained unchanged and evidence survived cleanup. UI, negative reporting, cleanup failure, native commands, cross-host behavior, and comparative benefit remain unverified. Private records remain outside version control.

Baseline: `2f133082c04b6b758ca594df8393ca62b8d52d4d`. The checkout was clean before this document.

## 1. Goal and scope

Create an explicit-only `gstack-prototype` for a bounded empirical question. It produces a disposable instrument, observed evidence, a conclusion, and honest limits. It does not require a full plan or multiple candidates.

Users can ask whether a parser handles an input, an interaction reaches a usable state, or a platform supports a capability. A timing probe can inform a decision but does not establish a reliable speedup without appropriate measurement.

Success conditions: clear question and decision rule; bounded safe execution; actual observation on the relevant surface; preserved evidence after owned-resource cleanup; no production mutation or automatic implementation; consistent Plan integration and host metadata.

Non-goals: an Arena, a benchmark framework, production code, automatic dependency installation, a scheduler, model routing, or a custom browser harness. Use available tools and existing project commands.

## 2. Design and evidence

### Caller usage

Example: explicitly request a local prototype to determine whether the installed CSV parser preserves empty fields, using synthetic inputs, no network/install, and a 30-second probe limit. The output is the observation and its decision consequence, not a production patch.

Example: request a disposable UI prototype for a bulk-selection interaction. Operate its states with an existing browser driver and capture the result. A product preference remains the user's decision; observed interaction behavior is evidence, not a vote on preference.

The prototype invocation permits scoped disposable work. It does not grant arbitrary network access, paid services, extra model calls, production writes, or unlimited iteration.

### Existing owners and constraints

- [Plan's prototype reference](../../skills/gstack-plan/references/prototype.md) already defines the observation, isolation, execution, cleanup, and evidence feed. Reuse its method rather than invent a second full recipe.
- [Plan step 3](../../skills/gstack-plan/SKILL.md) reads that reference conditionally and remains useful without an installed sibling. Plan itself stops before implementation.
- [Arena](../../skills/gstack-arena/SKILL.md) compares independent candidates. Prototype answers an empirical question; variants are optional and need no extra model calls by default.
- [README](../../README.md) owns the skill list, both installer lists, host commands, layout, attribution, and validation claims.
- [Authoring checks](../../skills/gstack-create-skill/references/authoring-checks.md) cover format, references, policy preservation, and evidence levels.
- Local pstack `skills/poteto-mode/playbooks/prototype.md:7-12` supplies a disposable, isolated, operated prototype. Omit automatic Feature routing, unconditional CDN use, and any inference that throwaway code can discard safety.

These are observed source contracts. No prototype or runtime skill trial is executed for this plan.

### Five-step standalone contract

1. **Frame.** State the empirical question, inputs, relevant surface, observation, decision rule, output paths, and execution limits. If no empirical question exists, explain the mismatch and stop or ask for the specific missing choice.
2. **Prepare.** Inspect existing tools and environment. Choose isolated scratch state, safe copied inputs, evidence location, and cleanup ownership. Ask about missing access or expensive/destructive actions before execution. A folder is not a sandbox.
3. **Build and drive.** Create only the minimum instrument, then run or operate it on the matching surface. Use one variant unless comparison is necessary. Fix probe setup only within the disposable scope, not production source.
4. **Observe and conclude.** Inspect actual outputs, exit status, state and side effects. Record the exact inputs and run context. Distinguish observed facts, assumptions, subjective preferences, stand-in limitations, and unresolved conditions.
5. **Preserve and clean up.** Stop only owned processes and remove only disposable runtime state, including after failed attempts. Keep evidence accessible, record cleanup failures and active resources, and deliver the result without promoting code or automatically starting implementation.

Report one conclusion: question answered by the stated observation, or unresolved with a specific limit. An unfavorable experiment can still answer the question; it is not automatically a failed skill run. Do not force an adoption verdict or confuse a failed approach with a broken probe.

Data shape: a small experiment note containing question, scope/grant, method, inputs, observation, decision consequence, limitations, scratch/evidence paths, and cleanup state. Reuse existing project evidence conventions; no mandatory JSON schema, helper, or dashboard.

### Plan integration and one source of method detail

Choose a standalone Prototype skill with the complete experiment method. Keep Plan's existing reference path as a short planning-specific adapter, not another full experiment recipe.

The adapter decides whether a small probe is worth doing during planning, checks the planning request's scope, and carries the observation into the plan. It permits a minimal safe local probe through ordinary tools without a mandatory sibling dependency. Detailed standalone or expanded experiments can use Prototype only through the host's authorized invocation path.

Do not use the adapter to reproduce a blocked manual-only sibling call. If the host rejects the handoff, preserve the question as a gate or request an authorized invocation. Plan must not silently transform its small-probe allowance into the entire standalone workflow.

Keep essential safety boundaries in both workflows where their permissions differ; keep detailed experiment procedures in Prototype only. This is scoped responsibility, not a second copy of the method. Review the adapter for accidental loss of Plan's existing isolated-probe behavior.

### Alternatives and tradeoffs

- **Keep two full copies:** rejected because experiment changes can drift.
- **Make Prototype require Plan's reference:** rejected because a standalone experimental entry point should not require the planning package.
- **Make Plan require Prototype:** rejected because the current Plan contract has no required sibling and host invocation gates can block composition.
- **Add a shared support package or generator:** rejected because this repository has no established resource distribution layer. Packaging complexity exceeds the current need.

Chosen tradeoff: standalone method ownership plus a small planning adapter. Some intrinsic safety rules remain local to both entry points; one authoritative experiment recipe prevents procedure duplication.

## 3. Work units

### A. Prototype package and cases

Create `skills/gstack-prototype/SKILL.md`, `agents/openai.yaml`, and `evaluations/prototype/cases.md`. Keep the five-step method in the main skill unless a real conditional branch justifies a reference. Do not add empty resource directories or mandatory helper scripts.

Use matching name, MIT notice, `disable-model-invocation: true`, and Codex `policy.allow_implicit_invocation: false`. Preserve configured provider and host permissions.

Five cases: local parser probe; operated UI prototype; bounded performance probe; unavailable or unsafe environment; failed attempt/cleanup with evidence preservation. Each has expected observations, allowed mutations, and blocker rules.

### B. Atomic Plan and repository integration

Update `skills/gstack-plan/references/prototype.md` into the planning adapter. Adjust Plan's step-3 wording only if needed to make its reduced probe versus standalone invocation distinction clear. Update `evaluations/plan/cases.md` to retain the cheap empirical-fork case and include missing/blocked sibling behavior without losing independent Plan use.

Update README availability, both installer lists, commands, conditional-method ownership, layout, attribution, and experimental status. Package and integration should land together; do not advertise a missing skill or replace a live reference with a broken pointer.

Units A and B form one publishable change because method ownership and integration are connected. The main agent owns edits; preserve unrelated files and user changes.

### C. Local verification and authorized trials

Read the final artifacts and run existing structural/path checks. Independent review and fresh-session smoke require separately approved counts and limits. No paid trial runs merely because implementation was approved.

Do not import pstack's fixed model choices or prototype-to-Feature transition. A later explicit request owns production work.

## 4. Verification

All implementation checks below are proposed, not completed:

- Package: parse metadata, compare folder/name, check manual-only policy, resolve references and license pointers, and statically walk all five cases.
- Integration: inspect Plan's empirical-fork behavior, standalone method ownership, blocked handoff handling, both installer lists, command syntax, layout, and attribution. Plan must still function without Prototype installed.
- Local commands: extend `python3 reports/check-create-skill.py` for new files if available. That ignored local script is not a shipped tool. Otherwise use existing YAML parsing, file/path checks and disposable-HOME installer execution directly. Run `git diff --check` and compare changed paths with Units A-B.
- Installer: in temporary HOME, verify all advertised links, repeat refusal, and the final destination's dangling-symlink conflict before any writes. Do not run against the real machine for a test.
- Runtime probe trial, if approved: use a synthetic parser input and one fresh session; inspect actual read/run records, conclusion, source hashes, owned cleanup, and evidence after cleanup. An unsupported parser input can be a valid negative answer.
- UI trial, if approved and available: drive the scratch app with an existing browser tool, inspect states, capture evidence, stop the owned server, and verify retained artifacts. Missing browser capability leaves UI behavior unverified.
- Plan regression, if approved: run the bounded empirical-fork case without the Prototype sibling and ensure the plan records the observation while leaving production unchanged. Separately test that a blocked standalone handoff is not bypassed.

Freeze fixtures, mutation boundaries, checks and budgets before trials. Calibrate checks with a source mutation, unoperated UI screenshot, evidence lost in cleanup, and a false claim that a single timing proves a speedup. Include failed attempts and linked source evidence; do not silently revise a grading rule after results.

Final goal-level check: the standalone workflow answers its bounded question with actual evidence and preserves scope; Plan stays independent and uses the adapter correctly. Static checks alone leave runtime behavior unverified. A/B adoption claims require the existing Eval workflow and budget.

## 5. Gates and first action

No product choice blocks instruction authoring. Open gates are implementation authorization, host capability checks before experiments, bounded model-call/review grants, and separate installation/publication permission.

First action after implementation approval: write Unit A's five-case contract and minimal standalone skill, then update the Plan adapter and README in the same scoped change. Do not run a prototype or launch agents automatically.

Planning evidence: source inspection and a clean status at the recorded baseline. A direct Python check passed all five plan sections, five local references, and the plain-dash policy. `git diff --check` passed; status shows only this new document. Main-agent review traced scope, method ownership, optional sibling invocation, evidence preservation, and Plan regression gates. No independent review or runtime evidence is claimed.
