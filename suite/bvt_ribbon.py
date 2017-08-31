import unittest

import ui
from ui import UI
from ui.low.find import Find

__author__ = 'John Underwood'


class BvtRibbon(unittest.TestCase):
    """
    This test group clicks on most of the buttons inside the ribbon, and checks
    that each drawer displays as expected. Use this suite as part of a
    Build Verification Test - BVT

    Tests all buttons with the exception of "View Jobs Map" and "Manage Files",
    since these create new tab pages and not drawers.
    """
    ui.log.info(">>> Inside BvtRibbon class")
    debug = 'all'  # use 'all'; or test individual case methods below
    process = UI()
    runtime = {}  # used indirectly inside tearDown()
    close = ()  # used inside tearDown()

    entity = 'Peter Bertolozzi'  # 'matt lambert st:wv'
    entity_id = '567754'  # '91273'

    def setUp(self):
        self.runtime = {}
        self.close = ()

    def tearDown(self):
        # Each test case MUST have a 'close' key in the runtime, which
        # should select a drawer's Close or Cancel button's element.
        self.process.wait(1)
        self.close = ('close', )
        self.process.execute(self.close)

    @classmethod
    def setUpClass(cls):
        override = {'entity': cls.entity, 'entityId': cls.entity_id, }
        Find(override)
        cls.process.wait(3)  # wait for workspace ribbon to display

    @classmethod
    def tearDownClass(cls):
        cls.process.wait(2)
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*

    @unittest.skipUnless(debug is 'correspond' or debug is 'all',
                         "testing {}".format(debug,))
    def test_correspond(self):
        ui.log.debug(">>> Inside function test_correspond()")

        self.runtime = {
            'correspond': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]'),
            'close': ('Click', '//*[@id="correspondenceChooser_form"]/div/a')
        }                      #
        expected = 'Select a Template'
        self.process.update(self.runtime)
        order = ('correspond', )
        self.process.execute(order)
        result = self.process.results(
            expected,
            locator='//*[@id="correspondenceChooser_form"]/div/a', )
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'emailer' or debug is 'all',
                         "testing {}".format(debug,))
    def test_emailer(self):
        ui.log.debug(">>> Inside function test_emailer()")

        runtime = {
            'emailer': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[2]/i'),
            'close': ('Click', '//*[@id="emailer_form"]/div[5]/a[2]'),
        }
        expected = ') Emailer'
        self.process.update(runtime)
        order = ('emailer', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'emails' or debug is 'all',
                         "testing {}".format(debug,))
    def test_emails(self):
        ui.log.debug(">>> Inside function test_emails()")

        self.runtime = {
            'emails': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[3]/i'
            ),
            'close': ('Click', '//*[@id="emailGrid_form"]/div[2]/a'),
        }
        expected = ') Emails'
        self.process.update(self.runtime)
        order = ('emails', )
        self.process.execute(order)
        self.process.wait(3)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'phone' or debug is 'all',
                         "testing {}".format(debug,))
    def test_phone(self):
        ui.log.debug(">>> Inside function test_phone()")

        self.runtime = {
            'phone': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]/i'
            ),
            'close': ('Click', '//*[@id="phoneGrid_form"]/div[2]/a'),
        }
        expected = ') Phone Numbers'
        self.process.update(self.runtime)
        order = ('phone', )
        self.process.execute(order)
        UI().wait(1)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'addresses' or debug is 'all',
                         "testing {}".format(debug,))
    def test_addresses(self):
        ui.log.debug(">>> Inside function test_addresses()")

        self.runtime = {
            'addresses': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[5]/i'
            ),
            'close': ('Click', '//*[@id="addressGrid_form"]/div[2]/a'),
        }
        expected = ') Addresses'
        self.process.update(self.runtime)
        order = ('addresses', )
        self.process.execute(order)
        self.process.wait()  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'comments' or debug is 'all',
                         "testing {}".format(debug,))
    def test_comments(self):
        ui.log.debug(">>> Inside function test_comments()")

        self.runtime = {
            'comments': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[6]/i'
            ),
            'close': ('Click', '//*[@id="commentsGrid_form"]/div[2]/a'),
        }
        expected = 'Comments'
        self.process.update(self.runtime)
        order = ('comments', )
        self.process.execute(order)
        UI().wait(1)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'contacts' or debug is 'all',
                         "testing {}".format(debug,))
    def test_contacts(self):
        ui.log.debug(">>> Inside function test_contacts()")

        self.runtime = {
            'contacts': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[7]/i'
            ),
            'close': ('Click', '//*[@id="contacts_form"]/div[3]/a'),
        }
        expected = 'Contacts'
        self.process.update(self.runtime)
        order = ('contacts', )
        self.process.execute(order)
        UI().wait(1)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'passwords' or debug is 'all',
                         "testing {}".format(debug,))
    def test_passwords(self):
        ui.log.debug(">>> Inside function test_passwords()")

        self.runtime = {
            'passwords': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[9]/i'
            ),
            'close': ('Click', '//*[@id="urlPasswords_form"]/div[2]/a'),
        }
        expected = 'Passwords'
        self.process.update(self.runtime)
        order = ('passwords', )
        self.process.execute(order)
        UI().wait(1)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'licenses' or debug is 'all',
                         "testing {}".format(debug,))
    def test_licenses(self):
        ui.log.debug(">>> Inside function test_licenses()")

        self.runtime = {
            'licenses': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[1]/span'
            ),
            'close': ('Click', '//*[@id="licenseGrid_form"]/div[2]/a'),
        }
        expected = ') Licenses'
        self.process.update(self.runtime)
        order = ('licenses', )
        self.process.execute(order)
        UI().wait(1)  # wait for the drawer
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'malpractice' or debug is 'all',
                         "testing {}".format(debug,))
    def test_malpractice(self):
        ui.log.debug(">>> Inside function test_malpractice()")

        self.runtime = {
            'malpractice': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[2]/span'
            ),
            'close': ('Click',
                      '//*[@id="malpracticeGrid_form_drawer"]/div[4]/a'),
        }
        expected = ') Malpractice Claims &amp; Carriers'
        self.process.update(self.runtime)
        order = ('malpractice', )
        self.process.execute(order)
        UI().wait(1)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'experience' or debug is 'all',
                         "testing {}".format(debug,))
    def test_experience(self):
        ui.log.debug(">>> Inside function test_experience()")

        self.runtime = {
            'experience': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[3]/span'
            ),
            'close': ('Click', '//*[@id="experienceGrid_form_drawer"]/div[3]/a'),
        }
        expected = ') Experience'
        self.process.update(self.runtime)
        order = ('experience', )
        self.process.execute(order)
        self.process.wait()
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'examinations' or debug is 'all',
                         "testing {}".format(debug,))
    def test_examinations(self):
        ui.log.debug(">>> Inside function test_examinations()")

        self.runtime = {
            'exams': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[4]/span'
            ),
            'close': ('Click',
                      '//*[@id="examinationGrid_form_drawer"]/div[3]/a'),
        }
        expected = ') Examinations'
        self.process.update(self.runtime)
        order = ('exams', )
        self.process.execute(order)
        self.process.wait()
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'education' or debug is 'all',
                         "testing {}".format(debug,))
    def test_education(self):
        ui.log.debug(">>> Inside function test_education()")

        self.runtime = {
            'education': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[2]/a[5]/span'
            ),
            'close': ('Click', '//*[@id="educationGrid_form_drawer"]/div[3]/a'),
        }
        expected = ') Education'
        self.process.update(self.runtime)
        order = ('education', )
        self.process.execute(order)
        self.process.wait()
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'entity' or debug is 'all',
                         "testing {}".format(debug,))
    def test_edit_entity(self):
        ui.log.debug(">>> Inside function test_edit_entity()")

        self.runtime = {
            'editEntity': (
                'Click', '//*[@id="ribbon_form"]/ul/li/div[3]/div[1]/div[6]/a[1]'
            ),
            'close': ('Click',
                      '//*[@id="editEntityInformation_form"]/div[3]/a[3]'),
        }
        expected = ') Manage Entity'
        self.process.update(self.runtime)
        order = ('editEntity', )
        self.process.execute(order)
        self.process.wait(2)  # drawer is slow to display
        result = self.process.results(
            expected,
            locator='//*[@id="editEntityInformation_form"]/div[3]/a[3]', )
        self.assertTrue(result, msg=expected)

