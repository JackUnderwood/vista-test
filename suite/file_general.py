__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect


class TestSuiteFoo(unittest.TestCase):
    print(">> Inside TestSuiteFoo class")
    process = UI()

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

    @classmethod
    def tearDownClass(cls):
        UI().teardown()
