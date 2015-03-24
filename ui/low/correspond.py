__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class Correspond(UI):
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CORRESPD")
        log.info("__init__() called")

        runtime = {
            'correspond': ("Click", '//*[@id="slide-out"]/li[3]/ul/li/a', ""),
            'send': ("Click", '//*[@id="slide-out"]/li[3]/ul/li/div/ul/li[2]/a', ""),

            # 'correspond': ("Chain", [
            #     ('click', {'on_element': '//*[@id="slide-out"]/li[3]/ul/li/a'}),
            #     ('move_to_element', {'to_element': '//*[@id="yt1"]/li[2]/a'}),
            #     ('click', {'on_element': '//*[@id="slide-out"]/li[3]/ul/li/div/ul/li[2]/a'}),
            # ], ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspond', 'send', )
        process.execute(order)
