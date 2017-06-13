__author__ = 'John Underwood'
"""This module is specific to the results table inside Manage Job Posts page.
"""


def find_valid_rows(process, class_name):
    """
    Get the available job rows that have been approved and meets all validations.
    (The 'fa-ban' icon is not visible.)
    :param process: UI class instance
    :param class_name: the class name
    :return: list - a list of valid job numbers
    """
    valid_rows = []
    rows = process.find_elements_by_class_name(class_name)
    for row in rows:
        # source = row.get_attribute('innerHTML')
        ele = row.find_element_by_xpath('./td[5]/i[2]')
        result = str(ele.get_attribute('class'))  # 'fa fa-ban jobFault'
        if 'jobFault' not in result:
            row_id = row.find_element_by_xpath('./td[1]').text
            valid_rows.append(row_id)

    return valid_rows


def find_rows(process, row_class_name, locator, name):
    """
    Find a series of rows within the result-target table body
    :param process: The UI driver
    :param row_class_name: The rows' class name
    :param locator: The xpath selector
    :param name: Name of the attribute/property to retrieve.
    :return: a list of tuples, i.e. [('id_12345', 'yes'), ('id_54321`, 'no'), ..]
    Usage:
    find_rows(process, 'expandable-row', ready_to_post_locator, 'innerHTML')
    """
    valid_rows = []
    table = process.find_element('//*[@id="result-target"]/tbody')
    rows = table.find_elements_by_class_name(row_class_name)
    for row in rows:
        row_id = row.get_attribute('id')
        ele = row.find_element_by_xpath(locator)
        value = ele.get_attribute(name)
        valid_rows.append((row_id, value))

    return valid_rows


def get_row_numbers(process):
    trs = process.find_elements('//*[@id="result-target"]/tbody/tr')
    rows = [row.find_element_by_xpath('./td[1]').text for row in trs]
    return rows


def get_class_attribute(process, locator):
    class_attr = process.spy(locator, 'class')
    class_attr = class_attr.strip()
    return class_attr


def get_color(rgb):
    import re

    res = re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+)', rgb).group()
    r, g, b = [int(s) for s in re.findall('\\d+', res)]
    hex_color = '#%02x%02x%02x' % (r, g, b)
    return hex_color


def get_job_status(class_attribute):
    status = None
    if "approved" in class_attribute:
        status = "approved"
    elif "ready" in class_attribute:
        status = "ready"
    elif "nopost" in class_attribute:
        status = "nopost"
    elif "rejected" in class_attribute:
        status = "rejected"
    else:
        pass
    return status
