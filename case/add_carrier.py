__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddCarrier(UI):
    License()
    Checklist()

    runtime = {
        'malpractice': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[4]'),
        'addCarrier': ('Click', '//*[@id="malpractice_form"]/a[2]'),
        'findInsuranceProvider': ('Type', '#insurance_provider_id_desc', 'ame'),
        'selectInsuranceProvider': ('Click', '#167224'),  # Neurology
        'startDate': ('Type', '#start_date', '01072015'),
        'endDate': ('Type', '#end_date', '05182015'),
        'coverageAmount': ('Type', '#coverage_amount', '2000000'),
        'policyNumber': ('Type', '#policy_number', 'WWF42BAR69'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Carrier saved"
    process = UI()
    process.update(runtime)
    order = ('malpractice', 'addCarrier', 'findInsuranceProvider',
             'selectInsuranceProvider', 'startDate', 'endDate',
             'coverageAmount', 'policyNumber', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
