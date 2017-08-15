from ui import UI

__author__ = 'John Underwood'


class JobAdvanced(UI):
    """
    Click the "Advanced +" button.
    """

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'advanced': ('Click', '//*[@id="job-search-wrap"]/sub/a', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('advanced', )
        process.execute(order)
