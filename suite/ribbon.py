import unittest

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.expand_ribbon import ExpandRibbon

__author__ = 'John Underwood'


class TestSuiteRibbon(unittest.TestCase):
    ui.log.info(">>> Inside TestSuiteFileGeneral class")
    debug = 'workspace'  # use 'all'; or test individual case methods below
    process = UI()
    override = {'rowNum': '7'}

    def setUp(self):
        License()
        Checklist(self.override)
        ExpandRibbon()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().wait(3)
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'entity' or debug is 'all',
                         "testing {}".format(debug,))
    def test_edit_entity(self):
        print(">>> Inside function test_edit_entity()")

        runtime = {
            'editEntity': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li[1]/div[2]/div[1]/div[6]/a[1]'
            ),
            'addressDescription': ('Type', '#address_description', 'Business'),
            'addressType': (
                'Select',
                '#address_correspondence_method_type_id',
                'Work'
            ),
            'address': ('Type', '#address_1', '123 N Main St'),
            'city': ('Type', '#city', 'Lindon'),
            'state': ('Select', '#state', 'Utah'),
            'zipCode': ('Type', '#zip_code', '84042'),
            'save': ('Click', '#save-n-check'),
        }
        expected = 'Saved information'
        self.process.update(runtime)
        order = ('editEntity', 'addressDescription', 'addressType',
                 'address', 'city', 'state', 'zipCode', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, 'toast-container', 5)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'phone' or debug is 'all',
                         "testing {}".format(debug,))
    def test_edit_phone(self):
        print(">>> Inside function test_edit_phone()")

        runtime = {
            'phone': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[2]/div[4]/div[1]/a[4]/i',
            ),
            'editPhone': (
                'Click',
                '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[15]/a/i'
            ),
            'revisePhone': ('Type', '#phone', '8012251155'),
            'phoneType': (
                'Select', '#phone_correspondence_method_type_id', 'Other'),
            'save': ('Click', '//*[@button="save"]')
        }
        expected = 'Phone number saved!'
        self.process.update(runtime)
        order = ('phone', 'editPhone', 'revisePhone', 'phoneType', 'save')
        self.process.execute(order)
        result = self.process.results(expected, 'toast-container', 5)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'workspace' or debug is 'all',
                         "testing {}".format(debug,))
    def test_workspace(self):
        print(">>> Inside function test_workspace()")

        expected = self.process.get(
            '//*[@id="ribbon_form"]/ul/li/div[1]/div/div[1]/div', 'innerHTML')
        expected = expected.split(' ')[29]
        # print(">>>>>>>>>>>>>> ENTITY: {}".format(expected,))

        runtime = {
            'addWorkspace': ('Click', '#save-to-find'),
            'workspace': ('Click', '//*[@id="previous-results"]/i'),
        }
        self.process.update(runtime)
        order = ('addWorkspace', 'workspace',)
        self.process.execute(order)

        actual = self.process.get(
            '//*[@id="ribbon_form"]/ul/li/div[1]/div/div[1]/div', 'title')
        actual = actual.split(' ')[1]
        # print(">>>>>>>>>>>>>> TITLE: {}".format(actual))
        result = self.process.compare(expected, actual)
        self.assertTrue(result, )

        # Clear out the Workspace
        runtime = {
            'id': expected,
            'clear': (
                'Click', '//*[@id="extended-results-body-&id;"]/div[2]/a[1]')
        }
        self.process.update(runtime)
        order = ('clear', )
        self.process.execute(order)
