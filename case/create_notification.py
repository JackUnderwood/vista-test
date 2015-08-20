__author__ = 'John Underwood'

from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog


class CreateNotification(UI):
    RemindMe()
    RemindMeDialog()

    process = UI()
    process.results('New Notification Received')
    process.wait(3)
    process.teardown()
