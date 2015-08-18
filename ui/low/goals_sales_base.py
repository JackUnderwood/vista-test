__author__ = 'John Underwood'
from ui import UI


class GoalsSalesBase(UI):
    """
    Click on the Goals | Manage Sales Base link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '6',
            'goals': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'sales': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[4]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('goals', 'sales', )
        process.execute(order)
