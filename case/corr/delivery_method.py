from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.checklist_send_corr import ChecklistSendCorr

__author__ = 'John Underwood'


def get_all_options_from_select(process):
    options = []
    elements = process.find_elements('#license_id')
    if elements[0].tag_name == 'select':
        options = elements[0].text.split('\n')
    return options


class DeliveryMethod(UI):
    """
    Use a specific provider 'Adelaide Viguri'
    """
    res = []
    # select = browser.find_element_by_id('license_id')
    # options = [x for x in select.find_elements_by_tag_name('option')]
    # for element in options:
    #    print element.get_attribute("value")
    # TODO: dynamically pull data from the screen
    data = {
        'providerRow': '3',
        'provider': 'Adelaide Viguri',
        'license': 'NJ - Permanent - 25MB09884600 - Active',
    }
    process = UI()
    License()
    Checklist({'rowNum': data['providerRow']})
    ChecklistSendCorr()
    # No 'runtime' elements have been executed yet, so we need to
    # check for the new window.
    process.check_for_new_window()
    # source = process.get_source()
    # s = process.spy('#correspond_form', 'innerHTML')
    options = get_all_options_from_select(process)
    res.append(process.is_available('#desc_provider_id'))
    runtime = {
        'license': ('Select', '#license_id', data['license']),
    }
    process.update(runtime)
    process.execute(('license',))
    process.wait()

    process.teardown()
