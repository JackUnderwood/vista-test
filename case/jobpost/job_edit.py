import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_active_hot import JobActiveHot
from tool.jobpost.helpers import find_white_rows
from tool.generators.generator import gen_key

__author__ = 'John Underwood'


class JobEdit(UI):
    """
    Fill in necessary elements using incomplete (white) job and save the
    filled job.
    """
    JobPosts()
    JobActiveHot()

    runtime = {
        'pageSize': ('Select', '#page-size', '100'),
    }
    process = UI()
    process.update(runtime)
    process.wait()
    process.execute(('pageSize', ))
    process.wait(2)

    # Get only the 'white' rows--rows with no status set.
    res = find_white_rows(process)
    if res['job_number'] is None:
        ui.log.warning('{} :: job_number not available test case stopped!'.
                       format(res['error_msg']))
        process.teardown()

    runtime = {
        'subtitleText': "Get Started Right Away {}".format(gen_key(5),),
        'descText': "Some text",
        'edit': ('Click', '#edit_' + res['job_number'],),
        'subtitle': ('Type', '#jobs__job_board_subtitle', '&subtitleText;'),
        'template': ('Select',
                     '#JobDescriptionTemplates__job_description_template_id',
                     'Cardiology'),
        'description': ('TypeInCkeditor', '.cke_wysiwyg_frame', '&descText;'),
        'save': ('Click', '#edit-save'),
        'expand': ('Click', '#view_{}'.format(res['job_number'],)),
        'ready': (
            'Click',
            '//*[@id="jobEdit"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/label')
    }
    expected = runtime['subtitleText']
    # process = UI()
    process.update(runtime)
    order = ('edit', 'subtitle', 'template', )
    process.execute(order)
    process.accept_alert()
    actual = process.spy('#jobs__job_board_subtitle', 'value')
    process.compare(expected, actual)

    process.execute(('ready', 'save',))
    process.wait()
    process.execute(('expand',))
    process.results(expected)

    process.wait()
    process.teardown()
