from ui import UI
from tool.vlog import VLog
__author__ = 'John Underwood'


class JobTemplates(UI):
    """
    Branches to the Jobs Management | Job Templates creation page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="JOBS")
        log.info("JobTemplates __init__() called")
        runtime = {
            'level': self.MANAGE_JOBS,
            'jobTemplates':  ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('jobTemplates', )
        process.execute(order)

