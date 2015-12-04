from ui import UI

__author__ = 'John Underwood'


class SalesTeamRevenueBonus(UI):
    """
    Click on the Sales | Manage Team Revenue Bonus link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '7',
            'sales': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'bonus': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[5]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('sales', 'bonus', )
        process.execute(order)