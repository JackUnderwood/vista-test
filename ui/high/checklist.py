__author__ = 'John Underwood'
from ui import UI


class Checklist(UI):
    """
    Pre-requirement: needs to display Licensing landing page - execute
    low.license first.

    Test case goes into the Checklists.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'showAll': ('Click', '//*[@id="checklist-form-container"]/div[1]/a'),
            'rowNum': '1',  # Clicks on grids first row.
            'provider': (
                'Click',
                '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[&rowNum;]/td[8]/a',
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('showAll', 'provider', )
        process.execute(order)
