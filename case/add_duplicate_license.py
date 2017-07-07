from ui import UI
from ui.low.license import License
from tool.generators.state_codes import get_state_name
from tool.generators.generator import get_future_date
from tool.data_access import get_credential_fullname

__author__ = 'John Underwood'


class AddDuplicateLicense(UI):
    """
    Prerequisite requires a license of this type - may require running this
    test twice.
    """
    runtime = {
        'all': ('Click', '//*[@id="checklist-form-container"]/div[1]/a'),
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
    process.execute(('all', ))
    state = process.spy('//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[7]',
                        'innerHTML')
    type = process.spy('//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[8]',
                       'innerHTML')
    cred = process.spy('//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[9]',
                       'innerHTML')
    provider = process.spy(
        '//*[@id="licenseRequestsGrid_grid"]/tbody/tr[1]/td[4]/a', 'innerHTML')

    full_state_name = get_state_name(state)
    full_cred_name = get_credential_fullname(cred)
    desired_date = get_future_date(days=60, style='%m%d%Y')

    process.update({
        'stateOfLicense': ('Select', '#state_code_id', full_state_name),
        'credentialType': ('Select', '#credential_id', full_cred_name,),
        'licenseType': ('Select', '#license_type_id', type),
        'findEntity': ('Type', '#entity_id_number_desc', provider),
        'dateDesired': ('Type', '#date_desired', desired_date),
    })
    order = ('addRequest', 'findEntity', 'selectEntity', 'findUser',
             'selectUser', 'licensor', 'stateOfLicense', 'credentialType',
             'licenseType', 'team', 'status', 'assignmentStatus', 'dateDesired',
             'notes', 'save', )
    process.execute(order)
    process.wait(2)
    process.results(expected)
    process.wait(3)
    process.teardown()
