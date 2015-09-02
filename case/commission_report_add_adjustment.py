__author__ = 'John Underwood'

import ui
from ui import UI
from ui.low.sales_commission_report import SalesCommissionReport
from tool.utilities import strip_alpha


class ViewCommissionReport(UI):
    SalesCommissionReport()
    amount = 25000

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
            str(amount)),
        'save': (
            'Click',
            '//*[@id="revenue-table"]/tbody[2]/tr[9]/td[5]/a[1]/i'),
    }
    expected = "Saved adjustment"
    process = UI()
    process.update(runtime)
    order = ('find', 'result', 'month', 'year', )
    process.execute(order)
    process.wait(2)

    primary_total = process.get(
        '//*[@id="revenue-table"]/tbody[12]/tr[1]/td[9]', 'innerHTML')
    ui.log.info("PRIMARY {}".format(primary_total, ))
    primary_total = strip_alpha(primary_total)
    ui.log.info("PRIMARY NUMERIC {}".format(primary_total, ))

    order = ('addAdjustment', 'assignNumber', 'findClient', 'selectCare',
             'findProvider', 'selectProvider', 'amount', 'save')
    process.execute(order)

    rate = process.get(
        '//*[@id="revenue-table"]/tbody[1]/tr/td[1]/div', 'innerHTML')
    ui.log.info("RATE VALUE {}".format(rate, ))
    rate = strip_alpha(rate)

    adjusted_subtotal = rate * amount
    adjusted_total = process.get(
        '//*[@id="revenue-table"]/tbody[12]/tr[1]/td[9]', 'innerHTML')
    adjusted_total = strip_alpha(adjusted_total)
    ui.log.info("ADJUSTED {}".format(adjusted_total, ))
    ui.log.info("DIFFERENCE {}".format(adjusted_total - primary_total))
    ui.log.info("COMPARISON {}".
                format(adjusted_subtotal - (adjusted_total-primary_total)))
    process.compare(adjusted_subtotal, adjusted_total-primary_total)
    process.results(expected)
    process.wait(2)
    process.teardown()