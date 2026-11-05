# Prototype a planning question

Use a prototype only when a concrete empirical question can change the design. A sketch that cannot answer that question is extra work.

## Define the observation

State the question, smallest probe, relevant inputs, expected observation, and decision rule before execution. For alternatives, use matched inputs and conditions. For performance, record build mode, cache state, runs, and limits; a single timing is a probe, not a reliable speedup claim.

Examples include a parser's behavior on a saved input, an interaction's usable states, or whether a platform exposes a required capability. Ask the user about genuine preferences rather than pretend an experiment settles them.

## Isolate the probe

Use a unique scratch directory outside production source. Reuse available tools and safe synthetic data. A folder alone is not a sandbox: inspect commands for access to external data, services, credentials, and shared state.

A planning request permits only a small, reversible local probe within its scope. Ask before dependency installation, production access, destructive actions, paid services, extra model calls, or an experiment beyond the authorized resource limit. If a safe bound is unclear, propose the probe and stop before execution.

Use copied inputs, isolated ports or data directories, and owned processes. If the real target cannot be isolated, record the blocker. Do not stop an existing service or modify the working checkout to make a prototype run.

## Execute and inspect

Build only what the question needs. Compare variants through the same interface when practical. Inspect actual output, exit status, side effects, or UI state. For a visual decision, drive the interaction and capture screenshots or a video; an unoperated mockup does not prove behavior.

Record the exact command or interaction, inputs, observation, and evidence path. Identify environmental limits and stand-in differences. If the observation cannot reach the real condition, leave that condition unresolved.

Treat a failed probe as evidence about the probe or candidate, not permission for production repairs. Change one relevant condition at a time. Keep the failed observation when it informs the design.

## Preserve evidence and clean up

Keep evidence outside disposable runtime state. Stop only processes the probe started, remove only its own temporary state, and confirm that evidence survives cleanup. Run this cleanup after failed attempts too.

Report cleanup failures and remaining process or resource identifiers. Leave scratch source clearly labeled throwaway; do not promote it into production or install it automatically.

## Feed the plan

Use the observed result to choose the design, reject a hypothesis, or name the next unresolved gate. Link the evidence and state what the probe does not establish. The plan still stops before production implementation.

## Origin

Adapted from pstack's MIT-licensed [Prototype playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) by Lauren Tan. This version preserves plan-only scope and adds explicit resource, isolation, and cleanup boundaries.
