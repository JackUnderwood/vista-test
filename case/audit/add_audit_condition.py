from ui import UI

__author__ = 'John Underwood'


class AuditEditCondition(UI):
    """
    Click Add Audit Condition; opens the 'Create New Audit Condition' drawer
    """
    process = UI()
    process.go_to_driver_url("http://indytest/auditConfig")
    user = 'Angie King'

    runtime = {
        'add': ('Click', '#newAuditCondition'),
        'searchUser': ('Type', '#userDescription', user),
        'selectUser': ('Click', '//*[@item_id="1001"]'),
        'table': ('Select', '#historyTablesId', 'address'),
        'address1': ('Click', '//*[@id="fields_1"]/div[2]/label[1]'),
        'address2': ('Click', '//*[@id="fields_1"]/div[2]/label[2]'),
        'city':     ('Click', '//*[@id="fields_1"]/div[2]/label[7]'),
        'save': ('Click', '#saveButton')
    }
    expected = 'Audit Conditions Saved Successfully.'
    process.update(runtime)
    order = ('add', 'searchUser', 'selectUser', 'table',
             'address1', 'address2', 'city', 'save')
    process.execute(order)
    actual = process.spy('//*[@id="editNew"]/div[1]/p', 'innerHTML')
    process.compare(expected, actual)

    process.wait(1)
    process.teardown()
