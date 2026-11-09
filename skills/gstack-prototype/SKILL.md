---
name: gstack-prototype
description: Answer a bounded empirical question with a disposable prototype, direct observations, retained evidence, and scoped cleanup.
disable-model-invocation: true
license: MIT
---

# Prototype

Build an instrument to answer a question, not production code. Use available project tools and the host's permitted capabilities. A full plan, multiple variants, and extra agents are not required.

The request permits only scoped disposable work. Do not install dependencies, access production, use paid services, launch extra model calls, commit, publish, or expand scope without authorization. Keep credentials and private data out of shared artifacts.

## 1. Frame the question

State the empirical question, relevant inputs and surface, smallest useful observation, and decision rule before execution. Separate observable behavior from product preferences. If no empirical question exists, explain the mismatch or ask for the missing decision; do not invent a prototype.

Choose scratch and evidence destinations, ownership, and execution limits. Use project conventions or a unique local location. Check existing content before writes. If a safe resource bound is unclear, propose the experiment and pause before execution.

Use one variant unless comparison is necessary. Matched variants use the same relevant inputs and conditions. A prototype comparison is not independent model agreement or an Arena run.

Completion: a scoped question, observable decision rule, permitted destinations, and safe execution bounds, or a specific blocker.

## 2. Prepare an isolated probe

Inspect existing commands, libraries, control interfaces, and runtime prerequisites. Prefer installed tools and synthetic or copied inputs. Inspect commands before execution for network, external state, credentials, and destructive side effects.

Use a unique scratch directory outside production source and isolated ports or data directories where needed. Folder separation is not a sandbox. Do not alter production files, user edits, existing services, or shared data to make the probe work.

Keep evidence outside disposable runtime state. Identify owned processes and how to stop them safely; a process name or stale PID alone is not ownership proof. If the target cannot be reached or isolated safely, report the blocker instead of substituting an undisclosed stand-in.

Completion: a reachable safe probe with known dependencies, mutation boundaries, evidence paths, and cleanup ownership.

## 3. Build and drive

Create only what the question needs. Reuse an existing executable or interface when no new code is necessary. Keep scratch source explicitly throwaway; omit unrelated abstractions and infrastructure.

Run or operate the relevant surface. For UI work, use an available driver to exercise the interaction and inspect its states; capture the action and resulting state. A static screenshot or unoperated mockup does not prove interaction behavior.

Inspect actual output, exit status, and relevant side effects. A failure may expose candidate behavior or a broken probe; establish which before concluding. Correct setup only within authorized scratch scope. Bound retries and preserve informative failed observations. Clean up owned resources after failed attempts before another attempt.

Completion: an observed result on the intended surface, or a recorded failure or access limit; no unobserved success claim.

## 4. Observe and conclude

Record exact inputs, commands or interaction steps, run context, observations, and evidence locations. Distinguish observed facts, assumptions, user preferences, and stand-in differences. State what the experiment does not establish.

For timing probes, record build mode, cache state, workload, runs, and measurement boundaries. A single timing is a probe, not a reliable speedup claim. Do not compare unlike scenarios or let faster incorrect output count as a win.

Conclude either that the question is answered within the stated conditions, or that it remains unresolved with a specific limitation. An unfavorable result can answer the question successfully. Missing capability or broken observation cannot prove the candidate fails.

Completion: a decision consequence supported by direct evidence, or an explicit unresolved question without inflated claims.

## 5. Preserve evidence and clean up

Retain useful outputs, screenshots, logs, and failed observations outside runtime scratch state. Stop only owned processes and remove only disposable state permitted by the agreed lifecycle. Confirm evidence remains readable after cleanup. Keep useful scratch source only when its retention is agreed, and label it throwaway.

Report cleanup failures and remaining resource identifiers. A resolved experiment with failed cleanup is not a fully completed handback. Never hide stranded resources or delete unrelated files to produce a clean result.

Deliver a short experiment note or reply with the question, scope, method, observation, conclusion, limitations, scratch/evidence paths, and cleanup status. Give one next action when unresolved.

Stop at the experiment result. Do not promote the prototype into production, install it, or automatically route to implementation. A later request owns the real build.

Completion: inspected evidence survives cleanup, owned resources are accounted for, and the result remains explicitly experimental.

## Origin

Adapted from Lauren Tan's MIT-licensed pstack [Prototype playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md). The upstream notice appears in `../../LICENSE`.

This version removes automatic implementation routing and unconditional external dependencies. It retains scoped empirical work with explicit observation, isolation, resource, and cleanup limits.
