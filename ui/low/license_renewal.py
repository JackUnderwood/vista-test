from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class LicenseRenewal(UI):
    """
    Begins at the main page and branches to the Expiring Licenses page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("License Renewal __init__() called")
        runtime = {
            'level': self.LICENSING,
            'hover': ('Hover', '#slide-out'),
            'expire': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('hover', 'expire', )
        process.execute(order)

