# Skill authoring survey

Survey date: 2026-11-04. Target: a portable, explicit-only `gstack-create-skill` that creates and updates skills.

## Sources and authority

| Source | Inspected material | Result |
| --- | --- | --- |
| Cursor | [Skills](https://cursor.com/docs/skills), [creation help](https://cursor.com/help/customization/skills), local pstack authoring caller | Public format and built-in purpose available; installed built-in source unavailable. |
| Matt Pocock | `skills/productivity/writing-for-agents/SKILL.md` and `SKILL-MECHANICS.md` in the local matt-skills checkout | Authoring reference, not a current create-skill recipe. |
| Anthropic | [Claude Code skills](https://code.claude.com/docs/en/skills), [authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Create/update, progressive disclosure, case trials, iteration, and optional empirical comparison. |
| OpenAI | [Codex skills](https://developers.openai.com/codex/skills), [skill-creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md), its metadata reference and scripts | Create/update, optional resources, script execution, limited validation, and explicit invocation metadata. |
| Agent Skills | [Specification](https://agentskills.io/specification) | Portable format baseline; host invocation controls remain extensions. |

Use product documentation for host behavior, the specification for portable format, and utility source for its actual validation scope.

The local Matt checkout has revision `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`. Its authoring source is [writing-for-agents](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md).

The Anthropic survey reports latest file-change commit `b0cbd3df1533b396d281a6886d5132f623393a9c`, dated 2026-03-06. The OpenAI survey reports creator path-change commit `4ab6e0fd99c6667163bc34173e3ed3a3fed75ebc`, dated 2026-02-09. These are repository history observations, not product release dates. Main-branch URLs can change.

## Guidance retained

1. Establish concrete purpose, examples, outputs, and boundaries before authoring. Read and reuse an existing target before creating another.
2. Keep common instructions inline. Give conditional references explicit read conditions. Use observable completion criteria and one authoritative home for each rule.
3. Add scripts for repeated or fragile deterministic work, not for every skill. Test executable resources; omit unused scaffolding.
4. Check format, references, metadata, and dependencies separately from behavior. Preserve unrelated changes and invocation policy during updates.
5. Use representative cases and observed failures for iteration. Delegate comparative claims to the existing Eval protocol rather than add a second runner.

Matt supplies the strongest document-structure vocabulary. Anthropic supplies the explicit draft/test/review iteration. OpenAI supplies clear resource roles and create-versus-update handling. Cursor supplies the public skill contract and pstack's authoring integration pattern.

## Important conflicts and limits

### Cursor source access

A direct read of `/Users/gordon/.cursor/skills-cursor/create-skill/SKILL.md` returned `ENOENT`. The survey also failed to locate an installed Cursor source. This does not establish the contents or license of the built-in.

Local pstack `skills/poteto-mode/playbooks/authoring-a-skill.md:5-7` delegates to the built-in, then checks metadata and references. `skills/reflect/SKILL.md:55-59` routes substantive changes through its draft/test/iterate loop. These are callers, not the built-in implementation.

The new skill is an original synthesis, not a recovered Cursor port. It does not copy vendor scripts or substantial source passages.

### Manual-only routing is host-specific

Claude Code's current **Control who invokes a skill** section says it blocks autonomous invocation of a manual-only skill and instructs the agent not to reproduce the steps another way. **Where you write the skill's name** documents a separate user permission mechanism. A sibling path is not portable authorization.

Codex's optional `agents/openai.yaml` supports `policy.allow_implicit_invocation: false`. Its product contract differs from Claude Code's frontmatter controls. Neither declaration is a filesystem sandbox.

Matt's local `SKILL-MECHANICS.md:7-19` describes manual-only routing restrictions. pstack's `docs/harness/claude-code.md:12` instead recommends direct reads. Prefer current host constraints when these conflict. Do not advertise direct reads as a universal bypass.

### Validation is limited

OpenAI's `quick_validate.py` checks selected frontmatter properties. The inspected source does not establish local references, directory-name equality, host policy, or behavioral quality. Its accepted fields also differ from the portable specification.

OpenAI's `generate_openai_yaml.py` writes a fresh metadata file. It can erase existing policy or dependencies. Preserve and recheck those fields if a generator runs.

Anthropic's authoring utilities and viewer are platform-specific aids. This synthesis does not require their CLI, viewer, optimizer, or packaging scripts.

### Evaluation costs and claims

Manual-only skills need explicit-execution checks, not automatic-description optimization by default. Automatic target skills can require trigger and non-trigger cases.

A structural pass and a static walkthrough do not prove reliable agent behavior. Extra model runs require a bounded approved matrix. The existing `gstack-eval` owns baseline isolation, checks, blinded review limits, holdouts, and adoption verdicts.

## Implementation decision

Add one five-step authoring skill and one conditional check reference. Use the repository's explicit-only metadata. Connect approved substantive Reflect edits to the creator, then route behavioral comparisons to Eval when authorized.

Keep small Reflect edits direct. Keep installation and publication separate. Preserve host invocation gates rather than promise identical automation across Claude Code, Codex, and pi.

## Verification scope

Research used primary pages and source inspection. No Cursor built-in execution or cross-host behavioral comparison occurred. The local crew reports retain detailed passages and paths under ignored `.pi/crew/`; they are not runtime dependencies.

Implementation validation appears in the task's final report. Do not infer empirical gains from the guidance above.
