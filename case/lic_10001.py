__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License


class Lic10001(UI):
    runtime = {
        'addRequest': (
            'Click',
            '//*[@id="licenseRequestsGrid_form"]/a',
        ),
        'findEntity': ('Type', '#entity_id_number_desc', 'matt lambert'),
        'selectEntity': ('Click', '#91273'),  # lambert's unique id
        'wait': ('Wait', 'user_name', 5),
        'findUser': ('Type', '#requester_id_desc', 'john underwood'),
        'selectUser': ('Click', '#1515'),
        'licensor': ('Select', '#owner_id', 'Crystal Liebl'),
        'stateOfLicense': ('Select', '#state_code_id', 'Virginia'),
        'credentialType': ('Select', '#credential_id', 'Medical Doctor', ),
        'licenseType': ('Select', '#license_type_id', 'Permanent'),
        'team': ('Select', '#team_id', 'Family Practice'),
        'status': ('Select', '#license_status_id', 'Assigned'),
        'assignmentStatus': ('Select', '#license_purpose_id',
                             'Scheduled Assignment'),
        'dateDesired': ('Type', '#date_desired', '10152016'),
        'notes': ('Type', '#note', 'Lorem ipsum dolor sit amet , mea ne ipsum'),
        'save': ('Click', '#license-change-confirm'),

        # result: "Saved Request and notification sent to Licensing User"
    }
    License()
    process = UI()
    process.update(runtime)
    order = ('addRequest', 'findEntity', 'selectEntity', 'wait', 'findUser',
             'selectUser', 'licensor', 'stateOfLicense', 'credentialType',
             'licenseType', 'team', 'status', 'assignmentStatus', 'dateDesired',
             'notes', 'save', )
    process.execute(order)
    process.wait(5)
    process.teardown()

