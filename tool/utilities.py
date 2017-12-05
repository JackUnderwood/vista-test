import configparser
import time
import re
import random

__author__ = 'John Underwood'
"""
Utilities module used for a variety of general functions
Provides global constants & variables
"""

# Constants
CONFIG_FILE = 'config.ini'

# Global Variables
url = ''  # the testing url; either the test or the dev server


def get_configurations(section, option):
    """
    Get a value from the configuration file, for example, CONFIG_FILE may have
    [DEFAULT]
    test_url = http://indytest/

    :param section: the ini's section, e.g. '[DEFAULT]'
    :param option: the section's option (or key), e.g. 'test_url'
    :return: the option's value, e.g. "http://indytest/"
    """
    config = configparser.ConfigParser()
    config.sections()
    config.read(CONFIG_FILE)
    return config.get(section, option)


def todays_date(style="%d%m%Y"):
    """
    Get today's date in the DDMMYYYY format
    :param style: string - default DDMMYYYY
    :return: e.g. '08202015'
    """
    return time.strftime(style)


def todays_time(style="%I:%M %p"):
    """
    Get the current time in the HH:MM <period> format
    Note: AM or PM is the 'period' of time in the day
    :param style: string - default HH:MM <period>
    :return: e.g. '10:27 AM'
    """
    return time.strftime(style)


def strip_alpha(value):
    """
    Takes in a string, strips all chars, except digits and decimal point
    :param value: string of characters, e.g. "$16,234.67"
    :return: float number, e.g. 16234.67
    """
    value = re.sub('[^0-9.]', '', value)
    return float(value)


def digits_only(value):
    """
    Takes in a string, and strips all chars except digits
    :param value: string of characters, e.g. "123-12-1234"
    :return: string, e.g. "123121234"
    """
    return re.sub('[^0-9]', '', value)


def test_for_symbols(replacer):
    """
    Test the string for the placeholder, which should be in the
    format: &placeholder;
    :param replacer: string
    :return: Boolean
    """
    if replacer.find('&') is -1:
        return False
    sub = replacer[replacer.find('&')+1:]
    if sub.find(';') is -1:
        return False
    return True


def get_random_value(values):
    """
    Get the a random value from the passed in list of values
    :param values: list of values
    :return: a single, random value
    """
    return random.choice(values)


def find_email(string):
    """
    Find email address inside an innerHTML string.
    :param string: string
    :return: Boolean
    """
    pattern = r'[A-Z0-9][A-Z0-9._%+-]*@(?:[A-Z0-9-]+\.)+[A-Z]{2,}'
    result = re.search(pattern, string, re.IGNORECASE)
    return True if result else False


def time_it(ndigits=7):
    """
    Decorator to time functions.
    :param ndigits: number - rounding precision
    :return: function
    """
    def decorate(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            return round(end - start, ndigits)
        return wrapper
    return decorate
