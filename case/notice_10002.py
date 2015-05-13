__author__ = 'John Underwood'

from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog


class Notice10002(UI):
    RemindMe()
    override = {
        'button': ('Click', '//*[@@for="widgetNotification"]/div/div[3]/a[2]')
    }
    RemindMeDialog(override)
