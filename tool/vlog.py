__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back
from selenium.webdriver.remote.remote_connection import LOGGER

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
TRACE = 15  # TODO: Add another level
DEBUG = 10


class VLog(logging.Logger):
    """
    The Test Framework logger - VISTA LOG (VLOG)
    The purpose of this derived class is to add coloration to logs and
    add new debug levels. TODO: Also, provides options to write to file and
    display on the console simultaneously.
    """
    def __init__(self, name="VTF", level=logging.INFO, log_name="vtf"):
        init()  # initialize colorama
        LOGGER.setLevel(logging.WARNING)  # for Selenium - prevent verbose
        logging.Logger.__init__(self, name, level)
        logging.basicConfig(filename='log/example.log', filemode='w',
                            level=level)  # filename is a placeholder JNU!!!

        # see https://docs.python.org/3.4/howto/logging-cookbook.html
        console = logging.StreamHandler()
        formatter = logging.Formatter('%(name)-8s: %(levelname)-9s:%(message)s')
        console.setFormatter(formatter)
        logging.getLogger(log_name).addHandler(console)
        self.logger = logging.getLogger(log_name)

    def debug(self, msg, *args, **kwargs):
        msg = " " + Fore.GREEN + msg + Fore.RESET
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = " " + Fore.CYAN + msg + Fore.RESET
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = " " + Fore.YELLOW + msg + Fore.RESET
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = " " + Fore.RED + msg + Fore.RESET
        self.logger.error(msg, *args, **kwargs)

    # def exception(self, msg, *args, **kwargs):  # Use error()
    #     msg = " " + Fore.RED + Back.YELLOW + msg + Back.RESET + Fore.RESET
    #     self.logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = " " + Fore.WHITE + Back.RED + msg + Back.RESET + Fore.RESET
        self.logger.critical(msg, *args, **kwargs)
