__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddEntity(UI):
    License()
    Checklist()

    runtime = {
        'experience': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[1]'),
        'addExperience': ('Click', '//*[@id="experienceGrid_form"]/a[1]'),
        'addEntity': ('Click', '//*[@display="drawer"]/div/a'),
        'name': ('Type', '#entity_name', 'Sierra Medicine'),
        'addressDesc': ('Type', '#address_description', 'Home Office'),
        'addressType': ('Select', '#address_correspondence_method_type_id', 'Work'),
        'addrClick': ('Click', '#address_1'),
        'address': ('Type', '#address_1', '123 State Street'),
        'city': ('Type', '#city', 'Portland'),
        'state': ('Select', '#state', 'Oregon'),
        'zipcode': ('Type', '#zip_code', '65432'),
        'email': ('Type', '#email_address', 'staff@sierramed.com'),
        'emailType': ('Select', '#email_correspondence_method__type_id', 'Work'),
        'phone': ('Type', '#phone', '5051236789'),
        'phoneType': ('Select', 'phone_correspondence_method_type_id', 'Other'),
        'save': ('Click', '//*[@button="save"]'),
    }

    expected = "Information saved"
    process = UI()
    process.update(runtime)
    order = ('experience', 'addExperience', 'addEntity', 'name', 'addressDesc',
             'addressType', 'addrClick', 'address', 'city', 'state', 'zipcode', 'email',
             'emailType', 'phone', 'phoneType', 'save'
             )
    process.execute(order)
    process.results(expected)
    process.wait(3)
    process.teardown()
