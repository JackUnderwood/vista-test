from ui import UI
from ui.low.license import License

__author__ = 'John Underwood'


class AddRequest(UI):
    runtime = {
        'addRequest': (
            'Click', 'css=#licenseRequestsGrid_form>div.row>div.col.s9>a'),
        'findEntity': ('Type', '#entity_id_number_desc', 'Peter Bertolozzi'),
        'selectEntity': ('Click', '#user_name'),  # bertolozzi's unique id
        'findUser': ('Type', '#requester_id_desc', 'john underwood'),
        'selectUser': ('Click', '#1515'),
        'licensor': ('Select', '#owner_id', 'Crystal Liebl'),
        'stateOfLicense': ('Select', '#state_code_id', 'Vermont'),
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
        # //*[@id="toast-container"]/div
        # # "This would create a duplicate license."
    }
    expected = "This would create a duplicate license"
    License()
    process = UI()
    process.update(runtime)
    order = ('addRequest', 'findEntity', 'selectEntity', 'findUser',
             'selectUser', 'licensor', 'stateOfLicense', 'credentialType',
             'licenseType', 'team', 'status', 'assignmentStatus', 'dateDesired',
             'notes', 'save', )
    process.execute(order)
    process.wait(2)
    process.results(expected)
    process.wait(3)
    process.teardown()
