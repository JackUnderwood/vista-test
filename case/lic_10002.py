__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class Lic10002(UI):
    """
    May want to remove this test since 'new_license.py' does the same thing.
    """
    License()
    Checklist()
