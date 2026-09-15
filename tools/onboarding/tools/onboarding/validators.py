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

"""Input validation for onboarding answers."""

from __future__ import annotations

from pathlib import Path

# Official S-CORE role catalog: role id -> (title, process-area tags).
# https://eclipse-score.github.io/process_description/main/roles/index.html
ROLE_CATALOG: dict[str, tuple[str, str]] = {
    "architecture_community": ("Architecture Community Member", "architecture_design"),
    "committer": ("Committer", "development"),
    "contributor": ("Contributor", "development"),
    "delivery_team": ("Delivery Team", "cross_functional"),
    "infrastructure_tooling_community": ("Infrastructure Tooling Community Member", "development"),
    "platform_team": ("Platform Team", "cross_functional"),
    "process_community": ("Process Community Member", "process_management"),
    "project_lead": ("Project Lead", "process_management"),
    "security_team": ("Project Security Team", "verification; security_analysis"),
    "quality_manager": ("Quality Manager", "quality_management"),
    "release_team": ("Release Team", "cross_functional"),
    "safety_engineer": ("Safety Engineer", "safety_analysis"),
    "safety_external_auditor": ("Safety External Auditor", "safety_management"),
    "safety_manager": ("Safety Manager", "safety_management"),
    "security_engineer": ("Security Engineer", "security_analysis"),
    "security_external_auditor": ("Security External Auditor", "security_management"),
    "security_manager": ("Security Manager", "security_management"),
    "testing_community": ("Testing Community Member", "verification"),
}
ROLES = set(ROLE_CATALOG)
CONTRIBUTION_TYPES = {"bug_fix", "improvement", "poc", "documentation", "feature", "question"}


class ValidationError(ValueError):
    """Raised when an onboarding answer fails validation."""


def validate_role(role: str) -> str:
    if role not in ROLES:
        raise ValidationError(f"Unknown role '{role}'. Expected one of: {sorted(ROLES)}")
    return role


def validate_contribution_type(contribution_type: str) -> str:
    if contribution_type not in CONTRIBUTION_TYPES:
        raise ValidationError(
            f"Unknown contribution type '{contribution_type}'. Expected one of: {sorted(CONTRIBUTION_TYPES)}"
        )
    return contribution_type


def validate_repository_path(root: Path) -> Path:
    if not (root / "MODULE.bazel").is_file():
        raise ValidationError(f"'{root}' does not look like an S-CORE Bazel repository (no MODULE.bazel).")
    return root
