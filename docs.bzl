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

"""Repository-local compatibility wrapper for SCORE docs-as-code.

The upstream macro does not currently support ``source_dir = "."``. Delegate
all normal cases to upstream and keep only the root-layout workaround here.
"""

load("@module_template_docs_hub_env//:requirements.bzl", "all_requirements")
load("@rules_python//python:defs.bzl", "py_binary")
load("@rules_python//sphinxdocs:sphinx.bzl", "sphinx_build_binary", "sphinx_docs")
load("@score_docs_as_code//:docs.bzl", upstream_docs = "docs")
load("@score_tooling//:defs.bzl", "score_virtualenv")
load("@score_tooling//bazel/rules/rules_score:rules_score.bzl", "sphinx_module")

_INCREMENTAL_PY = "@score_docs_as_code//src:incremental.py"
_ROOT_DOCS_GLOBS = [
    "**/*.png",
    "**/*.svg",
    "**/*.md",
    "**/*.rst",
    "**/*.html",
    "**/*.css",
    "**/*.puml",
    "**/*.need",
    "**/*.yaml",
    "**/*.json",
    "**/*.csv",
    "**/*.inc",
    "more_docs/**/*.rst",
]
_ROOT_DOCS_EXCLUDES = [
    ".git/**",
    ".pytest_cache/**",
    ".ruff_cache/**",
    ".venv_docs/**",
    "_build/**",
    "bazel-*/**",
]
_DOCS_VARIANTS = [
    ("docs", "incremental", "sourcelinks_json", "Build documentation:\nbazel run //:docs", False),
    ("docs_combo", "incremental", "merged_sourcelinks", "Build full documentation with all dependencies:\nbazel run //:docs_combo", True),
    ("docs_link_check", "linkcheck", "sourcelinks_json", "Verify Links inside Documentation:\nbazel run //:link_check\n (Note: this could take a long time)", False),
    ("docs_check", "check", "sourcelinks_json", "Verify documentation:\nbazel run //:docs_check", False),
    ("live_preview", "live_preview", "sourcelinks_json", "Live preview documentation in the browser:\nbazel run //:live_preview", False),
    ("live_preview_combo_experimental", "live_preview", "merged_sourcelinks", "Live preview full documentation with all dependencies in the browser:\nbazel run //:live_preview_combo_experimental", True),
]

def _rewrite_targets(labels, old_suffix, new_suffix):
    out = []
    for x in labels:
        s = str(x)
        if s.endswith(old_suffix):
            out.append(s.replace(old_suffix, new_suffix))
        else:
            out.append(s)
    return out

def _merge_sourcelinks(name, sourcelinks, known_good = None):
    extra_srcs = []
    known_good_arg = ""
    if known_good != None:
        extra_srcs = [known_good]
        known_good_arg = "--known_good $(location %s)" % known_good

    native.genrule(
        name = name,
        srcs = sourcelinks + extra_srcs,
        outs = [name + ".json"],
        cmd = """
        $(location @score_docs_as_code//scripts_bazel:merge_sourcelinks) \
            --output $@ \
            {known_good_arg} \
            $(SRCS)
        """.format(known_good_arg = known_good_arg),
        tools = ["@score_docs_as_code//scripts_bazel:merge_sourcelinks"],
    )

def _missing_requirements(deps):
    found = []
    missing = []

    def _target_to_packagename(target):
        return target.split("/")[-1].split(":")[0]

    all_packages = [_target_to_packagename(pkg) for pkg in all_requirements]

    def _find(pkg):
        for dep in deps:
            if _target_to_packagename(dep) == pkg:
                return True
        return False

    for pkg in all_packages:
        if _find(pkg):
            found.append(pkg)
        else:
            missing.append(pkg)
    if len(missing) == len(all_requirements):
        return all_requirements
    if len(missing) == 0:
        return []
    if len(found) > 0:
        fail(
            "Some docs-as-code dependencies are in deps: " + ", ".join(found) +
            "\n   ... but others are missing: " + ", ".join(missing) +
            "\nInconsistent deps for docs(): either include all dependencies or none of them.",
        )
    fail("This case should be unreachable?!")

def _add_docs_binary(name, action, sourcelinks_target, help_text, use_combo_data, docs_data, combo_data, deps, known_good = None):
    env = {
        "ACTION": action,
        "SOURCE_DIRECTORY": ".",
        "DATA": str(combo_data if use_combo_data else docs_data),
        "SCORE_SOURCELINKS": "bazel-bin/" + sourcelinks_target + ".json",
    }
    if known_good:
        env["KNOWN_GOOD_JSON"] = "$(location " + known_good + ")"

    py_binary(
        name = name,
        tags = ["cli_help=" + help_text],
        main = _INCREMENTAL_PY,
        srcs = [_INCREMENTAL_PY],
        data = combo_data if use_combo_data else docs_data,
        deps = deps,
        env = env,
    )

def _sourcelinks_json(name, srcs):
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [name + ".json"],
        cmd = """
        $(location @score_docs_as_code//scripts_bazel:generate_sourcelinks) \
            --output $@ \
            $(SRCS)
        """,
        tools = ["@score_docs_as_code//scripts_bazel:generate_sourcelinks"],
        visibility = ["//visibility:public"],
    )

def _docs_from_repo_root(data, deps, scan_code, known_good):
    module_deps = deps
    deps = deps + _missing_requirements(deps) + [
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
        srcs = native.glob(_ROOT_DOCS_GLOBS, exclude = _ROOT_DOCS_EXCLUDES, allow_empty = True),
        visibility = ["//visibility:public"],
    )

    _sourcelinks_json(name = "sourcelinks_json", srcs = scan_code)
    data_with_docs_sources = _rewrite_targets(data, "//:needs_json", "//:docs_sources")
    combo_sourcelinks = _rewrite_targets(data, "//:needs_json", "//:sourcelinks_json")
    _merge_sourcelinks(name = "merged_sourcelinks", sourcelinks = [":sourcelinks_json"] + combo_sourcelinks, known_good = known_good)

    docs_data = data + [":sourcelinks_json"]
    combo_data = data_with_docs_sources + [":merged_sourcelinks"]
    if known_good:
        docs_data.append(known_good)
        combo_data.append(known_good)

    for name, action, sourcelinks_target, help_text, use_combo_data in _DOCS_VARIANTS:
        _add_docs_binary(name, action, sourcelinks_target, help_text, use_combo_data, docs_data, combo_data, deps, known_good)

    native.alias(
        name = "docs_combo_experimental",
        actual = ":docs_combo",
        deprecation = "Target '//:docs_combo_experimental' is deprecated. Use '//:docs_combo' instead.",
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
        config = ":conf.py",
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
        allow_persistent_workers = False,
    )

    sphinx_module(
        name = native.module_name() + "_module",
        srcs = [":docs_sources"],
        index = "docs/index.rst",
        sphinx = "@score_tooling//bazel/rules/rules_score:score_build",
        deps = module_deps,
        visibility = ["//visibility:public"],
    )

def docs(source_dir = "docs", data = [], deps = [], scan_code = [], known_good = None):
    """Creates all targets related to documentation."""

    if native.package_name() != "":
        fail("docs() must be called from the root package. Current package: " + native.package_name())

    if source_dir != ".":
        upstream_docs(
            source_dir = source_dir,
            data = data,
            deps = deps,
            scan_code = scan_code,
            known_good = known_good,
        )
        return

    _docs_from_repo_root(data = data, deps = deps, scan_code = scan_code, known_good = known_good)