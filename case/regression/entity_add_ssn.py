__author__ = 'John Underwood'

import ui
from ui import UI
from tool.utilities import digits_only
from tool.generators.generator import gen_name


class EntityAddSsn(UI):
    """
    Regression test for story #102370974
    """
    ssn = '333-22-4444'
    full, first, last = gen_name()

    ui.log.info("First name: {0} & Last name: {1}".format(first, last,))
    runtime = {
        'find': ('Type', '#main_desc', full),
        'addNewEntity': (
            'Click',
            '/html/body/header/nav/div/ul[1]/li[4]/div/div/div[4]/div/div[1]/a'),
        'entityType': ('Select', '#entity_type', 'Physician'),
        'firstName': ('Type', '#entity_first_name', first),
        'lastName': ('Type', '#entity_name', last),
        'ssn': ('Type', '#ssn', digits_only(ssn)),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[3]/a[1]'),
        'addressCheck': ('Click', 'ci.fa.fa-save.left'),
        'select': ('Click', '#user_name'),
        'editEntity': (
            'Click', '//*[@id="ribbon_form"]/ul/li/div[2]/div[1]/div[6]/a'),
    }
    process = UI()
    process.update(runtime)
    order = ('find', 'addNewEntity', 'entityType', 'firstName',
             'lastName', 'ssn', 'save', )
    process.execute(order)
    process.wait(3)

    order = ('find', 'select', 'editEntity', )
    process.execute(order)
    actual = process.get('#ssn', 'value')
    ui.log.info('SSN value is {}'.
                format(actual if actual is not '' else 'None',))
    process.compare(ssn, actual)
    process.wait(5)
    process.teardown()
