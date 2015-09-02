__author__ = 'John Underwood'

import ui
from ui import UI
from tool.utilities import digits_only


class EntityAddSsn(UI):
    """
    Regression test for story #102370974
    """
    ssn = '123-12-1234'
    runtime = {
        'find': ('Type', '#main_desc', 'bert'),
        'addNewEntity': (
            'Click',
            '/html/body/header/nav/div/ul[1]/li[4]/div/div/div[4]/div/div[1]/a'),
        'entityType': ('Select', '#entity_type', 'Physician'),
        'firstName': ('Type', '#entity_first_name', 'James'),
        'lastName': ('Type', '#entity_name', 'Kramer'),
        'ssn': ('Type', '#ssn', digits_only(ssn)),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[3]/a[1]'),
    }

    process = UI()
    process.update(runtime)
    order = ('find', 'addNewEntity', 'entityType', 'firstName',
             'lastName', 'ssn')
    process.execute(order)
    process.wait(3)
    actual = process.get('#ssn', 'value')
    ui.log.info('SSN value is {}'.format(actual,))
    process.compare(ssn, actual)
    process.wait(5)
    process.teardown()
