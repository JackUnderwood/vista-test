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
    """
    Get license type from license_type table
    :return: dict - returns code as key and description as the value
    {'P': 'Permanent', ... }
    """
    sql = """
    SELECT license_type license, description
    FROM license_types_codes
    WHERE can_use = 'Y'
    """

    # [('P', 'Permanent'), ... ]
    record_set = get_record(sql)
    result = dict(record_set)
    return result


def get_license_fullname(license_type):
    """
    Returns the full license name--the description
    :param license_type: string - 'P'
    :return: string - 'Permanent'
    """
    lic = get_license_type()
    return lic[license_type]
