__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License


class Lic10001(UI):
    License()
    UI().teardown()
