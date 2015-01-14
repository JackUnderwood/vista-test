__author__ = 'John Underwood'

from ui import UI
from ui.low.file import FileBegin
from ui.high.file_my_queue import FileMyQueue


class File10001(UI):
    """
    This test case is a trial test to see how the vtf will be use. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should it use vtf base file), etc.
    """
    FileBegin()
    FileMyQueue()
    UI().teardown()

