__author__ = 'John Underwood'
from ui import UI


class GoalsCommissionReport(UI):
    """
    Click on the Goals | Commission Report link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '3',
            'goals': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'commReport': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('goals', 'commReport', )
        process.execute(order)
