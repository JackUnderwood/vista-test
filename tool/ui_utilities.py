"""
This module is for access to elements inside the ui, and performing
specific actions on those elements, such as getting all available options
from a drop down list.
"""
import ui

__author__ = 'John Underwood'


def get_all_options_from_select(process, locator):
    """
    Retrieve all options from a select tag.
    :param process: UI object
    :param locator: string
    :return: list of strings
    """
    options = []
    elements = process.find_elements(locator)
    if elements[0].tag_name == 'select':
        options = elements[0].text.split('\n')
    return options


def get_option(options, partial):
    """
    Find an option that has the passed partial string.
    :param options: list of strings - options from a <select>
    :param partial: string - use a partial string to find the list's element
    :return: string - first possible option
    """
    it = filter(lambda option: partial in option, options)
    try:
        res = next(it)
    except StopIteration as si:
        res = ''
        ui.log.info('get_option() - no options for partial "{}" :: {}'.
                    format(partial, si))
    return res
