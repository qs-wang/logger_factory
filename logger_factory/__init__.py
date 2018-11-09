import logging
import os
from logging.config import fileConfig
from logging.config import dictConfig


def config_logger_with_dict(config_dict=dict(
    version=1,
    formatters={
        "f": {"format":
              "[%(asctime)s - %(filename)s:%(lineno)s - %(funcName)12s()] %(levelname)-8s %(message)s"}
    },
    datefmt="%m-%d %H:%M",
    handlers={
        "h": {"class": "logging.StreamHandler",
              "formatter": "f",
              "level": os.environ.get("LOGLEVEL", "INFO")}
    },
    root={
        "handlers": ["h"],
        "level": os.environ.get("LOGLEVEL", "INFO"),
    },
)):
        dictConfig(config_dict)



def config_logger_with_file(config_file=None):
    if (config_file is not None):
        fileConfig("logging_config.ini", disable_existing_loggers=False)
    else:
       config_logger_with_dict()


def config_logger(config_file=None):
    config_logger_with_file(config_file)

def create_logger(name):
    return logging.getLogger(name)
