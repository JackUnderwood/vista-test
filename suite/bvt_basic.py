import unittest

import ui
from ui import UI
from ui.low.home import Home

__author__ = 'John Underwood'


class BvtBasic(unittest.TestCase):
    ui.log.debug(">> Inside BvtBasic class")

    process = UI()
    debug = 'all'

    def setUp(self):
        Home()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().wait(3)
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(
        debug is 'workspace' or debug is 'all', "testing {}".format(debug,))
    def test_workspace(self):
        ui.log.debug('>>> Inside function test_workspace()')

        from ui.low.my_workspace import MyWorkspace
        MyWorkspace()
        expected = 'Use Find... to load your workspace.'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'advance' or debug is 'all', "testing {}".format(debug,))
    def test_advance_find(self):
        ui.log.debug('>>> Inside function test_advance_find()')

        from ui.low.advance_find import AdvanceFind
        AdvanceFind()
        expected = 'Advanced Find'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'find' or debug is 'all', "testing {}".format(debug,))
    def test_find(self):
        ui.log.debug('>>> Inside function test_find()')
        expected = 'Find'
        runtime = {
            'find': ('Type', '#main_desc', 'Matt Lambert st:wv'),
            'select': ('Click', '//*[@item_id="91273"]'),
            'purge': (
                'Click', '//*[@id="extended-results-body-91273"]/div[2]/a[1]')}
        self.process.update(runtime)
        self.process.execute(('find', 'select', ))
        result = self.process.results(
            ' Matt Lambert', 'extended-results-body-91273')
        self.process.execute(('purge', ))
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'modifiers' or debug is 'all', "testing {}".format(debug,))
    def test_modifiers(self):
        ui.log.debug('>>> Inside function test_modifiers()')
        expected = 'Available Modifiers'
        self.process.update({'modifiers': ('Click', '#modifierList'), })
        self.process.execute(('modifiers', ))
        result = self.process.results(expected, 'modifiers')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'suggestion' or debug is 'all', "testing {}".format(debug,))
    def test_suggestion_box(self):
        ui.log.debug('>>> Inside function test_suggestion_box()')
        expected = 'Suggestion Box'
        self.process.update(
            {'sbox': (
                'Click',
                'css=body>header>nav>div>ul.right>li:nth-child(2)>a>i'),
             'cancel': (
                'Click',
                'css=#suggestionBox_form>'
                'div.right-align.button-container>a:nth-child(2)')})
        self.process.execute(('sbox', ))
        result = self.process.results(expected)
        self.process.execute(('cancel', ))  # local clean up
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'create_notice' or debug is 'all', "testing {}".format(debug,))
    def test_create_notification(self):
        ui.log.debug('>>> Inside function test_create_notification()')
        expected = 'Create Notification'
        self.process.update(
            {'createNote': ('Click', '#remindMeButton'),
             'cancel': (
                 'Click',
                 'css=#widgetNotification_form>'
                 'div.right-align.button-container>a:nth-child(2)')})
        self.process.execute(('createNote', ))
        result = self.process.results(expected)
        self.process.execute(('cancel', ))
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'directory' or debug is 'all', "testing {}".format(debug,))
    def test_employee_directory(self):
        ui.log.debug('>>> Inside function test_employee_directory()')
        expected = 'Employee Directory'
        self.process.update(
            {'directory': ('Click', '#button_employee_directory'),
             'cancel': (
                 'Click',
                 'css=#userGrid_form>div.right-align.button-container>a')})
        self.process.execute(('directory', ))
        result = self.process.results(expected)
        self.process.wait(1)
        self.process.execute(('cancel', ))
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'notify' or debug is 'all', "testing {}".format(debug,))
    def test_notify(self):
        ui.log.debug('>>> Inside function test_notify()')
        from tool.utilities import get_configurations
        user = get_configurations('USER', 'name')
        expected = ' ({}) Notify'.format(user, )
        self.process.update(
            {'notify': ('Click', '#button_notification'),
             'close': ('Click', 'css=#notifyGrid_form>'
                                'div.right-align.button-container>a')})
        self.process.execute(('notify', ))
        result = self.process.results(expected)
        self.process.execute(('close', ))
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'home' or debug is 'all', "testing {}".format(debug,))
    def test_home(self):
        ui.log.debug('>>> Inside function test_home()')
        expected = "Let's take a look at how to navigate "
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'wiki' or debug is 'all', "testing {}".format(debug,))
    def test_wiki(self):
        ui.log.debug('>>> Inside function test_wiki()')
        from ui.low.wiki import Wiki
        Wiki()
        expected = 'Full View'
        actual = self.process.get('//*[@id="wiki_form"]/a', 'innerHTML')
        result = self.process.compare(expected, actual.strip())
        self.process.update(
            {'close': ('Click', '//*[@id="wikieditClose"]')})
        self.process.execute(('close', ))
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'license' or debug is 'all', "testing {}".format(debug,))
    def test_license(self):
        ui.log.debug('>>> Inside function test_license() landing page')
        from ui.low.license import License
        License()
        expected = 'License Request'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'reports' or debug is 'all', "testing {}".format(debug,))
    def test_license_reports(self):
        ui.log.debug('>>> Inside function test_license_reports()')
        from ui.low.license_report import LicenseReport
        LicenseReport()
        expected = 'License Report'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'expire' or debug is 'all', "testing {}".format(debug,))
    def test_license_expire(self):
        ui.log.debug('>>> Inside function test_license_expire()')
        from ui.low.license_expire import LicenseExpire
        LicenseExpire()
        expected = 'Expiring Licenses'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'requirements' or debug is 'all', "testing {}".format(debug,))
    def test_license_requirements(self):
        ui.log.debug('>>> Inside function test_license_requirements()')
        from ui.low.license_requirements import LicenseRequirements
        LicenseRequirements()
        expected = 'Manage State License Requirements'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'sales_report' or debug is 'all', "testing {}".format(debug,))
    def test_sales_commission_report(self):
        ui.log.debug('>>> Inside function test_sales_commission_report()')
        from ui.low.sales_commission_report import SalesCommissionReport
        SalesCommissionReport()
        expected = 'Commission Report'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'goals' or debug is 'all', "testing {}".format(debug,))
    def test_sales_corporate_goals(self):
        ui.log.debug('>>> Inside function test_sales_corporate_goals()')
        from ui.low.sales_corporate import SalesCorporate
        SalesCorporate()
        expected = 'Goals'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'rates' or debug is 'all', "testing {}".format(debug,))
    def test_sales_commission_rates(self):
        ui.log.debug('>>> Inside function test_sales_commission_rates()')
        from ui.low.sales_commission_rates import SalesCommissionRates
        SalesCommissionRates()
        expected = 'Commission Rates'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'base' or debug is 'all', "testing {}".format(debug,))
    def test_sales_base(self):
        ui.log.debug('>>> Inside function test_sales_base()')
        from ui.low.sales_base import SalesBase
        SalesBase()
        expected = 'Standard Sales Base'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'file' or debug is 'all', "testing {}".format(debug,))
    def test_file(self):
        ui.log.debug('>>> Inside function test_file()')
        from ui.low.file import File
        from tool.utilities import get_configurations
        File()
        user = get_configurations('USER', 'name')
        expected = "{}'s Files".format(user,)
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
    #
    # @unittest.skipUnless(
    #     debug is 'watch' or debug is 'all', "testing {}".format(debug,))
    # def test_watch(self):
    #     ui.log.debug('>>> Inside function test_watch()')
    #     from ui.low.watch import Watch
    #     Watch()
    #     expected = ''  # Unknown
    #     result = self.process.results(expected)
    #     self.assertTrue(result, msg=expected)
    #
    # @unittest.skipUnless(
    #     debug is 'manage' or debug is 'all', "testing {}".format(debug,))
    # def test_watch_manage(self):
    #     ui.log.debug('>>> Inside function test_watch_manage()')
    #     from ui.low.watch_manage import WatchManage
    #     WatchManage()
    #     expected = ''  # Unknown
    #     result = self.process.results(expected)
    #     self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'user' or debug is 'all', "testing {}".format(debug,))
    def test_user_config(self):
        ui.log.debug('>>> Inside function test_user_config()')
        from ui.low.user_config import UserConfig
        UserConfig()
        expected = 'User Information'
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'admin' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_home(self):
        ui.log.debug('>>> Inside function test_admin_home()')

    @unittest.skipUnless(debug is 'status' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_user_status(self):
        ui.log.debug('>>> Inside function test_admin_user_status()')

    @unittest.skipUnless(debug is 'actions' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_edit_actions(self):
        ui.log.debug('>>> Inside function test_admin_edit_actions()')

    @unittest.skipUnless(debug is 'policies' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_edit_policies(self):
        ui.log.debug('>>> Inside function test_admin_edit_policies()')

    @unittest.skipUnless(debug is 'acls' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_assign_acls(self):
        ui.log.debug('>>> Inside function test_admin_assign_acls()')

    @unittest.skipUnless(debug is 'dash' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_dash(self):
        ui.log.debug('>>> Inside function test_admin_dash()')

    @unittest.skipUnless(debug is 'send' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_send_notification(self):
        ui.log.debug('>>> Inside function test_admin_send_notification()')

    @unittest.skipUnless(debug is 'namelist' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_namelist(self):
        ui.log.debug('>>> Inside function test_admin_namelist()')

    @unittest.skipUnless(debug is 'template' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_template_creator(self):
        ui.log.debug('>>> Inside function test_admin_template_creator()')

    @unittest.skipUnless(debug is 'checklist' or debug is 'all',
                         "testing {}".format(debug,))
    def test_admin_checklist_creator(self):
        ui.log.debug('>>> Inside function test_admin_checklist_creator()')
