__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class MyWorkspace(UI):
    """
    Begins at the main page and opens My Workspace panel.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="MYWORKSP")
        log.info("My Workspace __init__() called")
        runtime = {
            'workspace': ('Click', '//*[@id="previous-results no-print"]', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('workspace', )
        process.execute(order)
