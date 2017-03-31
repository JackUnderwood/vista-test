from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class FileCvTemplate(UI):
    """
    Click on the File | CV Template link from the Nav bar,
    branches to the CV Template Creator page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CVTEMP")
        log.info("CV Template __init__() called")
        runtime = {
            'level': self.FILE,
            'hover': ('Hover', '#slide-out'),
            'cvTemplate': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('cvTemplate', )
        process.execute(order)

