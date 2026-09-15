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

"""Onboarding CLI: single entry point into the S-CORE AI SDLC ecosystem.

Stdlib-only (argparse + input()) so this binary has no external pip
dependency beyond what //tools/onboarding already needs.

Usage:
    bazel run @score_onboarding//tools/onboarding:sdlc
    python -m tools.onboarding
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from .discovery import discover_repository
from .output import build_context_envelope, handoff_summary, write_context
from .recommendation import WORKFLOWS, recommend_workflow, select_workflow
from .state_machine import OnboardingStateMachine, State
from .validators import ROLES, validate_contribution_type, validate_role

ROLE_CHOICES = sorted(ROLES)
CONTRIBUTION_CHOICES = ["bug_fix", "improvement", "poc", "documentation", "feature", "question"]


def _prompt_choice(question: str, choices: list[str], default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        answer = input(f"{question} ({'/'.join(choices)}){suffix}: ").strip() or (default or "")
        if answer in choices:
            return answer
        print(f"Please choose one of: {', '.join(choices)}")


def _prompt_confirm(question: str, default: bool = True) -> bool:
    suffix = "Y/n" if default else "y/N"
    answer = input(f"{question} [{suffix}]: ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


def run_sdlc(repo_root: Path) -> None:
    """Run the interactive onboarding flow and produce .onboarding/context.json."""
    machine = OnboardingStateMachine()
    print("Welcome to Eclipse S-CORE onboarding. Type /sdlc anytime to restart.")
    machine.advance()  # -> CONTRIBUTOR_CHECK

    machine.advance()  # -> ROLE_DETECTION
    role = _prompt_choice("Your role", ROLE_CHOICES)
    validate_role(role)

    machine.advance()  # -> REPOSITORY_DISCOVERY
    machine.advance()  # -> TECHNOLOGY_DISCOVERY
    repository = discover_repository(repo_root)
    print(
        f"Detected repository '{repository.name}': ASIL={repository.asil}, "
        f"languages={repository.languages}, toolchains={repository.toolchains}, "
        f"build={repository.build_system}, docs={repository.docs_system}"
    )

    machine.advance()  # -> CONTRIBUTION_SELECTION
    contribution_type = _prompt_choice("Contribution type", CONTRIBUTION_CHOICES)
    validate_contribution_type(contribution_type)

    machine.advance()  # -> WORKFLOW_STYLE
    recommended, reason = recommend_workflow(contribution_type, repository.asil)
    print(f"Recommended workflow: {recommended} ({reason})")

    machine.advance()  # -> WORKFLOW_FRAMEWORK
    user_choice = _prompt_choice("Workflow (or 'recommend' to accept)", [*WORKFLOWS, "recommend"], default="recommend")
    selected, overridden = select_workflow(recommended, None if user_choice == "recommend" else user_choice)

    machine.advance()  # -> SUMMARY
    print(f"\nSummary: role={role}, contribution={contribution_type}, workflow={selected}")
    machine.data["summary_confirmed"] = _prompt_confirm("Confirm and generate context.json?")
    machine.advance()  # -> READY_FOR_HANDOFF (if confirmed)

    if machine.state != State.READY_FOR_HANDOFF:
        print("Onboarding cancelled. No context.json was written.")
        return

    envelope = build_context_envelope(
        repository=repository,
        role=role,
        contribution_type=contribution_type,
        workflow=selected,
        workflow_reason=reason,
        user_override=overridden,
    )
    path = write_context(envelope, repo_root)
    print(f"\nContext written to {path}")

    print("\nRecommended next steps (confirm before starting):")
    for agent in handoff_summary(envelope):
        print(f"  - Start {agent}")


def _default_repo_root() -> Path:
    # Under `bazel run`, cwd is the runfiles sandbox, not the real checkout.
    # Bazel sets BUILD_WORKSPACE_DIRECTORY to the actual invocation directory.
    workspace_dir = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    return Path(workspace_dir) if workspace_dir else Path.cwd()


def cli(argv: list[str] | None = None) -> None:
    # The Bazel target is already named "sdlc"; no subcommand needed.
    parser = argparse.ArgumentParser(prog="sdlc")
    parser.add_argument("--repo-root", type=Path, default=_default_repo_root())

    args = parser.parse_args(argv)
    run_sdlc(args.repo_root)


if __name__ == "__main__":
    cli()
