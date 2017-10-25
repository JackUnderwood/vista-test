# import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class EditEducation(UI):
    """ See TestRail test case C276 - Edit Education
    1 - Click Education inside a provider's ribbon
    2 - Click an education row's edit button
    3 - Change a value in the Manage Education drawer's form, e.g. Use in CV
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
        'feedback': 'Education saved',
    }
    no_records_found = "No records found"
    License()
    Checklist()

    runtime = {
        'education': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[5]/span'),
        'entries': ('Select', '//*[@id="educationGrid_grid_1_length"]/'
                              'label/select', '100'),
        'add': ('Click', '//*[@id="educationGrid_form_drawer"]/a[1]'),
        'find': ('Type', '#education_entity_id_desc', expected['entity']),
        'select': ('Click', '#user_name'),
        'degree': ('Select', '#education_degree_id', expected['degree']),
        'type': ('Select', '#education_type_id', expected['type']),
        'start': ('Type', '#start_date', expected['start']),
        'end': ('Type', '#end_date', expected['end']),
        'cv': ('Click', '//*[@for="use_on_cv"]'),  # change this during edit
        'save': ('Click', '//*[@button="save"]')
    }  # //*[@id="educationGrid_grid_1"]/tbody/tr[6]/td[12]/a/i
    process = UI()
    process.update(runtime)
    process.execute(('education',))
    process.wait()
    process.execute(('entries',))

    # Count the number of rows.
    row = process.get_table_size('#educationGrid_grid_1')
    process.wait()
    process.update({
        'edit': ('Click', '//*[@id="educationGrid_grid_1"]/tbody/tr[{}]'
                          '/td[12]/a'.format(row,))
    })
    process.execute(('add', 'find', 'select', 'degree', 'type',
                    'start', 'save', ))
    process.wait()
    before = process.spy('//*[@id="educationGrid_grid_1"]/tbody/tr[{}]'
                         '/td[6]/i'.format(row,), 'title')  # "Not Verified"

    process.execute(('edit',))  # Manage Experience drawer
    process.wait()
    process.execute(('cv', 'save'))  # make the edit
    process.wait()
    process.results(expected['feedback'])
    after = process.spy('//*[@id="educationGrid_grid_1"]/tbody/tr[{}]'
                        '/td[6]/i'.format(row,), 'title')
    not_use = 'Not Use on CV'
    use_cv = 'Use on CV'
    if not_use in before:
        process.compare(use_cv, after)
    elif use_cv in before:
        process.compare(not_use, after)
    process.wait(3)
    process.teardown()
