__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddExamination(UI):
    License()
    Checklist()

    runtime = {
        'exam': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[3]'),
        'addExam': ('Click', '//*[@id="examinationGrid_form"]/a[1]'),
        'checkPassed': (
            'Click',
            '//*[@id="examinationEdit_form"]/div[1]/div/label',
        ),
        'selectExamination': (
            # Comprehensive Osteopathic Medical Achievement Test (COMAT)
            'Select',
            '#examination_id',
            'COMAT'
        ),
        'selectState': ('Select', '#state_code_id', 'Colorado'),
        'examDate': ('Type', '#exam_date', '01052015'),
        'score': ('Type', '#score', '94'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Examination saved"
    process = UI()
    process.update(runtime)
    order = ('exam', 'addExam', 'checkPassed', 'selectExamination',
             'selectState', 'examDate', 'score', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
