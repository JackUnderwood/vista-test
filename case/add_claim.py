from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'

NOTES = """In computer programming, a placeholder is a character, word, or 
string of characters that may be used to take up space until such a time that 
the space is needed. For example, a programmer may know that He needs a certain 
number of values or variables, but doesn't yet know what to input. He can use 
a placeholder as a temporary solution until a proper value or variable can be 
assigned. For example, the designer of an online newsletter may have a template 
that they fill with dummy text so they can get an idea of how to layout a page 
looks. One of the most common filler texts is lorem ipsum."""


class AddClaim(UI):
    License()
    Checklist()

    runtime = {
        'malpractice': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/li[5]/a'),
        'addClaim': ('Click', '//*[@id="malpracticeGrid_form_inline"]/a[1]'),
        'findInsuranceProvider': ('Type', '#insurance_provider_id_desc', 'ame'),
        'selectInsuranceProvider': ('Click', '#62963'),  # Orthopaedic Surgeons
        'status': ('Select', '#claim_status_id', 'Open'),
        'startDate': ('Type', '#start_date', '01062015'),
        'endDate': ('Type', '#end_date', '05172015'),
        'description': ('Type', '#description', 'Needle in a haystack'),
        'settleAmount': ('Type', '#settlement_amount', '550000'),
        'claimNumber': ('Type', '#claim_number', 'WTF42FOO69'),
        'note': ('Type', '#note', NOTES),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Claim saved"
    process = UI()
    process.update(runtime)
    order = ('malpractice', 'addClaim', 'findInsuranceProvider',
             'selectInsuranceProvider', 'status', 'startDate', 'endDate',
             'description', 'settleAmount', 'claimNumber', 'note', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
