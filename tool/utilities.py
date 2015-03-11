"""
Utilities module used for a variety of functions
Provides global constants
"""
__author__ = 'John Underwood'
import configparser

CONFIG_FILE = 'config.ini'


def get_configurations():
    config = configparser.ConfigParser()
    config.sections()
    config.read(CONFIG_FILE)
    return config