Simple logger factory
=============================
This is the simple utility tool to help create the python logger. 
The logger can be configured by a pass in config file. 
If not it'll create the default logger. The log level then be controled by LOGLEVEL env variable. If the env variable is not set, the default level is INFO


Install
-------------

.. code-block:: bash

    $ pip install logger_factory

    
Usage
=====
Default logger:
.. code-block:: python
    from logger_factory import create_logger

    logger = create_logger("mylogger")
    logger.info("hello world")

Config via config.ini file:
.. code-block:: python
    from logger_factory import create_logger

    logger = create_logger("mylogger", "config.ini")
    logger.info("hello world")

