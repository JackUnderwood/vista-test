import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_search import JobSearch
__author__ = 'John Underwood'


class JobStatusUpdate(UI):
    """
    Regression test for story #129534633 - check that job row's status
    (background color) updates. class=
    nopost      rust    #fdb
    approved    green   #cec
    ready       blue    #cee
    rejected    purple  #fcf
    """
    JobPosts()
    override = {'value': '92137'}
    JobSearch(override)
    runtime = {}

    process = UI()
    class_attr = process.spy(
        '//*[@id="result-target"]/tbody/tr[1]', 'class')
    class_attr = class_attr.strip()
    ui.log.info("CLASS: {}".format(class_attr, ))

    if "approved" in class_attr:
        # Change to Ready to Post
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif "ready" in class_attr:
        # Change to Reject
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif "nopost" in class_attr:
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif "rejected" in class_attr:
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_rejection_history__is_rejected')
    else:
        pass

    process.wait()
    process.teardown()
