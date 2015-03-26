#! python
import os
import sys
import importlib
import pprint

from tool.testrail import *

import tool.utilities as utils
from tool.vlog import VLog

log = None  # TODO: have the ability to set level as a command line arg.


def arguments_parser(arguments):
    """
    Return only the path for now.
    """
    print(" Script's file name: {0}".format(arguments[0]))
    print(" Number of arguments: {0}".format(len(arguments)))
    counter = 0
    args_dict = {}
    for arg in arguments:
        counter += 1
        if arg.find(".\\") == 0:
            args_dict['path'] = arg
    return args_dict


# Get the arguments passed in at the command line.
# Using powershell, path shows: .\vtf.py .\case\testcase
if len(sys.argv) > 1:
    args = arguments_parser(sys.argv[1:])  # send args only
    if 'path' not in args:
        print("vtf <path> <-- The path argument is incorrectly written")
        raise Exception

    log_level = utils.get_configurations("DEFAULT", "log_level")
    log_level_value = VLog.INFO  # default log level
    if log_level == 'DEBUG':
        log_level_value = VLog.DEBUG
    elif log_level == 'WARNING':
        log_level_value = VLog.WARNING
    elif log_level == 'ERROR':
        log_level_value = VLog.ERROR
    elif log_level == 'CRITICAL':
        log_level_value = VLog.CRITICAL
    log = VLog(name="vtf", level=log_level_value, log_name="VTF")
    # log.debug("Testing...")  # this should display if log_level == 10
    # log.info("Testing...")
    # log.warning("Testing...")
    # log.error("Testing...")
    # log.critical("Testing...\n")

    path = args['path']
    full_path = path
    if path.find('.py') is -1:
        full_path = path + ".py"
    if os.path.exists(full_path):
        log.debug("This is the path: {0}".format(full_path, ))
        # client = APIClient('https://vistastaff.testrail.com/')
        # client.user = 'john.underwood@vistastaff.com'
        # client.password = '********'
        # case = client.send_get('get_case/8')
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(case)
    else:
        #  TODO: throw an exception here - needs improvement
        log.error("path '{0}' does not exist".
                  format(full_path, ))
        raise Exception

    # Need replace to make path friendly for __import__()
    # Change path '.\case\testcase' to 'case.testcase'
    if path.find('.') == 0:
        # Using powershell, path shows: '.\case\testcase' to 'case\testcase'
        path = path[2:]
    path = path.replace('\\', '.')  # for win paths
    path = path.replace('/', '.')  # for unix paths
    path = path.replace('.py', '')
    # The path should now be 'case.testcase'
    log.info("The new, altered path: {0}".format(path,))
    # Import the passed in module - executes it.
    try:
        # See link for alternative:
        # https://docs.python.org/3/reference/import.html
        importlib.import_module(path)
        log.debug("Try importlib {}".format(path,))
        # command_module = __import__("%s" % path)
    except ImportError as ie:
        #  TODO: test this throw an exception
        log.exception("Thrown exception error: unable to __import__(): {0}".
                      format(ie))
        tb = sys.exc_info()[2]
        raise ImportError().with_traceback(tb)
else:
    log.critical("vtf <path> <-- You are missing the path argument")
