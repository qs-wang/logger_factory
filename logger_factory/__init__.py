import logging
import os
from logging.config import fileConfig

def config_logger(config_file=None):
    if (config_file is not None):
        fileConfig('logging_config.ini', disable_existing_loggers=False)
    else:
        # default config
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                            format="[%(asctime)s - %(filename)s:%(lineno)s - %(funcName)s()]-12s %(levelname)-8s %(message)s",
                            datefmt="%m-%d %H:%M")


def create_logger(name):
    return logging.getLogger(name)
