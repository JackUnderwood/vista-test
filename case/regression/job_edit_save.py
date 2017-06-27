import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch
__author__ = 'John Underwood'


class JobEditSave(UI):
    """
    Regression test for story #129543903 - Edit Job drawer's Save button
    """
    ui.log.info("JobEditSave __init__() called")
    JobPosts()
    override = {'value': '90000-92150'}
    JobSearch(override)

    process = UI()

    # Get the first row's job number.
    job_number = process.spy(
        '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
    ui.log.info("JobNumber: {}".format(job_number, ))

    edit_button_id = '#edit_{}'.format(job_number, )

    runtime = {
        'edit': ('Click', edit_button_id),
    }
    process.update(runtime)
    order = ('edit',)
    process.execute(order)
    process.wait_for_element(
        '#JobDescriptionTemplates__job_description_template_id', wait_time=10)
    value_in_class = process.spy('#edit-save', 'class')
    ui.log.info("RESULT: {}".format(value_in_class, ))

    actual = 'disabled' in value_in_class
    process.compare(True, actual, 'Is the Save button "disabled"? {}'.
                    format('YES' if actual else 'NO'))
    process.wait(1)
    process.teardown()
