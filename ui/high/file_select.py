from ui import UI

__author__ = 'John Underwood'


class FileSelect(UI):
    """
    Pre-requirement: needs to be on the File page - execute low.file first.
    Uses the 'My Files' file set - default
    """

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'cat': '1',
            'sub': '1',
            'subcategory': (
                'Click', '//*[@id="fileList"]/div[3]/div[&cat;]/div[&sub;]'),
            'file': '1',
            'selectFile': (
                'Click',
                '//*[@id="fileList"]/div[3]/div[&cat;]/div[&sub;]/div[&file;]'),
        }
        process = UI(override)
        process.update(runtime)
        order = ('subcategory', 'selectFile', )
        process.execute(order)
