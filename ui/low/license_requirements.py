__author__ = 'John Underwood'
from ui import UI
from tool.vlog import VLog


class LicenseRequirements(UI):
    """
    Begins at the main page and branches to the Manage State License
    Requirements page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("License Requirements __init__() called")
        runtime = {
            'level': '5',
            'license': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i',),
            'requirements': (
                'Click',
                '//*[@id="slide-out"]/li[2]/ul/li/div/ul/li[3]/a', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('license', 'requirements', )
        process.execute(order)

