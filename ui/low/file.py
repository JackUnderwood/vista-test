__author__ = 'John Underwood'
from base import UI


class A(UI):
    def __init__(self, override=None):
        super().__init__()
        print("A __init__", override)
        runtime = {
            'file': ("Click", "//*[@id='yw1']/li[6]/a/i", ""),
        }
        process = UI(override)
        process.update(runtime)
        order = ('file',)
        process.execute(order)