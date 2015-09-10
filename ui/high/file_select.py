__author__ = 'John Underwood'
from ui import UI


class FileSelect(UI):

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'generic': ('Click', '//*[@id="vsubnav"]/div/div[6]/a[1]'),
            'sub': '1',
            'subcategory': (
                'Click', '//*[@id="fileList"]/div[3]/div[1]/div[&sub;]'),
            'line': '1',
            'selectFile': (
                'Click',
                '//*[@id="fileList"]/div[3]/div[1]/div[&sub;]/div[&line;]'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('generic', 'subcategory', 'selectFile', )
        process.execute(order)
