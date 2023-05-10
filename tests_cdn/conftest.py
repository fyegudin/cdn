import pytest
import configparser
import logging
from cdn.components.clients.client import Client


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.ini", help="Path to configuration file")


@pytest.fixture(scope="session")
def config(request):
    config_file = request.config.getoption("--config")
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


@pytest.fixture
def client(config):
    cache_type = config.get("CDN", "cache_type")
    return Client(cache_type)


@pytest.fixture(scope="session")
def logger(config):
    log_file = config.get("Logging", "log_file")
    log_level = config.get("Logging", "log_level")
    logging.basicConfig(filename=log_file, level=log_level)
    return logging.getLogger()
