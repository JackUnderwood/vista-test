from ui import UI

__author__ = 'John Underwood'


class JobSearch(UI):

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'jobNum': '54274',  # override={'jobNum': '54274'}
            'search': ('Type', '#job_number', '&jobNum;'),
            'submit': ('Click', '//*[@id="content"]/form/input[2]', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('search', 'submit', )
        process.execute(order)
