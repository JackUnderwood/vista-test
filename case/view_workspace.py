from ui import UI
from ui.low.my_workspace import MyWorkspace

__author__ = 'John Underwood'


class ViewWorkspace(UI):
    MyWorkspace()
    runtime = {}
    
    process = UI()
    process.results('Use Find... to load your workspace.')
    process.wait(3)
    process.teardown()
