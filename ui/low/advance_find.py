import ui
from ui import UI

__author__ = 'John Underwood'


class AdvanceFind(UI):
    """
    Begins at the main page and opens My Workspace panel.
    """
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Advance Find __init__() called")

        runtime = {'advanceFind': (
            'Click',
            'css=body>header>nav>div>ul.left>li:nth-child(2)>a:nth-child(1)>i')}
        process = UI(override)
        process.update(runtime)
        order = ('advanceFind', )
        process.execute(order)
