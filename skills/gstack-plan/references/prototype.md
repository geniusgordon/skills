# Empirical probes during planning

Use a small local probe only when its observation can change the design. Define the question, decision rule, and safe resource bound before execution. Otherwise retain the uncertainty as a plan gate.

## Planning boundary

Plan permits only a small, reversible probe within its request. Prefer an existing command with synthetic or copied input. Use isolated scratch state outside production source and keep evidence outside disposable runtime state. Inspect actual output or operated UI state, not a plausible explanation.

Preserve production files, user edits, existing services, and shared data. Ask before installs, production access, destructive actions, paid services, extra model calls, or an expanded experiment. A folder is not a sandbox. If isolation, observation, or a safe limit is unavailable, report the blocker.

Account for owned resources after every attempt, retain useful failed observations, and confirm evidence survives cleanup. A failed probe does not authorize production repairs. A timing sample does not prove a reliable speedup.

## Standalone experiments

The complete standalone method belongs to `gstack-prototype`. Use it for an explicitly requested experiment beyond a minimal planning probe, through the host's permitted invocation path. It is optional; Plan has no required sibling dependency.

Do not read and reproduce a blocked manual-only sibling workflow as a workaround. If a handoff is blocked, request authorized invocation or keep the question unresolved. This adapter does not expand Plan's small-probe allowance into a full experiment.

## Feed the plan

Record the observation, its inputs and evidence path, decision consequence, environmental limits, and remaining uncertainty. Separate executed evidence from proposed checks. Stop at the plan; scratch code is not shippable implementation.

## Origin

The planning boundary adapts pstack's MIT-licensed [Prototype playbook](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/playbooks/prototype.md) by Lauren Tan. Detailed standalone instructions live in Prototype; this adapter keeps planning probes scoped and independent of sibling installation.
