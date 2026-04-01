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

from pathlib import Path

_DOCS_CONF = Path(__file__).resolve().parent / "docs" / "conf.py"
exec(compile(_DOCS_CONF.read_text(encoding="utf-8"), str(_DOCS_CONF), "exec"), globals())

exclude_patterns = list(exclude_patterns) + [
    "_build",
    "docs/index.rst",
    "docs/score/**",
]
templates_path = [str(Path("docs") / path) for path in templates_path]