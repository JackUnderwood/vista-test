__author__ = 'John Underwood'
from ui import UI


class SalesCommissionReport(UI):
    """
    Click on the Sales | Commission Report link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': self.SALES,
            'hover': ('Hover', '#slide-out'),
            'sales': ("Chain", [
                ('move_to_element', {
                    'to_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('move_to_element', {  # report
                    'to_element': '//*[@id="slide-out"]/li[&level;]/ul/li/div/'
                                  'ul/li[1]/a'}),
                ('click', {
                    'on_element': '//*[@id="slide-out"]/li[&level;]/ul/li/div/'
                                  'ul/li[1]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('hover', 'sales', )
        process.execute(order)

