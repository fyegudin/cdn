import logging
import os
import sys

FORMATTER = logging.Formatter("%(asctime)s - %(filename)s - %(threadName)s - "
                              "%(funcName)s - %(lineno)d - %(levelname)s - %(message)s")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)

    return console_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    log_level = os.environ.get("LOG_LEVEL", "DEBUG")
    logger.setLevel(getattr(logging, log_level))
    logger.addHandler(get_console_handler())
    logger.propagate = False

    return logger


def get_status():
    pass
