__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class License(UI):
    """
    Begins at the main page and branches to the Licensing landing page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("License __init__() called")
        runtime = {
            'level': '3',
            'license': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i', ),
            'landing': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('license', 'landing', )
        process.execute(order)
