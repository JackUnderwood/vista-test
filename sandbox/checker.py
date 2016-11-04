from ui import UI


class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    process = UI()
    from ui.low.find import Find
    Find()

    # Reserve - do not alter anything below ^*^*^*^*^*^
    process.wait(5)
    process.teardown()
