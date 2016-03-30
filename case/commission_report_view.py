from ui import UI
from ui.low.sales_commission_report import SalesCommissionReport

__author__ = 'John Underwood'


class ViewCommissionReport(UI):
    """
    This case is not needed at this time.
    """
    SalesCommissionReport()

    runtime = {
        'find': ('Type', '#user_key_id_desc', 'Catherine Dotson'),
        'result': ('Click', '//*[@associated-id="user_key_id_desc"]'),
        'month': ('Select', '#month', 'March'),
        'year': ('Select', '#year', '2015'),
    }
    expected = "19,987.20"
    process = UI()
    process.update(runtime)
    order = ('month', 'find', 'result', 'year', )
    process.execute(order)
    process.wait(2)
    process.results(expected)
    process.wait(2)
    process.teardown()
