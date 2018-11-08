import logging
import os
from logging.config import fileConfig

def create_logger(name, config_file=None):
    if (config_file not None) and (os.path.exists(os.path.abspath(config_file)):
        fileConfig('logging_config.ini')
    else:
        # default config
        logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"),
                    format="[%(asctime)s - %(filename)s:%(lineno)s - %(funcName)s()]-12s %(levelname)-8s %(message)s",
                    datefmt="%m-%d %H:%M")

    return logging.getLogger(name)