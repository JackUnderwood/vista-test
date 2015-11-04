from os.path import abspath
import random

PATH = 'tool\\generators\\states_codes'


def get_area_code(state):
    """
    Gets the State's area code.
    :param state: string
    :return: string - the area code
    """
    file = abspath(PATH)
    with open(file) as name_file:
        for line in name_file:
            _state, area_codes = line.split('|')
            if state.capitalize() == _state:
                return random.choice(area_codes.split())

    return ''
