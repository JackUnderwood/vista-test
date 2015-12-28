from os.path import abspath
import random

PATH = 'tool\\generators\\states_codes'


def get_random_area_code(state_iso_code):
    """
    Gets the State's area code.
    :param state_iso_code: two character string
    :return: string - the area code
    """
    state_iso_code = state_iso_code.upper()
    states = get_states()
    area_codes = states[state_iso_code][1]
    return random.choice(area_codes)


def get_random_state_iso_code():
    """
    Gets a random state_iso_code/country iso
    :return: string - the state_iso_code's 2 digit iso, i.e. Utah's iso is UT
    """
    iso_codes = get_state_iso_codes()
    return random.choice(iso_codes)


def get_random_state_name():
    """
    Gets a random state_iso_code/country name
    :return: string - a state_iso_code's full name
    """
    state_full_names = get_state_names()
    return random.choice(state_full_names)


def get_state_iso_codes():
    """
    Returns a list of U.S. state_iso_code's & territory's iso two character codes
    :return: list - two character iso codes
    """
    states = get_states()
    return list(states.keys())


def get_state_names():
    """
    Returns a list of state_iso_code & country names
    :return: list
    """
    states = get_states()
    return [states[state][0] for state in states]


def get_state_name(state_iso_code):
    """
    :param state_iso_code: two character string
    :return: string - the state_iso_code's full name
    """
    state_iso_code = state_iso_code.upper()
    states = get_states()
    assert state_iso_code in states
    return states[state_iso_code][0]


def get_states():
    """
    Populates a dictionary of U.S.A. states and territories.
    :return: dict - 'key' is State's iso code : 'value' is a tuple in the form of
    <key>: (<state_name>, [<ac1>, <ac2>,..., <acN>],...,N)...}
    {'OR': ('Oregon', ['458', '503', '541', '971']),...,N)...}
    """
    file = abspath(PATH)
    states = {}
    with open(file) as name_file:
        for line in name_file:
            _state, _state_code, _area_codes = line.split('|')
            states[_state_code] = (_state, _area_codes.split())
    return states
