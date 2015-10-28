import unittest

import ui
from ui import UI
from ui.low.file import File
import tool.utilities as utils

__author__ = 'John Underwood'


class TestSuiteFileGeneral(unittest.TestCase):
    ui.log.info(">>> Inside TestSuiteFileGeneral class")
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
        ui.log.info(">>> Inside function test_generic_files()")
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
        ui.log.info(">>> Inside function test_my_files()")
        runtime = {
            'myfile': ('Click', '//*[@id="vsubnav"]/div/div[6]/a[2]', )
        }
        expected = "{}'s Files".format(self.user_name)
        self.process.update(runtime)
        self.process.execute(('myfile', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

