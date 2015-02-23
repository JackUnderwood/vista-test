#! python
import os
import sys
import importlib
import pprint

from tool.testrail import *

from tool.vlog import VLog
# TODO: have the ability to set level as a command line arg.
log = VLog(name="vtf", level=10, log_name="vtf")  # set to debug level 10


def arguments_parser(args):
    """
    Return only the path for now.
    """
    log.info("Script's file name: {0}".format(args[0]))
    log.info("Number of arguments: {0}".format(len(args)))
    counter = 0
    arguments = {}
    for arg in args:
        counter += 1
        if arg.find(".\\") == 0:
            log.debug("Found path argument")
            arguments['path'] = arg
        elif arg.find("--log-level=") == 0:
            log.debug("Found level argument")
            arguments['logLevel'] = arg[arg.find("=")+1:]
        log.debug("Argument index[{0}] : {1}".format(counter, arg))
    return arguments


# Get the arguments passed in at the command line.
# Using powershell, path shows: .\vtf.py .\case\testcase
if len(sys.argv) > 1:
    args = arguments_parser(sys.argv[1:])  # send args only
    if 'path' not in args:
        log.critical("vtf <path> <-- You are missing the path argument")
        raise Exception
    if 'logLevel' in args:  # TODO: still not working
        print("INSIDE logLevel")
        log_level = int(args['logLevel'])
        log = VLog(name="start", level=log_level, log_name="start")
        log.info("Testing...")
        log.debug("Testing...")  # this should display if log_level == 10
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
    log.info("New altered path: {0}".format(path,))
    # Import the passed in module - executes it.
    try:
        # See link for alternative:
        # https://docs.python.org/3/reference/import.html
        importlib.import_module(path)
        # command_module = __import__("%s" % path)
    except ImportError as ie:
        #  TODO: test this throw an exception
        log.exception("Thrown exception error: unable to __import__(): {0}".
                      format(ie))
        tb = sys.exc_info()[2]
        raise ImportError().with_traceback(tb)
else:
    log.critical("vtf <path> <-- You are missing the path argument")
