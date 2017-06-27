from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.db import get_record
from tool.generators.state_codes import get_states

__author__ = 'John Underwood'


def create_license_dictionary(lic):
    """
    Return dictionary with keys 'state', 'credential', 'type'
    :param lic: string
    :return: dict
    """
    # states = get_states()
    lic = tuple(lic.split('/'))
    keys = ['state', 'credential', 'type']
    license_data = {key: lic[i] for i, key in enumerate(keys)}
    # license_data['state'] = "{} - {}".format(license_data['state'],
    #                                          states[license_data['state']][0])
    return license_data


def get_state_option(state):
    states = get_states()
    return "{} - {}".format(state, states[state][0])


def get_credential_option(credential):
    """
    Build an option for the Select Credential drop down.
    :param credential: string - a credential, such as 'MD'
    :return: string - option string, such as 'MD - Medical Doctor'
    """
    sql = """
        SELECT description
        FROM credential_code
        WHERE can_use = 1
        AND credential_name = '{}'
    """.format(credential, )
    record_set = get_record(sql)
    description = record_set[0][0] if record_set else ''
    return "{} - {}".format(credential, description)


def get_license_type_option(lic_type):
    """

    :param lic_type: string - license type such as 'Permanent'
    :return: string - license type option string, such as 'P - Permanent'
    """
    sql = """
      SELECT license_type
      FROM license_types_codes
      WHERE can_use = 'Y'
      AND description = '{}'
    """.format(lic_type,)
    record_set = get_record(sql)
    lic_code = record_set[0][0] if record_set else ''
    return "{} - {}".format(lic_code, lic_type)


class RequirementInactive(UI):
    """
    Regression test for story #113028615
    1 - Start on the Licensing Landing Page and click a provider's name
    2 - Click on one of the provider's requirement checklists
    3 - Click the Edit button on a requirement, set to inactive, and Save
    4 - Click on the Add Requirement button—plus sign
    5 - Create a new requirement, and Save
    Expected:
    The inactive requirement remains inactive
    """
    License()
    Checklist()

    runtime = {
        'checklist': ('Click', 'css=#content>div.row>div.col.s3>ul>'
                               'li:nth-child(7)>a'),
        'manage': (
            'Click',
            '//*[@id="checklist-form-container"]/div[3]/div[5]/a/i'),
        'active': (
            'Click',
            '//*[@id="stateLicenseRequirementEdit_form"]/div[1]/div[2]'
            '/label/span'),
        'save': (
            'Click', '//*[@id="stateLicenseRequirementEdit_form"]/div[5]/a[2]')
    }
    # #content>div.row>div.col.s3>ul>li:nth-child(7) > a
    process = UI()
    process.update(runtime)
    order = ('checklist', )
    process.execute(order)

    # Get the first Requirement's label
    initial = process.spy(
        '//*[@id="checklist-form-container"]/div[3]/div[1]/label',
        'innerHTML', ).strip()
    # Get the type of license, e.g. 'NY/DO/Permanent'
    license_string = process.spy(
        'css=#content>div.row>div.col.s3>ul>li:nth-child(7)>a', 'innerHTML')
    license = create_license_dictionary(license_string)
    # Set the first Requirement to Inactive
    order = ('manage', )
    process.execute(order)
    process.wait(2)  # need time to display the requirement listing
    order = ('active', 'save', )
    process.execute(order)
    process.wait()
    process.execute(('checklist', ))

    # Comparison should NOT match
    process.results(
        initial,
        negative=True,
        message="requirement '{}' should not be active".format(initial, ))
    # Add a new Requirement
    state = get_state_option(license['state'])
    cred_option = get_credential_option(license['credential'])
    license_type = get_license_type_option(license['type'])
    process.update({
        'add': ('Click', '//*[@id="checklist-form-container"]/div[2]/div/a/i'),
        'state': ('Select', '#state_code_id', state),
        'credential': ('Select', '#credential_id', cred_option),
        'type': ('Select', '#license_type_id', license_type)
    })
    process.execute(('add',))
    process.wait()
    process.execute(('state', 'credential', 'type',))

    # Test case: check to see if the Inactive Requirement becomes active
    # Set Requirements back to the 'Active' state
    process.wait(5)
    process.teardown()
