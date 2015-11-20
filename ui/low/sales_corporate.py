from ui import UI

__author__ = 'John Underwood'


class SalesCorporate(UI):
    """
    Click on the Sales | Manage Corporate Goals link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '7',
            'sales': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'corporate': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', 'corporate', )
        process.execute(order)
