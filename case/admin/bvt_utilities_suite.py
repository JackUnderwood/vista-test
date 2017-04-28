import unittest

import ui
from ui import UI

__author__ = 'John Underwood'


class BvtUtilities(unittest.TestCase):
    ui.log.info(">> Inside BvtUtilities class")

    process = UI()
    debug = 'all'

    def setUp(self):
        self.process.get("utilities")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.process.wait(3)
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*

    @unittest.skipUnless(
        debug is 'acls' or debug is 'all', "testing {}".format(debug,))
    def test_acls(self):
        ui.log.info('>>> Inside function test_acls()')

        self.process.update({
            'acls': ('Click', '//*[@id="content"]/div[1]/div/a[1]')
        })
        self.process.execute(('acls',))
        expected = 'Edit ACLs'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'policies' or debug is 'all', "testing {}".format(debug,))
    def test_policies(self):
        ui.log.info('>>> Inside function test_policies()')

        self.process.update({
            'policies': ('Click', '//*[@id="content"]/div[1]/div/a[2]')
        })
        self.process.execute(('policies',))
        expected = 'Edit Policies'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'roles' or debug is 'all', "testing {}".format(debug, ))
    def test_roles(self):
        ui.log.info('>>> Inside function test_roles()')

        self.process.update({
            'roles': ('Click', '//*[@id="content"]/div[1]/div/a[3]')
        })
        self.process.execute(('roles',))
        expected = 'Edit ACL Assignments by Role'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'home' or debug is 'all', "testing {}".format(debug, ))
    def test_home_page(self):
        ui.log.info('>>> Inside function test_home_page()')

        self.process.update({
            'home': ('Click', '//*[@id="content"]/div[2]/div/a[1]')
        })
        self.process.execute(('home',))
        expected = 'Homepage Editor'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'lookup' or debug is 'all', "testing {}".format(debug, ))
    def test_lookup_tables(self):
        ui.log.info('>>> Inside function test_lookup_tables()')

        self.process.update({
            'lookup': ('Click', '//*[@id="content"]/div[2]/div/a[2]')
        })
        self.process.execute(('lookup',))
        expected = 'Table'
        # expected = self.process.spy('#tableSelect', 'innerHTML')
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'ful' or debug is 'all', "testing {}".format(debug, ))
    def test_transfer_ful(self):
        ui.log.info('>>> Inside function test_transfer_ful()')

        self.process.update({
            'ful': ('Click', '#tful')
        })
        self.process.execute(('ful',))
        expected = 'Transfer Follow Up Logs'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

