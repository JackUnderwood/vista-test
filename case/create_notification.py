from ui import UI
from ui.low.remind_me import RemindMe
from ui.high.remind_me_dialog import RemindMeDialog
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class CreateNotification(UI):
    RemindMe()

    expected = gen_key()
    override = {
        'selectEntity': ('Click', '//*[@id="who"]/div/div/div[1]/div/a[2]'),
        'find': ('Type', '#notifyRegardingDesc', 'care'),
        'select': ('Click', '//*[@item_id="198206"]'),  # Honolulu Health Care
        'notes': ('Type', '#message_body', expected),
    }
    RemindMeDialog(override)

    runtime = {
        'notify': ('Click', '//*[@id="button_notification"]/i'),
        'present': ('Click', '//label[@for="future" and contains(., "Future")]'),
        'showDetails': ('Click', '//*[@id="undefined"]/td[1]'),
        'cancel': ('Click', '//*[@id="undefined"]/td[31]/i[2]'),
    }
    process = UI()
    process.update(runtime)
    order = ('notify', 'present', )
    process.execute(order)

    page = process.spy('#notifyGrid_grid_info', 'innerHTML')
    print("PAGE: {}".format(page,))
    # Expect "Showing page 1 of 1" not 'Showing page 1 of 0'
    success = process.compare('1', page[-1:])

    if success:
        order = ('showDetails', )
        process.execute(order)
        actual = process.spy('#message_body', 'innerHTML')
        process.compare(expected, actual)
        order = ('cancel', )  # remove the notice
        process.execute(order)

    process.teardown()
