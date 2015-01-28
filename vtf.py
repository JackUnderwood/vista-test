#! python
import os
import sys
import importlib

from tool.clog import CLog



def arguments_parser(args):
    """
    Return only the path for now.
    """
    print("Script's file name: ", args[0])
    print("Number of arguments: ", len(args))
    counter = 0
    for arg in args:
        counter += 1
        if arg.find("/"):
            print("Found the path")
            return arg
        print_str = " Argument index[{0}] : {1}".format(counter, arg)
        print(print_str)
        # print("Argument index[%d] : %s" % (counter, arg))
    return ""


# Get the arguments passed in at the command line.
if len(sys.argv) > 1:
    log = CLog(name="vtf", log_name="NAN")
    path = arguments_parser(sys.argv[1:])  # pass just the args
    full_path = path + ".py"
    log.info(" MESSAGE ..........")
    print("\033[95mCOLOR THIS NOW\033[0m")
    if os.path.exists(full_path):
        print("This is the path:", full_path)
    else:
        #  TODO: throw an exception here
        print("Thrown exception: path does not exist:", full_path)
        raise OSError

    # Need replace to make path friendly for __import__()
    path = path.replace('\\', '.')  # for win paths
    path = path.replace('/', '.')  # for unix paths
    path = path.replace('.py', '')
    print("New Path:", path)
    # Import the passed in module - executes it.
    try:
        # See link for alternative:
        # https://docs.python.org/3/reference/import.html
        importlib.import_module(path)
        # command_module = __import__("%s" % path)
    except ImportError:
        #  TODO: test this throw an exception
        print("Thrown exception error: unable to __import__()")
        tb = sys.exc_info()[2]
        raise ImportError(...).with_traceback(tb)
else:
    print("vtf <path> --> You are missing the path argument")
