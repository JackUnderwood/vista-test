__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.expand_ribbon import ExpandRibbon


class EditEntity(UI):
    License()
    Checklist()
    ExpandRibbon()

    runtime = {
        'editEntity': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[2]/div[1]/div[6]/a[1]'
        ),
        'addressDescription': ('Type', '#address_description', 'Business'),
        'addressType': (
            'Select',
            '#address_correspondence_method_type_id',
            'Work'
        ),
        'address': ('Type', '#address_1', '123 N Main St'),
        'city': ('Type', '#city', 'Lindon'),
        'state': ('Select', '#state', 'Utah'),
        'zipCode': ('Type', '#zip_code', '84042'),
        'save': ('Click', '#save-n-check'),
        # 'expectedError': ('Wait', '//*[@id="toast-container"]/div', 10),
        # 123 N Main St, Lindon, UT 84042
        # has a class called "toast red"
    }
    expected = 'Saved information'
    process = UI()
    process.update(runtime)
    order = ('editEntity', 'addressDescription', 'addressType',
             'address', 'city', 'state', 'zipCode', 'save', )  # 'expectedError'
    process.execute(order)
    process.results(expected, 'toast-container', 5)
    process.wait(3)
    process.teardown()
