import ui
from ui import UI

__author__ = 'John Underwood'


class Watch(UI):
    def __init__(self, override=None):
        super().__init__()
        ui.log.debug("Inside Watch class")

        runtime = {
            'level': '8',
            'watch': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'sub': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('watch', 'sub', )
        process.execute(order)
