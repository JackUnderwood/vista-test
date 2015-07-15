__author__ = 'John Underwood'
from ui import UI


class GoalsCorporate(UI):
    """
    Click on the Goals | Manage Corporate Goals link from the Nav bar.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'level': '3',
            'goals': ('Click', '//*[@id="slide-out"]/li[&level;]/ul/li/a/i'),
            'corporate': (
                'Click',
                '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[1]/a'
            ),
        }

        process = UI(override)
        process.update(runtime)
        order = ('goals', 'corporate', )
        process.execute(order)
