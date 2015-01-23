__author__ = 'John Underwood'
from ui import UI


class FileMyQueue(UI):
    """
    Pre-requirement: needs to be on the File page - execute file mod first.
    Case test goes into My Queue and then returns to File's listings.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'myQueue': ("Click", '//*[@id="myqueue"]/span', ""),
            'myQueueGo': ("Click", '//*[@id="myqueueGo"]', "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('myQueue', 'myQueueGo',)
        process.execute(order)

