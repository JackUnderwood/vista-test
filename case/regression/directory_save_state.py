from ui import UI
from tool.utilities import get_configurations
from tool.generators.state_codes import get_random_fifty_states_iso_code
__author__ = 'John Underwood'


class DirectorySaveState(UI):
    """
    Regression test for story #105687354
    """
    username = get_configurations("USER", "name")
    # TODO check for the value of the current State and remove it from the list
    # [state for state in states if state != 'CA']
    state = get_random_fifty_states_iso_code()  # add func skip='CA'
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'username': (
            'Type',
            '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input',
            username),
        'edit': (
            'Click',
            '//*[@id="employeeDirectoryMini_grid"]/tbody/tr/td[10]/a/i'),
        'state': ('Select', '#state', state),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]')
    }
    expected = state
    process = UI()
    process.update(runtime)
    order = ('directory', 'username', 'edit', 'state', 'save', )
    process.execute(order)
    process.wait(1)

    # Spy into the form's State field to check its value
    order = ('directory', 'username', 'edit', )
    process.execute(order)
    process.wait(3)  # avoids StaleElementReferenceException
    state_value = process.get_selected_option('#state')

    process.compare(expected, state_value)
    process.teardown()



