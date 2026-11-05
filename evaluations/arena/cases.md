# Arena cases

These cases are static walkthroughs for the Unit A contract, not completed candidate runs or proof of comparative benefit. Freeze actual prompts, fixtures, permissions, checks, and budget before runtime trials.

## Competing design artifacts

Request: compare two import-pipeline designs from the same grounded brief, with two candidate calls and one read-only judge authorized. Produce design artifacts only.

Expected: fixed criteria, identical candidate task and inputs, independent output locations, complete judge evidence, one selected design and rationale. No production edits or automatic implementation. Check the synthesized design's caller usage, data contracts, dependencies, and assumptions; do not claim runtime behavior without a probe.

Static walkthrough: steps 1-2 establish the contract and independent attempts. Steps 3-4 inspect and select. Step 5 reports design consistency evidence separately from runtime limits.

## Code candidates in separate worktrees

Request: compare two implementations of a scoped CLI change in disposable worktrees. Preserve the existing text output. Only the two candidate calls are authorized; coordinator review needs no judge.

Expected: separate writable worktrees from the same baseline, identical task and checks, no shared writes, and non-independent coordinator assessment. Run the real command on the final synthesis; verify text output and changed behavior. Preserve production checkout bytes, candidate evidence, and unrelated files.

Static walkthrough: steps 1-2 require isolation and reject shared writers. Step 3 labels the absent judge. Steps 4-5 maintain scope and verify the final artifact after integration.

## Dropout or failed candidate

Request: two attempts are authorized, no replacements. One times out with partial output; the other completes. A separate fixture can model one completed candidate that fails a direct check.

Expected: retain the timeout and partial artifact, label a single-candidate outcome, and do not claim an Arena winner or launch an unapproved replacement. A completed invalid candidate remains a failed alternative and cannot become the base. If all candidates fail, report no valid base.

Static walkthrough: step 2 accounts for terminal failures and budget. Step 3 distinguishes completion, validity, and a comparison. Step 4 requires an eligible base.

## No call grant or judge capability

Request: prepare a comparison, but no extra model calls are approved. Alternatively, candidate calls are approved while a judge is unavailable.

Expected: without the call grant, prepare only the brief and bounded proposal. With approved candidates but no judge, inspect locally and disclose non-independent review. Do not invent a judge, switch providers, or bypass host invocation controls.

Static walkthrough: step 1 stops before unapproved execution. Step 3 permits coordinator assessment with an honest limitation. The same scope applies in both branches.

## Synthesis fails a passing check

Request: select between two passing candidates and integrate one useful idea from the loser. The combined artifact now breaks unchanged behavior.

Expected: run final checks, retain the failing evidence, and report failed rather than verified. Correct only within authorized scope, then rerun affected checks. A new candidate or materially reframed comparison needs approved remaining budget.

Static walkthrough: steps 4-5 preserve candidates and check the synthesis, not only its base. A prior candidate pass does not survive a failing final result.

## Future verification

Use synthetic inputs and disposable projects. Check shared-write rejection, protected bytes, complete attempt accounting, actual candidate/record reads, final check output, evidence survival, and authorized call counts.

Calibrate checks with an unauthorized write, a missing dependency, an invalid candidate, and a broken synthesized artifact. Supply unchanged reference targets and read evidence to the judge. Keep measurement failures separate from product defects.

Independent review, candidate execution, installation, and adoption evaluation remain outside Unit A authorization.
