__author__ = 'John Underwood'

from ui import UI
from ui.low.travel import TravelBegin
from ui.high.travel_specialty import TravelSpecialty
from ui.high.travel_mi import TravelMiddleInitial


class Travel10001(UI):
    """
    NOT IN A USABLE STATE.
    Purpose: dummy testcase; goes to the Travel page.
    This test case is a trial test to see how the vtf will be used. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should be used by vtf file) etc.
    Change the runtime to use specialty IMHSP and select specific assignment.
    """
    TravelBegin()
    runtime = {  # specialty IMHSP
        'selectSpecialty': ("Click", '//*[@id="content"]/div[6]/div', ""),
        'selectAssign': ("Click", '//*[@id="138861"]/div[1]', "")}
    process = UI()
    process.update(runtime)
    TravelSpecialty()

    TravelMiddleInitial()
    process.teardown()
