from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import get_today_date

__author__ = 'John Underwood'


class EditExamination(UI):
    """ See TestRail test case C277 - Edit Education
    1 - Click Examination inside a provider's ribbon
    2 - Click an exam row's edit button
    3 - Change value in the Manage Examinations drawer's form, e.g. Score, Passed
    4 - Save the changes
    Expected: Examination saved successfully, and row shows new changed value
    """
    actual = {}
    expected = {
        'score': '93',
        'passed': 'Verified',
        'feedback': 'Examination saved',
    }
    today_date = get_today_date().replace('/', '')

    License()
    Checklist()
    runtime = {
        'exams': ('Click',
                  '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[4]'),
        'length': ('Select',
                   '//*[@id="examinationGrid_grid_1_length"]/label/select',
                   '100'),
        'add': ('Click', '//*[@id="examinationGrid_form_drawer"]/a[1]'),
        'passed': ('Click', '//*[@id="examinationEdit_form"]/div[1]/div/label'),
        'examName': ('Select', '#examination_id', 'NBOME'),
        'state': ('Select', '#state_code_id', 'Utah'),
        'date': ('Type', '#exam_date', today_date),
        'score': ('Type', '#score', expected['score']),
        'attempts': ('Type', '#attempts', '1'),
        'save': ('Click', '//*[@id="examinationEdit_form"]/div[6]/a[1]')
    }
    process = UI()
    process.update(runtime)
    order = ('exams',)
    process.execute(order)
    process.wait()
    order = ('length', 'add', 'examName', 'state', 'date', 'attempts', 'save')
    process.execute(order)
    process.wait()
    row = process.get_table_size('#examinationGrid_grid_1')-1  # remove header
    # second row 'tr[2]' if one row 'tr'
    placeholder = 'tr[{}]'.format(row,) if row > 1 else 'tr'
    process.update({
        'edit': ('Click',
                 '//*[@id="examinationGrid_grid_1"]/tbody/{}/td[8]/a/i'.
                 format(placeholder,))
        #         //*[@id="examinationGrid_grid_1"]/tbody/tr[2]/td[8]/a/i
    })
    process.execute(('edit', 'passed', 'score', 'save'))  # make the edits
    process.wait()
    process.results(expected['feedback'])
    process.wait()
    actual['passed'] = process.spy('//*[@id="examinationGrid_grid_1"]/tbody'
                                   '/{}/td[1]/i'.format(placeholder,), 'title')
    actual['score'] = process.spy('//*[@id="examinationGrid_grid_1"]/tbody'
                                  '/{}/td[3]'.format(placeholder,), 'innerHTML')
    process.compare(expected['passed'], actual['passed'],
                    message='"Passed" field')
    process.compare(expected['score'], actual['score'],
                    message='"Score" field')
    process.wait()
    process.teardown()


