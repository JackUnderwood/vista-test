__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.file import File
import tool.utilities as utils


class TestSuiteFile(unittest.TestCase):
    print(">> Inside TestSuiteFile class")
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
    def test_file_reset(self):
        print(">>> Inside function test_file_reset()")
        runtime = {
            'reset': ('Click', '//*[@id="vsubnav"]/div/i', )
        }
        expected = 'Options set to default'
        self.process.update(runtime)
        self.process.execute(('reset', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_my_files(self):
        print(">>> Inside function test_my_files()")
        runtime = {
            'myfile': ('Click', '//*[@id="vsubnav"]/div/div[6]/span', )
        }
        expected = self.user_name
        self.process.update(runtime)
        self.process.execute(('myfile', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
