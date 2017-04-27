import ui
from ui import UI

__author__ = 'John Underwood'


class CorrTemplateCreator(UI):
    """
    Navigate to Administrator | Template Creator page
    """
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Correspond Template Creator __init__() called")
        runtime = {
            'level': self.ADMIN,
            'hover': ('Hover', '#slide-out'),
            'corrTemplateCreator':  ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[9]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('hover', 'corrTemplateCreator', )
        process.execute(order)

