__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddExperience(UI):
    License()

    override = {'rowNum': '3'}
    Checklist(override)

    runtime = {
        'experience': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[1]'),
        'addExperience': ('Click', '//*[@id="experienceGrid_form"]/a[1]'),
        'findClient': ('Type', '#client_id_number_desc', 'acute family'),
        'selectClient': ('Click', '#user_name'),
        'check': ('Click', '//*[@id="ExperienceEdit_form"]/div[4]/div[4]/label'),
        'description': ('Type', '#description', 'Genetics research'),
        'startDate': ('Type', '#start_date', '01042015'),
        'endDate': ('Type', '#end_date', '05172015'),
        'department': ('Type', '#department', 'Urology'),
        'departmentChair': ('Type', '#department_chair', 'Jack Shoop'),
        'capacity': ('Type', '#capacity', 'Rare Genetic Diseases'),
        'notes': ('Type', '#notes', 'Notes on rare genetic diseases'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Experienced saved"
    process = UI()
    process.update(runtime)
    order = ('experience', 'addExperience', 'findClient', 'selectClient',
             'check', 'description', 'startDate', 'endDate', 'department',
             'departmentChair', 'capacity', 'notes', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
