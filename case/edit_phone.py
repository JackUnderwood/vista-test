__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.expand_ribbon import ExpandRibbon


class EditPhone(UI):
    License()
    Checklist()
    ExpandRibbon()

    runtime = {
        'phone': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div[1]/a[4]/i',
        ),
        'editPhone': (
            'Click',
            '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[14]/a/i'
        ),
        'revisePhone': ('Type', '#phone', '8012251155'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = 'Phone saved!'
    process = UI()
    process.update(runtime)
    order = ('phone', 'editPhone', 'revisePhone', 'save')
    process.execute(order)
    process.results(expected, 'toast-container', 8)
    process.wait(2)
    process.teardown()
