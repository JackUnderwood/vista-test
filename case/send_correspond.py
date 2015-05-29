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
    }
    expected = "Attachments"
    process = UI()
    process.update(runtime)
    order = ('licenseStanding', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
