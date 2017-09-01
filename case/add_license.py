from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import gen_account_number

__author__ = 'John Underwood'


class AddLicense(UI):
    License()
    Checklist()

    license_number = gen_account_number(size=10)

    runtime = {
        'licenseIcon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[1]/span'
        ),
        'newLicense': ('Click', '//*[@id="licenseGrid_form"]/a[1]'),
        'licenseStanding': ('Select', '#license_standing', 'Good'),
        'selectState': ('Select', '#state_code_id', 'Oregon'),
        'credentialType': ('Select', '#credential_id', 'Medical Doctor'),
        'licenseType': ('Select', '#license_type_id', 'Permanent'),
        'dateGranted': ('Type', '#date_granted', '05042015'),
        'dateEffective': ('Type', '#date_effective', '05182015'),
        'dateExpires': ('Type', '#date_expires', '10102016'),
        'licenseNumber': ('Type', '#license_number', license_number),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Licenses Updated"  # "Licenses Updated Comment Created"
    process = UI()
    process.update(runtime)
    order = ('licenseIcon', 'newLicense', 'licenseStanding',
             'selectState', 'credentialType', 'licenseType', 'dateGranted',
             'dateEffective', 'dateExpires', 'licenseNumber', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
