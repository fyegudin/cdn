import abc
import allure
import json
import requests

from cdn.components.clients.client import Client

from cdn.helper.logger import get_logger

logger = get_logger(__name__)


class ClientTestCase(metaclass=abc.ABCMeta):
    ADMIN_USERNAME = "cdn"
    ADMIN_PASSWORD = "cdn"

    def __init__(self,
                 url: str,
                 description: str,
                 reported_issues: list,
                 expected_results: dict,
                 *args, **kwargs) -> None:
        self.client = Client(router_url=url)

        self.test_description = description
        self.reported_issues = {issue.split('/')[-1]: issue for issue in reported_issues}
        self.expected_results = expected_results

        self.enter_ok = True

    def _prepare_client(self):
        try:
            self.client.exit()
            self.client.start()
        except Exception as e:
            logger.error(f"Failed to exit/start agent {e}")
            self.enter_ok = False

    def __enter__(self):
        try:
            msg = "Client TearUp "
            with allure.step(msg):
                logger.info(msg)
                self._prepare_client()
        except Exception as e:
            logger.error(f"ClientTestCase TearUp failed with the following exception: {e}")
            self.enter_ok = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        msg = "Tear Down ClientTestCase"
        with allure.step(msg):
            logger.info(msg)
            self.client.exit()

    @staticmethod
    def attach_request(request: dict) -> None:
        allure.attach(json.dumps(request, indent=2),
                      "Request",
                      attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_response(response: requests.Response) -> None:
        try:
            response_data = json.dumps(response.json(), indent=2)
            attachment_type = allure.attachment_type.JSON
        except Exception:
            response_data = str(response.text)
            attachment_type = allure.attachment_type.TEXT

        allure.attach(response_data,
                      "Response",
                      attachment_type=attachment_type)

    @property
    @abc.abstractmethod
    def description(self) -> str:
        pass
