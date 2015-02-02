#! python
import os
import sys
import importlib

from tool.clog import CLog

log = CLog(name="vtf", log_name="vtf")


def arguments_parser(args):
    """
    Return only the path for now.
    """
    log.info("Script's file name: {0}".format(args[0]))
    log.info("Number of arguments: {0}".format(len(args)))
    counter = 0
    for arg in args:
        counter += 1
        if arg.find("/"):
            log.info("Found the path")
            return arg
        log.info(" Argument index[{0}] : {1}".format(counter, arg))
    return ""


# Get the arguments passed in at the command line.
if len(sys.argv) > 1:
    path = arguments_parser(sys.argv[1:])  # pass just the args
    full_path = path + ".py"
    if os.path.exists(full_path):
        log.debug("This is the path: {0}".format(full_path, ))
    else:
        #  TODO: throw an exception here - needs improvement
        log.error("path '{0}' does not exist".
                  format(full_path, ))
        raise Exception

    # Need replace to make path friendly for __import__()
    path = path.replace('\\', '.')  # for win paths
    path = path.replace('/', '.')  # for unix paths
    path = path.replace('.py', '')
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
