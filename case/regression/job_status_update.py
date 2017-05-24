import re

import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch
__author__ = 'John Underwood'


def get_class_attribute(process, locator):
    class_attr = process.spy(locator, 'class')
    class_attr = class_attr.strip()
    ui.log.info("CLASS: {}".format(class_attr, ))
    return class_attr


def get_color(rgb):
    res = re.search(r'rgba\((\d+),\s*(\d+),\s*(\d+)', rgb).group()
    r, g, b = [int(s) for s in re.findall('\\d+', res)]
    hex_color = '#%02x%02x%02x' % (r, g, b)
    return hex_color


def get_job_status(class_attribute):
    status = None
    if "approved" in class_attribute:
        status = "approved"
    elif "ready" in class_attribute:
        status = "ready"
    elif "nopost" in class_attribute:
        status = "nopost"
    elif "rejected" in class_attribute:
        status = "rejected"
    else:
        pass
    return status


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
    job_id = '97848'
    override = {'value': job_id}
    JobSearch(override)
    runtime = {}

    process = UI()
    locator = '//*[@id="result-target"]/tbody/tr[1]'
    class_attributes = get_class_attribute(process, locator)
    class_attr = get_job_status(class_attributes)
    expected_status = None
    expected_color = None
    if class_attr is None:
        # Change from 'not ready' (white) to 'ready' (blue)
        expected_status = 'ready'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        runtime = {
            'edit': ('Click', '#edit_{}'.format(job_id)),
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

    elif class_attr == "ready":
        # Change from "Ready to Post" to "Approved"
        expected_status = 'approved'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        process.update({
            'expand': ('Click', '//*[@id="result-target"]/tbody/tr[1]'),
            'approve': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[1]'.
                format(job_id)),
        })
        process.execute(('expand', 'approve', ))

    elif class_attr == "approved":
        # Change from "Approved" to "Rejected"
        expected_status = 'rejected'
        expected_color = statuses[expected_status]
        # job_id = process.spy(
        #     '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        process.update({
            'expand': ('Click', '//*[@id="result-target"]/tbody/tr[1]'),
            'reject': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[2]'.
                format(job_id)),
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
        rejected_state = process.spy('#inGrid_reject_{}'.format(job_id),
                                     'checked')
        if rejected_state == 'checked':
            ui.log.warning('rejected box already checked')
            process.wait()
            process.teardown()

        process.execute(('reject', 'wait', 'other', 'confirm', 'save',
                         'waitForExpand'))
        process.wait(8)

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

    actual_status = get_class_attribute(process, locator)  # 'ready'
    process.compare(expected_status, actual_status,
                    message="compare status value")

    rgb = process.get_css_property(
        '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
    actual_color = get_color(rgb)
    process.compare(expected_color, actual_color,
                    message="compare background color")

    process.wait()
    process.teardown()
