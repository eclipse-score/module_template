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

load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "onboarding_lib",
    srcs = [
        "__init__.py",
        "cli.py",
        "discovery.py",
        "models.py",
        "output.py",
        "recommendation.py",
        "state_machine.py",
        "validators.py",
    ],
    data = [
        "agent/onboarding.agent.yaml",
        "agent/onboarding.skill.md",
        "schemas/context.schema.json",
    ],
    imports = ["../.."],
)

py_binary(
    name = "sdlc",
    srcs = ["__main__.py"],
    main = "__main__.py",
    deps = [":onboarding_lib"],
)

[
    py_test(
        name = test_file.removesuffix(".py"),
        srcs = [test_file],
        deps = [":onboarding_lib"],
    )
    for test_file in [
        "tests/test_state_machine.py",
        "tests/test_discovery.py",
        "tests/test_recommendation.py",
        "tests/test_output.py",
    ]
]
