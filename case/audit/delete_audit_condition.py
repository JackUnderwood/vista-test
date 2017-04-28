from ui import UI

__author__ = 'John Underwood'


class DeleteAuditCondition(UI):
    """
    Create an audit configuration, then delete it.

    Click on the audit config's delete button for a successful delete.
    Note: incomplete test case; currently unable to successfully delete
    audit conditions inside audit - #143717105 get 403 error--missing acl
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

    runtime.update({
        'delete': ('Click', '//*[@id="remove_{}"]/i'.format(locator_id,)),
    })
    expected = 'Are you sure you wish to remove audits'
    process.update(runtime)
    order = ('delete', )
    process.execute(order)

    found = process.results(expected)
    if found:
        runtime.update({
            'continue': ('Click', '#confirmButton'),
        })
        expected = 'The requested audit has been removed'
        process.update(runtime)
        order = ('continue', )
        process.execute(order)
        process.results(expected)

    process.wait(3)
    process.teardown()

