__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddExamination(UI):
    License()
    Checklist()

    runtime = {
        'examinations': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[3]'),
        'addExperience': ('Click', '//*[@id="examinationGrid_form"]/a[1]'),
        'checkPassed': ('Click', '//*[@for="passed"]', ),
        'selectExamination': (
            'Select',
            '#examination_id',
            'Comprehensive Osteopathic Medical Achievement Test'
        ),
        'selectState': ('Select', '#state_code_id', 'Colorado'),
        'examDate': ('Type', '#exam_date', '01052015'),
        'score': ('Type', '#score', '94'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Examination saved"
    process = UI()
    process.update(runtime)
    order = ('examinations', 'addExperience', 'checkPassed',
             'selectExamination', 'selectState', 'examDate', 'score', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()