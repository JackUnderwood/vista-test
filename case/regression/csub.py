__author__ = 'John Underwood'
from base import UI
import ui.low.file as asub


class C(UI):
    asub.A()
    UI().teardown()

