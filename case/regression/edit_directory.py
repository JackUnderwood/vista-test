from ui import UI
from tool.utilities import get_configurations
from tool.generators.generator import gen_number

__author__ = 'John Underwood'


class EditDirectory(UI):
    """
    Regression test for story #104556112
    """
    username = get_configurations("USER", "username")
    birth_day = gen_number(29)
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'username': (
            'Type',
            '//*[@id="userGrid_grid"]/tfoot/tr/th[12]/input',
            username),
        'edit': ('Click', '//*[@id="userGrid_grid"]/tbody/tr/td[17]/a/i'),
        'birthday': ('Select', '#birth_day', birth_day),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]')
    }
    expected = "User Configuration Saved!"
    process = UI()
    process.update(runtime)
    order = ('directory', 'username', 'edit', 'birthday', 'save', )
    process.execute(order)
    process.wait(1)
    process.results(expected)
    process.teardown()

