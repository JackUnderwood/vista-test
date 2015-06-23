__author__ = 'John Underwood'
"""
Utilities module used for a variety of functions
Provides global constants & variables
"""
import configparser

# Constants
CONFIG_FILE = 'config.ini'

# Global Variables
url = ''  # the testing url; either the test or the dev server


def get_configurations(section, option):
    config = configparser.ConfigParser()
    config.sections()
    config.read(CONFIG_FILE)
    return config.get(section, option)
