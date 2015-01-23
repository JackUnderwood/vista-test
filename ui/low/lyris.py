__author__ = 'John Underwood'
from ui import UI


class LyrisBegin(UI):
    """
    Begins at the main page and branches to the Lyris dialog.
    """
    def __init__(self, override=None):
        super().__init__()
        print("LyrisBegin __init__")
        runtime = {
            'lyris': ("Click", '//*[@id="lyris"]', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('lyris',)
        process.execute(order)