"""Onboarding state machine.

Linear flow with two branch guards (returning contributor skip, confirmation
gate before handoff).
"""

from __future__ import annotations

from enum import Enum
from typing import Callable


class State(str, Enum):
    GREETING = "greeting"
    CONTRIBUTOR_CHECK = "contributor_check"
    ROLE_DETECTION = "role_detection"
    REPOSITORY_DISCOVERY = "repository_discovery"
    TECHNOLOGY_DISCOVERY = "technology_discovery"
    CONTRIBUTION_SELECTION = "contribution_selection"
    WORKFLOW_STYLE = "workflow_style"
    WORKFLOW_FRAMEWORK = "workflow_framework"
    SUMMARY = "summary"
    READY_FOR_HANDOFF = "ready_for_handoff"


def _always(_data: dict) -> bool:
    return True


def _summary_confirmed(data: dict) -> bool:
    return bool(data.get("summary_confirmed"))


# Ordered transitions: (from_state, to_state, guard)
_TRANSITIONS: list[tuple[State, State, Callable[[dict], bool]]] = [
    (State.GREETING, State.CONTRIBUTOR_CHECK, _always),
    (State.CONTRIBUTOR_CHECK, State.ROLE_DETECTION, _always),
    (State.ROLE_DETECTION, State.REPOSITORY_DISCOVERY, _always),
    (State.REPOSITORY_DISCOVERY, State.TECHNOLOGY_DISCOVERY, _always),
    (State.TECHNOLOGY_DISCOVERY, State.CONTRIBUTION_SELECTION, _always),
    (State.CONTRIBUTION_SELECTION, State.WORKFLOW_STYLE, _always),
    (State.WORKFLOW_STYLE, State.WORKFLOW_FRAMEWORK, _always),
    (State.WORKFLOW_FRAMEWORK, State.SUMMARY, _always),
    (State.SUMMARY, State.READY_FOR_HANDOFF, _summary_confirmed),
]


class OnboardingStateMachine:
    """Drives the onboarding flow one step at a time."""

    def __init__(self) -> None:
        self.state: State = State.GREETING
        self.data: dict = {}

    def advance(self) -> State:
        """Move to the next state if its guard passes; otherwise stay put."""
        for from_state, to_state, guard in _TRANSITIONS:
            if self.state == from_state and guard(self.data):
                self.state = to_state
                break
        return self.state

    def is_done(self) -> bool:
        return self.state == State.READY_FOR_HANDOFF
