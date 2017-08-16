import ui
from tool.jobpost.helpers import get_class_attribute, get_job_status, get_color
from tool.jobpost.helpers import get_row_numbers
from tool.utilities import get_random_value
from ui import UI
from ui.high.job_search import JobSearch
from ui.low.job_posts import JobPosts

__author__ = 'John Underwood'


class JobStatusUpdate(UI):
    """
    To access a condition, you'll need to change the job_id. For example, 
    if you want to access the first condition, then use a job number that 
    is not ready (white).
    
    Regression test for story #129534633 - check that job row's status
    (background color) updates. class=
    nopost      rust    #ffddbb
    approved    green   #cceecc
    ready       blue    #cceeee
    rejected    purple  #ffccff
    """
    statuses = {'nopost': '#ffddbb',
                'approved': '#cceecc',
                'ready': '#cceeee',
                'rejected': '#ffccff'}
    JobPosts()

    override = {'value': '80000-97000'}
    JobSearch(override)
    runtime = {}

    process = UI()
    all_rows = get_row_numbers(process)
    # Every other index is empty, i.e. ['97000', '', 96999, '', ..., '']
    rows = [r for r in all_rows if r != '']
    row_job_number = get_random_value(rows)
    ui.log.info("JOB NUMBER: {}".format(row_job_number, ))
    row_index = all_rows.index(row_job_number) + 1  # offset for zero-base list

    locator = '//*[@id="result-target"]/tbody/tr[{}]'.format(row_index,)
    class_attributes = get_class_attribute(process, locator)
    ui.log.info("CLASS: {}".format(class_attributes, ))
    class_attr_status = get_job_status(class_attributes)
    ui.log.info("STATUS: {}".format(class_attr_status, ))
    expected_status = None
    expected_color = None
    if class_attr_status is None:
        # Change from 'not ready' (white) to 'ready' (blue)
        expected_status = 'ready'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        runtime = {
            'edit': ('Click', '#edit_{}'.format(row_job_number)),
            'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle'),
            'template': ('Select',
                         '#JobDescriptionTemplates__job_description_template_id',
                         'Allergy'),
            'ready': (
                'Click',
                '//*[@id="jobEdit"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/label'),
            'save': ('Click', '#edit-save')
        }
        process.update(runtime)
        process.execute(('edit', 'subtitle', 'template',))
        process.accept_alert()
        process.execute(('ready', 'save',))

    elif class_attr_status == "ready":
        # Change from "Ready to Post" to "Approved"
        expected_status = 'approved'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        process.update({
            'expand': ('Click', locator),
            'approve': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[1]'.
                format(row_job_number)),
        })
        process.execute(('expand', 'approve', ))

    elif class_attr_status == "approved":
        # Change from "Approved" to "Rejected"
        expected_status = 'rejected'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        process.update({
            'expand': ('Click', locator),
            'reject': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[2]'.
                format(row_job_number)),
            'wait': (
                'Wait', '#job_board_rejection_history__rejection_reason_id',
                {'condition': 'element_to_be_clickable'}),
            'other': ('Select',
                      '#job_board_rejection_history__rejection_reason_id',
                      'Other'),
            'confirm': ('Click', '#confirm-reject'),
            'save': ('Click', '#edit-save'),
            'waitForExpand': (
                # The drawer hides 'expand' button; when drawer dismisses,
                # the expand button is available again
                # Todo: the 'wait_for_element()' is not working as expected
                'Wait', '//*[@id="result-target"]/thead/tr[1]/td[3]/i[1]',
                {'condition': 'element_to_be_clickable'}),
        })
        process.execute(('expand', ))
        process.wait()
        rejected_state = process.spy('#inGrid_reject_{}'.format(row_job_number),
                                     'checked')
        if rejected_state == 'checked':
            ui.log.warning('rejected box already checked')
            process.wait()
            process.teardown()

        process.execute(('reject', 'wait', 'other', 'confirm', 'save',
                         'waitForExpand'))
        process.wait(2)

    # elif class_attr == "nopost":
    #     # Change to Approved
    #     pass
    #
    # elif class_attr == "rejected":
    #     # Change to Approved
    #     pass
    #
    else:
        pass
    process.wait(2)  # give the row time to refresh its values
    actual_status = get_class_attribute(process, locator)
    process.compare(expected_status, actual_status,
                    message="compare status value")

    rgb = process.get_css_property(locator, 'background-color')
    actual_color = get_color(rgb)
    process.compare(expected_color, actual_color,
                    message="compare background color")

    process.wait()
    process.teardown()
