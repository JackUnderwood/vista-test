__author__ = 'John Underwood'

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import gen_email, split_name


class AddEmail(UI):
    License()
    Checklist()
    # //*[@id="displayContent_1441310382386"]/h3
    # /html/body/main/div[2]/div[1]/h3

    runtime = {
        'expand': ('Click', '//*[@id="ribbon_form"]/ul/li/div[1]'),
        'email': (
            'Click', '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div[1]/a[3]'),
    }   # //*[@id="emailGrid_grid"]/tbody/tr/td[3]
    #     //*[@id="emailGrid_grid"]/tbody/tr[2]/td[3]
    process = UI()
    process.update(runtime)
    order = ('expand', 'email')
    process.execute(order)
    # Spy for the name in the drawers
    name = process.get('/html/body/main/div[2]/div[1]/h3', 'innerHTML')
    name = name[8:-1]  # static length of first eight elements 'Emails ('
    ui.log.debug('EXTRACTED NAME {}'.format(name,))
    email = gen_email(name)
    ui.log.debug('EMAIL ADDRESS {}'.format(email,))

    runtime = {
        'addEmail': ('Click', '//*[@id="emailGrid_form"]/a'),
        'emailAddress': ('Type', '#email_address', email),
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Work'),
        'save': ('Click', '//*[@id="editEmail_form"]/div[10]/a[1]')
    }
    process.update(runtime)
    order = ('addEmail', 'emailAddress', 'emailType', 'save')
    process.execute(order)
    process.wait(3)
    process.teardown()
