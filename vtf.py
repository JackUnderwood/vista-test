#! python
"""
Reserve words for the Vista Testing Framework:
• suite - files that are test suites must reside inside the ./suite/ dir
• test - used in test function names
"""
import os
import sys
import importlib
import unittest
import pprint

from tool.testrail import *

import tool.utilities as utils
from tool.vlog import VLog

log = None  # TODO: have the ability to set level as a command line arg.
# url = None


def arguments_parser(arguments):
    """
    Return only the path for now.
    """
    print(" Script's file name: {}".format(arguments[0]))
    print(" Number of arguments: {}".format(len(arguments)))
    args_dict = {}
    for arg in arguments:
        if arg.find(".\\") == 0:
            args_dict['path'] = arg
        elif arg.find('=') is not -1:
            args_dict[arg[:arg.find('=')]] = arg[arg.find('=')+1:]
    print(" Argument List: {}".format(str(args_dict), ))
    return args_dict


# Get the arguments passed in at the command line.
# Using powershell terminal, path shows: .\vtf.py .\case\testcase
# Command line arguments: platform=test log_level=warning anything=else
# platform may equal 'test' or 'dev'
if len(sys.argv) > 1:
    args = arguments_parser(sys.argv[1:])  # send args only
    if 'path' not in args:
        print("vtf <path> <-- The path argument is incorrectly written")
        raise Exception

    log_level = utils.get_configurations("LOGGING", "log_level")
    if 'log_level' in args:
        log_level = args['log_level'].upper()

    log_level_value = VLog.INFO  # default if everything else fails
    if log_level == 'DEBUG':
        log_level_value = VLog.DEBUG
    elif log_level == 'WARNING':
        log_level_value = VLog.WARNING
    elif log_level == 'ERROR':
        log_level_value = VLog.ERROR
    elif log_level == 'CRITICAL':
        log_level_value = VLog.CRITICAL
    print(" Log level is {}".format(log_level_value, ))
    log = VLog(name="vtf", level=log_level_value, log_name="VTF")
    # log.debug("Testing debug...")  # this displays if log_level == 10
    # log.info("Testing info...")
    # log.warning("Testing warning...")
    # log.error("Testing error...")
    # log.exception("Testing exception...")
    # log.critical("Testing critical...")

    url = utils.get_configurations("DEFAULT", "test_url")
    if 'platform' in args:
        if args['platform'] == 'test':
            url = utils.get_configurations("DEFAULT", "test_url")
        elif args['platform'] == 'dev':
            url = utils.get_configurations("DEFAULT", "dev_url")
        else:
            log.warning("Unrecognizable platform: {}".format(args['platform'],))
    utils.url = url  # set the global only once, and only here

    path = args['path']
    full_path = path
    if path.find('.py') is -1:
        full_path = path + ".py"
    if os.path.exists(full_path):
        log.debug("This is the path: {}".format(full_path, ))
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

    if path.find('suite') is not -1:
        log.info("This is a SUITE!")
        suite = unittest.TestSuite()
        try:
            mod = __import__(path, globals(), locals(), ['suite'])
            suite_function = getattr(mod, 'suite')
            suite.addTest(suite_function)
            print("The 'try:' was successful")
        except (ImportError, AttributeError):
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(path))
        unittest.TextTestRunner().run(suite)  # RUN the suite

    else:
        # Import the passed-in module & executes it.
        try:
            # See link for alternative:
            # https://docs.python.org/3/reference/import.html
            importlib.import_module(path)  # RUN the test case
            log.debug("Successfully tried importlib {}".format(path,))
            # command_module = __import__("%s" % path)
        except ImportError as ie:
            #  TODO: test this throw an exception
            log.exception("Thrown exception error: unable to __import__(): {0}".
                          format(ie))
            tb = sys.exc_info()[2]
            raise ImportError().with_traceback(tb)
else:
    log.critical("vtf <path> <-- You are missing the path argument")

