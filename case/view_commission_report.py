__author__ = 'John Underwood'

from ui import UI
from ui.low.sales_commission_report import SalesCommissionReport


class ViewCommissionReport(UI):
    SalesCommissionReport()

    runtime = {
        'find': ('Type', '#user_key_id_desc', 'Catherine Dotson'),
        'result': ('Click', '//*[@associated-id="user_key_id_desc"]'),
        'month': ('Select', '#month', 'March'),
        'year': ('Select', '#year', '2015'),
    }
    expected = "16,674.67"
    process = UI()
    process.update(runtime)
    order = ('find', 'result', 'month', 'year', )
    process.execute(order)
    process.wait(2)
    process.results(expected)
    process.wait(2)
    process.teardown()
