#! python
"""
Reserve words for the Vista Testing Framework:
• suite - files that are test suites must reside inside the ./suite/ dir
• test - used in test function names

Using powershell terminal, path shows: .\vtf.py .\case\<testcase>
Command line arguments: --platform=test --log=warning --<anything=else>
platform may equal 'test' or 'dev'
"""
import os
import sys
import importlib
import unittest
import argparse
import pprint

from tool.testrail import *

import tool.utilities as utils
from tool.vlog import VLog

# ^*^*^*^*^*^* Get the arguments passed in at the command line *^*^*^*^*^*^
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="provides path to test case or suite")
parser.add_argument("-p", "--platform", type=str, help="determines test or dev")
parser.add_argument("-g", "--log_level",  type=str, help="sets the log level")
args = parser.parse_args()

# ^*^*^*^*^*^* Set up the logging *^*^*^*^*^*^
log = None
log_level = utils.get_configurations("LOGGING", "log_level")

if args.log_level:
    log_level = args.log_level.upper()
print(" LOG LEVEL:", log_level)
log_level_value = VLog.INFO  # default if everything else fails
if log_level == 'DEBUG':
    log_level_value = VLog.DEBUG
elif log_level == 'WARNING':
    log_level_value = VLog.WARNING
elif log_level == 'ERROR':
    log_level_value = VLog.ERROR
elif log_level == 'CRITICAL':
    log_level_value = VLog.CRITICAL
print(" LOG LEVEL is {}".format(log_level_value, ))

log = VLog(name="vtf", level=log_level_value, log_name="VTF")
# log.debug("Testing debug...")  # this displays if log_level == 10
# log.info("Testing info...")
# log.trace("Testing trace...")
# log.warning("Testing warning...")
# log.error("Testing error...")
# log.exception("Testing exception...")
# log.critical("Testing critical...")

# ^*^*^*^*^*^* Set up the test environment *^*^*^*^*^*^
url = utils.get_configurations("DEFAULT", "test_url")
if args.platform:
    if args.platform == 'test':
        url = utils.get_configurations("DEFAULT", "test_url")
    elif args.platform == 'dev':
        url = utils.get_configurations("DEFAULT", "dev_url")
    elif args.platform == 'local':
        url = utils.get_configurations("DEFAULT", "local_url")
    else:
        log.warning("Unrecognizable platform: {}".format(args['platform'],))
utils.url = url  # set the global only once, and only here

# ^*^*^*^*^*^* Launch the test case or suite *^*^*^*^*^*^
path = args.path
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
    log.error("path '{0}' does not exist".format(full_path, ))
    raise Exception

# Need replacement to make path friendly for __import__()
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
        # log.debug("Successfully tried importlib {}".format(path,))
        # command_module = __import__("%s" % path)
    except ImportError as ie:
        log.exception("Thrown exception error: unable to __import__(): {}: {}".
                      format(ie, path, ))
        tb = sys.exc_info()[2]
        raise ImportError().with_traceback(tb)
