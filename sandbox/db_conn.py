# import pymssql
# import configparser

# import book
# from tool.utilities import CONFIG_FILE
from tool.db import get_record

"""
This file is independent from the VTF, so it requires its
own configparser. Change ABS_PATH if this project changes
to a new location.
"""

__author__ = 'John Underwood'

sql = "SELECT * FROM name_list WHERE entity_id_number={}".format('778784',)

row = get_record(sql)
print(row[0])
print(len(row))
print("ID={}, Name={}, First={}".format(row[0][0], row[0][1], row[0][2]))
# ABS_PATH = 'C:/Projects/test/'  # UPDATE path if necessary
#
# config = configparser.ConfigParser()
# config.sections()
# config.read(ABS_PATH + CONFIG_FILE)
# server = config.get("SYSTEM", "db_server")
# user = config.get("USER", "db_user")
#
#
# # You'll need to create a book.py file at the root level and add your password
# # Add a single line >>> password = "myPassword"
# conn = pymssql.connect(server, user, book.password, 'VISTA_Test')
#
# cursor = conn.cursor()
# cursor.execute(
#     'SELECT * FROM name_list WHERE entity_id_number={}'.format('778784'))
# row = cursor.fetchone()
# while row:
#     print("ID={}, Name={}, First={}".format(row[0], row[1], row[2]))
#     row = cursor.fetchone()
#
# conn.close()
