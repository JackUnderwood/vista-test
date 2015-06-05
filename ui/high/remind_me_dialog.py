__author__ = 'John Underwood'
from ui import UI


class RemindMeDialog(UI):
    """
    Pre-requirement: needs to display Remind Me dialog - execute low.remind_me
    first.

    Test case goes into Remind Me.
    """
    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'refer': (
                'Click',
                '//*[@id="widgetNotification_form"]/div[2]/div/label',
            ),
            'type': ('Click', '//*[@id="type"]/div/i[3]'),
            'in': ('Click', '//*[@id="count"]/span[3]'),
            'timePeriod': ('Click', '//*[@id="time"]/span[3]'),
            'subject': ('Type', '#notifySubject', 'Test Subject'),
            'notes': (
                'Type',
                '#notifyNotes',
                'Lorem ipsum dolor sit amet, in pro summo contentiones. In sea.'
            ),
            'button': ('Click', '//*[@button="save"]'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('refer', 'type', 'in', 'timePeriod', 'subject',
                 'notes', 'button', )
        process.execute(order)
