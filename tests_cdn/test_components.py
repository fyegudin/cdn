import logging

import allure
from cdn.components.caches.ec2_cache import EC2Cache
from cdn.components.caches.physical_cache import PhysicalCache
from cdn.components.monitor.monitor import Monitor
from cdn.components.clients.client import Client
from cdn.components.router.router import Router
from cdn.helper.logger import get_logger

logger = get_logger(__name__)


@allure.feature('Login')
@allure.story('Valid credentials')
def test_valid_login(caplog):
    caplog.set_level(logging.INFO)
    logging.info("This message will be included in the report: Valid credentials")
    # Test logic here
    assert True


@allure.feature('Login')
@allure.story('Invalid credentials')
def test_invalid_login():
    msg = "Starting test invalid login"
    with allure.step(msg):
        logger.info(msg)
    # Test logic here
    assert False


# test_cache_ec2.py
def test_cache_ec2_init():
    msg = "Starting test cache ec2 init"
    with allure.step(msg):
        logger.info(msg)
    cache = EC2Cache(instance_id="1234")
    assert isinstance(cache, EC2Cache)


# test_cache_physical.py
def test_cache_physical_init():
    msg = "Starting test cache physical init"
    with allure.step(msg):
        logger.info(msg)
    cache = PhysicalCache(ip_address="192.16.0.173")
    assert isinstance(cache, PhysicalCache)


# test_monitor.py
def test_monitor_init():
    msg = "Starting test monitor init"
    with allure.step(msg):
        logger.info(msg)
    monitor = Monitor(caches="any")
    assert isinstance(monitor, Monitor)


# test_router.py
def test_router_init():
    msg = "Starting test router init"
    with allure.step(msg):
        logger.info(msg)
    router = Router(caches="any")
    assert isinstance(router, Router)


# test_client.py
def test_client_init():
    msg = "Starting test client init"
    with allure.step(msg):
        logger.info(msg)
    client = Client(router_url="any")
    assert isinstance(client, Client)
