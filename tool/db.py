import pymssql

import tool.utilities as utils
from book import password

""" Everything to do with database access.
"""
__author__ = "John Underwood"


def get_record(sql):
    """
    Takes in an SQL SELECT statement and returns a list of row(s)
    :param sql: string - SELECT statement only
    :return: list - result of row(s)
    """
    assert "SELECT" in sql
    server = utils.get_configurations('SYSTEM', 'db_server')
    username = utils.get_configurations('USER', 'db_user')
    database = utils.get_configurations('SYSTEM', 'db_test')
    conn = pymssql.connect(server, username, password, database)
    cursor = conn.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()
    result_set = []
    while row:
        result_set.append(row)
        row = cursor.fetchone()

    conn.close()
    return result_set
