__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back


class Flog(logging):
    """
    The test Framework LOGger (FLOG)
    The purpose of this derived class is to add coloration to logs and
    add new debug levels. Also, provides options to write to file and
    display on the console simultaneously.
    """
    def __init__(self, name="VTF", level=logging.NOTSET):
        init()  # initialize color scheme
        logging.basicConfig(level=logging.INFO)
        self.logger = super().getLogger(name, level)
        # self.logger = logging.getLogger(name, level)
        self.logger.info('Start logging the Vista Testing Framework')

    def debug(self, msg, *args, **kwargs):
        msg = Fore.GREEN + msg + Fore.RESET
        # super().debug(msg, *args, **kwargs) # a sample of super()
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = Fore.CYAN + msg + Fore.RESET
        self.logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = Fore.YELLOW + msg + Fore.RESET
        self.logger.debug(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = Fore.RED + msg + Fore.RESET
        self.logger.debug(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = Fore.RED + Back.YELLOW + msg + Fore.RESET + Back.RESET
        self.logger.debug(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = Fore.WHITE + Back.RED + msg + Fore.RESET + Back.RESET
        self.logger.debug(msg, *args, **kwargs)