from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class EntityComments(UI):
    """
    Begins at the main page and branches to the Manage Entities | Comments page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="TRANSFER")
        log.info("TransferFollowUpLogs __init__() called")
        runtime = {
            'level': self.MANAGE_ENTITIES,
            'hover': ('Hover', '#slide-out'),
            'comments': ("Chain", [
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
        order = ('hover', 'comments', )
        process.execute(order)

