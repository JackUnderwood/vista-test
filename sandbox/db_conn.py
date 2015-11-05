import pymssql

import book
from tool.utilities import get_configurations

__author__ = 'John Underwood'


server = get_configurations('SYSTEM', 'db_server')
user = get_configurations('USER', 'db_user')

# Create a book.py file at the root level and add your password.
conn = pymssql.connect(server, user, book.password, 'VISTA_Test')

cursor = conn.cursor()
cursor.execute(
    "SELECT * FROM name_list WHERE entity_id_number={}".format('778784'))
row = cursor.fetchone()
while row:
    print("ID={}, Name={}, First={}".format(row[0], row[1], row[2]))
    row = cursor.fetchone()

conn.close()
