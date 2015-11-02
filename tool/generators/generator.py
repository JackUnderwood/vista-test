import random
import string

from names import get_full_name

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


def gen_phone_number(state):
    """
    Components of a phone number are (i.e. 123-456-9876)
    Area Code -> 123,
    Exchange Code, -> 456, and
    Subscriber Number - > 9876
    The area code will be determined by the state that is passed in, and
    randomly selected from the list of associated numbers.
    The exchange code is generated using [2-9] for first digit, and [0-9]
    for second and third digits--exception, third digit cannot be 1 if
    the second digit is 1.
    The subscriber number is [0-9] for each of the four digits, [0000-9999]
    See https://en.wikipedia.org/wiki/North_American_Numbering_Plan
    :param state: string with full state's name, e.g. "New York"
    :return: string
    """
    return ''


def gen_address():
    """
    Dict keys with full address
    :return: dict {'address1': <address1>, 'address2': <address2>,
    'address3': <address3>, 'city': <city>, 'state': <state>,
    'zipcode': <zipcode>}
    """
    return ''


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


def gen_key():
    """
    Create a unique key value; use as an identifier for text
    :return: a 12 character string
    """
    return ''.join(random.choice(string.ascii_uppercase) for i in range(12))


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


def __state():
    """
    STUB
    :return: string
    """
    return ''


def __zip_code():
    """
    STUB
    :return: string
    """
    return ''


# ^*^*^*^*^ Helper functions ^*^*^*^*^
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
    num = num.zfill(base_length)  # reduce the above to this single line
    return num
