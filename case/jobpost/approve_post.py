from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch

__author__ = 'John Underwood'


class ApprovePost(UI):
    """
    Test the Approved job button in both areas of the app.
    -The button inside the expanded row.
    -The button inside the Edit Job drawer/page.
    Uses the Job Board Status option 'Ready to Post'
    """
    JobPosts()

    runtime = {
        'JobBoardStatus': ('Click', 'css=.ui-multiselect.ui-widget.'
                                    'ui-state-default.ui-corner-all.multi_s.'
                                    'multi_s_job_board_status'),
        'JobBoardStatusReady': (
            'Click', '#ui-multiselect-s_job_board_status-option-2'),
    }
    process = UI()
    process.update(runtime)
    order = ('JobBoardStatus', 'JobBoardStatusReady', )
    process.execute(order)
    # Check the first job on the list
    job_number = process.spy(
        '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')

    runtime.update({
        'view': ('Click', '#view_{}'.format(job_number,)),
    })
    process.update(runtime)
    order = ('view', )
    process.execute(order)
    attr_class = process.spy('//*[@id="result-target"]/tbody/tr[1]', 'class')
    ready_to_post = process.spy(
        '//*[@id="expandable_{}"]/td/div/div[3]/div[2]/div[4]/div/div/div[2]'.
        format(job_number,), 'innerHTML')

    expected = "Approval for job {} saved".format(job_number, )
    if 'ready' in attr_class:
        runtime = {'approve': ('Click', '//*[@for="inGrid_approve_{}"]'.
                               format(job_number))}
        process.update(runtime)
        process.execute(('approve',))
        process.wait(1)
        process.results(expected, locator='toast-container',
                        message='approved the job')
    else:
        process.compare(True, False, message='not set to "Ready to Post"')

    process.wait(3)
    process.teardown()
