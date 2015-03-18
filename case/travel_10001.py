__author__ = 'John Underwood'

from ui import UI
from ui.low.travel import Travel
from ui.high.travel_specialty import TravelSpecialty
from ui.high.travel_mi import TravelMiddleInitial


class Travel10001(UI):
    """
    Purpose: dummy testcase; goes to the Travel page.
    This test case is a trial test to see how the vtf will be used. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should be used by vtf file) etc.
    Change the runtime to use specialty IMHSP and select specific assignment.
    """
    Travel()
    process = UI()
    # process.update(runtime)

    override = {
        'div': '4',
        'provider': '140826', }
    TravelSpecialty(override)

    override = {'enterMi': 'N', }
    TravelMiddleInitial(override)
    process.wait(3)
    process.teardown()
