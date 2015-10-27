import ui
from ui import UI
__author__ = 'John Underwood'


class Checklist(UI):
    """
    Pre-requirement: needs to start from Licensing landing page - execute
    low.license first.

    Test case goes into the Checklists.
    """
    entity = '__OVERRIDE__'

    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'showAll': ('Click', '//*[@id="checklist-form-container"]/div[1]/a'),
            'rowNum': '1',
            'provider': (
                'Click',
                '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[&rowNum;]/td[4]/a',
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('showAll', )
        process.execute(order)

        row = process.runtime['rowNum']
        # Provides entity's name for derived classes
        self.entity = process.get(
            '//*[@id="licenseRequestsGrid_grid"]/tbody/tr['+row+']/td[4]/a',
            'innerHTML')

        process.update(runtime)
        order = ('provider', )
        process.execute(order)
