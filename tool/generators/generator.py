__author__ = 'John Underwood'
"""
TODO: Create a set of generators,
i.e. phone number generator, address generator, etc.
"""
from names import get_full_name


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


def gen_email(full_name):
    """
    Takes pieces from full name and creates an email address
    :param full_name: string '<first name> <last name>'
    :return: string 'firstlast@<domain>.com'
    """
    first, last = split_name(full_name)
    email = first + last + '@gmail.com'
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


# ^*^*^*^*^ Helper functions ^*^*^*^*^
def split_name(full_name):
    name_list = full_name.split(' ')
    first_name, last_name = name_list[0], name_list[1]
    return first_name, last_name
