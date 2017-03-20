from ui import UI
from tool.utilities import get_configurations
from tool.generators.state_codes import get_random_fifty_states_iso_code
__author__ = 'John Underwood'


class DirectorySaveState(UI):
    """
    Regression test for story #105687354
    """
    name = get_configurations("USER", "name")
    # TODO check for the value of the current State and remove it from the list
    # [state for state in states if state != 'CA']
    state = get_random_fifty_states_iso_code()  # add func skip='CA'
    edit = '//*[@id="employeeDirectoryMini_grid"]/tbody/tr/td[10]/a/i'
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'name': (
            'Type',
            '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input',
            name),
        'edit': ('Click', edit),
        'state': ('Select', '#state', state),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]'),
        'close': ('Click', '//*[@id="employeeDirectoryMini_form"]/div/div[2]/a')
    }
    expected = state
    process = UI()
    process.update(runtime)
    order = ('directory', 'name', 'edit', )
    process.execute(order)
    process.wait(1)  # give drawer time to catch up before selecting a state
    order = ('state', 'save', )
    process.execute(order)
    # Make sure the user is still active; one bug makes user inactive when saved
    if process.is_available(edit):
        # Spy into the form's State field to check its value
        order = ('edit', )
        process.execute(order)
        process.wait(3)  # avoids StaleElementReferenceException
        state_value = process.get_selected_option('#state')
        process.compare(expected, state_value)
    else:
        pass
    process.teardown()

