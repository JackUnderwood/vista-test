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
        'addAdjustment': (
            'Click', '//*[@id="revenue-table"]/tbody[2]/tr[9]/td/a'),
        'assignNumber': (
            'Type',
            '//*[@id="revenue-table"]/tbody[2]/tr[9]/td[1]/input[2]',
            '123456789'),
        'findClient': (
            'Type', '//*[@id="adj_client_id_desc"]', 'care'),
        'selectCare': ('Click', '//*[@item_id="198206"]'),
        'findProvider': (
            'Type', '//*[@id="adj_provider_id_desc"]', 'matt lambert st:wv'),
        'selectProvider': ('Click', '//*[@item_id="91273"]'),
        'amount': (
            'Type',
            '//*[@id="revenue-table"]/tbody[2]/tr[9]/td[4]/input',
            '25000'),
        'save': (
            'Click',
            '//*[@id="revenue-table"]/tbody[2]/tr[9]/td[5]/a[1]/i'),
    }  #
    expected = "Saved adjustment"
    process = UI()
    process.update(runtime)
    order = ('find', 'result', 'month', 'year', 'addAdjustment',
             'assignNumber', 'findClient', 'selectCare', 'findProvider',
             'selectProvider', 'amount', 'save')
    process.execute(order)
    process.wait(2)
    process.results(expected)
    process.wait(2)
    process.teardown()
