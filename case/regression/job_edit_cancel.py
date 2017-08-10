import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch
__author__ = 'John Underwood'


class JobEditCancel(UI):
    """
    Regression test for story #129542317 - Edit Job drawer's Cancel button should
    not display 'Are you sure you want to lose your work?' alert box when no
    changes have been made.
    """
    ui.log.info("JobEditCancel __init__() called")
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
        'cancelEdit': ('Click', '#edit-close'),
        'reset': ('Click', '//*[@id="job-search-wrap"]/div[3]/div[3]/button')
    }
    process.update(runtime)
    order = ('edit',)
    process.execute(order)
    process.wait_for_element(
        '#JobDescriptionTemplates__job_description_template_id', wait_time=10)
    order = ('cancelEdit', )
    process.execute(order)

    # Click on Reset button, if Alert is displayed, then Reset button is not
    # available and the test should throw an exception, and fail the test.
    # Use the page title as a pseudo result.
    order = ('reset', )
    process.execute(order)
    process.results("Manage Job Posts")

    process.wait(1)
    process.teardown()


