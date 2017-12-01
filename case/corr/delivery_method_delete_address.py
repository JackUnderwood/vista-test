from ui import UI
from tool.prerequisite.physical_address import PhysicalAddress
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.checklist_send_corr import ChecklistSendCorr
from tool.ui_utilities import get_option, get_all_options_from_select
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


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
    6  - Repeat previous step, click the Delete button on one of the
         throw-away addresses
    7  - Click the Confirm button to delete the address
    8  - Click the Addresses drawer's Close button
    9a - Select an existing address (or addresses, if you want to test
         multiple selections)
    9b - Click the Select Delivery Method modal's Save button
    """
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

    options = get_all_options_from_select(process, '#license_id')
    option = get_option(options, '- Pending')
    runtime = {
        'license': ('Select', '//*[@id="license_id"]', option),  # 2a
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

    # Step 4
    addr_table = process.spy('//*[@id="addressGrid_grid"]/tbody', 'innerHTML')
    process.wait()

