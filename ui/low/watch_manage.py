import ui
from ui import UI

__author__ = 'John Underwood'


class WatchManage(UI):
    def __init__(self, override=None):
        super().__init__()
        ui.log.debug("Inside WatchManage class")

        runtime = {
            'level': self.WATCH,
            'hover': ('Hover', '#slide-out'),
            'watch': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'manage': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('hover', 'watch', 'manage', )
        process.execute(order)
