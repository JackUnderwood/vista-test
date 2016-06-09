from ui import UI
from ui.low.jobs_edit import JobsEdit
from ui.high.job_search import JobSearch

__author__ = 'John Underwood'


class JobEdit(UI):
    JobsEdit()
    JobSearch()

    runtime = {
        'subtitleText': "Get Started Right Away",
        'text': "Some text",
        'subtitle': ('Type', '#job_board_subtitle', '&subtitleText;'),
        'template': ('Select', '#template', 'Marketing Tab'),
        'description': ('Type', '.cke_wysiwyg_frame', '&text;'),
    }
    expected = runtime['subtitleText']
    process = UI()
    process.update(runtime)
    order = ('subtitle', 'template', 'description', )
    process.execute(order)
    actual = process.get('css=#content>div>div:nth-child(2)>div>p.subtitle')
    process.compare(expected, actual)
    process.wait(1)
    process.teardown()
