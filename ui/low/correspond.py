__author__ = 'John Underwood'
"""
This file is out-of-date as of 4/30/2015

Sample of the Chain:
'correspond': ("Chain", [
    ('click', {'on_element': '//*[@id="slide-out"]/li[3]/ul/li/a'}),
    ('click', {'on_element': '//*[@id="slide-out"]/li[3]/ul/li)
]),
"""
from ui import UI
from tool.vlog import VLog


class Correspond(UI):
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="CORRESPD")
        log.info("__init__() called")

        runtime = {  # //*[@id="slide-out"]/li[3]
            'correspond': ("Click", '//*[@id="slide-out"]/li[2]/a/i'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspond', )
        process.execute(order)
