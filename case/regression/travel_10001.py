__author__ = 'John Underwood'

from ui import UI
from ui.low.travel import TravelBegin
from ui.high.travel_em import TravelEm
from ui.high.travel_em_middle_init import TravelMiddleInitial


class Travel10001(UI):
    """
    Purpose: dummy testcase; goes to the Travel page.
    This test case is a trial test to see how the vtf will be use. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should be used by vtf file) etc.
    """
    TravelBegin()
    TravelEm()
    TravelMiddleInitial()
    UI().teardown()

