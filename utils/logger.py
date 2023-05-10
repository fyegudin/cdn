import logging

"""To collect the logs from all components, you can run the test suite and then inspect the log files (cache.log, 
monitor.log, router.log, client.log) for any errors or warnings. """

# Configure logging for the caches
cache_logger = logging.getLogger('cache')
cache_logger.setLevel(logging.DEBUG)
cache_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
cache_file_handler = logging.FileHandler('cache.log')
cache_file_handler.setLevel(logging.DEBUG)
cache_file_handler.setFormatter(cache_formatter)
cache_logger.addHandler(cache_file_handler)

# Configure logging for the monitor
monitor_logger = logging.getLogger('monitor')
monitor_logger.setLevel(logging.DEBUG)
monitor_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
monitor_file_handler = logging.FileHandler('monitor.log')
monitor_file_handler.setLevel(logging.DEBUG)
monitor_file_handler.setFormatter(monitor_formatter)
monitor_logger.addHandler(monitor_file_handler)

# Configure logging for the router
router_logger = logging.getLogger('router')
router_logger.setLevel(logging.DEBUG)
router_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
router_file_handler = logging.FileHandler('router.log')
router_file_handler.setLevel(logging.DEBUG)
router_file_handler.setFormatter(router_formatter)
router_logger.addHandler(router_file_handler)

# Configure logging for the client
client_logger = logging.getLogger('client')
client_logger.setLevel(logging.DEBUG)
client_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
client_file_handler = logging.FileHandler('client.log')
client_file_handler.setLevel(logging.DEBUG)
client_file_handler.setFormatter(client_formatter)
client_logger.addHandler(client_file_handler)

# Log some messages
cache_logger.info('Cache initialized')
monitor_logger.debug('Monitor started')
router_logger.error('Error in router')
client_logger.warning('Client request timed out')

