from ui import UI
from tool.utilities import get_configurations, get_random_value
from tool.generators.state_codes import FIFTY_STATES

__author__ = 'John Underwood'


class DirectorySaveState(UI):
    """
    Regression test for stories #105687354--the State field doesn't save--and
    #141898925--makes user inactive ** fixed 4/12/2017
    """
    name = get_configurations("USER", "name")
    states = FIFTY_STATES
    edit_locator = '//*[@id="employeeDirectoryMini_grid"]/tbody/tr/td[10]/a/i'
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'name': (
            'Type',
            '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input',
            name),
        'edit': ('Click', edit_locator)
    }
    process = UI()
    process.update(runtime)
    order = ('directory', 'name', )
    process.execute(order)
    process.wait(1)  # give drawer time to catch up before selecting a state
    order = ('edit', )
    process.execute(order)

    # See what is currently inside the State field; don't want to use
    # the same State iso code.
    current_state = process.get_selected_option('#state')
    states_minus_current = []
    for state in states:
        if state != current_state:
            states_minus_current.append(state)
    # states_minus_current = [state for state in states
    #                         if state != current_state]
    state = get_random_value(states_minus_current)
    expected = state
    runtime.update({
        'state': ('Select', '#state', state),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]'),
        'close': ('Click', '//*[@id="employeeDirectoryMini_form"]/div/div[2]/a')
    })
    process.update(runtime)
    process.execute(('state', 'save', ))
    process.wait(3)
    # Make sure the user is still active; one bug makes user inactive when saved
    if process.is_available(edit_locator):
        # Spy into the form's State field to check its value
        # order = ('edit', )
        # process.execute(order)
        process.wait()  # avoids StaleElementReferenceException
        state_value = process.get_selected_option('#state')
        process.compare(expected, state_value)
    else:
        msg = """User's row
        is no longer available; test failed early; may be caused by
        user_config table's can_use='N'--user is no longer active"""
        process.compare(True, False, message=msg)

    process.teardown()
