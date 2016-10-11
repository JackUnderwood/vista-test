import unittest

import ui
from ui import UI
from ui.low.file import File
from ui.high.file_select import FileSelect

__author__ = 'John Underwood'


class TestSuiteFileTool(unittest.TestCase):
    ui.log.info(">>> Inside TestSuiteFileTool class")
    process = UI()
    debug = 'reassign'  # use 'all'; or test individual case methods below
    override = {'cat': '3', }  # Correspondence category

    def setUp(self):
        File()
        FileSelect(self.override)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'rename' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_rename(self):
        ui.log.info(">>> Inside function test_file_rename()")
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

    @unittest.skipUnless(debug is 'reassign' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_reassign(self):
        ui.log.info(">>> Inside function test_file_reassign()")

        runtime = {
            'reassign': ('Click', '#reassign'),
            'selectType': (
                'Click',
                'css=#reassignSearchContainer>div>div.find-form>'
                'i.vistatt.search-type.fa.fa-user.active'),
            'select': ('Click', 'css=#reassignSearchContainer>div>'
                                'div.find-form>div>a:nth-child(3)'),
            'inputProvider': (
                'Type',
                '#reassignSearchDescription',
                'lambert matt st:wv'),
            'selectProvider': ('Click', '//*[@item_id="91273"]'),
            'subcategory': ('Select', '#reassignCategory', 'Certifications'),
            'copy': ('Click', '#reassignCopy')
        }
        expected = "File copied successfully."
        self.process.update(runtime)
        order = ('reassign', 'selectType', 'select', 'inputProvider',
                 'selectProvider', 'subcategory', 'copy')
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'rotate' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_rotate(self):
        ui.log.info(">>> Inside function test_file_rotate()")

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

    @unittest.skipUnless(debug is 'edit' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_edit(self):
        ui.log.info(">>> Inside function test_file_edit() - splice the file")

        runtime = {
            'edit': ('Click', '#edit'),
            'next': (
                'Click', '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[2]'),
            'selectPage1': (
                'Click',
                '//*[@id="toolPanelContainer"]/div[2]/div[4]/div[2]/div[2]'),
            'subcategory': ('Select', '#editCategory', 'Provider Licensing'),
            'filename': ('Type', '#editFilename', 'qa_automation.pdf'),
            'create': (
                'Click', '//*[@id="toolPanelContainer"]/div[2]/div[7]/a[3]')
            # TODO: auto generate file names
        }
        expected = "Files successfully edited"
        self.process.update(runtime)
        order = ('edit', 'next', 'selectPage1', 'next', 'subcategory',
                 'filename', 'next', 'create')
        self.process.execute(order)
        self.process.wait(1)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'deactivate' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_deactivate(self):
        ui.log.info(">>> Inside function test_file_deactivate()")

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

    @unittest.skipUnless(debug is 'reactivate' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file_reactivate(self):
        ui.log.info(">>> Inside function test_file_reactivate()")

        runtime = {
            'active': (
                'Click', 'css=#vsubnav>div>div.fileActiveContainer>label'),
            'delete': ('Click', '#delete'),
            'activate': ('Click', '//*[@button="delete"]'),
        }
        expected = "Status updated successfully"
        self.process.update(runtime)
        order = ('active', )
        self.process.execute(order)
        FileSelect(self.override)
        order = ('delete', 'activate')
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
