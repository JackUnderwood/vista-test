import ui
from ui import UI
from ui.low.job_posts import JobPosts
__author__ = 'John Underwood'


class JobStatusUpdate(UI):
    """
    Regression test for story #129534633 - check that job row's status
    (background color) updates.
    """
    JobPosts()


    runtime = {
        '': ('', ''),
    }
