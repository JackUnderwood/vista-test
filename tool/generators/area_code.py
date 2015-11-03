from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'state': full_path('states_codes'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cumulative, _ = line.split()
            if float(cumulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None):
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return "{0} {1}".format(get_first_name(gender), get_last_name())


def get_area_code():
    file = abspath('tool\\generators\\states_codes')
    # with open(file) as name_file:
    #     for line in name_file:
    #         _state, area_codes = line.split('|')
    #         if _state is state:
    #             return random.choice(area_codes)
    print(file)
    return None
