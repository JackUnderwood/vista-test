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
        override = {'level': '4'}
        File(override)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipIf(debug, "debugging a single test")
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

    @unittest.skipIf(debug, "debugging a single test")
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

    @unittest.skipIf(debug, "debugging a single test")
    def test_category(self):
        print(">>> Inside function test_category()")
        runtime = {
            'category': ('Click', '//*[@id="vsubnav"]/div/div[2]/ul', )
        }
        expected = "System Correspondence"  # can also use 'System Documents'
        self.process.update(runtime)
        self.process.execute(('category', ))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipIf(debug, "debugging a single test")
    def test_category_one_selected(self):
        print(">>> Inside function test_category_one_selected()")
        runtime = {
            'category': ('Click', '//*[@id="vsubnav"]/div/div[2]/ul', ),
            'selectCategoryOption': (
                'Click',
                '//*[@id="vsubnav"]/div/div[2]/ul/ul/li[1]'
            ),
        }
        expected = "Category (1)"
        self.process.update(runtime)
        self.process.execute(('category', 'selectCategoryOption'))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_subcategory(self):
        # TODO: test_subcategory() gives a false positive result
        print(""">>> Inside function test_subcategory().
        This should fail, but doesn't; false positive result.""")
        runtime = {  # really need to click subcategory
            'reset': ('Click', '//*[@id="vsubnav"]/div/i', )
        }
        expected = 'System Files'
        self.process.update(runtime)
        self.process.execute(('reset',))
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
