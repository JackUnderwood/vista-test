#! python
__author__ = 'John Underwood'
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="provides path to test case or suite", type=str)
parser.add_argument("-p", "--platform", help="determines test or dev", type=str)
parser.add_argument("-l", "--log", help="determines log level", type=str)
args = parser.parse_args()

print("PATH:", args.path)
print("PLATFORM:", args.platform)
print("LOG LEVEL:", args.log)
