import ui
from ui import UI


class Check(UI):
    """
    Use this class to check newly created ui/high, ui/low classes, or
    case classes.
    Change the import statement above.
    Change the class call below.
    """
    ui.log.debug("INSIDE CHECKER")
    process = UI()
    from ui.low.job_posts import JobPosts
    from ui.high.job_active_hot import JobActiveHot
    JobPosts()
    process.wait()
    JobActiveHot()

    # Reserve - do not alter anything below ^*^*^*^*^*^
    process.wait(5)
    process.teardown()
