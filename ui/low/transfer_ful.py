from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class TransferFollowUpLogs(UI):
    """
    Begins at the main page and branches to the Transfer Follow Up Logs page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="TRANSFER")
        log.info("TransferFollowUpLogs __init__() called")
        runtime = {
            'level': '3',
            'transFul': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('transFul', )
        process.execute(order)

