__author__ = 'John Underwood'

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist


class AddEntity(UI):
    """
    The following are unable to access element: address, city, state,
    zipcode, phone, phone type
    Appears to be the 'type' attribute is set to 'hidden' and selenium is
    getting confused by the two <input> tags.

    See http://stackoverflow.com/questions/6101461/
    how-to-force-selenium-to-click-on-element-which-is-not-currently-visible
    Selenium determines an element is visible or not by the following criteria
    (use a DOM inspector to determine what css applies to your element, make
    sure you look at 'Computed' style):
        - visibility != hidden
        - display != none (is also checked against every parent element)
        - opacit0y != 0 (this is not checked for clicking an element)
        - height and width are both > 0
        - for an input, the attribute type != hidden
    """
    License()
    Checklist()

    runtime = {
        'experience': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[1]'),
        'addExperience': ('Click', '//*[@id="experienceGrid_form"]/a[1]'),
        'addEntity': ('Click', '//*[@id="ExperienceEdit_form"]/div[1]/div/a'),
        'name': ('Type', '#entity_name', 'Sierra Medicine Three'),
        'addressDesc': ('Type', '#address_description', 'Home Office'),
        'addressType': (
            'Select', '#address_correspondence_method_type_id', 'Work'),
        'address1': ('Type', '//*[@name="address_1"]', '123 State Street'),
        'address2': ('Type', '#address_2', 'Suite 400'),
        'city': ('Type', '#city', 'Portland'),
        'state': ('Select', '#state', 'Oregon'),
        'zipcode': ('Type', '#zip_code', '65432'),
        'email': ('Type', '#email_address', 'staff@sierramed4.com'),
        'emailType': ('Select', '#email_correspondence_method_type_id', 'Work'),
        'phone': ('Type', '#phone', '5051236789'),
        'phoneType': ('Select', 'phone_correspondence_method_type_id', 'Other'),
        'save': ('Click', '//*[@id="editEntityInformation_form"]/div[2]/a[1]'),
    }

    expected = "Saved information"
    process = UI()
    process.update(runtime)
    order = ('experience', 'addExperience', 'addEntity', 'name', 'addressDesc',
             'addressType',  # 'address1','address2','city','state','zipcode',
             'email', 'emailType', 'save', )
    process.execute(order)
    process.results(expected, 'toast-container', 8)
    process.wait(3)
    process.teardown()
