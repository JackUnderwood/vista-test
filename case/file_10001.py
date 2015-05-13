__author__ = 'John Underwood'

from ui import UI
from ui.low.file import File
from ui.high.file_my_file import FileMyFile


class File10001(UI):
    """
    Purpose: dummy testcase; goes to the File page.
    This test case is a trial test to see how the vtf will be use. It tests
    naming convention of regression files, tests interaction between modules,
    tests how to handle setup and teardown (should it use vtf base file), etc.
    """
    File()
    FileMyFile()
    UI().wait(4)
    UI().teardown()
