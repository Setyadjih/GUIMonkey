import datetime
from pathlib import Path
import tempfile
import logging
import sys

from rich.logging import RichHandler

LOGGER_FORMAT = '%(asctime)s - ' \
                '%(module)s.%(funcName)s - ' \
                '(%(levelname)s): %(message)s'
FORMATTER = logging.Formatter(LOGGER_FORMAT)


def get_console_handler():
    """Get the console log handler

    :rtype: logging.StreamHandler
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(file_name):
    """Get the file log handler

    :rtype: logging.StreamHandler
    """
    # set log path to temp location
    # this path resolve to something like this:
    # C:\Users\<USER_NAME>\AppData\Local\Temp\_LOG
    log_temp_location_path = Path(tempfile.gettempdir()).joinpath("_LOG")
    if not log_temp_location_path.exists():
        log_temp_location_path.mkdir(parents=True, exist_ok=True)

    today = str(datetime.date.today())
    log_file = log_temp_location_path.joinpath(f"{file_name}_{today}.log")

    file_handler = logging.FileHandler(log_file.as_posix())
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(name=__name__):
    """get the logging handler for the application. Default to the __name__

    :param logger_name: name of logging handler
    :return: logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # logger.addHandler(get_console_handler())
    logger.addHandler(RichHandler())
    logger.addHandler(get_file_handler(name))
    logger.propagate = False
    return logger
