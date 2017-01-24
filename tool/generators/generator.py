import random
import string

from names import get_full_name
from tool.generators.state_codes import get_random_area_code
from tool.generators.state_codes import get_random_state_iso_code

__title__ = 'generator'
__version__ = '0.1.1'
__author__ = 'John Underwood'
"""
TODO: Create a set of generators,
i.e. phone number generator, address generator, etc.
"""

# Note: custom domains make up for a third of email accounts, so every
# third email account should be 'other'.
COMMON_EMAIL_DOMAINS = ('gmail', 'yahoo', 'aol', 'comcast', 'hotmail', 'msn',
                        'sbcglobal', 'verizon', 'roadrunner', 'optimum')


def gen_name(gender=None):
    """
    Wraps the names.get_full_name(), so user only needs to import
    this module.
    :param gender: 'male' or 'female' - see names.get_first_name()
    :return: string <full name>
    """
    return get_full_name(gender)


def gen_phone_number(state_iso_code):
    """
    Components of a phone number are (i.e. 123-456-9876):
    Area Code -> 123,
    Exchange Code, -> 456, and
    Subscriber Number - > 9876
    - The 'area code' will be determined by the state_iso_code that is passed in,
    and randomly selected from the list of associated area codes.
    - The 'exchange code' is generated using [2-9] for first digit, and [0-9]
    for second and third digits--exception, third digit cannot be 1 if
    the second digit is 1.
    - The 'subscriber number' is [0-9] for each of the four digits, [0000-9999]
    See https://en.wikipedia.org/wiki/North_American_Numbering_Plan
    :param state_iso_code: string with state_iso_code's name, e.g. "VA"
    :return: string - format aaaeeessss (i.e. 1234569876)
    """
    area_code = get_random_area_code(state_iso_code)

    exchange = get_exchange_number()
    # The following should be a rare occurrence.
    while exchange[1] == '1' and exchange[2] == '1':
        exchange = get_exchange_number()

    subscriber_number = num_pad(random.randrange(0, 10000), 4)

    return area_code + exchange + subscriber_number


def gen_address():
    """
    Dict keys with full address
    :return: dict {'address1': <address1>, 'address2': <address2>,
    'address3': <address3>, 'city': <city>, 'state_iso_code': <state_iso_code>,
    'zipcode': <zipcode>}
    """
    state_iso_code = get_random_state_iso_code()
    zip_code = get_random_area_code(state_iso_code)
    address = {'stateIsoCode': state_iso_code,
               'zipCode': zip_code, }
    return address


def gen_ssn():
    """
    SSN format is <aaa-gg-ssss> area, group, and serial.
    - The area portion of ssn--first three digits--000, 666, and 900-999
      are excluded; includes positive integers from 001-665 667-899.
    - The group portion of ssn is 01 through 99.
    - The serial portion of ssn--last four digits--includes positive integers
      of 0001 through 9999
    :return: string <social security number>
    """
    area = num_pad(random.randrange(1, 900), 3)
    g = lambda x: str(x) if x > 9 else '0{}'.format(x,)
    group = g(random.randrange(1, 99))
    serial = num_pad(random.randrange(1, 9999), 4)
    return area + '-' + group + '-' + serial


def gen_email(full_name):
    """
    Takes pieces from full name and creates an email address
    :param full_name: string '<first name> <last name>'
    :return: string 'firstlast@<domain>.com'
    """
    first, last = split_name(full_name)
    domain = COMMON_EMAIL_DOMAINS[
        random.randrange(0, len(COMMON_EMAIL_DOMAINS), 1)]
    email = first[:2] + last + '@' + domain + '.com'
    return email.lower()


def gen_key(range_size=12):
    """
    Create a unique key value; use as an identifier for text
    :param range_size: integer - number of chars in string
    :return: a 12 character string - default 12
    """
    return ''.join(random.choice(string.ascii_uppercase)
                   for i in range(range_size))


def gen_number(number):
    """
    Generate a number 0 through 'number'
    :param number: integer in the form of a number or string
    :return: number as type string, e.g. '42'
    """
    base_length = len(str(number))
    str_num = str(random.randrange(0, number, 1))
    return num_pad(str_num, base_length)


# ^*^*^*^*^ Private functions ^*^*^*^*^
def __address1():
    """
    STUB
    :return: string
    """
    return ''


def __address2():
    """
    STUB
    :return: string
    """
    return ''


def __address3():
    """
    STUB
    :return: string
    """
    return ''


def __city():
    """
    STUB
    :return: string
    """
    return ''


def __state_iso_code():
    """
    STUB
    :return: string - two characters
    """
    return ''


def __zip_code():
    """
    STUB
    :return: string
    """
    return ''


# ^*^*^*^*^ Helper functions ^*^*^*^*^
def get_exchange_number():
    return num_pad(random.randrange(200, 1000), 3)


def split_name(full_name):
    """
    Split the full name into first and last
    :param full_name: <full name>
    :return: tuple of strings (<firstname>, <lastname>)
    """
    name_list = full_name.split(' ')
    first_name, last_name = name_list[0], name_list[1]
    return first_name, last_name


def num_pad(num, base_length):
    """
    Pad a number with zeros
    Example: num may be 42, and base_length is 5, then the return
    value should be '00042'
    :param num: number or number as a string
    :param base_length: integer
    :return: a number as a string
    """
    num = str(num)
    # while len(num) < base_length:
    #     num = '0' + num
    num = num.zfill(base_length)  # reduce the 'while' to this single line
    return num
