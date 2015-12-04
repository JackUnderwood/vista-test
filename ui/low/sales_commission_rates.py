from ui import UI

__author__ = 'John Underwood'


class SalesCommissionRates(UI):
    """
    Click on the Sales | Manage Commission Rates link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '7',
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
