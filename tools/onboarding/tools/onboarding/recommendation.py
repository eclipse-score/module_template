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

"""Maps onboarding answers to a recommended workflow, allows user override."""

from __future__ import annotations

WORKFLOWS = [
    "sdlc_harness",
    "speckit",
    "bmad",
    "technical_analysis",
    "issue_planning",
    "traditional",
]

# Downstream agents each workflow may hand off to (label -> agent id). Onboarding
# only recommends these; it never executes them.
HANDOFF_MAP: dict[str, list[str]] = {
    "sdlc_harness": ["plan-tech-analysis", "plan-requirements", "code-design"],
    "speckit": ["plan-issue-creation", "plan-requirements"],
    "bmad": ["plan-tech-analysis", "plan-requirements"],
    "technical_analysis": ["plan-issue-creation", "plan-requirements"],
    "issue_planning": ["plan-tech-analysis", "plan-requirements"],
    "traditional": ["code-design"],
}

# Base mapping from contribution_type to workflow, per onboarding.skill.md.
_CONTRIBUTION_MAP: dict[str, tuple[str, str]] = {
    "bug_fix": ("sdlc_harness", "Bug fixes benefit from SDLC Harness traceability."),
    "improvement": ("speckit", "Improvements are well-suited to spec-driven planning."),
    "poc": ("bmad", "Proof-of-concept work fits a Build-Measure-Analyze-Design loop."),
    "documentation": ("traditional", "Documentation-only changes can follow the traditional flow."),
    "feature": ("sdlc_harness", "New features require the full SDLC lifecycle for traceability."),
    "question": ("issue_planning", "Open questions should start with issue definition."),
}


def recommend_workflow(contribution_type: str, asil: str = "QM", description: str = "") -> tuple[str, str]:
    """Rule-based recommendation. Returns (workflow, reason)."""
    if asil and asil.upper() != "QM":
        return "sdlc_harness", "Safety-relevant module (ASIL != QM) requires full SDLC Harness traceability."
    if contribution_type in _CONTRIBUTION_MAP:
        return _CONTRIBUTION_MAP[contribution_type]
    return "technical_analysis", "Unclear or complex scope requires decomposition before planning."


def select_workflow(recommended: str, user_choice: str | None = None) -> tuple[str, bool]:
    """Returns (selected_workflow, was_overridden)."""
    if user_choice and user_choice in WORKFLOWS:
        return user_choice, user_choice != recommended
    return recommended, False


def get_handoff_recommendations(workflow: str) -> list[str]:
    return HANDOFF_MAP.get(workflow, [])
