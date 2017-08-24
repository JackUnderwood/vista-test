import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_active_hot import JobActiveHot
from tool.jobpost.helpers import find_white_rows, enter_job_number

__author__ = 'John Underwood'


class JobAcceptEdit(UI):
    """
    Check that the JS alert box appears when trying to cancel an edited job.
    Looks for the Reset button element on the screen; if it can see Reset,
    then the drawer dismissed as expected.
    """
    process = UI()
    JobPosts()
    JobActiveHot()

    process.wait()
    res = find_white_rows(process)
    job_number = res['job_number']
    if job_number is None:
        ui.log.warning('{} :: job_number not available test case stopped!'.
                       format(res['error_msg']))
        process.teardown()

    runtime = {
        'subtitleText': "Rural Healthcare Central Texas",
        'edit': ('Click', '#edit_' + job_number,),
        'subtitle': ('Type', '#jobs__job_board_subtitle', '&subtitleText;'),
        'cancel': ('Click', '#edit-close', )
    }
    # expected = "Are you sure you want to lose your work?"
    process.scroll_to_top_of_page()
    process.wait()
    enter_job_number(process, job_number)
    process.update(runtime)
    order = ('edit', 'subtitle', 'cancel', )
    process.execute(order)

    alert_message_text = 'Are you sure you want to lose your work?'
    alert_text = process.accept_alert()
    # The Job Edit drawer should be gone; we're back to Manage Job Posts page
    actual = True if alert_message_text in alert_text else False
    process.compare(True, actual)
    process.wait()
    process.teardown()
