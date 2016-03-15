from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class AddEducationRibbon(UI):
    """ Add education through the ribbon.
    """
    License()
    Checklist()

    runtime = {
        'education': (
            'Click',
            '//*[@id="ribbon_form"]/ul/li/div[2]/div[4]/div[2]/a[5]/span'),
        'addEducation': ('Click', '//*[@id="educationGrid_form"]/a[1]'),
        'findEducation': ('Type', '#education_entity_id_desc', 'Tulane'),
        'selectEducation': ('Click', '#user_name'),
        'useEducationCv': ('Click', '//label[@for="use_on_cv"]'),
        'selectDegree': ('Select',
                         '#education_degree_id', 'Bachelor of Science'),
        'selectType': ('Select', '#education_type_id', 'Undergraduate'),
        'startDate': ('Type', '#start_date', '09011992'),
        'endDate': ('Type', '#end_date', '06011996'),
        'save': ('Click', '//*[@id="EducationEdit_form"]/div[10]/a[1]')
    }
    expected = "Education saved"
    process = UI()
    process.update(runtime)

    order = ('education', )
    process.execute(order)
    process.wait(2)  # wait for drawer to expand

    order = ('addEducation', 'findEducation', 'selectEducation',
             'selectDegree', 'selectType', 'useEducationCv', 'startDate',
             'endDate', 'save', )
    process.execute(order)

    process.results(expected)
    process.wait(3)
    process.teardown()
