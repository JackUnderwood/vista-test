from ui import UI

__author__ = 'John Underwood'


class EditAudit(UI):
    """
    Requires an existing audit configuration.
    """
    process = UI()
    process.get("auditConfig")
    user = 'Angie King'

    runtime = {
        'add': ('Click', '#newAuditCondition'),
        'searchUser': ('Type', '#userDescription', user),
        'selectUser': ('Click', '//*[@item_id="1001"]'),
        'table': ('Select', '#historyTablesId', 'address'),
        'address1': ('Click', '//*[@id="fields_1"]/div[2]/label[1]'),
        'address2': ('Click', '//*[@id="fields_1"]/div[2]/label[2]'),
        'city':     ('Click', '//*[@id="fields_1"]/div[2]/label[7]'),
        'save': ('Click', '#saveButton'),
        'close': ('Click', '#closeButton'),
    }
    process.update(runtime)  # create a new audit condition
    order = ('add', 'searchUser', 'selectUser', 'table',
             'address1', 'address2', 'city', 'save', 'close')
    process.execute(order)
    process.wait(1)

    # Spy into the first result's row, and get its unique id
    # Outer HTML: <td class=" hiddendiv">902_17</td>
    # e.g. locator_id = 902_17
    locator_id = process.spy('//*[@id="auditConfig_grid"]/tbody/tr[1]/td[1]',
                             'innerHTML')

    runtime = {
        'edit': ('Click', '//*[@id="edit_{}"]/i'.format(locator_id, )),
        'option': ('Click',
                   '//*[@id="editExisting"]/div[1]/div[4]/div[2]/label[18]'),
        'save': ('Click', '#saveButton')
    }
    expected = 'Audit Conditions Saved Successfully.'
    process.update(runtime)
    order = ('edit', 'option', 'save')
    process.execute(order)
    actual = process.spy('//*[@id="editExisting"]/div[1]/p', 'innerHTML')
    process.compare(expected, actual)

    process.wait(1)
    process.teardown()
