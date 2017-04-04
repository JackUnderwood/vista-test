from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddExperience(UI):
    """ JNU note: Use CSS as a target - see 'addExperience' key
        JNU note: Use name as a target - see 'description' key
    """
    License()
    Checklist(override={'rowNum': '10'})

    runtime = {
        'experience': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/li[2]/a'),
        # 'addExperience': ('Click', '//*[@id="experienceGrid_form"]/a[1]'),
        'addExperience': ('Click', 'css=#experienceGrid_form_inline>a.leaf.btn'),
        'findClient': ('Type', '#client_id_number_desc', 'acute family'),
        'selectClient': ('Click', '//*[@item_id="315711"]'),  # Acute Family
        'check': ('Click', '//*[@id="ExperienceEdit_form"]/div[5]/div[2]/label'),
        'description': ('Type', 'name=description', 'Genetics research'),
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
             'description', 'check', 'startDate', 'endDate', 'department',
             'departmentChair', 'capacity', 'notes', 'save', )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
