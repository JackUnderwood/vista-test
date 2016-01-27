__author__ = 'John Underwood'
from ui import UI


class SalesCommissionReport(UI):
    """
    Click on the Sales | Commission Report link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '7',
            'sales': ("Chain", [
                ('move_to_element', {
                    'to_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element': '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'}
                 ),
            ]),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', )
        process.execute(order)

