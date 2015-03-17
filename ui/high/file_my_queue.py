__author__ = 'John Underwood'
from ui import UI


class FileMyQueue(UI):
    """
    Pre-requirement: needs to be on the File page - execute low.file first.
    Test case goes into MyQueue.
    """
    def __init__(self, override=None):
        super().__init__(override)

        runtime = {
            'subNav': ("Wait", "vsubnav", 5),
            'category': (
                "Click",
                '//*[@id="vsubnav"]/div/div[8]/i/span',
                ""
            ),
        }
        process = UI()
        process.update(runtime)
        order = ('subNav', 'category', )
        process.execute(order)
