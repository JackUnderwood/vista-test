__author__ = 'John Underwood'
from ui import UI
from tool.clog import CLog


class CorrespondBegin(UI):
    def __init__(self, override=None):
        super().__init__()
        log = CLog(name="vtf", log_name="CorrespondBegin")
        log.info("__init__() called")

        runtime = {
            'correspond': ("Click", '//*[@id="yw1"]/li[5]/a/i', ""),
            'creator': ("Click", '//*[@id="yt0"]/li[2]/a', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspond', 'creator')
        process.execute(order)

