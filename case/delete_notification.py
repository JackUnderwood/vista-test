from ui import UI

__author__ = 'John Underwood'


class DeleteNotification(UI):
    """ The CreateNotification case must be run first.
    """
    runtime = {
        'notify': ('Click', '//*[@id="button_notification"]/i'),
        'present': ('Click', '//label[@for="today" and contains(., "Present")]'),
        'cancelNotice': ('Click', '//*[@id="undefined"]/td[31]/i[2]'),
    }
    expected = "Notification deleted"
    process = UI()
    process.update(runtime)
    order = ('notify', 'present', 'cancelNotice', )
    process.execute(order)
    process.results(expected)
    process.teardown()
