
__author__ = 'John Underwood'


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
