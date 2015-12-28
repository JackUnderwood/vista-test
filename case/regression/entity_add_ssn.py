import ui
from ui import UI
from tool.utilities import digits_only
from tool.generators.generator import gen_name, gen_ssn, split_name
from tool.generators.generator import gen_phone_number
from tool.db import get_record
__author__ = 'John Underwood'


class EntityAddSsn(UI):
    """
    Regression test for story #102370974
    """
    ssn = gen_ssn()
    full = "Blane Workman"  # gen_name()
    first, last = split_name(full)
    pn = gen_phone_number('UT')
    formatted_phone_number = pn[:3] + ' ' + pn[3:6] + '-' + pn[6:]

    sql = """
        SELECT entity_id_number
        FROM phone
        WHERE phone_number = '{}'
    """.format(formatted_phone_number, )
    assert isinstance(sql, str)

    ui.log.info("First name: {0} & Last name: {1}".format(first, last,))
    runtime = {
        'find': ('Type', '#main_desc', full),
        'addNewEntity': (
            'Click',
            '/html/body/header/nav/div/ul[1]/li[4]/div/div/div[4]/div/div[1]/a'),
        'entityType': ('Select', '#entity_type', 'Physician'),
        'status': ('Select', '#entity_status', 'Possible'),
        'firstName': ('Type', '#entity_first_name', first),
        'lastName': ('Type', '#entity_name', last),
        'phoneNum': ('Type', '#phone', pn),
        'phoneType': ('Select', '#phone_correspondence_method_type_id', 'Work'),
        'ssn': ('Type', '#ssn', digits_only(ssn)),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[3]/a[1]'),
        'fullName': full,
        # '//span[contains(@id, "user_name") and text()="&fullName;"]'
        # '//span[@id="user_name" and contains(., "&fullName;")]'
    }
    process = UI()
    process.update(runtime)
    order = ('find', 'addNewEntity', 'entityType', 'status', 'firstName',
             'lastName', 'phoneNum', 'phoneType', 'ssn', 'save', )
    process.execute(order)
    process.wait(3)
    record = get_record(sql)
    runtime = {
        'findPhone': (  # e:123 333-4444
            'Type', '#main_desc', 'p:' + formatted_phone_number),
        'userId': str(record[0][0]),
        'select': ('Click', '#&userId;'),
        'displaySsn': ('Click', '//*[@id="ribbon_form"]/ul/li/div[2]/div[1]/'
                                'div[3]/span[1]/a'),
        'continue': ('Click', '//*[@button="continue"]'),
    }

    process.update(runtime)
    order = ('findPhone', 'select', 'displaySsn', 'continue', )
    process.execute(order)
    actual = process.get(
        '//*[@id="ribbon_form"]/ul/li/div[2]/div[1]/div[3]/span[1]',
        'innerHTML', )
    ui.log.info('SSN value is {}'.
                format(actual if actual is not '' else 'None',))
    process.compare(ssn, actual)
    process.wait(5)
    process.teardown()
