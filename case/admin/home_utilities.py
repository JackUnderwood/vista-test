from ui import UI
from ui.low.admin_home import AdminHome

__author__ = 'John Underwood'


class HomeUtilities(UI):
    """
    Access the administrator home page; Utilities page
    """
    AdminHome()
    process = UI()
    process.results('Utilities')
    process.wait()
    process.teardown()
