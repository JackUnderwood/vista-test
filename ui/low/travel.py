__author__ = 'John Underwood'
from ui import UI


class TravelBegin(UI):
    """
    Begins at the main page and branches to the Travel page.
    """
    def __init__(self, override=None):
        super().__init__()
        print("TravelBegin __init__")
        runtime = {
            'travel': ("Click", '//*[@id="yw1"]/li[4]/a/i', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('travel',)
        process.execute(order)