__author__ = 'John Underwood'
"""
Utilities module used for a variety of functions
Provides global constants
"""
import configparser

CONFIG_FILE = 'config.ini'

# Set when 'pdf' is in the file's name, e.g. file_basic_pdf.py
is_pdf = False


def get_configurations(section, option):
    config = configparser.ConfigParser()
    config.sections()
    config.read(CONFIG_FILE)
    return config.get(section, option)