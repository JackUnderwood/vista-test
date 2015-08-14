__author__ = 'John Underwood'

from ui import UI
from ui.low.my_workspace import MyWorkspace


class ViewWorkspace(UI):
    MyWorkspace()
    runtime = {}
    
    process = UI()
    process.results('Use Find... to load your workspace.')
    process.wait(3)
    process.teardown()
