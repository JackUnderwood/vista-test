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

        runtime = {  # Clicks on grids first row.
            'provider': (
                'Click',
                '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[8]/a',
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('provider', )
        process.execute(order)
