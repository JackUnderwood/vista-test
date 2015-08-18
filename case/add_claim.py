__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

NOTES = """Id vix minimum philosophia, pri clita lobortis inimicus ex. Qui
decore nusquam id. Eum modo electram deseruisse no, eos at clita menandri.
Vel alii cetero saperet in, mea te erant causae labitur, liber partiendo
est et.  Et vix malis intellegat consectetuer, mel regione democritum id, cum
delicata iracundia ea. Pro cu saepe eligendi dissentias, detraxit evertitur in
eos. Nonumes suscipit scaevola duo te, eam quot facer constituto cu, ex causae
utamur inimicus mei."""


class AddClaim(UI):
    License()
    Checklist()

    runtime = {
        'malpractice': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[4]'),
        'addClaim': ('Click', '//*[@id="malpracticeGrid_form"]/a[1]'),
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
