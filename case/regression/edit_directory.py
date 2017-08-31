from ui import UI
from tool.utilities import get_configurations
from tool.generators.generator import gen_number

__author__ = 'John Underwood'


class EditDirectory(UI):
    """
    Regression test for story #104556112
    """
    username = get_configurations("USER", "name")
    birth_day = gen_number(29, padding=2)
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'username': (
            'Type',
            '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input',
            username),
        'edit': (
            'Click',
            '//*[@id="employeeDirectoryMini_grid"]/tbody/tr[1]/td[10]/a/i'),
        'birthday': ('Select', '#birth_day', birth_day),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]')
    }
    expected = "User Configuration Saved!"
    process = UI()
    process.update(runtime)
    order = ('directory', 'username', 'edit', )
    process.execute(order)
    process.wait(4)
    order = ('birthday', 'save', )
    process.execute(order)
    process.wait(1)
    process.results(expected)
    process.teardown()

