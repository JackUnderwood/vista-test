import ui
from ui import UI

__author__ = 'John Underwood'


class LicenseReport(UI):
    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'level': '5',  # not available in 'chain' commands
            # TODO: add replacer for chain commands in check_for_placeholder()
            'report': ("Chain", [
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[5]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[5]/ul/li/div/ul/li[2]/a'}), ]),
        }
        process = UI(override)
        process.update(runtime)
        process.execute(('report', ))
