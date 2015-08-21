__author__ = 'John Underwood'
from ui import UI


class SalesBase(UI):
    """
    Click on the Sales | Manage Sales Base link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '6',
            'sales': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'base': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', 'base', )
        process.execute(order)
