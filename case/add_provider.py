import ui
from ui import UI
from tool.utilities import digits_only
from tool.generators.generator import gen_name, gen_ssn, split_name
from tool.generators.generator import gen_email, gen_phone_number
from tool.generators.state_codes import get_state_name

__author__ = 'John Underwood'


class AddProvider(UI):
    """
    Checks for Default Phone inside Workspace
    """
    state_iso_code = 'CA'
    state = get_state_name(state_iso_code)
    ssn = gen_ssn()
    full = gen_name()
    first, last = split_name(full)
    ui.log.info("FIRST NAME: {} - LAST NAME: {}".format(first, last,))

    email = gen_email(full)
    phone_number = gen_phone_number(state_iso_code)
    formatted_phone_number = (
        phone_number[:3] + ' ' + phone_number[3:6] + '-' + phone_number[6:])
    ui.log.info("PHONE NUMBER: {} - FORMATTED: {}".format(
        phone_number, formatted_phone_number, ))

    expected = '(' + (phone_number[:3] + ') ' + phone_number[3:6] +
                      '-' + phone_number[6:])

    runtime = {
        'find': ('Type', '#main_desc', full),
        'addNewEntity': (
            'Click',
            '/html/body/header/nav/div/ul[1]/li[4]/div/div/div[4]/div/div[1]/a'),
        'entityType': ('Select', '#entity_type', 'Physician'),

        'title': ('Type', '#title', 'Dr.'),
        'status': ('Select', '#entity_status', 'Possible'),
        'firstName': ('Type', '#entity_first_name', first),
        'middleName': ('Type', '#entity_middle_name', 'Tester'),
        'lastName': ('Type', '#entity_name', last),
        'addressDesc': ('Type', '#address_description', 'Home Office'),
        'addressType': (
            'Select', '#address_correspondence_method_type_id', 'Work'),
        'address1': (
            'Type', 'css=input#address_1.address_1', '4972 Verdugo Way'),
        'city': ('Type', 'css=input#city.city', 'Camarillo'),
        'state': ('Select', 'css=select#state.browser-default', state),
        'zipcode': ('Type', 'css=input#zip_code.zip_code', '93012'),
        'email': ('Type', '#email_address', email),
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Work'),
        'phoneNumber': ('Type', '#phone', phone_number),
        'phoneType': ('Select', '#phone_correspondence_method_type_id', 'Work'),
        'ssn': ('Type', '#ssn', digits_only(ssn)),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[3]/a[1]'),

        'findModifier': (
            'Type', '#main_desc', full + ' p:' + formatted_phone_number),
        'fullName': full,
        'select': ('Click', 'css=#user_name'),
        'displaySsn': ('Click', '//*[@id="ribbon_form"]/ul/li/div[2]/div[1]/'
                                'div[3]/span[1]/a'),
        'continue': ('Click', '//*[@button="continue"]'),
    }
    process = UI()
    process.update(runtime)
    order = ('find', 'addNewEntity', 'entityType', 'title', 'status',
             'firstName', 'middleName', 'lastName',  'addressDesc',
             'addressType',  # 'address1', 'city', 'state', 'zipcode',
             'email', 'emailType', 'phoneNumber', 'phoneType', 'ssn', 'save', )
    process.execute(order)
    process.wait()
    success = process.results('Saved information', locator='toast-container',
                              wait_time=8)
    if success:
        order = ('findModifier', )
        process.execute(order)
        process.wait(3)
        order = ('select', )
        process.execute(order)
        process.wait(1)
        process.results(expected, locator='ribbon_form', wait_time=5)

    process.teardown()
