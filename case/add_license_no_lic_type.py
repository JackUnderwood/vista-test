from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddLicenseNoLicenseType(UI):
    """
    Very similar to AddLicense, but looking for a 'Cannot be blank' warning
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
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[1]/span'
        ),
        'newLicense': ('Click', '//*[@id="licenseGrid_form"]/a'),
        'licenseStanding': ('Select', '#license_standing', 'Good'),
        'selectState': ('Select', '#state_code_id', 'Oregon'),
        'credentialType': ('Select', '#credential_id', 'Medical Doctor'),
        'licenseType': ('Select', '#license_type_id', 'Permanent'),
        'dateGranted': ('Type', '#date_granted', '05042015'),
        'dateEffective': ('Type', '#date_effective', '05182015'),
        'licenseNumber': ('Type', '#license_number', 'n2676961'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "License Type"  # 'Cannot be blank'
    process = UI()
    process.update(runtime)
    order = ('licenseIcon', 'newLicense', 'selectState',
             'credentialType', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
