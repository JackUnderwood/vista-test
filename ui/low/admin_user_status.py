import ui
from ui import UI

__author__ = 'John Underwood'


class AdminUserStatus(UI):
    """
    Navigate to Administrator | User Status lists all users that are using the
    INDY app and those that have not logged on; allows refreshing of all ACLs.
    """
    def __init__(self, override=None):
        super().__init__()
        ui.log.info("Administrator User Status __init__() called")
        runtime = {
            'level': self.ADMIN,
            'hover': ('Hover', '#slide-out'),
            'userStatus':  ("Chain", [
                ('move_to_element', {
                    'to_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/a/i[1]'}),
                ('click', {
                    'on_element':
                        '//*[@id="slide-out"]/li[&level;]/ul/li/div/ul/li[2]/a'}
                 ),
            ]),
        }
        process = UI(override)
        process.update(runtime)
        order = ('hover', 'userStatus', )
        process.execute(order)

