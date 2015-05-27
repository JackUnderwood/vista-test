__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class SendCorrespond(UI):
    License()
    Checklist()

    runtime = {
        'expandRibbon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li[1]/div[1]/div/div[1]'
        ),
        'correspondIcon': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div/a[1]/i'
        ),
        'selectTemplate': (
            'Click',
            '//*[@id="correspondenceChooser_form"]/p[2]/p[7]/a'
        ),

        'licenseStanding': ('Select', '#license_id', 'Good'),
        'selectState': ('Select', '#state_code_id', 'Idaho'),
        'credentialType': ('Select', '#credential_id', 'Medical Doctor'),
        'licenseType': ('Select', '#license_type_id', 'Permanent'),
        'dateGranted': ('Type', '#date_granted', '05042015'),
        'dateEffective': ('Type', '#date_effective', '05182015'),
        'dateExpires': ('Type', '#date_expires', '10102016'),
        'licenseNumber': ('Type', '#license_number', 'n2676961'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Licenses Updated"  # "Licenses Updated Comment Created"
    process = UI()
    process.update(runtime)
    order = ('expandRibbon', 'correspondIcon', 'selectTemplate',
             'licenseStanding',
             'selectState', 'credentialType', 'licenseType', 'dateGranted',
             'dateEffective', 'dateExpires', 'licenseNumber', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
