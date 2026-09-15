<!--
*******************************************************************************
Copyright (c) 2026 Contributors to the Eclipse Foundation

See the NOTICE file(s) distributed with this work for additional
information regarding copyright ownership.

This program and the accompanying materials are made available under the
terms of the Apache License Version 2.0 which is available at
https://www.apache.org/licenses/LICENSE-2.0

SPDX-License-Identifier: Apache-2.0
*******************************************************************************
-->

# Onboarding Skill

Single entry point into the Eclipse S-CORE AI SDLC ecosystem. Collects
context, classifies the contribution, recommends a workflow, and hands off —
it does not execute SDLC Harness, Technical Analysis, or Planning itself.

## Role Detection
Present the official S-CORE role catalog as a numbered list and ask the
contributor to submit just the number (or the role id) — do not make them
type a free-text role name. Returning contributors may skip the introduction.

| # | Title | Role id | Tags |
| - | ----- | ------- | ---- |
| 1 | Architecture Community Member | `architecture_community` | architecture_design |
| 2 | Committer | `committer` | development |
| 3 | Contributor | `contributor` | development |
| 4 | Delivery Team | `delivery_team` | cross_functional |
| 5 | Infrastructure Tooling Community Member | `infrastructure_tooling_community` | development |
| 6 | Platform Team | `platform_team` | cross_functional |
| 7 | Process Community Member | `process_community` | process_management |
| 8 | Project Lead | `project_lead` | process_management |
| 9 | Project Security Team | `security_team` | verification; security_analysis |
| 10 | Quality Manager | `quality_manager` | quality_management |
| 11 | Release Team | `release_team` | cross_functional |
| 12 | Safety Engineer | `safety_engineer` | safety_analysis |
| 13 | Safety External Auditor | `safety_external_auditor` | safety_management |
| 14 | Safety Manager | `safety_manager` | safety_management |
| 15 | Security Engineer | `security_engineer` | security_analysis |
| 16 | Security External Auditor | `security_external_auditor` | security_management |
| 17 | Security Manager | `security_manager` | security_management |
| 18 | Testing Community Member | `testing_community` | verification |

Source of truth: `validators.ROLE_CATALOG`
If unsure, the contributor should pick `contributor` (id `3`).

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
- `improvement` → SDLC Harness
- `poc` → SDLC Harness
- `documentation` → Traditional
- otherwise → Technical Analysis / Issue Planning

If the repository's ASIL level is not `QM`, always recommend SDLC Harness
regardless of contribution type, since safety-relevant work requires full
traceability. The contributor may always override the recommendation.

## Guardrails
- Never write outside `.onboarding/context.json`.
- Never auto-start a downstream agent; always require explicit confirmation.
- Never fabricate repository metadata that discovery could not detect —
  surface it as `"Unknown"` and let the contributor confirm/correct it. The
  ASIL level is the exception: the schema only accepts `QM, A, B, C, D`, so an
  undetected or unrecognized value defaults to `"QM"` instead of `"Unknown"`.
  `project_config.bzl` may spell this `"ASIL-A"`, `"ASIL-B"`, etc.; discovery
  strips the `ASIL-` prefix so the stored value matches the schema.

## Open-source contribution rules
Point contributors to `CONTRIBUTION.md` for PR/issue templates, the ECA/DCO
signing requirement, and commit message rules before any handoff.
