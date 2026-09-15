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

import unittest

from tools.onboarding.recommendation import recommend_workflow, select_workflow


class TestRecommendation(unittest.TestCase):
    def test_bug_fix_recommends_sdlc_harness(self) -> None:
        workflow, _reason = recommend_workflow("bug_fix", asil="QM")
        self.assertEqual(workflow, "sdlc_harness")

    def test_improvement_recommends_speckit(self) -> None:
        workflow, _reason = recommend_workflow("improvement", asil="QM")
        self.assertEqual(workflow, "speckit")

    def test_poc_recommends_bmad(self) -> None:
        workflow, _reason = recommend_workflow("poc", asil="QM")
        self.assertEqual(workflow, "bmad")

    def test_documentation_recommends_traditional(self) -> None:
        workflow, _reason = recommend_workflow("documentation", asil="QM")
        self.assertEqual(workflow, "traditional")

    def test_non_qm_asil_forces_sdlc_harness(self) -> None:
        workflow, reason = recommend_workflow("documentation", asil="B")
        self.assertEqual(workflow, "sdlc_harness")
        self.assertIn("ASIL", reason)

    def test_user_override_is_honored(self) -> None:
        selected, overridden = select_workflow("sdlc_harness", user_choice="bmad")
        self.assertEqual(selected, "bmad")
        self.assertTrue(overridden)

    def test_accepting_recommendation_is_not_an_override(self) -> None:
        selected, overridden = select_workflow("sdlc_harness", user_choice=None)
        self.assertEqual(selected, "sdlc_harness")
        self.assertFalse(overridden)


if __name__ == "__main__":
    unittest.main()
