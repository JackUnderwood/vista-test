from ui import UI


class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    process = UI()
    from ui.low.job_posts import JobPosts
    from ui.high.job_active_hot import JobActiveHot
    JobPosts()
    process.wait()
    JobActiveHot()

    # Reserve - do not alter anything below ^*^*^*^*^*^
    process.wait(5)
    process.teardown()
