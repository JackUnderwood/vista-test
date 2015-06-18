"""
Figure out how to launch a suite within the package instead of
using it as a test scaffold, e.g.
if __name__ = "__main__":
    unittest.main()
"""
__author__ = 'John Underwood'
import unittest

testmodules = [
    'case.testsuite',
]

suite = unittest.TestSuite()

for tm in testmodules:
    try:
        mod = __import__(tm, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn)
        print("Try: was successful")
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(tm))

unittest.TextTestRunner().run(suite)
