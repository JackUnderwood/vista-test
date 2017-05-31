
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
