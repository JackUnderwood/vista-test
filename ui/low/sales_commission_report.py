__author__ = 'John Underwood'
from ui import UI


class SalesCommissionReport(UI):
    """
    Click on the Sales | Commission Report link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '6',
            'sales': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'commReport': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', 'commReport', )
        process.execute(order)
