import ui
from ui import UI

__author__ = 'John Underwood'


class UserConfig(UI):
    def __init__(self, override=None):
        super().__init__()
        ui.log.debug('Inside UserConfig class')

        runtime = {
            'level': '10',
            'user': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'config': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('user', 'config', )
        process.execute(order)
