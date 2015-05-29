__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.ribbon_corr import RibbonToCorrespondence


class SendCorrespond(UI):
    License()
    Checklist()
    RibbonToCorrespondence()

    runtime = {
        'licenseStanding': ('Select', '#license_id', 'AZ - P - 2145 - A'),
        'entity': ('Click', '//*[@id="add-recipient-container"]/span[1]'),
        'findEntity': (
            'Type',
            '//*[@id="client_id_1_desc_5568b9eecbc2e"]',  # tripping up on this
            'care'
        ),
        'selectEntity': ('Click', '//*[@item_id="108206"]'),
        'checkAddress': (
            'Click',
            '//*[@id="delivery-locations"]/form/div[1]/p/label'
        ),
        'saveDeliveryMethod': (
            'Click',
            '//*[@id="delivery-locations"]/form/div[5]/a[1]'
        ),
        'send': ('Click', '#corr_send')
    }
    expected = "Your message was successfully sent"
    process = UI()
    process.update(runtime)
    order = ('licenseStanding', 'entity', 'findEntity', 'selectEntity',
             'checkAddress', 'saveDeliveryMethod', 'send')
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
