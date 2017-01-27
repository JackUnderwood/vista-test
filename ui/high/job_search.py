from ui import UI

__author__ = 'John Underwood'


class JobSearch(UI):
    """
    Search for a job number or a range of numbers, such as...
        - a single job number: 54274
        - a range of job numbers: 90000-92150
        - an implied range:
            - 90000-5100 same as 90000-95100
            - 90000-100  same as 90000-90100
    """

    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'value': '12345',  # override={'value': '12345'}
            'search': ('Type', '#s_job_number', '&value;'),
            'refresh': (
                'Click',
                '//*[@id="job-search-wrap"]/div[2]/div[2]/button', ),
        }
        process = UI(override)
        process.update(runtime)
        order = ('search', 'refresh', )
        process.execute(order)
