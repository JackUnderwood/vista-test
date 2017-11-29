from ui import UI
from ui.low.find import Find

__author__ = 'John Underwood'


class PhysicalAddress(UI):
    """
    Adds a new physical address for a provider.
    Values are preset using our VISTA physical address.
    May override the address description, addressType, address1, address2,
    city, state, zipCode, and country fields.
    """
    def __init__(self, override=None):
        super().__init__()
        Find(override)

        runtime = {
            'description': 'QA Physical Address',
            'addressType': 'Other',
            'address1': '2800 E Cottonwood Pkwy',
            'address2': 'Suite 400',
            'city': 'Cottonwood Heights',
            'state': 'Utah',
            'zipCode': '84121',
            'country': 'United States',
            # Executable runtime elements follow.
            'home': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[5]/i',),
            'add': ('Click', '//*[@id="addressGrid_form"]/a'),
            'addrDescription': ('Type', '#address_description', '&description;'),
            'addrType': ('Select', '#correspondence_method_type_id',
                         '&addressType;'),
            'addr1': ('Type', '#address_1', '&address1;'),
            'addr2': ('Type', '#address_2', '&address2;'),
            'addrCity': ('Type', '#city', '&city;'),
            'addrState': ('Select', '#state', '&state;'),
            'addrZip': ('Type', '#zip_code', '&zipCode;'),
            'addrCountry': ('Select', '#country_code', '&country;'),
            'save': ('Click', '#save-n-check'),
            'saveAddressCheck': ('Click', 'css=.waves-effect.waves-light.btn.'
                                          'right-align.modal-action.'
                                          'modal-close'),
            'closeAddresses': ('Click', '#addressGridClose'),
            'closeWorkspace': ('Click', 'css=.waves-effect.waves-light.'
                                        'btn.right-align')
        }
        process = UI(override)
        process.update(runtime)
        order = ('home', 'add', 'addrDescription', 'addrType', 'addr1', 'addr2',
                 'addrCity', 'addrState', 'addrZip', 'addrCountry', 'save',
                 'saveAddressCheck', 'closeAddresses', 'closeWorkspace')
        process.execute(order)
        process.wait()
