import ui
from ui import UI

__author__ = 'John Underwood'


class Wiki(UI):
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Wiki __init__() called")
        runtime = {
            'level': self.WIKI,
            'wiki': ('Click', '//*[@id="slide-out"]/li[&level;]/a/i', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('wiki', )
        process.execute(order)
