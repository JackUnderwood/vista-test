__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class NewLicense(UI):
    License()
    Checklist()
    UI().wait(4)

    runtime = {
        # 'tester': (
        #     'Click',
        #     '/html/body/header/nav/div/ul[2]/li[4]/a[1]/i'
        #     # //*[@id="ribbon_form"]/ul/li[2]/div[1]
        #     # //*[@id="ribbon_form"]/ul/li[1]/div[1]
        #     # //*[@id="ribbon_form"]/ul/li[1]
        # ),
        'expandRibbon': (
            'Click',
            # '//*[@id="ribbon_form"]/ul/li[1]'
            '/html/body/header/nav/div/ul[2]/li[4]/a[1]/i'
        )
    }
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', )
    process.execute(order)
    process.wait(5)
    process.teardown()
