__author__ = 'John Underwood'

from ui import UI
from ui.low.lyris import LyrisBegin


class Lyris10001(UI):
    """
    Purpose: dummy testcase; goes to the Lyris page.
    This test case is a trial test to see how the vtf will be use. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should be used by vtf file) etc.
    """
    LyrisBegin()
    UI().teardown()


