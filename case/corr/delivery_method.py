import re
from html.parser import HTMLParser

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.checklist_send_corr import ChecklistSendCorr

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


def find_email(string):
    # Find email address inside an innerHTML string.
    pattern = r'[A-Z0-9][A-Z0-9._%+-]*@(?:[A-Z0-9-]+\.)+[A-Z]{2,}'
    result = re.search(pattern, string, re.IGNORECASE)
    return True if result else False


class CountTopLevelDiv(HTMLParser):
    # Count the number of top level divs
    count = 0

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == 'item-id':
                self.count += 1


class DeliveryMethod(UI):
    """
    Uses the TestRail test case
    C123 - "Select delivery method for Provider Licensing"
    1 - Select License Renewal template
    2 - Select a Provider License
    3 - Click on the Entity button under Add Recipient(s) header
    4a- Click inside the Find... field and type in a search string,
      e.g. "Matt Lambert st:wv"
    4b- Click the Results item
    5 - Click the Cancel button
    6 - Click Select Delivery Method link
    7 - Click the Save button
    8 - Click a delivery method, e.g. ground
    9 - Click the Cancel button
    10- Click 'Select Delivery Method' again
    11- Click a delivery method
    12- Click the Save button
    13- Click the physical address, email address, or fax number
    14- Click a secondary item if available
    15- Click the Save button
    16- Click the X next to the entity's Find...
    """
    res = []
    process = UI()

    License()
    checklist = Checklist()
    expected = checklist.entity
    ChecklistSendCorr()  # Step 1
    # No 'runtime' elements have been executed yet, so we need to
    # check for the new window.
    process.check_for_new_window()
    actual = process.spy('#desc_provider_id', 'value')
    res.append(process.is_available('#desc_provider_id'))
    res.append(process.compare(expected, actual))
    if not all(res):
        ui.log.warning('INCOMPLETE TEST::unable to match provider name "{}"'.
                       format(expected,))
        process.teardown()
        quit()

    options = get_all_options_from_select(process, '#license_id')
    option = get_option(options, '- Pending')
    runtime = {
        'license': ('Select', '//*[@id="license_id"]', option)
    }
    process.update(runtime)
    process.execute(('license',))  # Step 2
    process.wait()

    # Before removal, need to shrink ckeditor.
    script = 'arguments[0].setAttribute("style","height:400px")'
    process.change_attribute('#cke_1_contents', script)

    process.update({
        'entity': ('Click', '//*[@id="add-recipient-container"]/span[1]'),
        'find': ('Type', '<input>', 'n:{} id:{}'.
                 format(checklist.entity, checklist.entity_id)),
        'select': ('Click', '//*[@item_id="{}"]'.format(checklist.entity_id))
    })
    process.execute(('entity', 'find', 'select'))  # Step 3, Step 4
    process.wait()
    process.update({
        'cancel': ('Click', '//*[@id="delivery-locations"]/form/div[8]/a[2]')
    })
    process.execute(('cancel',))  # Step 5
    process.wait()
    process.update({
        'reselect': ('Click', '.select-address')
    })
    process.execute(('reselect',))  # Step 6
    process.wait()
    save_class = process.spy(
        '//*[@id="delivery-locations"]/form/div[8]/a[1]', 'class')
    res.append(process.compare(True, ('disabled' in save_class)))  # Step 7
    process.update({
        'ground': ('Click', '//*[@id="delivery-locations"]/form/div[2]/p/label')
    })
    process.execute(('ground',))  # Step 8
    ground_class = process.spy('#ground_0', 'class')
    res.append(process.compare(True, ('selected' in ground_class)))  # checkbox
    save_class = process.spy(
        '//*[@id="delivery-locations"]/form/div[8]/a[1]', 'class')
    res.append(process.compare(True, ('disabled' not in save_class)))  # save
    process.execute(('cancel',))  # Step 9
    send_class = process.spy('#corr_send', 'class')
    res.append(process.compare(True, ('disabled' in send_class)))
    process.execute(('reselect',))  # Step 10
    ground_class = process.spy('#ground_0', 'class')
    res.append(process.compare(True, ('selected' not in ground_class)))
    process.execute(('ground',))  # Step 11
    process.wait()
    save_class = process.spy(  # check that Save is active
        '//*[@id="delivery-locations"]/form/div[8]/a[1]', 'class')
    res.append(process.compare(True, ('disabled' not in save_class)))
    process.update({
        'save': ('Click', '//*[@id="delivery-locations"]/form/div[8]/a[1]')
    })
    process.execute(('save',))  # Step 12
    send_class = process.spy('#corr_send', 'class')
    res.append(process.compare(True, ('disabled' not in send_class)))
    res.append(process.is_available('css=.waves-effect.waves-light.btn.'
                                    'btn-small'))

    process.update({  # Step 13
        'groundAddress': ('Click', 'css=.waves-effect.waves-light.btn.btn-small')
    })
    process.execute(('groundAddress',))
    process.wait()
    save_class = process.spy(  # check that Save is active
        '//*[@id="delivery-locations"]/form/div[8]/a[1]', 'class')
    res.append(process.compare(True, ('disabled' not in save_class)))
    ground_class = process.spy('#ground_0', 'class')
    res.append(process.compare(True, ('selected' in ground_class)))
    # Check to see if email address is available - Step 14.
    attr = process.spy(
        '//*[@id="delivery-locations"]/form/div[4]/div/div[4]/label',
        'innerHTML')
    found = find_email(attr)
    if not found:
        ui.log.warning('INCOMPLETE TEST::Delivery Method missing email::Step 14')
        process.teardown()
        quit()
    process.update({
        'emailTo': (
            'Click',
            '//*[@id="delivery-locations"]/form/div[4]/div/div[1]/label'),
    })
    process.execute(('emailTo',))
    selected = process.spy(  # check that previous address is still selected
        '#ground_0', 'class')
    res.append(process.compare(True, ('selected' in selected)))
    # Save the delivery methods - Step 15.
    process.execute(('save',))
    delivery_methods = process.spy('css=.select-address', 'innerHTML')
    parse = CountTopLevelDiv()
    parse.feed(delivery_methods)
    res.append(process.compare(2, parse.count))
    process.wait()
    process.update({
        'remove': ('Click', '//*[@id="add-recipient-container"]/div[2]/i')
    })
    process.execute(('remove',))
    res.append(process.is_available('css=.select-address'))
    process.compare(True, all(res))
    process.wait()
    process.teardown()
