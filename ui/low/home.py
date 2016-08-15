import ui
from ui import UI
__author__ = 'John Underwood'


class Home(UI):
    """
    Click on the Home link from the Nav bar, branches to the Home page.
    """
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Home __init__() called")
        runtime = {
            'level': self.HOME,
            'home': ('Click', '//*[@id="slide-out"]/li[&level;]/a/i'),
        }
        process = UI()
        process.update(runtime)
        process.execute(('home',))
