__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class File(UI):
    """
    Click on the File link from the Nav bar, branches to the File page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="FILE")
        log.info("File __init__() called")
        runtime = {
            'level': '5',
            'file': ('Click', '//*[@id="slide-out"]/li[&level;]/a/i', ''),
        }
        process = UI(override)
        process.update(runtime)
        order = ('file', )
        process.execute(order)
