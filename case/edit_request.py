__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License


class EditRequest(UI):
    runtime = {
        'editRequest': (
            'Click',
            '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[15]/a/i'),
        'dateDesired': ('Type', '#date_desired', '10152016'),
        'dateCompleted': ('Type', '#completed_date', '10012016'),
        'notes': ('Type', '#note', 'Lorem ipsum dolor sit amet , mea ne ipsum'),
        'save': ('Click', '#license-change-confirm'),
    }
    expected = "Saved Request"
    License()
    process = UI()
    process.update(runtime)
    order = ('editRequest', 'dateDesired', 'dateCompleted', 'notes', 'save', )
    process.execute(order)
    process.results(expected, 'toast-container', 8)
    process.wait(3)
    process.teardown()
