# *******************************************************************************
# Copyright (c) 2025 Contributors to the Eclipse Foundation
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

load("@aspect_rules_py//py:defs.bzl", "py_binary")
load("@pip_process//:requirements.bzl", "all_requirements")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("@score_tooling//:defs.bzl", "score_virtualenv")

def _rewrite_needs_json_to_docs_sources(labels):
    """Replace '@repo//:needs_json' -> '@repo//:docs_sources' for every item."""
    out = []
    for x in labels:
        s = str(x)
        if s.endswith("//:needs_json"):
            out.append(s.replace("//:needs_json", "//:docs_sources"))
        else:
            out.append(s)
    return out

def _docs_glob_patterns(source_dir):
    prefixes = ["png", "svg", "md", "rst", "html", "css", "puml", "need", "yaml", "json", "csv", "inc"]

    if source_dir in ["", "."]:
        return ["**/*." + ext for ext in prefixes] + ["more_docs/**/*.rst"]

    return [source_dir + "/**/*." + ext for ext in prefixes] + ["more_docs/**/*.rst"]

def _config_label(source_dir):
    if source_dir in ["", "."]:
        return ":conf.py"
    return ":" + source_dir + "/conf.py"

def docs(source_dir = "docs", data = [], deps = []):
    """Creates all targets related to documentation."""

    call_path = native.package_name()

    if call_path != "":
        fail("docs() must be called from the root package. Current package: " + call_path)

    deps = deps + all_requirements + [
        "@score_docs_as_code//src:plantuml_for_python",
        "@score_docs_as_code//src/extensions/score_sphinx_bundle:score_sphinx_bundle",
    ]

    sphinx_build_binary(
        name = "sphinx_build",
        visibility = ["//visibility:private"],
        data = data,
        deps = deps,
    )

    native.filegroup(
        name = "docs_sources",
        srcs = native.glob(_docs_glob_patterns(source_dir), allow_empty = True),
        visibility = ["//visibility:public"],
    )

    data_with_docs_sources = _rewrite_needs_json_to_docs_sources(data)

    py_binary(
        name = "docs",
        tags = ["cli_help=Build documentation:\nbazel run //:docs"],
        srcs = ["@score_docs_as_code//src:incremental.py"],
        data = data,
        deps = deps,
        env = {
            "SOURCE_DIRECTORY": source_dir,
            "DATA": str(data),
            "ACTION": "incremental",
        },
    )

    native.alias(
        name = "docs_combo_experimental",
        actual = ":docs",
        visibility = ["//visibility:public"],
    )

    py_binary(
        name = "docs_check",
        tags = ["cli_help=Verify documentation:\nbazel run //:docs_check"],
        srcs = ["@score_docs_as_code//src:incremental.py"],
        data = data,
        deps = deps,
        env = {
            "SOURCE_DIRECTORY": source_dir,
            "DATA": str(data),
            "ACTION": "check",
        },
    )

    py_binary(
        name = "live_preview",
        tags = ["cli_help=Live preview documentation in the browser:\nbazel run //:live_preview"],
        srcs = ["@score_docs_as_code//src:incremental.py"],
        data = data,
        deps = deps,
        env = {
            "SOURCE_DIRECTORY": source_dir,
            "DATA": str(data),
            "ACTION": "live_preview",
        },
    )

    native.alias(
        name = "live_preview_combo_experimental",
        actual = ":live_preview",
        visibility = ["//visibility:public"],
    )

    score_virtualenv(
        name = "ide_support",
        tags = ["cli_help=Create virtual environment (.venv_docs) for documentation support:\nbazel run //:ide_support"],
        venv_name = ".venv_docs",
        reqs = deps,
        data = data,
    )

    sphinx_docs(
        name = "needs_json",
        srcs = [":docs_sources"],
        config = _config_label(source_dir),
        extra_opts = [
            "-W",
            "--keep-going",
            "-T",
            "--jobs",
            "auto",
            "--define=external_needs_source=" + str(data),
        ],
        formats = ["needs"],
        sphinx = ":sphinx_build",
        tools = data,
        visibility = ["//visibility:public"],
    )