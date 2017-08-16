__author__ = 'John Underwood'
"""This module is specific to the results table inside Manage Job Posts page.
"""
error_msg = ""


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


def _click_fa_arrow_right(process):
    """
    Click the grid's right, forward arrow to see the grid's next page
    of results
    :return: Boolean
    """
    process.wait()
    forward_button_locator = ('css=#result-target>tfoot>tr>td:nth-child(2)>'
                              'i.fa.fa-arrow-right.fa-lg')
    forward_button = process.spy(forward_button_locator, 'class')
    if forward_button is None:
        return False  # already on the last page; no more pages available

    process.update({
        'faux_click': (  # use this click to give the nav tools focus
            'Click', '//*[@id="result-target"]/tfoot/tr/td[2]/span'),
        'fa_arrow_right': ('Click', forward_button_locator),
    })
    process.scroll_to_bottom_of_page()
    process.execute(('faux_click', 'fa_arrow_right',))
    process.wait()
    return True


def find_white_rows(process):
    """
    Find rows that have no status -- white rows
    :return: number or None
    """
    global error_msg
    locators = [
        './td/div/div[3]/div[2]/div[6]/div/div/div[2]/strong',  # don't post
        './td/div/div[3]/div[3]/div[6]/div/div/div/div[2]/strong',  # subtitle
        './td/div/div[3]/div[3]/div[7]/div/div/div/div[2]/strong'  # description
    ]

    while True:
        rows = find_rows(process, 'expandable-row', locators[0], 'innerHTML')
        if not check_valid(process, rows):
            return None

        valid_dont_post = [r[0][r[0].find('_') + 1:] for r in rows if 'No' in r]
        rows = find_rows(process, 'expandable-row', locators[1], 'innerHTML')
        msg_no_valid_rows = ('no valid rows available; database needs to '
                             'be refreshed ')
        if not check_valid(process, rows):
            if not _click_fa_arrow_right(process):
                error_msg += msg_no_valid_rows
                return None
            continue
        valid_subtitle = [r[0][r[0].find('_') + 1:] for r in rows if 'No' in r]
        valid_rows = (set(valid_dont_post)) & (set(valid_subtitle))

        if not check_valid(process, valid_rows):
            if not _click_fa_arrow_right(process):
                error_msg += msg_no_valid_rows
                return None
            continue

        return valid_rows.pop()


def find_ready_approved_rows(process):
    """
    Find rows that have Ready to Post checked and set as Approved--green rows
    :return: list - rows
    """
    locators = [
        './td/div/div[3]/div[2]/div[5]/div/div/div[2]/strong',  # ready to post
        './td/div/div[3]/div[2]/div[3]/div/div/div/div[2]/strong',  # approved
        './td/div/div[3]/div[3]/div[6]/div/div/div/div[2]/strong',  # subtitle
    ]
    while True:
        rows = find_rows(process, 'expandable-row', locators[0], 'innerHTML')
        if not check_valid(process, rows):
            return None

        valid_ready_to_post = [r[0][r[0].find('_') + 1:] for r in rows if
                               'Yes' in r]
        if not check_valid(process, valid_ready_to_post):
            if not _click_fa_arrow_right(process):
                return None
            continue

        valid_ready_to_post.sort(reverse=False)
        return valid_ready_to_post.pop()


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


def check_valid(process, rows_list):
    result = True
    if len(rows_list) < 1:
        process.compare(True, False, message="no valid rows available")
        result = False
    return result
