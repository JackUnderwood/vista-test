__author__ = 'John Underwood'
"""
Utilities module used for a variety of general functions
Provides global constants & variables
"""
import configparser
import time
import re

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


def todays_date():
    """
    Get today's date in the DDMMYYYY format
    :return: e.g. '08202015'
    """
    return time.strftime("%d%m%Y")


def todays_time():
    """
    Get the current time in the HH:MM <period> format
    Note: AM or PM is the 'period' of time in the day
    :return: e.g. '10:27 AM'
    """
    return time.strftime("%I:%M %p")


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
