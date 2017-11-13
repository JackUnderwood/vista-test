import ui
from ui import UI
from tool.generators.generator import gen_number
__author__ = 'John Underwood'


class Checklist(UI):
    """
    Pre-requirement: needs to start from Licensing landing page - execute
    low.license first.

    Test case goes into the Checklists.
    """
    entity = '__OVERRIDE__'
    entity_id = '__OVERRIDE__'

    def __init__(self, override=None):
        super().__init__()
        row = gen_number(50)

        runtime = {
            'rowNum': row,
            'showAll': ("Chain", [
                ('click', {
                    'on_element':
                        '//*[@id="checklist-form-container"]/div[1]/a'})]),
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
        self.entity = process.spy(
            '//*[@id="licenseRequestsGrid_grid"]/tbody/'
            'tr[{0}]/td[4]/a'.format(row, ), 'innerHTML')
        self.entity_id = process.spy(
            '//*[@id="licenseRequestsGrid_grid"]/tbody/'
            'tr[{0}]/td[3]'.format(row, ), 'innerHTML')
        ui.log.info("Grid's row number: {}".format(row,))
        ui.log.info('Provider name: {}'.format(self.entity,))
        ui.log.info('Provider id: {}'.format(self.entity_id,))

        process.update(runtime)
        order = ('provider', )
        process.execute(order)
