from ui import UI

__author__ = 'John Underwood'


class UserSecret(UI):
    """
    Click on the UserSecret link from the Header bar, opens the User's mini-find.
    Uses the default role for Licensor--Angie King 1001.
    """
    def __init__(self, override=None):
        super().__init__()
        runtime = {
            'role': 'Angie King',  # OVERRIDE
            'roleId': '1001',  # OVERRIDE
            'userSecret': ('Click', '/html/body/header/nav/div/ul[2]/li[5]/a/i', ),
            'find': ('Type', '#change-user-user_key_id_desc', '&role;'),
            'select': ('Click', '//*[@item_id="&roleId;"]')
        }
        process = UI(override)
        process.update(runtime)
        order = ('userSecret', 'find', 'select', )
        process.execute(order)
