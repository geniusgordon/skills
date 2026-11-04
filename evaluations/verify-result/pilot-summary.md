# Verify Result pilot summary

## Scope

Five cases, one baseline and one proposed run each. All ten calls used pi 1.5.0 with connexmatrix-gpt/gpt-6.1-sol and thinking off. Each call had a 180-second timeout.

Both versions used pi's default instructions and a snapshot of the user's general instructions. Ambient skills, extensions, MCP, and context discovery were disabled. The proposed version also received Verify Result as appended system instructions. These runs evaluate instruction execution, not automatic or manual command discovery.

## Outcomes

| Case | Baseline | Plus Verify Result | Baseline tokens | Proposed tokens |
| --- | --- | --- | --- | --- |
| CLI JSON output | Passed direct checks | Passed direct checks | 14019 | 19697 |
| Persistence | Passed cross-process readback | Passed cross-process readback | 13944 | 19200 |
| Empty export | Reproduced, fixed, and read back | Reproduced, fixed, and read back | 13014 | 17631 |
| Blocked staging | Correctly unverified | Correctly unverified | 5931 | 8027 |
| Documentation typo | Correct targeted edit | Correct edit with extra byte check | 9193 | 16398 |

Total reported tokens: 56101 baseline, 80953 proposed, approximately 44.3 percent more in the proposed runs. Provider metadata reported zero cost; it does not establish free usage or the billed price.

The coordinator ran `checks.py` against both final artifacts for each executable case. Every check passed. Full records for the last four cases show runtime checks and honest staging limits. The CLI case retained only partial tool summaries.

The proposed version sometimes added coverage or a clearer verdict. No case established a correctness improvement or regression. Baseline already performed the essential checks.

## Decision

Keep baseline for this controlled setup. Retain Verify Result as an experimental, manually invoked skill for later trials. Manual installation does not establish benefit.

## Limits

- One repetition per version and case; no holdouts or blinded judge.
- Reduced baseline, not the user's complete ambient workflow.
- No enforced filesystem sandbox; staging used an instruction-level external-access restriction.
- Partial CLI process records and no reliable dollar-cost measurements.
- Persistence preservation assertions were added after launch but before outputs were inspected; both versions received the same checks.

These pilots do not establish reliability across models or hosts. Raw session records and detailed reports remain local and outside version control.

## Reproduce fixture calibration

```sh
python3 evaluations/verify-result/calibrate.py
```

Calibration confirms four broken fixtures fail and repaired temporary copies pass. A CRLF output regression also fails the raw-byte check. Staging host isolation remains uncalibrated. Calibration proves the checks detect these defects, not that the skill improves agent behavior.
