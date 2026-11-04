# Authoring checks

Use this checklist on the final target, not a stale draft. Prefer available repository or host validators. Report their limits instead of adding a new validator framework.

## Format and invocation

- Parse the frontmatter as a YAML mapping. Require nonempty string `name` and `description`.
- Match the name to its directory. Use 1-64 lowercase letters, digits, and hyphens, with no leading, trailing, or consecutive hyphens.
- Keep the description within 1024 characters. State the capability and relevant use context without promises of reliable discovery.
- Check host-specific fields against the supported hosts. For explicit-only gstack targets, verify both the frontmatter and Codex policy.
- Preserve existing metadata, dependencies, and licenses. A metadata generator may overwrite rather than merge them.

Claude Code's format is more permissive than the portable core. A vendor validator may reject another host's valid fields. Resolve that mismatch explicitly; do not delete policy merely to get a pass.

## References and resources

Resolve local paths from the file's documented base, normally the skill root. Check every direct reference and cross-skill dependency. Read the relevant target content and verify Markdown anchors where used.

For external claims that determine behavior, inspect the authoritative passage. A reachable URL does not establish that it supports the claim. Report inaccessible or unverified sources.

Keep sibling dependencies explicit. A source-tree pointer can break when a distributor packages only one skill. Check the intended installed layout, or disclose that it remains untested.

Inspect scripts and commands before execution. Run changed executable resources on disposable data with expected success and failure checks. Respect permissions and avoid production writes. Remove placeholders and unused examples.

## Workflow quality

Check that each case reaches a concrete result or named blocker. Verify that scope, failure behavior, permissions, and completion conditions remain consistent across steps and callers.

Keep references conditional and directly discoverable. Use a table of contents for a reference above 100 lines. Remove duplicate rules and facts available through cheap environment lookups.

Separate invocation policy from file access. Claude Code documents that a blocked autonomous call must not be reproduced another way. Direct file reads are not a portable permission bypass.

## Evidence levels

- Structural check: metadata, references, and declared dependencies satisfy the checks executed.
- Static walkthrough: the author traces cases through the instructions without a fresh agent run.
- Smoke check: a host actually loads and exercises a path, with output or execution records.
- Comparative evaluation: matched baseline and proposed runs support a bounded behavioral conclusion.

Do not upgrade one evidence level into another. For a substantive behavior comparison, route to the sibling Eval workflow with authorization and a budget.
