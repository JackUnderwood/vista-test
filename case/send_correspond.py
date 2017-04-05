from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.ribbon_corr import RibbonToCorrespondence
from tool.db import get_record

__author__ = 'John Underwood'


class SendCorrespond(UI):
    """
    Use the default template 'License Renewal'.
    TODO: Test a variety of templates; requires an elif because each template
    uses different input fields OR create different test case for each template.
    """
    template = 'License Renewal'  # TODO test a variety of templates
    email = 'lambertmwl@gmail.com'
    sql = """
        SELECT ed.entity_id_number ID, ed.peoplesoft_name_on_check Name
        FROM entity_details ed, email_address ea
        WHERE ea.email_address = '{}'
        AND ed.entity_id_number = ea.entity_id_number;
    """.format(email, )
    assert isinstance(sql, str)
    record = get_record(sql)
    item_id = record[0][0]

    License()
    Checklist()
    process = UI()
    process.wait(2)
    override = {  # select 'License renewal'
        'selectTemplate':
            ('Click', '//*[@id="correspondenceChooser_form"]/p[2]/p[10]/a')}
    RibbonToCorrespondence(override)

    runtime = {
        'reselectTemplate': ('Select', '#template_id', template),
        'licenseStanding': ('Select', '#license_id', ),
        'entity': ('Click', '//*[@id="add-recipient-container"]/span[1]'),
        'findEntity': ('Type', '<input>', 'e:{}'.format(email, )),
        'selectEntity': ('Click', '//*[@item_id="{}"]'.format(item_id,)),
        'checkAddress': ('Click', '//span[text()="Personal"]'),
        'saveDeliveryMethod': ('Click', '//a[@button="save"]', ),
        'cya': ('Click', '//body', ),
        'send': ('Click', '#corr_send')
    }
    expected = "Your message was successfully sent"
    process.update(runtime)
    order = ('licenseStanding', 'entity', 'findEntity', 'selectEntity',
             'checkAddress', 'saveDeliveryMethod', 'cya', 'send')
    process.execute(order)
    process.results(expected, locator='toast-container')
    process.wait(3)
    process.teardown()
