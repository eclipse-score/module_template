import unittest

from tools.onboarding.state_machine import OnboardingStateMachine, State


class TestOnboardingStateMachine(unittest.TestCase):
    def test_linear_flow_reaches_summary(self) -> None:
        machine = OnboardingStateMachine()
        expected = [
            State.CONTRIBUTOR_CHECK,
            State.ROLE_DETECTION,
            State.REPOSITORY_DISCOVERY,
            State.TECHNOLOGY_DISCOVERY,
            State.CONTRIBUTION_SELECTION,
            State.WORKFLOW_STYLE,
            State.WORKFLOW_FRAMEWORK,
            State.SUMMARY,
        ]
        for state in expected:
            self.assertEqual(machine.advance(), state)

    def test_summary_blocks_without_confirmation(self) -> None:
        machine = OnboardingStateMachine()
        for _ in range(8):
            machine.advance()
        self.assertEqual(machine.state, State.SUMMARY)
        machine.advance()
        self.assertEqual(machine.state, State.SUMMARY)
        self.assertFalse(machine.is_done())

    def test_summary_advances_when_confirmed(self) -> None:
        machine = OnboardingStateMachine()
        for _ in range(8):
            machine.advance()
        machine.data["summary_confirmed"] = True
        machine.advance()
        self.assertEqual(machine.state, State.READY_FOR_HANDOFF)
        self.assertTrue(machine.is_done())


if __name__ == "__main__":
    unittest.main()
