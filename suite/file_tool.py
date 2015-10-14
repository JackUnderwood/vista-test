__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class TestSuiteFileTool(unittest.TestCase):
    print(">> Inside TestSuiteFileTool class")
    process = UI()

    def setUp(self):
        File()
        FileSelect()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    def test_file_rename(self):
        print(">>> Inside function test_file_rename()")
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
        runtime = {
            'reassign': ('Click', '#reassign'),
            'inputProvider': (
                'Type',
                '#reassigneSearchDescription',
                'lambert matt st:wv'
            ),
            'selectProvider': ('Click', '//*[@item_id="91273"]'),
            'subcategory': ('Select', '#reassignCategory', 'Certifications'),
            'copy': ('Click', '#reassignCopy')
        }

        expected = "File move successful"
        self.process.update(runtime)
        order = ('reassign', 'inputProvider', 'selectProvider',
                 'subcategory', 'copy')
        self.process.execute(order)
        self.process.results(expected)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    def test_file_delete(self):
        print(">>> Inside function test_file_delete()")
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
