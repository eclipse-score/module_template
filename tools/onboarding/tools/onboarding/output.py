# *******************************************************************************
# Copyright (c) 2026 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0
#
# SPDX-License-Identifier: Apache-2.0
# *******************************************************************************

"""Builds and writes the single onboarding context contract (Phase 4).

Replaces the earlier per-workflow files (sdlc_input.json, ...) with one
``.onboarding/context.json`` every downstream
workflow can consume.
"""

from __future__ import annotations

from pathlib import Path

from .models import ContextEnvelope, ContributorProfile, RepositoryContext, WorkflowSelection, WorkItem
from .recommendation import get_handoff_recommendations

DEFAULT_OUTPUT_DIR = ".onboarding"
DEFAULT_OUTPUT_FILE = "context.json"


def build_context_envelope(
    repository: RepositoryContext,
    role: str,
    contribution_type: str,
    workflow: str,
    workflow_reason: str = "",
    user_override: bool = False,
    module: str | None = None,
    description: str = "",
) -> ContextEnvelope:
    return ContextEnvelope(
        repository=repository,
        contributor=ContributorProfile(role=role, module=module),
        work_item=WorkItem(type=contribution_type, description=description),
        workflow=WorkflowSelection(selected=workflow, reason=workflow_reason, user_override=user_override),
    )


def write_context(envelope: ContextEnvelope, root: Path, output_dir: str = DEFAULT_OUTPUT_DIR) -> Path:
    target_dir = root / output_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / DEFAULT_OUTPUT_FILE
    target_path.write_text(envelope.to_json() + "\n", encoding="utf-8")
    return target_path


def handoff_summary(envelope: ContextEnvelope) -> list[str]:
    """Recommended next agents; onboarding never executes them itself."""
    return get_handoff_recommendations(envelope.workflow.selected)
