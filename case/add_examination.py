from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddExamination(UI):
    License()
    Checklist()

    runtime = {
        'exam': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/li[4]/a'),
        'addExam': ('Click', '//*[@id="examinationGrid_form_inline"]/a[1]'),
        'checkPassed': ('Click', '//label[@for="passed"]', ),
        # Comprehensive Osteopathic Medical Achievement Test (COMAT)
        'selectExamination': ('Select', '#examination_id', 'COMAT'),
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
