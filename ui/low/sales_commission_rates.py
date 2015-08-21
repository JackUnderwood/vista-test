__author__ = 'John Underwood'
from ui import UI


class SalesCommissionRates(UI):
    """
    Click on the Sales | Manage Commission Rates link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '6',
            'sales': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'rates': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', 'rates', )
        process.execute(order)
