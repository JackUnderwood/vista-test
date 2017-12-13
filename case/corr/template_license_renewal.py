from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class TemplateLicenseRenewal(UI):
    License()
    Checklist()
    process = UI()

