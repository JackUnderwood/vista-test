__author__ = 'John Underwood'
from ui import UI
from ui.low.goals_corporate import GoalsCorporate


class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    GoalsCorporate()

    UI().teardown()
