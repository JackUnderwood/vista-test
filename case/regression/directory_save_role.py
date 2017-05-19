from ui import UI
from ui.low.home import Home
from tool.vtf_html_parser import VtfHtmlParser

__author__ = 'John Underwood'


def parse_selected(data_to_parse):
    """
    Parse the data from options list.
    :param data_to_parse: string - partial HTML string
    :return: list of strings - all selected items
    """
    parse = VtfHtmlParser()
    parse.data = []
    parse.feed(data_to_parse)
    selected_options = []
    for datum in parse.data:
        try:
            if 'ms-selected' in datum[1]['class']:
                selected_options.append(datum[3]['data'])
                # print(datum[3]['data'])
        except IndexError:
            pass

    return selected_options


class DirectorySaveRole(UI):
    """
    Regression test for story #145041989--Roles don't save. Save a change
    to the Roles selection pane.
    """
    name = 'John Underwood'
    edit = '//*[@id="employeeDirectoryMini_grid"]/tbody/tr/td[10]/a/i'
    runtime = {
        'directory': ('Click', '#button_employee_directory'),
        'name': (
            'Type',
            '//*[@id="employeeDirectoryMini_grid"]/tfoot/tr/th[3]/input', name),
        'edit': ('Click', edit)
    }
    process = UI()
    process.update(runtime)
    order = ('directory', 'name', )
    process.execute(order)
    process.wait()  # give drawer time to catch up before clicking edit button
    order = ('edit', )
    process.execute(order)

    runtime.update({
        'company': ('Click',
                    '//*[@id="manageUser_form"]/div[2]/div[1]/ul/li[3]', ),
        'selectRole': ('Click', '//*[@id="ms-roles"]/div[1]'),
        'save': ('Click', '//*[@id="manageUser_form"]/div[3]/a[1]')
    })
    process.update(runtime)
    # Build <title> content; e.g. "(Jack Doe) Manage User"
    title = '({}) Manage User'.format(name, )
    process.wait_for_title(title, 20)
    process.execute(('company', ))
    process.wait()
    data1 = process.spy('//*[@id="ms-roles"]/div[2]/ul', 'innerHTML').strip()
    current_roles = parse_selected(data1)
    process.execute(('selectRole', 'save'))
    process.wait(2)

    Home()  # back to the beginning
    process.execute(('directory', 'name', ))
    process.wait()  # give drawer time to catch up before clicking edit button

    process.execute(('edit', ))
    process.wait_for_title(title, 20)
    process.execute(('company', ))
    process.wait()

    data2 = process.spy('//*[@id="ms-roles"]/div[2]/ul', 'innerHTML').strip()
    changed_roles = parse_selected(data2)

    # Find the difference
    current_roles_set = set(current_roles)
    changed_roles_set = set(changed_roles)
    newly_added_role = changed_roles_set.difference(current_roles_set)

    # See what is currently inside the assigned Roles field.
    process.compare(len(newly_added_role), True, message='difference is "{}"'.
                    format(newly_added_role, ))
    process.wait()
    process.teardown()
