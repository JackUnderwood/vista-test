from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class DeleteNotification(UI):
    RemindMe()
    override = {
        'notes': ('Type', '#message_body', gen_key()),
    }
    RemindMeDialog(override)

    runtime = {
        'notify': ('Click', '//*[@id="button_notification"]/i'),
        'future': ('Click', '//label[@for="future" and contains(., "Future")]'),
        'cancelNotice': ('Click', '//*[@id="undefined"]/td[31]/i[2]'),
    }

    expected = "Notification cancelled"
    process = UI()
    process.update(runtime)
    order = ('notify', 'future', 'cancelNotice', )
    process.execute(order)
    process.results(expected)
    process.teardown()
