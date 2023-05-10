from cdn.core.test_actions.test_action import TestAction


class ClientProcessAction(TestAction):

    @property
    def action_type(self):
        return TestAction.action_type
