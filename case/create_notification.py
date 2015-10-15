__author__ = 'John Underwood'

from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog
from tool.generators.generator import gen_key


class CreateNotification(UI):
    RemindMe()

    expected = gen_key()
    override = {
        'notes': ('Type', '#message_body', expected),
    }
    RemindMeDialog(override)

    runtime = {
        'notify': ('Click', '//*[@id="button_notification"]/i'),
        'present': ('Click', '//label[@for="today" and contains(., "Present")]'),
        'showDetails': ('Click', '//*[@id="undefined"]/td[1]'),
    }
    process = UI()
    process.update(runtime)
    order = ('notify', 'present', 'showDetails', )
    process.execute(order)
    process.wait(1)
    process.results(expected)
    process.teardown()
