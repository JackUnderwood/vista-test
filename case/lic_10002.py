__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License


class Lic10001(UI):
    runtime = {
        'provider': (
            'Click',
            '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[8]/a',
        ),
    }
    License()
    process = UI()
    process.update(runtime)
    order = ('provider', )
    process.execute(order)
    process.wait(5)
    process.teardown()
