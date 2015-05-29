__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddExperience(UI):
    License()
    Checklist()

    runtime = {
        'education': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[2]'),
        'addEducation': ('Click', '//*[@id="educationGrid_form"]/a[1]'),
        'findEducation': ('Type', '#education_entity_id_desc', 'utah'),
        'selectEducation': ('Click', '#user_name'),
        'selectDegree': ('Select', '#education_degree_id', 'Doctor of Medicine'),
        'selectType': ('Select', '#education_type_id', 'Medical School'),
        'startDate': ('Type', '#start_date', '01042015'),
        'endDate': ('Type', '#end_date', '05172015'),
        'director': ('Type', '#director', 'Dr. James Kildeare'),
        'honor': ('Type', '#honor', 'Summa cum Laude'),
        'checkCv': ('Click', '//*[@for="use_on_cv"]'),
        'save': ('Click', '//*[@button="save"]')
    }
    expected = "Education saved"
    process = UI()
    process.update(runtime)
    order = ('education', 'addEducation', 'findEducation', 'selectEducation',
             'selectDegree', 'selectType', 'startDate', 'endDate', 'director',
             'honor', 'checkCv', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()

