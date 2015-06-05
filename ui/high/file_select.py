__author__ = 'John Underwood'
"""
This test uses the Chrome PDF Viewer, so it needs the following driver's option
added; see UI() class: add_experimental_option('excludeSwitches', ['test-type'])

An infobar warning banner will display, "You are using an unsupported
command-line flag: --ignore-certificate-errors. Stability and security will
suffer."

Alter the above to avoid the banner:
add_experimental_option(
    'excludeSwitches',
    ['test-type', 'ignore-certificate-errors']
)
"""
from ui import UI


class FileSelect(UI):
    # May want to add placeholders for Category and Subcategory.

    def __init__(self, override=None):
        super().__init__(override)
        runtime = {
            'category': ('Click', '//*[@id="vsubnav"]/div/div[2]/ul', ),
            'selectCategory': (
                'Click',
                '//*[@id="vsubnav"]/div/div[2]/ul/ul/li[2]'
            ),
            'subcategory': ('Click', '//*[@id="vsubnav"]/div/div[3]/ul', ),
            'selectSubcategory': (
                'Click',
                '//*[@id="vsubnav"]/div/div[3]/ul/ul/li[12]'
            ),
            'selectFile': (
                'Click',
                '//*[@id="fileList"]/div[2]/div/div[2]/div[2]'
            )
        }
        process = UI()
        process.update(runtime)
        order = ('category', 'selectCategory', 'subcategory',
                 'selectSubcategory', 'selectFile', )
        process.execute(order)
