__author__ = 'John Underwood'
from ui import UI
# from ui.low.goals_team_revenue_bonus import GoalsTeamRevenueBonus
# from ui.low.goals_commission_rates import GoalsCommissionRates
# from ui.low.goals_commission_report import GoalsCommissionReport
from ui.low.goals_sales_base import GoalsSalesBase

class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    # GoalsTeamRevenueBonus()  # currently the page is blank
    # UI().results("")

    # GoalsCommissionRates()
    # UI().results("Commission Rates")

    # GoalsCommissionReport()
    # UI().results("Commission Report")

    GoalsSalesBase()
    UI().results("Standard Sales Base")

    # Reserve - do not alter anything below
    UI().wait(5)
    UI().teardown()
