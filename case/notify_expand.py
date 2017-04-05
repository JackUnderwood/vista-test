from ui import UI
__author__ = 'John Underwood'


class NotifyExpand(UI):

    runtime = {
        'notify': ('Click', '#button_notification'),
        'close': ('Click', '//*[@id="notifyGrid_form"]/div[2]/a')
    }
    expected = 'Notifications ('
    process = UI()
    process.update(runtime)
    order = ('notify', 'close', )
    process.execute(order)
    process.results(expected, negative=True)
    process.wait(3)
    process.teardown()
