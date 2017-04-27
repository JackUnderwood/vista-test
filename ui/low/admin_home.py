import ui
from ui import UI

__author__ = 'John Underwood'


class AdminHome(UI):
    """
    Navigate to Administrator | Home -- the Utilities page
    """
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Administrator Home __init__() called")
        runtime = {
            'level': self.ADMIN,
            'hover': ('Hover', '#slide-out'),
            'home':  ("Chain", [
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
        order = ('hover', 'home', )
        process.execute(order)

