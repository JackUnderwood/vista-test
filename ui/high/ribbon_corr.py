__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class SendCorrespond(UI):
    License()
    Checklist()

    runtime = {
        'expandRibbon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[1]/div/div[1]'
        ),
        'correspondIcon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div/a[1]/i'
        ),
        'selectTemplate': (
            'Click',
            '//*[@id="correspondenceChooser_form"]/p[2]/p[7]/a'
        ),
    }
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', 'correspondIcon', 'selectTemplate', )
    process.execute(order)
