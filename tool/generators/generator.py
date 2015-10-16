import random
import string

from names import get_full_name

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
    """
    SSN format is <aaa-gg-ssss> area, group, and serial.
    - The area portion of ssn--first three digits--000, 666, and 900-999
    are excluded; includes positive integers from 001-665 667-899.
    - The group portion of ssn is 01 through 99.
    - The serial portion of ssn--last four digits--includes positive integers
    of 1 through 9999
    :return:
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


# def format_serial(n):
#     """
#     Provides the serial portion of ssn--last four digits <aaa-gg-ssss>
#     :param n: positive integer of 1 through 9999
#     :return: string of serial portion of ssn
#     """
#     if n > 999:
#         s = str(n)
#     elif n > 99:
#         s = '0{}'.format(n)
#     elif n > 9:
#         s = '00{}'.format(n)
#     else:
#         s = '000{}'.format(n)
#     return s
#
#
# def format_area(n):
#     """
#     Provides formatting for area portion of ssn--first three digits
#     Note: 000, 666, and 900-999 are excluded
#     :param n: positive integer from 001-665 667-899.
#     :return: string of area portion of ssn
#     """
#     if n > 99:
#         a = str(n)
#     elif n > 9:
#         a = '0{}'.format(n)
#     else:
#         a = '00{}'.format(n)
#     return a


# ^*^*^*^*^ Helper functions ^*^*^*^*^
def split_name(full_name):
    name_list = full_name.split(' ')
    first_name, last_name = name_list[0], name_list[1]
    return first_name, last_name


def num_pad(num, base_length):
    num = str(num)
    done = False
    while not done:
        if len(num) < base_length:
            num = '0' + num
        else:
            done = True
    return num
