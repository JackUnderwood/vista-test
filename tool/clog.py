__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back

CRITICAL = 50
ERROR = 40
WARNING = 30
TRACE = 25  # TODO: Add another level
INFO = 20
DEBUG = 10


class CLog(logging.Logger):
    """
    The Test Framework logger - Color LOG (CLOG)
    The purpose of this derived class is to add coloration to logs and
    add new debug levels. Also, provides options to write to file and
    display on the console simultaneously.
    """
    def __init__(self, name="VTF", level=logging.INFO, log_name="vtf"):
        init()  # initialize colorama
        logging.Logger.__init__(self, name, level)
        logging.basicConfig(level=level)
        self.logger = logging.getLogger(log_name)

    def debug(self, msg, *args, **kwargs):
        msg = Fore.GREEN + msg + Fore.RESET
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = Fore.CYAN + msg + Fore.RESET
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = Fore.YELLOW + msg + Fore.RESET
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = Fore.RED + msg + Fore.RESET
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = Fore.RED + Back.YELLOW + msg + Fore.RESET + Back.RESET
        self.logger.exception(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = Fore.WHITE + Back.RED + msg + Fore.RESET + Back.RESET
        self.logger.critical(msg, *args, **kwargs)