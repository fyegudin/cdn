import allure
import re

from abstract_testcase import ClientTestCase
from cdn.helper.logger import get_status


class ClientStatusTestCase(ClientTestCase):
    def __init__(self, start_client: bool, url: str, description: str, reported_issues: list, expected_results: dict,
                 *args, **kwargs):
        super().__init__(url, description, reported_issues, expected_results, *args, **kwargs)
        self.start_client = start_client

    def __enter__(self) -> "ClientStatusTestCase":
        with allure.step("Tear Up ClientStatusTestCase"):
            if self.start_client:
                ClientTestCase.__enter__(self)

            return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        with allure.step("Tear Down ClientStatusTestCase"):
            if self.start_client:
                ClientTestCase.__exit__(self, exc_type, exc_val, exc_tb)

    @property
    def description(self) -> str:
        return f"""
        [Description]
        {self.test_description}

        [Test Flow]
        1. Start client: {self.start_client}
        2. Check client status


        [Expected results]
        Agent status: {self.expected_results["status"]}
        """

    def validate_status_response(self,
                                 actual_status: get_status,
                                 exception: Exception):
        if self.expected_results.get("agent_status_error_message", None):
            with allure.step("Validating error message"):
                actual_message = str(exception)
                expected_message = self.expected_results["agent_status_error_message"]
                assert expected_message in actual_message or \
                       re.match(expected_message, actual_message), \
                    f"Actual error message: '{actual_message}', " \
                    f"while expected error message: '{expected_message}'"
        else:
            expected_status = self.expected_results["status"]
            assert actual_status == expected_status, \
                f"Unexpected agent status: {actual_status}. Expected: {expected_status}"

    def run(self):
        try:
            actual_status = self.client.status()
            exception = None
        except Exception as e:
            actual_status = None
            exception = e

        self.validate_status_response(actual_status=actual_status,
                                      exception=exception)
