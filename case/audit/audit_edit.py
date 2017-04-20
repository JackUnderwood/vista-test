from ui import UI

__author__ = 'John Underwood'


class AuditEdit(UI):
    """
    Requires an existing audit configuration.
    """
    process = UI()
    process.get("auditConfig")

    runtime = {
        'edit': ('Click', '//*[@id="edit_902_17"]/i'),
        'option': ('Click',
                   '//*[@id="editExisting"]/div[1]/div[4]/div[2]/label[38]'),
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
