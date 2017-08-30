from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
__author__ = 'John Underwood'


class EditEntity(UI):
    """
    TODO: Need to check for address validation
    """
    License()
    Checklist({'rowNum': '6'})

    runtime = {
        'editEntity': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[1]/div[6]/a[1]'
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
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Other'),
        'save': ('Click', '#save-n-check'),
        # 'expectedError': (
        #     'Wait', '//*[@id="toast-container"]/div', {'wait_time': 8}),
        # 123 N Main St, Lindon, UT 84042
        # has a class called "toast red"
    }
    process = UI()
    expected = 'Saved information'
    process.update(runtime)
    order = ('editEntity', 'addressDescription', 'addressType',
             #  'address', 'city', 'state', 'zipCode',
             'emailType', 'save', )  # 'expectedError'
    process.execute(order)
    validation_check = process.get_source()
    if "address check" in validation_check:
        process.update({
            'saveAsIs': ('Click', 'css=.waves-effect.waves-light.btn.'
                                  'right-align.modal-action.modal-close')
        })
        process.execute(('saveAsIs', ))
    process.wait()
    process.results(expected, locator='toast-container', wait_time=20)
    process.wait()
    process.teardown()
