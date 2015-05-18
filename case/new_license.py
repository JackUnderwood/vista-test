__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class NewLicense(UI):
    License()
    Checklist()

    runtime = {
        'expandRibbon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[1]/div/div[1]'
        ),
        'licenseIcon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[2]/div[3]/div/a[6]'
        ),
        'newLicense': ('Click', '//*[@id="license_form"]/a'),
        'selectCredential': ('Select', '#credential_code', 'Medical Doctor'),
        'selectLicenseType': ('Select', '#license_type', 'Permanent'),
        'selectLicenseStanding': ('Select', '#license_standing', 'Good'),
        'selectState': ('Select', '#state_issued', 'Georgia'),
        'dateGranted': ('Type', '#date_granted', '05042015'),
        'dateEffective': ('Type', '#date_effective', '05182015'),
        'save': ('Click', '//*[@id="entityLicense_form"]/div[2]/a[1]')
    }
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', 'licenseIcon', 'newLicense', 'selectCredential',
             'selectLicenseType', 'selectLicenseStanding', 'selectState',
             'dateGranted', 'dateEffective', 'save', )
    process.execute(order)
    process.wait(5)
    process.teardown()
