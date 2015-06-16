__author__ = 'John Underwood'
"""
Utilities module used for a variety of functions
Provides global constants
"""
import configparser

CONFIG_FILE = 'config.ini'


def get_configurations(section, option):
    config = configparser.ConfigParser()
    config.sections()
    config.read(CONFIG_FILE)
    return config.get(section, option)
