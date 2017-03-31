from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class FileCvPartial(UI):
    """
    Click on the File | CV Partial link from the Nav bar,
    branches to the CV Template Partial Creator page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CVPART")
        log.info("CV Partial __init__() called")
        runtime = {
            'level': self.FILE,
            'hover': ('Hover', '#slide-out'),
            'cvPartial': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('cvPartial', )
        process.execute(order)

