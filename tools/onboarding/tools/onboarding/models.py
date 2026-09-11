"""Data model for the onboarding context envelope.

A single ``context.json`` replaces the earlier per-workflow input files
(``sdlc_input.json``, ``speckit_input.json``, ``bmad_input.json`` ...).
Every downstream workflow reads the same envelope shape.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field


@dataclass
class RepositoryContext:
    name: str
    asil: str = "QM"
    languages: list[str] = field(default_factory=list)
    toolchains: list[str] = field(default_factory=list)
    build_system: str = "Unknown"
    docs_system: str = "Unknown"


@dataclass
class ContributorProfile:
    role: str
    module: str | None = None


@dataclass
class WorkItem:
    type: str
    description: str = ""


@dataclass
class WorkflowSelection:
    selected: str
    reason: str = ""
    user_override: bool = False


@dataclass
class ContextEnvelope:
    repository: RepositoryContext
    contributor: ContributorProfile
    work_item: WorkItem
    workflow: WorkflowSelection

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
