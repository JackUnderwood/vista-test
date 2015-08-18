__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.expand_ribbon import ExpandRibbon


class AddEducationRibbon(UI):
    """ Add education through the ribbon.
    """
    License()
    Checklist()
    ExpandRibbon()

    runtime = {
        'education': ('Click',
                      '//*[@id="ribbon_form"]/ul/li/div[2]/div[3]/div[2]/a[4]/i'),
        'addEducation': ('Click', '//*[@id="educationGrid_form"]/a[1]'),
        'findEducation': ('Type', '#education_entity_id_desc', 'Tulane'),
        'selectEducation': ('Click', '#user_name'),
        'useEducationCv': ('Click',
                           '//*[@id="EducationEdit_form"]/div[4]/div[1]/label'),
        'selectDegree': ('Select',
                         '#education_degree_id', 'Bachelor of Science'),
        'selectType': ('Select', '#education_type_id', 'Undergraduate'),
        'startDate': ('Type', '#start_date', '09011992'),
        'endDate': ('Type', '#end_date', '06011996'),
        'save': ('Click', '//*[@id="EducationEdit_form"]/div[9]/a[1]')
    }
    expected = "Education saved"
    process = UI()
    process.update(runtime)
    order = ('education', 'addEducation', 'findEducation', 'selectEducation',
             'useEducationCv', 'selectDegree', 'selectType', 'startDate',
             'endDate', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()