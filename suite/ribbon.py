import unittest

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from tool.generators.generator import gen_name, gen_email

__author__ = 'John Underwood'


class TestSuiteRibbon(unittest.TestCase):
    """
    This test group click on all the buttons inside the ribbon, and checks
    that each drawer displays as expected. Use this suite as part of a
    Build Verification Test - BVT
    """
    ui.log.info(">>> Inside TestSuiteFileGeneral class")
    debug = 'all'  # use 'all'; or test individual case methods below
    process = UI()
    override = {'rowNum': '7'}
    cl = None

    def setUp(self):
        License()
        self.cl = Checklist(self.override)
        ui.log.info("Entity is '{}'".format(self.cl.entity))

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
        ui.log.debug(">>> Inside function test_edit_entity()")
        email = gen_email(gen_name())  # use any name

        runtime = {
            'editEntity': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[1]/div[6]/a[1]'
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
            'email': ('Type', '#email_address', email),
            'emailType': (
                'Select', '#email_correspondence_method_type_id', 'Work'),
            'save': ('Click', '#save-n-check'),
        }
        expected = 'Saved information'
        self.process.update(runtime)
        order = ('editEntity', 'addressDescription', 'addressType',
                 'address', 'city', 'state', 'zipCode', 'email',
                 'emailType', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, 'toast-container', 10)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'phone' or debug is 'all',
                         "testing {}".format(debug,))
    def test_edit_phone(self):
        ui.log.debug(">>> Inside function test_edit_phone()")

        runtime = {
            'phone': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]/i',
            ),
            'editPhone': (
                'Click',
                '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[15]/a/i'
            ),
            'revisePhone': ('Type', '#phone', '8012251155'),
            'phoneType': (
                'Select', '#phone_correspondence_method_type_id', 'Other'),
            'save': ('Click', 'css=#editPhone_form>div.right-align.'
                              'button-container>a:nth-child(1)')
        }
        expected = 'Phone number saved!'
        self.process.update(runtime)
        order = ('phone', 'editPhone', 'revisePhone', 'phoneType', 'save')
        self.process.execute(order)
        result = self.process.results(expected, 'toast-container', 5)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'workspace' or debug is 'none',
                         "testing {}".format(debug,))  # TODO: broken get()
    def test_workspace(self):
        ui.log.debug(">>> Inside function test_workspace()")

        expected = self.process.get(  # broken -> can't find element
            'css=#ribbon_form>ul>li>div.collapsible-header.active>div>div.col.'
            's5.truncate>div', 'title')
        # css=#ribbon_form>ul>li>div.collapsible-header.active>div>div.col.s5.truncate>div
        # expected = expected.split(' ')[29]
        expected = expected.strip()
        print(">>>>>>>>>>>>>> ENTITY: {}".format(expected,))

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

    @unittest.skipUnless(debug is 'correspond' or debug is 'all',
                         "testing {}".format(debug,))
    def test_correspond(self):
        ui.log.debug(">>> Inside function test_correspond()")

        runtime = {
            'correspond': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]'),
        }
        expected = 'Select a Template'
        self.process.update(runtime)
        order = ('correspond', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'emailer' or debug is 'all',
                         "testing {}".format(debug,))
    def test_emailer(self):
        ui.log.debug(">>> Inside function test_emailer()")

        runtime = {
            'emailer': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[2]'),
        }
        expected = '({0}) Emailer'.format(self.cl.entity, )
        self.process.update(runtime)
        order = ('emailer', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'emails' or debug is 'all',
                         "testing {}".format(debug,))
    def test_emails(self):
        ui.log.debug(">>> Inside function test_emails()")

        runtime = {
            'emails': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[3]'),
        }
        expected = '({}) Emails'.format(self.cl.entity, )
        self.process.update(runtime)
        order = ('emails', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'phones' or debug is 'all',
                         "testing {}".format(debug,))
    def test_phones(self):
        ui.log.debug(">>> Inside function test_phones()")

        runtime = {
            'phones': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]'),
        }
        expected = '({}) Phone Numbers'.format(self.cl.entity, )
        self.process.update(runtime)
        order = ('phones', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'addresses' or debug is 'all',
                         "testing {}".format(debug,))
    def test_addresses(self):
        ui.log.debug(">>> Inside function test_addresses()")

        runtime = {
            'addresses': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[5]'),
        }
        expected = '({}) Addresses'.format(self.cl.entity, )
        self.process.update(runtime)
        order = ('addresses', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'comments' or debug is 'all',
                         "testing {}".format(debug,))
    def test_comments(self):
        ui.log.debug(">>> Inside function test_comments()")

        runtime = {
            'comments': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[6]'),
        }
        expected = '({}) Comments'.format(self.cl.entity, )
        self.process.update(runtime)
        order = ('comments', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'contacts' or debug is 'all',
                         "testing {}".format(debug,))
    def test_contacts(self):
        ui.log.debug(">>> Inside function test_contacts()")

        runtime = {
            'contacts': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[7]'),
        }
        expected = 'Contacts'
        self.process.update(runtime)
        order = ('contacts', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'passwords' or debug is 'all',
                         "testing {}".format(debug,))
    def test_passwords(self):
        ui.log.debug(">>> Inside function test_passwords()")

        runtime = {
            'passwords': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[9]'),
        }
        expected = 'Passwords'
        self.process.update(runtime)
        order = ('passwords', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
