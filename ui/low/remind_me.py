__author__ = 'John Underwood'

from ui import UI


class RemindMe(UI):

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'remind': ('Click', '#remindMeButton'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('remind',)
        process.execute(order)
