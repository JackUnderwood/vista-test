import unittest

import ui
from ui import UI
from ui.low.find import Find
from ui.high.checklist import Checklist
from tool.generators.generator import gen_name, gen_email

__author__ = 'John Underwood'


class BvtRibbon(unittest.TestCase):
    """
    This test group click on most of the buttons inside the ribbon, and checks
    that each drawer displays as expected. Use this suite as part of a
    Build Verification Test - BVT
    Tests all buttons with the exception of "View Jobs Map" and "Manage Files"
    """
    ui.log.info(">>> Inside BvtRibbon class")
    debug = 'all'  # use 'all'; or test individual case methods below
    process = UI()
    runtime = {}  # used inside tearDown()
    close = ()  # used inside tearDown()

    entity = 'Peter Bertolozzi'  # 'matt lambert st:wv'
    entity_id = '567754'  # '91273'

    def setUp(self):
        self.runtime = {}
        self.close = ()

    def tearDown(self):
        # Each test case MUST have a 'close' key in the runtime, which
        # should select a drawer's Close or Cancel button's element.
        self.close = ('close', )
        self.process.execute(self.close)

    @classmethod
    def setUpClass(cls):
        override = {'entity': cls.entity, 'entityId': cls.entity_id, }
        Find(override)
        UI().wait(3)  # wait for workspace ribbon to display

    @classmethod
    def tearDownClass(cls):
        UI().wait(2)
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*

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
        UI.wait(1)
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
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'correspond' or debug is 'all',
                         "testing {}".format(debug,))
    def test_correspond(self):
        ui.log.debug(">>> Inside function test_correspond()")

        self.runtime = {
            'correspond': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]'),
            'close': ('Click', '//*[@id="correspondenceChooser_form"]/div/a')
        }
        expected = 'Select a Template'
        self.process.update(self.runtime)
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
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[2]/i'),
            'close': ('Click', '//*[@id="emailer_form"]/div[5]/a[2]'),
        }
        expected = ') Emailer'
        self.process.update(runtime)
        order = ('emailer', )
        self.process.execute(order)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

