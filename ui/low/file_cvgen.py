from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class FileCvGen(UI):
    """
    Click on the File | CV Generator link from the Nav bar,
    branches to the CV Generator page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CVGEN")
        log.info("CV Generator __init__() called")
        runtime = {
            'level': self.FILE,
            'hover': ('Hover', '#slide-out'),
            'cvgen': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('cvgen', )
        process.execute(order)
