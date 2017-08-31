from ui import UI
__author__ = 'John Underwood'


class ExpandRibbon(UI):
    """
    Pre-requirement: needs to display provider's Checklist page.

    Test case expands the ribbon.
    """
    def __init__(self, override=None):
        super().__init__()

        runtime = {
            'expandRibbon': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[1]/div/div[1]'
            ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('expandRibbon', )
        process.execute(order)
