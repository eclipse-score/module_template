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

# Eclipse S-CORE

Start onboarding: `/sdlc` (or `bazel run @score_onboarding//tools/onboarding:sdlc`)

The onboarding agent (`tools/onboarding/`):
- identifies repository context (ASIL, languages, toolchains, build/docs system)
- classifies your contribution (bug fix, improvement, PoC, documentation, feature, question)
- recommends a workflow (SDLC Harness, Technical Analysis, Issue Planning, Traditional)
- writes a single context contract to `.onboarding/context.json`

See [`tools/onboarding/tools/onboarding/agent/onboarding.skill.md`](tools/onboarding/tools/onboarding/agent/onboarding.skill.md)
for the full skill definition.

See [`CONTRIBUTION.md`](CONTRIBUTION.md) for contribution rules, PR/issue
templates, and the ECA/DCO signing requirement.
