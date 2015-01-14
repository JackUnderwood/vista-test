__author__ = 'John Underwood'
from ui import UI


class FileMyQueue(UI):
    """
    Case test goes into My Queue and then returns to File's listings.
    """
    def __init__(self, override=None):
        super().__init__()
        print("FileMyQueue __init__", override)

        runtime = {
            'myQueue': ("Click", '//*[@id="myqueue"]/span', ""),
            'myQueueGo': ("Click", '//*[@id="myqueueGo"]', "")
        }
        process = UI(override)
        process.update(runtime)
        order = ('myQueue', 'myQueueGo',)
        process.execute(order)

