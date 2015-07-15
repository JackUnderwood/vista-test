__author__ = 'John Underwood'
from ui import UI


class GoalsCommissionRates(UI):
    """
    Click on the Goals | Manage Commission Rates link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '4',
            'goals': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'rates': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[3]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('goals', 'rates', )
        process.execute(order)
