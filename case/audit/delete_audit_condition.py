from ui import UI

__author__ = 'John Underwood'


class DeleteAuditCondition(UI):
    """
    Create an audit configuration, then delete it.

    Click on the audit config's delete button for a successful delete.
    """
    process = UI()
    process.get("auditConfig")
    user = 'Angie King'
    # //*[@id="auditConfig_grid"]/tbody/tr[2]/td[1]
    locator_id = process.spy('css=.hiddendiv', 'innerHTML')

    runtime = {
        'add': ('Click', '#newAuditCondition'),
        'searchUser': ('Type', '#userDescription', user),
        'selectUser': ('Click', '//*[@item_id="1001"]'),
        'table': ('Select', '#historyTablesId', 'address'),
        'address1': ('Click', '//*[@id="fields_1"]/div[2]/label[1]'),
        'address2': ('Click', '//*[@id="fields_1"]/div[2]/label[2]'),
        'city':     ('Click', '//*[@id="fields_1"]/div[2]/label[7]'),
        'save': ('Click', '#saveButton'),
        'delete': ('Click', '//*[@id="remove_902_17"]/i'),
    }
    process.update(runtime)  # create a new audit condition
    order = ('add', 'searchUser', 'selectUser', 'table',
             'address1', 'address2', 'city', 'save')
    process.execute(order)


