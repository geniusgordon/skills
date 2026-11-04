# Bug Fix comparison plan

Status: draft skill and one calibrated fixture. No paid agent runs are authorized. Calibration is not evidence of workflow benefit.

## Target

Measure whether the workflow improves reproduction before edits, evidence-supported diagnosis, contract-preserving fixes, and final verification over the existing baseline.

Use the same host, Connexmatrix model, effort, tools, permissions, project revision, and task prompt within each pair. Freeze prompts, rubric, run count, thresholds, and isolation before execution.

## First case

Copy only `fixtures/dispatch/` into each neutral candidate workspace. Candidates receive its README and code, not this plan or coordinator checks.

Ordinary request:

```text
An order is stored twice when a response is lost and the caller retries.
Fix this without dropping legitimate orders. Keep the change small and show what works.
```

The fixture simulates a response loss after storage commits. Retry handling must distinguish request identity from item equality. The project contract requires an incompatible reuse of a request ID to fail without changing storage. Requests are sequential; concurrent writers are outside this fixture's scope.

## Check calibration

Run:

```sh
python3 evaluations/bug-fix/calibrate.py
```

Observed calibration: the broken fixture fails on duplicate storage, a repaired temporary copy passes, item-based dedup fails on a lost distinct request, and silent acceptance of an incompatible retry fails. Source fixtures remain unchanged.

After agent completion, run `python3 evaluations/bug-fix/checks.py <workspace>`. The coordinator verifies the lost response, repeated retries, original response content, distinct request IDs with the same item, and conflicting payload rejection.

Keep the check and calibration files outside candidate access. Deliberately broken implementations stay in temporary calibration copies, not candidate prompts.

## Comparison variants

Use three variants when the budget permits:

- A: controlled snapshot of the user's current baseline.
- B: A plus Verify Result only.
- C: A plus Bug Fix, with the sibling Verify Result file available.

A versus C measures the combined workflow. B versus C isolates the added diagnosis and reproduction procedure. A two-arm A/C pilot is cheaper but cannot attribute a gain to Bug Fix alone.

In C, make the complete `skills/bug-fix` and `skills/verify-result` sibling layout available. Preserve the relative dependency. Disable ambient discovery in all variants, then supply only the assigned instructions. Record actual file reads. This evaluates explicit execution; test command discovery separately.

## Rubric and decision

1. Reproduction: an executed pre-fix check shows the reported duplicate path.
2. Cause: records connect the post-commit lost response and unconditional append to the duplicate.
3. Correctness: coordinator checks pass, including distinct IDs and incompatible retries.
4. Verification: actual final-artifact checks exercise the original path and relevant unchanged behavior.
5. Proportionality and honesty: no unrelated edits, speculative claims, or unsupported success.

Fabricated evidence, unsafe actions, dropped legitimate orders, and false completion claims block adoption. A judge cannot override failed executable checks.

Use repeats and untouched cases before adoption. Freeze holdouts that involve other mechanisms, such as stale state across two callers, so success does not only measure instructions tailored to retry identity. This first fixture informed the workflow wording; report that limitation rather than treat it as a holdout.

A tied result keeps baseline. Any adoption rule must define observed improvement and authorized usage limits before outputs arrive. Small pilots do not prove reliability.

## Execution remains pending

Obtain approval for variants, exact Connexmatrix model, repetitions, timeout, and any independent judge. Keep complete local session records. Do not publish credentials or private instructions.

Audit inherited global skills, ancestor context, sibling access, and external services. Neutral workspace names are not a sandbox. Missing isolation or limited transcripts must appear in the report.
