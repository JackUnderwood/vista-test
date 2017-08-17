from ui import UI
from ui.low.job_posts import JobPosts
from tool.jobpost.helpers import find_white_rows

__author__ = 'John Underwood'


class JobEdit(UI):
    """
    Fill in necessary elements using incomplete (white) job and save the
    filled job.
    """
    JobPosts()

    runtime = {
        'jobStatus': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                               'ui-corner-all.multi_s.multi_s_job_status'),
        'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                 {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
        'jobStatusActive': (
            'Click', '#ui-multiselect-s_job_status-option-1'),
        'jobStatusHot': (
            'Click', '#ui-multiselect-s_job_status-option-4'),
        'pageSize': ('Select', '#page-size', '100')
    }
    process = UI()
    process.update(runtime)
    order = ('jobStatus', 'wait', 'jobStatusActive', 'jobStatusHot')
    process.execute(order)
    process.wait()
    process.execute(('pageSize', ))
    process.wait()

    # Get only the 'white' rows--rows with no status set.
    job_number = find_white_rows(process)
    if job_number is None:
        pass
    # # rows = process.find_elements(
    # #    '//*[@id="result-target"]/tbody/tr[@class=" " or @class="odd "]')
    # if not rows:
    #     process.compare(True, False, message="no white row jobs available")
    # else:
    #     row_ids = [row.find_element_by_xpath('./td[1]').text for row in rows]
    #     job_number = row_ids.pop(0)

    runtime = {
        'subtitleText': "Get Started Right Away",
        'descText': "Some text",
        'edit': ('Click', '#edit_' + job_number,),
        'subtitle': ('Type', '#jobs__job_board_subtitle', '&subtitleText;'),
        'template': ('Select', '#template', 'Marketing Tab'),
        'description': ('TypeInCkeditor', '.cke_wysiwyg_frame', '&descText;'),
        'save': ('Click', '#edit-save')
    }
    expected = runtime['subtitleText']
    process = UI()
    process.update(runtime)
    order = ('edit', 'subtitle', 'description', )
    process.execute(order)
    actual = process.spy('#jobs__job_board_subtitle', 'value')
    process.compare(expected, actual)

    expected = 'Job Saved'
    process.execute(('save',))
    process.wait()
    process.results(expected)

    process.wait()
    process.teardown()
