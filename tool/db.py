import pymssql

import tool.utilities as utils
from tool.vlog import VLog
from book import password

""" Everything to do with database access.
"""
__author__ = "John Underwood"


def get_record(sql):
    """
    Takes in an SQL SELECT statement and returns a list of row(s)
    :param sql: string - SELECT statement only
    :return: two dimensional list - rows x columns
    """
    log = VLog()
    assert "SELECT" in sql
    server = utils.get_configurations('SYSTEM', 'db_server')
    username = utils.get_configurations('USER', 'db_user')
    database = utils.get_configurations('SYSTEM', 'db_test')
    conn = None
    try:
        conn = pymssql.connect(server, username, password, database)
    except pymssql.OperationalError as oe:
        log.error('Connection error: {} : check password'.format(oe, ))
        exit()

    cursor = conn.cursor()
    cursor.execute(sql)

    row = cursor.fetchone()
    result_set = []
    while row:
        result_set.append(row)
        row = cursor.fetchone()

    conn.close()
    return result_set
