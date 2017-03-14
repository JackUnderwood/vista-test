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

    if class_attr == "approved":
        # Change to Ready to Post
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif class_attr == "ready":
        # Change to Reject
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif class_attr == "nopost":
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    elif class_attr == "rejected":
        # Change to Approved
        runtime['click'] = ('Click', '#job_board_post_status__is_ready_to_post')
    else:
        pass

    process.wait()
    process.teardown()
