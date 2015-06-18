__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


# Note: may want to put tests that use FileSelect class in a separate suite.
class TestSuiteFile(unittest.TestCase):
    print(">> Inside TestSuiteFile class")
    process = UI()

    # def __init__(self, override=None):
    #     super().__init__(override)
    #     self.process = UI()

    def setUp(self):
        File()

    def tearDown(self):
        pass

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

    def test_file_rename(self):
        print(">>> Inside function test_file_rename()")
        FileSelect()

        runtime = {
            'rename': ('Click', '#rename'),
            'execRename': ('Click', '//*[@button="rename"]')
        }
        expected = "Document Description Updated"
        self.process.update(runtime)
        order = ('rename', 'execRename')
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_file_reassign(self):
        print(">>> Inside function test_file_reassign()")
        FileSelect()

        runtime = {
            'reassign': ('Click', '#reassign'),
            'inputProvider': (
                'Type',
                '#reassigneSearchDescription',
                'lambert matt st:wv'
            ),
            'selectProvider': ('Click', '#user_name'),
            'category': ('Click', '//*[@id="reassignObjectContainer"]/ul'),
            'catLicenses': ('Click', '//*[@title="Licenses"]'),
            'subcategory': ('Click', '//*[@id="reassignCategoryContainer"]/ul'),
            'subcatStateLicense': ('Click', '//*[@title="State License"]'),
            'copy': ('Click', '#reassignCopy')
        }

        expected = "File move successful"
        self.process.update(runtime)
        order = ('reassign', 'inputProvider', 'selectProvider', 'category',
                 'catLicenses', 'subcategory', 'subcatStateLicense', 'copy')
        self.process.execute(order)
        self.process.results(expected)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_file_delete(self):
        print(">>> Inside function test_file_delete()")
        FileSelect()

        runtime = {
            'delete': ('Click', '#delete'),
            'deactivate': ('Click', '//*[@button="delete"]'),
        }
        expected = "Status updated successfully"
        self.process.update(runtime)
        order = ('delete', 'deactivate')
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_file_rotate(self):
        print(">>> Inside function test_file_rotate()")
        FileSelect()

        runtime = {
            'rotate': ('Click', '#rotate'),
            'selectPage': (
                'Click',
                '//*[@id="toolPanelContainer"]/div[2]/div/div/div[2]/div[2]',
            ),
            'rotateLeft': ('Click', '#rotateLeft'),
        }

        expected = "Rotate was successful"
        self.process.update(runtime)
        order = ('rotate', 'selectPage', 'rotateLeft', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @classmethod
    def tearDownClass(cls):
        UI().teardown()
