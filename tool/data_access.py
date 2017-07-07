from tool.db import get_record

__author__ = 'John Underwood'


def get_credentials():
    """
    Get credentials from credential_code table
    :return: dict - returns code as key and description as the value
    {'CRNA': 'Certified Registered Nurse Anesthetist', ... }
    """
    sql = """
    SELECT credential_name, description full_name
    FROM credential_code
    WHERE can_use = 1
    """

    # [('CRNA', 'Certified Registered Nurse Anesthetist'), ... ]
    record_set = get_record(sql)
    result = dict(record_set)
    return result


def get_credential_fullname(cred_code):
    """
    Returns the full credential's name--the description
    :param cred_code: string - 'MD'
    :return: string - 'Medical Doctor'
    """
    cred = get_credentials()
    return cred[cred_code]


def get_license_type():
    pass
