__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class File(UI):
    """
    Begins at the main page and branches to the File page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="FILE")
        log.info("File __init__() called")
        runtime = {
            'file': ('Click', '//*[@id="slide-out"]/li[3]/a/i', ''),
        }
        process = UI(override)
        process.update(runtime)
        order = ('file', )
        process.execute(order)
