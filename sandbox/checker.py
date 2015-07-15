__author__ = 'John Underwood'
from ui import UI
from ui.low.goals_team_revenue_bonus import GoalsTeamRevenueBonus

class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    GoalsTeamRevenueBonus()

    UI().wait(5)
    UI().teardown()
