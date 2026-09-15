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

# Sample Onboarding Session

```
$ python -m tools.onboarding
Welcome to Eclipse S-CORE onboarding. Type /sdlc anytime to restart.
Your role: developer
Detected repository 'module_template': ASIL=QM, languages=['cpp', 'rust'],
toolchains=['llvm'], build=Bazel, docs=Sphinx
Contribution type: bug_fix
Recommended workflow: sdlc_harness (Bug fixes benefit from SDLC Harness traceability.)
Workflow (or 'recommend' to accept) [recommend]: recommend

Summary: role=developer, contribution=bug_fix, workflow=sdlc_harness
Confirm and generate context.json? [Y/n]: y

Context written to .onboarding/context.json

Recommended next steps (confirm before starting):
  - Start plan-tech-analysis
  - Start plan-requirements
  - Start code-design
```

No downstream agent is started automatically — the contributor picks one of
the recommended next steps and confirms explicitly.
