from ui import UI
from ui.low.admin_user_status import AdminUserStatus

__author__ = 'John Underwood'


class RefreshAcls(UI):
    """
    Navigate to Administrator | User Status and click the 
    "Refresh All Users' ACLs" button
    """
    process = UI()
    AdminUserStatus()

    runtime = {
        'refresh': ('Click', '#reload-all-users')
    }
    expected = 'Automatically reloaded account permissions'
    process.update(runtime)
    process.execute(('refresh', ))
    process.wait()

    process.results(expected)
    process.teardown()
