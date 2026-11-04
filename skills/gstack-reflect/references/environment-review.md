# Environment review

Read this when the session shows repeated navigation friction, missing information, tool overhead, context pressure, or a failure that a structural check could prevent.

Find the missing capability before you add another skill rule:

| Observed friction | Inspect | Prefer |
| --- | --- | --- |
| Repeated file searches | Existing indexes, module boundaries, and nearby docs | One project-local navigation pointer or clearer module ownership |
| Repeated detectable mistakes | Types, lint, tests, and metadata | A check that rejects the mistake |
| Large instructions with no observed benefit | Always-loaded guidance and duplicate references | Delete no-ops or disclose guidance only where needed |
| Review rules burden every implementation turn | Existing review workflow and standards | Put review-specific guidance at the review step; keep implementation correctness requirements intact |
| Missing runtime evidence | Available controls, logs, read-only service access, and permissions | Propose the smallest safe information-access change |
| Repeated costly tool sequences | Existing command interfaces and measured overhead | A simpler invocation or small reusable tool, only after a repeated need |

Evidence must connect the proposed mechanism to an observed incident. A difficult task does not by itself prove poor tooling. Do not propose external access or automation without its scope, permission needs, and a checkable benefit.

Project-specific commands and architecture belong in project-local guidance. A global skill may hold the general decision rule, not private examples or stale paths.

Check existing instructions before adding a pointer. More pointers can also increase context and maintenance costs. A recurring clear-rule violation may need enforcement or execution checks rather than more emphatic prose.

## Provenance

Method reference: [Matt Pocock's retro skill](https://github.com/mattpocock/skills/tree/main/retro). This reference summarizes environment-review categories and does not require that skill to be installed.
