__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class FileBegin(UI):
    """
    Begins at the main page and branches to the File page.
    Other sibling files might be:
    - HomeBegin
    - TravelBegin
    - CorrTemplateCreatorBegin
    - CorrSendBegin
    - LyrisBegin
    - NotifyBegin
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="FILE")
        log.info("__init__() called")
        runtime = {
            'file': ("Click", "//*[@id='yw1']/li[6]/a/i", ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('file',)
        process.execute(order)