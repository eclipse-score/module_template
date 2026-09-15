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

"""Repository discovery: auto-detect ASIL, languages, toolchains, build/docs system.

Reads MODULE.bazel, project_config.bzl and README.md as plain text (never
executed) to keep discovery safe and dependency-free.
"""

from __future__ import annotations

import re
from pathlib import Path

from .models import RepositoryContext


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _detect_asil(project_config_text: str) -> str:
    match = re.search(r'"asil_level"\s*:\s*"([^"]+)"', project_config_text)
    return match.group(1) if match else "QM"


def _detect_declared_languages(project_config_text: str) -> list[str]:
    match = re.search(r'"source_code"\s*:\s*\[([^\]]*)\]', project_config_text)
    if not match:
        return []
    return [item.strip().strip('"').strip("'") for item in match.group(1).split(",") if item.strip()]


def _detect_languages(module_bazel_text: str, declared: list[str]) -> list[str]:
    languages = set(lang.lower() for lang in declared)
    if "rules_rust" in module_bazel_text:
        languages.add("rust")
    if "rules_cc" in module_bazel_text:
        languages.add("cpp")
    return sorted(languages)


def _detect_toolchains(module_bazel_text: str) -> list[str]:
    toolchains = []
    if "toolchains_llvm" in module_bazel_text:
        toolchains.append("llvm")
    if "score_bazel_cpp_toolchains" in module_bazel_text or "gcc" in module_bazel_text.lower():
        toolchains.append("gcc")
    if "qnx" in module_bazel_text.lower():
        toolchains.append("qnx")
    return toolchains


def _detect_qnx(root: Path, module_bazel_text: str) -> bool:
    if "qnx" in module_bazel_text.lower():
        return True
    scripts_dir = root / "scripts"
    if scripts_dir.is_dir():
        for script in scripts_dir.glob("*qnx*"):
            return True
    return False


def _detect_build_system(root: Path) -> str:
    return "Bazel" if (root / "MODULE.bazel").is_file() else "Unknown"


def _detect_docs_system(readme_text: str, root: Path) -> str:
    if (root / "docs" / "conf.py").is_file():
        return "Sphinx"
    lowered = readme_text.lower()
    if "doxygen" in lowered:
        return "Doxygen"
    if "mdbook" in lowered:
        return "mdBook"
    return "Unknown"


def discover_repository(root: Path, name: str | None = None) -> RepositoryContext:
    """Auto-detect repository metadata from MODULE.bazel, project_config.bzl, README.md."""
    module_bazel_text = _read(root / "MODULE.bazel")
    project_config_text = _read(root / "project_config.bzl")
    readme_text = _read(root / "README.md")

    declared_languages = _detect_declared_languages(project_config_text)
    languages = _detect_languages(module_bazel_text, declared_languages)
    toolchains = _detect_toolchains(module_bazel_text)
    if _detect_qnx(root, module_bazel_text) and "qnx" not in toolchains:
        toolchains.append("qnx")

    return RepositoryContext(
        name=name or root.name,
        asil=_detect_asil(project_config_text),
        languages=languages,
        toolchains=toolchains,
        build_system=_detect_build_system(root),
        docs_system=_detect_docs_system(readme_text, root),
    )
