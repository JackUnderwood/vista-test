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
    override = {'value': '97867'}
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
        job_id = process.spy(
            '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
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
        job_id = process.spy(
            '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        process.update({
            'expand': ('Click', '//*[@id="result-target"]/tbody/tr[1]'),
            'approve': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[1]'.
                format(job_id)),
        })
        process.execute(('expand', 'approve', ))

    elif class_attr == "ready":
        # Change to Reject
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif class_attr == "nopost":
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif class_attr == "rejected":
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_rejection_history__is_rejected')
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
