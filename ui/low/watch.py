import ui
from ui import UI

__author__ = 'John Underwood'


class Watch(UI):
    def __init__(self, override=None):
        super().__init__()
        ui.log.debug("Inside Watch class")

        runtime = {
            'level': self.WATCH,
            'hover': ('Hover', '#slide-out'),
            'watch': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('hover', 'watch', )
        process.execute(order)
