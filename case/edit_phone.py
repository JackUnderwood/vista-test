from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class EditPhone(UI):
    License()
    Checklist()

    runtime = {
        'phone': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]/i',
        ),
        'editPhone': (
            'Click',
            '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[15]/a/i'
        ),
        'revisePhone': ('Type', '#phone', '8012251155'),
        'phoneType': ('Select', '#phone_correspondence_method_type_id', 'Other'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = 'Phone number saved!'
    process = UI()
    process.update(runtime)
    order = ('phone', 'editPhone', 'revisePhone', 'phoneType', 'save')
    process.execute(order)
    process.results(expected, elem_id='toast-container', wait_time=8)
    process.wait(2)
    process.teardown()
