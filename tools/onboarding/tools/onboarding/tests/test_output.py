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

import json
import tempfile
import unittest
from pathlib import Path

from tools.onboarding.models import RepositoryContext
from tools.onboarding.output import build_context_envelope, write_context


class TestOutput(unittest.TestCase):
    def test_build_context_envelope_shape(self) -> None:
        repository = RepositoryContext(name="module_template", asil="QM", languages=["rust"])
        envelope = build_context_envelope(
            repository=repository,
            role="developer",
            contribution_type="bug_fix",
            workflow="sdlc_harness",
            workflow_reason="Bug fixes benefit from SDLC Harness traceability.",
        )
        data = envelope.to_dict()
        self.assertEqual(data["repository"]["name"], "module_template")
        self.assertEqual(data["contributor"]["role"], "developer")
        self.assertEqual(data["work_item"]["type"], "bug_fix")
        self.assertEqual(data["workflow"]["selected"], "sdlc_harness")

    def test_write_context_creates_single_file(self) -> None:
        repository = RepositoryContext(name="module_template", asil="QM")
        envelope = build_context_envelope(
            repository=repository, role="developer", contribution_type="bug_fix", workflow="sdlc_harness"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = write_context(envelope, root)
            self.assertEqual(path, root / ".onboarding" / "context.json")
            self.assertTrue(path.is_file())
            written = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(written["workflow"]["selected"], "sdlc_harness")


if __name__ == "__main__":
    unittest.main()
