__author__ = 'John Underwood'

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import gen_email, split_name


class AddEmail(UI):
    License()
    Checklist()

    runtime = {
        'email': (
            'Click', '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[3]'),
    }
    expected = "Email saved"
    process = UI()
    process.update(runtime)
    order = ('email', )
    process.execute(order)
    # Spy for the name in the drawers
    name = process.get('/html/body/main/div[2]/div[1]/h3', 'innerHTML')
    name = name[name.find('(')+1:name.find(')')]
    ui.log.debug('------EXTRACTED NAME {}'.format(name,))
    email = gen_email(name)
    ui.log.debug('-------EMAIL ADDRESS {}'.format(email,))

    runtime = {
        'addEmail': ('Click', '//*[@id="emailGrid_form"]/a'),
        'emailAddress': ('Type', '#email_address', email),
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Work'),
        'save': ('Click', '//*[@id="editEmail_form"]/div[9]/a[1]')
    }
    process.update(runtime)
    order = ('addEmail', 'emailAddress', 'emailType', 'save')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
