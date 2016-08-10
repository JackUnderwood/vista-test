from ui import UI


class Check(UI):
    """
    Use this class to check newly created ui/high or ui/low classes.
    Change the import statement above.
    Change the class call below.
    """
    process = UI()
    from ui.low.transfer_ful import TransferFollowUpLogs
    TransferFollowUpLogs()

    # from ui.low.license import License
    # from ui.high.checklist import Checklist
    # from tool.db import get_record

    # License()
    # cl = Checklist()
    # print("ENTITY: {}".format(cl.entity))

    # Test the new db module *^*^*^*^*^*
    # sql = """
    #     SELECT *
    #     FROM name_list nl
    #     WHERE nl.entity_id_number = 778785
    # """
    # results = get_record(sql)
    # for row in results:
    #     print("ID={}, Name={}, First={}".format(row[0], row[1], row[2]))

    # from ui.low.user_secret import UserSecret
    # UserSecret()

    # from ui.low.file import File
    # from ui.high.file_select import FileSelect
    # File()
    # process.results("John Underwood")
    # override = {
    #     'cat': '3',
    # }
    # FileSelect(override)

    # from ui.low.license import License
    # License()
    # process.results("License Request")

    # from ui.low.sales_team_revenue_bonus import SalesTeamRevenueBonus
    # SalesTeamRevenueBonus()  # currently the page is blank
    # process.results("")

    # from ui.low.sales_commission_rates import SalesCommissionRates
    # SalesCommissionRates()
    # process.results("Commission Rates")

    # from ui.low.sales_commission_report import SalesCommissionReport
    # SalesCommissionReport()
    # process.results("Commission Report")

    # from ui.low.sales_base import SalesBase
    # SalesBase()
    # process.results("Standard Sales Base")

    # Reserve - do not alter anything below
    process.wait(3)
    process.teardown()
