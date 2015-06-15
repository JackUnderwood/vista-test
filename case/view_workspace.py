__author__ = 'John Underwood'

from ui import UI
from ui.low.my_workspace import MyWorkspace

class ViewWorkspace(UI):
    MyWorkspace()
    # TODO: still need to view the workspace and test for a result
    runtime = {}
    
    process = UI()
    process.wait(3)
    process.teardown()
