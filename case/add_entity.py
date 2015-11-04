from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import gen_email, gen_name

__author__ = 'John Underwood'


class AddEntity(UI):
    """
    Add an Experience type entity.
    """
    License()
    Checklist()
    name = gen_name()
    email = gen_email(name)

    runtime = {
        'experience': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[1]'),
        'addExperience': ('Click', '//*[@id="experienceGrid_form"]/a[1]'),
        'addEntity': ('Click', '//*[@id="ExperienceEdit_form"]/div[1]/div/a'),
        'name': ('Type', '#entity_name', name),
        'status': ('Select', '#entity_status', 'Possible'),
        'addressDesc': ('Type', '#address_description', 'Home Office'),
        'addressType': (
            'Select', '#address_correspondence_method_type_id', 'Work'),
        'address1': ('Type', 'css=input#address_1.address_1', '275 E 200 S'),
        'address2': ('Type', 'css=input#address_2.address_2', ''),
        'city': ('Type', 'css=input#city.city', 'Salt Lake City'),
        'state': ('Select', 'css=select#state.browser-default', 'Utah'),
        'zipcode': ('Type', 'css=input#zip_code.zip_code', '84111'),
        'email': ('Type', '#email_address', email),
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Work'),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[2]/a[1]'),
    }

    expected = "Saved information"
    process = UI()
    process.update(runtime)
    order = ('experience', 'addExperience', 'addEntity', 'status', 'name',
             'addressDesc', 'addressType', 'address1', 'address2', 'city',
             'state', 'zipcode', 'email', 'emailType', 'save', )
    process.execute(order)
    process.results(expected, 'toast-container', 5)
    process.wait(3)
    process.teardown()
