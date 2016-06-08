from ui import UI
from ui.low.jobs_edit import JobsEdit
from ui.high.job_search import JobSearch

__author__ = 'John Underwood'


class JobEdit(UI):
    JobsEdit()
    JobSearch()

    runtime = {
        'text': "Some text",
        'subtitle': ('Type', '#job_board_subtitle', 'Get Started Right Away'),
        'template': ('Select', '#template', 'Marketing Tab'),
        'description': ('Type', '#job_board_subtitle', '&text;'),
    }
    expected = "Claim saved"
    process = UI()
    process.update(runtime)
    order = ('subtitle', 'template', 'description', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
