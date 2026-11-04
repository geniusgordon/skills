# Hard-debug methods

Use these methods when the trigger is intermittent, several causes fit the evidence, or an initial probe cannot distinguish them. Simple, established causes do not need a fixed number of hypotheses.

## Make the check repeatable

Name one command or interaction sequence that exercises the reported path and asserts the exact symptom. Run it before the fix. Prefer existing project controls; create a small replay script only when necessary.

Keep the signal fast and specific. Pin inputs, random seeds, and timing where feasible. For intermittent failures, repeat the trigger and record attempts and failures. Higher reproduction frequency helps diagnosis; a changed trigger still needs evidence that it represents the original mechanism.

Reduce one input or step at a time and rerun the check. Keep reductions only while the same failure survives. Retain the original scenario for final verification.

## Distinguish causes

Write the plausible causes that remain after initial evidence. Rank them by supporting evidence and probe cost. For each, state a prediction and a probe that could contradict it. Do not invent alternatives to reach a quota.

Choose the next probe for how much uncertainty it removes. Change one condition at a time. Prefer a debugger or targeted boundary observation over broad logging.

When a probe refutes a cause, remove product changes supported only by that cause. If repeated fixes share a failed premise, probe that premise directly.

## Keep instrumentation temporary

Give diagnostic logs a unique marker. Record which files and artifacts belong to the probe. Remove only your temporary instrumentation before the final reproduction, then inspect the marker and changed files to confirm cleanup.

For performance symptoms, establish the measured baseline and relevant profile before a fix. Separate instrumentation overhead from the behavior under measurement.

## Provenance

Method reference: [Matt Pocock's diagnosing-bugs skill](https://github.com/mattpocock/skills/tree/main/diagnosing-bugs). This reference summarizes methods; it does not copy the upstream procedure or require that skill to be installed.
