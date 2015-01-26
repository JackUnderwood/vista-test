__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back


class CLog(logging.Logger):
    """
    The Test Framework logger - Color LOG (CLOG)
    The purpose of this derived class is to add coloration to logs and
    add new debug levels. Also, provides options to write to file and
    display on the console simultaneously.
    """
    def __init__(self, name="VTF", level=logging.DEBUG):
        init()  # initialize colorama
        logging.Logger.__init__(self, name, level)
        self.log = logging.getLogger(name)

    def debug(self, msg, *args, **kwargs):
        msg = Fore.GREEN + msg + Fore.RESET
        self.log.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = Fore.CYAN + msg + Fore.RESET
        self.log.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = Fore.YELLOW + msg + Fore.RESET
        self.log.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = Fore.RED + msg + Fore.RESET
        self.log.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = Fore.RED + Back.YELLOW + msg + Fore.RESET + Back.RESET
        self.log.exception(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = Fore.WHITE + Back.RED + msg + Fore.RESET + Back.RESET
        self.log.critical(msg, *args, **kwargs)