from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch

__author__ = 'John Underwood'


class JobEdit(UI):
    job_number = '90000'
    JobPosts()
    JobSearch(override={'value': job_number})

    runtime = {
        'subtitleText': "Get Started Right Away",
        'descText': "Some text",
        'edit': ('Click', '#edit_' + job_number,),
        'subtitle': ('Type', '#jobs__job_board_subtitle', '&subtitleText;'),
        'template': ('Select', '#template', 'Marketing Tab'),
        'description': ('TypeInCkeditor', '.cke_wysiwyg_frame', '&descText;'),
    }
    expected = runtime['subtitleText']
    process = UI()
    process.update(runtime)
    order = ('edit', 'subtitle', 'description', )
    process.execute(order)
    actual = process.spy('#jobs__job_board_subtitle', 'value')
    process.compare(expected, actual)
    process.wait(1)
    process.teardown()
