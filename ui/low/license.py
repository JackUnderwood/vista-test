from ui import UI
from tool.vlog import VLog
__author__ = 'John Underwood'


class License(UI):
    """
    Begins at the main page and branches to the Licensing landing page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("License __init__() called")
        runtime = {
            'level': self.LICENSING,
            'hover': ('Hover', '#slide-out'),
            'license': ("Chain", [
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
        order = ('hover', 'license', )
        process.execute(order)
