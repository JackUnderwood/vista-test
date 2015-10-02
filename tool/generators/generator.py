__author__ = 'John Underwood'
"""
TODO: Create a set of generators,
i.e. phone number generator, address generator, etc.
"""
import random

from names import get_full_name

# Note: custom domains make up for a third of email accounts, so every
# third email account should be 'other'.
COMMON_EMAIL_DOMAINS = ('gmail', 'yahoo', 'aol', 'comcast', 'hotmail', 'msn',
                        'sbcglobal', 'verizon', 'roadrunner', 'optimum')


def gen_name(gender=None):
    """
    Wraps the names.get_full_name() and breaks name into pieces
    :param gender: 'male' or 'female' - see names.get_first_name()
    :return: tuple (<full name>, <first name>, <last name>)
    """
    full_name = get_full_name(gender)
    first_name, last_name = split_name(full_name)
    return full_name, first_name, last_name


def gen_phone_number():
    pass


def gen_address():
    """
    Dict keys are address1, address2, address3, city, state, zipcode
    :return: dict of address elements
    """
    pass


def gen_ssn():
    area = format_area(random.randrange(1, 899))
    g = lambda x: str(x) if x > 9 else '0{}'.format(x,)
    group = g(random.randrange(1, 99))
    serial = format_serial(random.randrange(1, 9999))
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


# ^*^*^*^*^ Private functions ^*^*^*^*^
def address1():
    pass


def address2():
    pass


def address3():
    pass


def city():
    pass


def state():
    pass


def zip_code():
    pass


def format_serial(n):
    """
    Provides the serial portion of ssn--last four digits <aaa-gg-ssss>
    :param n: positive integer of 1 through 9999
    :return: string of serial portion of ssn
    """
    if n > 999:
        s = str(n)
    elif n > 99:
        s = '0{}'.format(n)
    elif n > 9:
        s = '00{}'.format(n)
    else:
        s = '000{}'.format(n)
    return s


def format_area(n):
    """
    Provides formatting for area portion of ssn--first three digits
    Note: 000, 666, and 900-999 are excluded
    :param n: positive integer from 001-665 667-899.
    :return: string of area portion of ssn
    """
    if n > 99:
        a = str(n)
    elif n > 9:
        a = '0{}'.format(n)
    else:
        a = '00{}'.format(n)
    return a


# ^*^*^*^*^ Helper functions ^*^*^*^*^
def split_name(full_name):
    name_list = full_name.split(' ')
    first_name, last_name = name_list[0], name_list[1]
    return first_name, last_name
