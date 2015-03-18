__author__ = 'John Underwood'

from ui import UI
from ui.low.correspond import Correspond
from ui.high.corr_selections import CorrSelections


class Corr10003(UI):
    Correspond()
    override = {
        'board': 'AHPRA - ACT - Canberra',
        'find': 'brad'
    }
    CorrSelections(override)
    UI().wait(2)
    UI().teardown()
