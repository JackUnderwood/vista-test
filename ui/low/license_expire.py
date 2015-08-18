__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class LicenseExpire(UI):
    """
    Begins at the main page and branches to the Expiring Licenses page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("Expiring License __init__() called")
        runtime = {
            'level': '5',
            'license': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i',),
            'expiring': (
                'Click',
                '//*[@id="slide-out"]/li[2]/ul/li/div/ul/li[2]/a', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('license', 'expiring', )
        process.execute(order)

