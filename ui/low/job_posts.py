from ui import UI
from tool.vlog import VLog
__author__ = 'John Underwood'


class JobPosts(UI):
    """
    Navigates to the Manage Job Post page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="JOBS")
        log.info("JobPosts __init__() called")
        runtime = {
            'level': self.MANAGE_JOBS,
            'hover': ('Hover', '#slide-out'),
            'job':  ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('hover', 'job', )
        process.execute(order)
