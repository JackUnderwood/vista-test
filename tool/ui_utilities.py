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
    element = process.find_element(locator)
    if element.tag_name == 'select':
        options = element.text.split('\n')
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


def get_list_of_option_elements(process, locator, partial):
    """
    Returns a list of tuples; tuple format is (<option text>, <option value>)
    Each tuple's first element matches the passed in partial.
    :param process: ui object
    :param locator: string - i.e. xpath, css selector, etc.
    :param partial: string - e.g. ' - Pending'
    :return: list of tuples
    [('CA - Permanent -  - Pending', 640999),
     ('CT - Permanent - 41961 - Pending', 411330)]
    """
    values = []
    element = process.find_element(locator)
    options = [x for x in element.find_elements_by_tag_name("option")]
    for option in options:
        values.append((option.get_attribute("innerHTML"),
                       option.get_attribute("value")))
    option_items = [item for item in values if partial in item[0]]
    return option_items
