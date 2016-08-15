from ui import UI

from tool.utilities import todays_date

__author__ = 'John Underwood'


class RemindMeDialog(UI):
    """
    Pre-requirement: needs to display Remind Me dialog - execute low.remind_me
    first.

    Test case goes into the Remind Me drawer.
    """
    def __init__(self, override=None):
        super().__init__()
        month, day, year = (todays_date()[2:4], todays_date()[:2],
                            todays_date()[4:])
        runtime = {
            'dueDate': ('Type', '#due_datetime', month+day+year),
            'findIcon': ('Click', '//*[@id="who"]/div/div/div[1]/i[2]'),
            'selectEntity': ('Click', '//*[@id="who"]/div/div/div[1]/div/a[1]'),
            'find': ('Type', '#notifyRegardingDesc', 'matt lambert st:wv'),
            'select': ('Click', '//*[@item_id="91273"]'),
            'notes': (
                'Type',
                '#message_body',
                'Lorem ipsum dolor sit amet, in pro summo contentiones. In sea.'
            ),
            'submit': ('Click', '//*[@button="save"]'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('dueDate', 'findIcon', 'selectEntity', 'find', 'select',
                 'notes', 'submit')
        process.execute(order)
