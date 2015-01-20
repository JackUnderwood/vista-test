__author__ = 'John Underwood'
from ui import UI


class CorrespondBegin(UI):
    def __init__(self, override=None):
        super().__init__()
        print("CorrespondBegin __init__", override)
        runtime = {
            'correspond': ("Click", '//*[@id="yw1"]/li[5]/a/i', ""),
            'creator': ("Click", '//*[@id="yt0"]/li[1]/a', ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('correspond', 'creator')
        process.execute(order)

