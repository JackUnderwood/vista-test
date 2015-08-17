__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.expand_ribbon import ExpandRibbon
from ui.high.ribbon_corr import RibbonToCorrespondence


class SendCorrespond(UI):
    """
    Incomplete test case; has issues with multiple delivery methods using
    ids that are dynamic; they need to be static or constant.
    """
    License()
    override = {'showAll': ('Unknown', 'Unknown', 'Unknown'), }
    Checklist(override)
    ExpandRibbon()
    UI().wait(2)
    override = {  # select 'License renewal'
        'selectTemplate':
            ('Click', '//*[@id="correspondenceChooser_form"]/p[2]/p[9]/a')}
    RibbonToCorrespondence(override)

    runtime = {
        'licenseStanding': ('Select', '#license_id', ),
        'entity': ('Click', '//*[@id="add-recipient-container"]/span[1]'),
        'findEntity': ('Type', '<input>', 'matt lambert st:wv', ),
        'selectEntity': ('Click', '//*[@item_id="91273"]'),
        'checkAddress': ('Click', '//span[text()="Payroll Address"]'),
        'saveDeliveryMethod': ('Click', '//a[@button="save"]', ),
        'cya': ('Click', '//body', ),
        'send': ('Click', '#corr_send')
    }
    expected = "Your message was successfully sent"
    process = UI()
    process.update(runtime)
    order = ('licenseStanding', 'entity', 'findEntity', 'selectEntity',
             'checkAddress', 'saveDeliveryMethod', 'cya', 'send')
    process.execute(order)
    process.results(expected, 'toast-container')
    process.wait(3)
    process.teardown()
