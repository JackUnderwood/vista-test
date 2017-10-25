import random
import string
import datetime
import math

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

    exchange = _get_exchange_number()
    # The following should be a rare occurrence.
    while exchange[1] == '1' and exchange[2] == '1':
        exchange = _get_exchange_number()

    subscriber_number = _num_pad(random.randrange(0, 10000), 4)

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
      of 0001 through 9998
    :return: string <social security number>
    """
    area_portion = [x for x in range(1, 666)] + [x for x in range(667, 900)]
    random.shuffle(area_portion)
    area = _num_pad(area_portion[0], 3)  # use the first element
    group = _num_pad(random.randrange(1, 100), 2)
    serial = _num_pad(random.randrange(1, 9999), 4)
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
    assert range_size > 0, 'range_size must be greater than zero'
    return ''.join(random.choice(string.ascii_uppercase)
                   for _ in range(range_size))


def gen_number(size, padding=None):
    """
    Generate a number 1 through 'size'; may include left-zero padding.
    :param size: integer
    :param padding: integer - optional
    :return: string, e.g. '42'
    """
    assert int(size) > 0, 'size must be greater than zero'
    value = str(random.randrange(1, size + 1, 1))
    if padding is not None:
        value = _num_pad(value, padding)
    return value


def gen_account_number(size=12):
    """
    Generate an account number with a mix of digits and
    alpha chars-- three quarters of chars are digits
    :param size: integer - account number size/length
    :return: string - e.g. 'N2426A69'
    """
    assert size > 0, 'size must be greater than zero'
    char_size = int(math.floor(size/4))

    chars = list(string.ascii_uppercase)
    random.shuffle(chars)
    digits = [random.choice(string.digits) for _ in range(size-char_size)]
    account_number = digits + chars[:char_size]
    random.shuffle(account_number)
    return ''.join(account_number)


def split_name(full_name):
    """
    Split the full name into first and last
    :param full_name: <full name>
    :return: tuple of strings (<firstname>, <lastname>)
    """
    name_list = full_name.split(' ')
    first_name, last_name = name_list[0], name_list[1]
    return first_name, last_name


def get_future_date(days=1, style='%m/%d/%Y'):
    """
    Get a date from today's date to number of days in the future
    :param days: int
    :param style: string
    :return: string - '09/05/2017'
    """
    now = datetime.datetime.now()
    diff = datetime.timedelta(days=days)
    future = now + diff
    return future.strftime(style)


def get_today_date(style='%m/%d/%Y'):
    """
    Return today's date.
    :param style: string
    :return: string - '10/25/2017'
    """
    now = datetime.datetime.now()
    return now.strftime(style)


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
def _get_exchange_number():
    return _num_pad(random.randrange(200, 1000), 3)


def _num_pad(num, width):
    """
    Pad a number with zeros
    Example: num may be 42, and width is 5, then the return
    value should be '00042'
    :param num: number or number as a string
    :param width: integer
    :return: a number as a string
    """
    num = str(num)
    padded_num = num.zfill(width)
    return padded_num


