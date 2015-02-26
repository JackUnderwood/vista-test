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
            'subNav': ("Wait", "vsubnav", 5),
            'category': (
                "Click",
                '//*[@id="vsubnav"]/div/div[3]/ul/li',
                ""
            ),
            'element': (
                "Click",
                '//*[@id="vsubnav"]/div/div[3]/ul/ul/li'
                '[@alt="System Documents"]',
                ""
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('subNav', 'category', 'element')  # 'myQueueGo',)
        process.execute(order)
