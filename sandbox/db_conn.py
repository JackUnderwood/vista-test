

# import book
# from tool.utilities import CONFIG_FILE
from tool.db import get_record

"""
This file is independent from the VTF, so it requires its
own configparser. Change ABS_PATH if this project changes
to a new location.
"""

__author__ = 'John Underwood'

sql = "SELECT * FROM name_list WHERE entity_id_number='%s'" % '778784'

row = get_record(sql)
print(row[0])
print(len(row))
print("ID={}, Name={}, First={}".format(row[0][0], row[0][1], row[0][2]))

