from ui import UI

__author__ = 'John Underwood'


class LicenseReport(UI):
    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'level': self.LICENSING,
            'hover': ('Hover', '#slide-out'),
            'report': ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'}
                 ), ]),
        }
        process = UI(override)
        process.update(runtime)
        process.execute(('hover', 'report',))
