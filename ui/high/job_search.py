from ui import UI

__author__ = 'John Underwood'


class JobSearch(UI):

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'num': '54274',  # override={'number': '54274'}
            'job': ('Type', '#s_job_number', '&num;'),
            'search': (
                'Click',
                '//*[@id="job-search-wrap"]/div[2]/div[2]/button', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('job', 'search', )
        process.execute(order)
