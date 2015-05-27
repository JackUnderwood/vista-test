__author__ = 'John Underwood'

from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog


class Notice10002(UI):
    RemindMe()
    override = {  # Cancel button
        'button': ('Click', '//*[@button="close"]')
    }
    RemindMeDialog(override)
    UI().wait(2)
    UI().teardown()
