__author__ = 'John Underwood'
import logging

from colorama import init, Fore, Back


class VtfLog(logging):
    """
    The purpose of this derived class is to add coloration to logs and
    add new debug levels.
    """
    def __init__(self):
        init()  # initialize color scheme
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(name="vtf")
        self.logger.info('Start logging the Vista Testing Framework')
        pass

    def debug(self, msg, *args, **kwargs):
        msg = Fore.GREEN + msg + Fore.RESET
        super(VtfLog, self).debug(msg, *args, **kwargs)
        # self.logger.debug(Fore.GREEN + msg + Fore.RESET, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        msg = Fore.CYAN + msg + Fore.RESET
        super(VtfLog, self).info(msg, *args, **kwargs)
        # self.logger.debug(Fore.CYAN + msg + Fore.RESET, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        msg = Fore.YELLOW + msg + Fore.RESET
        super(VtfLog, self).debug(msg, *args, **kwargs)
        # self.logger.debug(Fore.YELLOW + msg + Fore.RESET, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        msg = Fore.RED + msg + Fore.RESET
        super(VtfLog, self).debug(msg, *args, **kwargs)
        # self.logger.debug(Fore.RED + msg + Fore.RESET, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        msg = Fore.RED + Back.YELLOW + msg + Fore.RESET + Back.RESET
        super(VtfLog, self).debug(msg, *args, **kwargs)
        # self.logger.debug(Fore.RED + Back.YELLOW + msg + Fore.RESET +
        #                  Back.RESET, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        msg = Fore.WHITE + Back.RED + msg + Fore.RESET + Back.RESET
        super(VtfLog, self).debug(msg, *args, **kwargs)
        # self.logger.debug(Fore.WHITE + Back.RED + msg + Fore.RESET +
        #                  Back.RESET, *args, **kwargs)