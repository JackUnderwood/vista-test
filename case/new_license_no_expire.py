__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class NewLicenseNoExpire(UI):
    """
    Very similar to NewLicense
    """
    License()
    Checklist()

    runtime = {
        'expandRibbon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[1]/div/div[1]'
        ),
        'licenseIcon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[2]/div[3]/div/a[7]'
        ),
        'newLicense': ('Click', '//*[@id="licenseGrid_form"]/a'),
        'licenseStanding': ('Select', '#license_standing', 'Good'),
        'selectState': ('Select', '#state_code_id', 'Idaho'),
        'credentialType': ('Select', '#credential_id', 'Medical Doctor'),
        'licenseType': ('Select', '#license_type_id', 'Permanent'),
        'dateGranted': ('Type', '#date_granted', '05042015'),
        'dateEffective': ('Type', '#date_effective', '05182015'),
        'licenseNumber': ('Type', '#license_number', 'n2676961'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Expiration Date"  # should be "Expiration Date"; was Experation
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', 'licenseIcon', 'newLicense', 'licenseStanding',
             'selectState', 'credentialType', 'licenseType', 'dateGranted',
             'dateEffective', 'licenseNumber', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
