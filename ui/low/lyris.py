__author__ = 'John Underwood'
from ui import UI
from tool.clog import CLog


class LyrisBegin(UI):
    """
    Begins at the main page and branches to the Lyris dialog.
    """
    def __init__(self, override=None):
        super().__init__()
        log = CLog(name="vtf", log_name="LyrisBegin")
        log.info("__init__() called")
        runtime = {
            'lyris': ("Click", '//*[@id="lyris"]', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('lyris',)
        process.execute(order)