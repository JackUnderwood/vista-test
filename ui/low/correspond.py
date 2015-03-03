__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class CorrespondBegin(UI):
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CORRESPD")
        log.info("__init__() called")

        runtime = {
            'correspond': ("Click", '//*[@id="yw1"]/li[5]/a/i', ""),
            'waitSub': ("Wait", "yt0", 5),
            'corrSend': ("Click", '//*[@id="yt0"]/li[2]/a', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspond', 'waitSub', 'corrSend')
        process.execute(order)

