from ui import UI
from tool.prerequisite.physical_address import PhysicalAddress
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.checklist_send_corr import ChecklistSendCorr
from tool.ui_utilities import get_list_of_option_elements
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


def get_row_index(process, locator, pattern):
    """
    Returns the HTML table's "one-based" index number
    :param process: UI object
    :param locator: string - a selector type, i.e. xpath, id, class, etc.
    :param pattern: string - the pattern to look for
    :return: number - the index number
    """
    element = process.find_element(locator)
    data = element.text
    # 'Home 33 Eaton Street West Haven CT 06516 N Y Other\n
    #  Work (2017) 2134 La Porte Rd 2134 La Porte Rd Waterloo IA 50702 N N Work'
    rows = data.split('\n')
    index = None
    for i, value in enumerate(rows):
        # pattern, e.g. 'Work (2017)
        if pattern in value:
            index = i+1  # html uses 'one' based indexes
            break
    return index


class DeliveryMethod(UI):
    """
    Uses the TestRail test case:
     C2766 - Delete address inside Delivery Method

    Prerequisite: Create a throw-away address for a provider
    1a - Click on a provider's name inside one of the License Request rows
    1b - Click on the Send a Template Correspondence icon inside the ribbon
    1c - Click on one of the correspondence templates
    2a - Fill in all the available prompts
    2b - Add a recipient by clicking the Entity button
    2c - Type in the provider's name with a throw-away address;
         see above Preconditions; inside the mini Find..., and select the result
         from Results drop down
    3  - Click on the Physical Addresses' Manage Physical Addresses button
    4  - Click the Delete button on one of the throw-away addresses--trash icon
    5  - Click the Cancel button
    6  - Repeat previous step, click the Delete button on the throw-away address
    7  - Click the Confirm button to delete the address
         Note: assumes the prerequisite address will never be a default address
    8  - Click the Addresses drawer's Close button
    9a - Select an existing address (or addresses, if you want to test
         multiple selections)
    9b - Click the Select Delivery Method modal's Save button
    """
    res = []
    process = UI()
    License()
    checklist = Checklist()

    # Set the prerequisite
    override = {
        'entity': checklist.entity,
        'entityId': checklist.entity_id,
        'description': 'QA Delivery Method {}'.format(gen_key(4)),
        'addressType': 'Other',
        'address1': '2800 E Cottonwood Pkwy',
        'address2': 'Suite 400',
        'city': 'Cottonwood Heights',
        'state': 'Utah',
        'zipCode': '84121',
        'country': 'United States',
    }
    PhysicalAddress(override)  # Prerequisite
    process.refresh()

    ChecklistSendCorr()  # Step 1

    option = get_list_of_option_elements(process, '#license_id', '- Pending')
    runtime = {
        'license': ('Select', '//*[@id="license_id"]',
                    {'value': option[0][1], 'select_type': 'value'}),  # 2a
        'entity': ('Click', '//*[@id="add-recipient-container"]/span[1]'),  # 2b
        'find': ('Type', '<input>', 'n:{} id:{}'.
                 format(checklist.entity, checklist.entity_id)),  # 2c
        'select': ('Click', '//*[@item_id="{}"]'.format(checklist.entity_id)),
        'manageAddr': ('Click', '//*[@id="delivery-locations"]/form/div[1]/'
                                'div[2]/a/i'),
    }
    process.update(runtime)
    process.execute(('license', 'entity', 'find', 'select'))  # Step 2
    process.wait()

    process.execute(('manageAddr',))  # Step 3
    process.wait()

    index = get_row_index(process, '//*[@id="addressGrid_grid"]/tbody',
                          override['description'])
    process.update({
        'trashcan': ('Click', '//*[@id="addressGrid_grid"]/tbody/tr[{}]/'
                              'td[27]/a/i'.format(index,))
    })
    process.execute(('trashcan',))  # Step 4
    process.wait()

    # Get the random id and insert it into the xpath. Cancel
    delete_dialog_id = process.spy('//*[@for="delete_record"]', 'id')
    process.update({
        'cancel': ('Click', '//*[@id="{}"]/div/div/a[2]'.
                   format(delete_dialog_id,))
    })
    process.execute(('cancel',))
    actual = process.spy('//*[@id="addressGrid_grid"]/tbody/tr[{}]/td[3]'.
                         format(index,), 'innerHTML')
    res.append(process.compare(override['description'], actual))  # Step 5

    process.execute(('trashcan',))  # Step 6

    # Get the random id and insert it into the xpath. Confirm
    delete_dialog_id = process.spy('//*[@for="delete_record"]', 'id')
    process.update({
        'confirm': ('Click', '//*[@id="{}"]/div/div/a[1]'.
                    format(delete_dialog_id,))
    })
    process.execute(('confirm',))
    process.wait()
    res.append(process.results('Address deleted'))
    index = get_row_index(process, '//*[@id="addressGrid_grid"]/tbody',
                          override['description'])
    res.append(process.compare(None, index))  # Step 7

    process.update({
        'close': ('Click', '#addressGridClose'),
    })
    process.execute(('close',))
    process.wait()
    checkboxes = process.spy('//*[@id="delivery-locations"]/form/div[2]',
                             'innerHTML')
    res.append(process.compare(False,
                               override['description'] in checkboxes))  # Step 8

    # Select an address and close - Step 9
    process.update({
        'checkAddr': ('Click',
                      '//*[@id="delivery-locations"]/form/div[2]/p[1]/label'),
        'save': ('Click', '//*[@id="delivery-locations"]/form/div[8]/a[1]')
    })
    process.execute(('checkAddr', 'save'))
    send = process.spy('//*[@id="corr_send"]', 'class')
    res.append(process.compare(True, 'disabled' not in send,
                               message='"Send" button is active'))
    process.compare(True, all(res))
    process.wait()
    process.teardown()
