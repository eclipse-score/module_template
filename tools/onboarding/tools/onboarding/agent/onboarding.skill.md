# Onboarding Skill

Single entry point into the Eclipse S-CORE AI SDLC ecosystem. Collects
context, classifies the contribution, recommends a workflow, and hands off —
it does not execute SDLC Harness, SpecKit, BMAD, Technical Analysis, or
Planning itself.

## Role Detection
Ask the contributor for their role: `developer`, `reviewer`, `maintainer`, or
`committer`. Returning contributors may skip the introduction.

## Repository Discovery
Read (never execute) `MODULE.bazel`, `project_config.bzl`, `README.md`, and
`CONTRIBUTION.md` at the repository root. Extract: repository name, module,
ASIL level, declared languages, build system.

## Technology Discovery
From `MODULE.bazel`, detect toolchains by dependency name:
- `rules_rust` → Rust
- `rules_cc` → C++
- `toolchains_llvm` → LLVM
- `qnx` (in `MODULE.bazel` or `scripts/`) → QNX

## Contribution Classification
Ask for the contribution type: `bug_fix`, `improvement`, `poc`,
`documentation`, `feature`, or `question`.

## Workflow Recommendation
Map contribution type to a workflow (see `recommendation.py`):
- `bug_fix` → SDLC Harness
- `improvement` → SpecKit
- `poc` → BMAD
- `documentation` → Traditional
- otherwise → Technical Analysis / Issue Planning

If the repository's ASIL level is not `QM`, always recommend SDLC Harness
regardless of contribution type, since safety-relevant work requires full
traceability. The contributor may always override the recommendation.

## Guardrails
- Never write outside `.onboarding/context.json`.
- Never auto-start a downstream agent; always require explicit confirmation.
- Never fabricate repository metadata that discovery could not detect —
  surface it as `"Unknown"` and let the contributor confirm/correct it.

## Open-source contribution rules
Point contributors to `CONTRIBUTION.md` for PR/issue templates, the ECA/DCO
signing requirement, and commit message rules before any handoff.
