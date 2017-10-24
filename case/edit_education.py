# import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class EditEducation(UI):
    """ See TestRail test case C276 - Edit Education
    1 - Click Education inside a provider's ribbon
    2 - Click an education row's edit button
    3 - Change a value in the Manage Education drawer's form, e.g. Degree Type
    4 - Save the changes
    Expected: Education saved successfully, and row shows new changed value
    """
    expected = {
        'entity': 'ALL University of Utah School of Medicine',
        'degree': 'Doctor of Medicine',
        'type': 'Doctorate',
        'start': '01042015',
        'end': '05172015',
        'cv': 'fa-check',
    }
    no_records_found = "No records found"
    License()
    Checklist(override={'rowNum': 5})  # JNU!!! remove arg later

    runtime = {
        'education': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[5]/span'),
        'add': ('Click', '//*[@id="educationGrid_form_drawer"]/a[1]'),
        'edit': ('Click',
                 '//*[@id="educationGrid_grid_1"]/tbody/tr[1]/td[12]/a'),
        'find': ('Type', '#education_entity_id_desc', expected['entity']),
        'select': ('Click', '#user_name'),
        'degree': ('Select', '#education_degree_id', expected['degree']),
        'type': ('Select', '#education_type_id', expected['type']),
        'start': ('Type', '#start_date', expected['start']),
        'end': ('Type', '#end_date', expected['end']),
        'cv': ('Click', '//*[@for="use_on_cv"]'),  # change this during edit
        'save': ('Click', '//*[@button="save"]')
    }
    process = UI()
    process.update(runtime)
    process.execute(('education',))
    process.wait()

    # Count the number of rows.
    row = process.get_table_size('#educationGrid_grid_1')
    process.wait()

    # find out why getting: "'NoneType' object has no attribute 'get_attribute'"
    experiment = process.spy('//*[@id="experienceGrid_grid_1"]/tbody/tr[{}]'
                         '/td[4]/i'.format(3,), 'title')

    process.update({
        'edit': ('Click', '//*[@id="educationGrid_grid_1"]/tbody/tr[{}]'
                          '/td[12]/a'.format(row,))
    })
    process.execute(('add', 'find', 'select', 'degree', 'type',
                    'start', 'save',))
    process.wait()
    before = process.spy('//*[@id="experienceGrid_grid_1"]/tbody/tr[{}]'
                         '/td[4]/i'.format(row,), 'title')
    # //*[@id="experienceGrid_grid_1"]/tbody/tr[3]/td[4]/i
    process.execute(('edit',))  # Manage Experience drawer
    process.wait()
    process.execute(('cv', 'save'))  # make the edit
    process.wait()
    # # Check that rows exist inside grid;
    # if no_records_found in value:
    #     ui.log.info("Education grid: {}".format(no_records_found,))
    #     process.teardown()
    # # Spy into the each of the row's elements to get all current values.
    # value = process.spy(
    #     '//*[@id="educationGrid_grid_1"]/tbody/tr[4]/td[1]',
    #     'innerHTML')
    # expected['entity'] = value[value.find('</span> ')+8:]
    # process.execute(('edit',))
    # process.wait()
    # process.execute(('find', 'select',))
    # # Find if "Use Education on CV" is checked; if not, check it
    # is_checked = process.is_selected('//*[@for="use_on_cv"]')
    # if not is_checked:
    #     process.execute(('cv',))
    # option = process.get_selected_option('#education_degree_id', 'text')
    # if option == 'Select Degree':
    #     process.execute(('degree',))
    # process.wait()
    # option = process.get_selected_option('#education_type_id', 'text')
    # if option == 'Select Type':
    #     process.execute(('type',))
    # value = process.spy('#start_date', 'value')
    # if not value:
    #     process.execute(('start',))
    process.wait(3)
    process.teardown()
