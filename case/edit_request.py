from ui import UI
from ui.low.license import License
from tool.utilities import get_configurations

__author__ = 'John Underwood'


class EditRequest(UI):
    """
    Edit a license request.
    """
    License()
    username = get_configurations('USER_IMPOSTOR', 'name')

    runtime = {
        'showAll': ('Click', '//*[@id="checklist-form-container"]/div[1]/a'),
        'editRequest': (  # clicks table's first row's Edit icon--pencil icon
            'Click',
            '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[16]/a[2]/i'),
        'licensor': ('Select', '#owner_id', username),
        'dateDesired': ('Type', '#date_desired', '10152016'),
        'dateReceived': ('Type', '#board_received_date', '10012016'),
        'notes': ('Type', '#note', 'Lorem ipsum dolor sit amet , mea ne ipsum'),
        'save': ('Click', '#license-change-confirm'),
    }
    expected = "Saved Request"
    process = UI()
    process.update(runtime)
    order = ('showAll', 'editRequest', 'licensor', 'dateDesired', 'dateReceived',
             'notes', 'save', )
    process.execute(order)
    process.results(expected, locator='toast-container', wait_time=8)
    process.wait(3)
    process.teardown()
