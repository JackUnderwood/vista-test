from ui import UI
from tool.vlog import VLog

__author__ = 'John Underwood'


class LicenseTimeReport(UI):
    """
    Navigates to the Average Licensing Time by State page.
    """
    def __init__(self, override=None):
        super().__init__()
        log = VLog(name="vtf", log_name="LICENSE")
        log.info("License Requirements __init__() called")
        runtime = {
            'level': self.LICENSING,
            'hover': ('Hover', '#slide-out'),
            'timeline': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('hover', 'timeline', )
        process.execute(order)

