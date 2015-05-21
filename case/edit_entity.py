__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class EditEntity(UI):
    License()
    Checklist()

    runtime = {
        'expandRibbon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[1]/div/div[1]'
        ),
        'providerId': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[2]/div[1]/div[6]/a[1]'
        ),
        'addressDescription': ('Type', '#address_description', 'Business'),
        'addressType': (
            'Select',
            '#address_correspondence_method_type_id',
            'Work'
        ),
        'address': ('Type', '#address_1', '123 Main St.'),
        'city': ('Type', '#city', 'Geneva'),
        'state': ('Select', '#state', 'Utah'),
        'zipCode': ('Type', '#zip_code', '84056'),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[4]/a[1]')
    }
    expected = "Cannot Be Blank"
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', 'providerId', 'addressDescription',
             'addressType', 'address', 'city', 'state', 'zipCode', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(5)
    process.teardown()
