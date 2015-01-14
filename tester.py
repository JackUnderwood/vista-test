__author__ = 'John Underwood'

from ui import UI
from ui.low.file import FileBegin


class Tester(UI):

    FileBegin()
    UI().teardown()
