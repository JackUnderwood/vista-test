__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.file import File
import tool.utilities as utils


class TestSuiteFileGeneral(unittest.TestCase):
    print(">> Inside TestSuiteFileGeneral class")
    debug = False
    process = UI()
    user_name = utils.get_configurations("USER", "name")

    def setUp(self):
        File()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipIf(debug, "debugging a single test")
    def test_generic_files(self):
        print(">>> Inside function test_category()")
        runtime = {
            'generic': ('Click', '//*[@id="vsubnav"]/div/div[6]/a[1]', )
        }
        expected = "System Files"  # can also use 'System Documents'
        self.process.update(runtime)
        self.process.execute(('generic', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipIf(debug, "debugging a single test")
    def test_my_files(self):
        print(">>> Inside function test_my_files()")
        runtime = {
            'myfile': ('Click', '//*[@id="vsubnav"]/div/div[6]/a[2]', )
        }
        expected = self.user_name + "'s Files"
        self.process.update(runtime)
        self.process.execute(('myfile', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

