import unittest

import ui
from ui import UI

__author__ = 'John Underwood'


class BvtBasic(unittest.TestCase):
    ui.log.debug(">> Inside BvtBasic class")

    process = UI()
    debug = 'suggestion'

    def setUp(self):
        pass

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
        self.process.results('Use Find... to load your workspace.')

    @unittest.skipUnless(
        debug is 'advance' or debug is 'all', "testing {}".format(debug,))
    def test_advance_find(self):
        ui.log.debug('>>> Inside function test_advance_find()')

        from ui.low.advance_find import AdvanceFind
        AdvanceFind()
        self.process.results('Advanced Find')

    @unittest.skipUnless(debug is 'find' or debug is 'all', "testing {}".format(debug,))
    def test_find(self):
        ui.log.debug('>>> Inside function test_find()')
        runtime = {
            'find': ('Type', '#main_desc', 'Matt Lambert st:wv'),
            'select': ('Click', '//*[@item_id="91273"]'),}
        self.process.update(runtime)
        self.process.execute(('find', 'select', ))
        self.process.results(
            ' Matt Lambert', 'extended-results-body-91273')

    @unittest.skipUnless(
        debug is 'modifiers' or debug is 'all', "testing {}".format(debug,))
    def test_modifiers(self):
        ui.log.debug('>>> Inside function test_modifiers()')
        self.process.update({'modifiers': ('Click', '#modifierList'), })
        self.process.execute(('modifiers', ))
        self.process.results( 'Available Modifiers:', 'modifiers')

    @unittest.skipUnless(
        debug is 'suggestion' or debug is 'all', "testing {}".format(debug,))
    def test_suggestion_box(self):
        ui.log.debug('>>> Inside function test_suggestion_box()')
        self.process.update(
            {'sbox': ('Click', 'css=body>header>nav>div>ul.right>li:nth-child(2)>a>i'),
             'cancel': (
                'Click',
                'css=#suggestionBox_form>'
                'div.right-align.button-container>a:nth-child(2)')})
        self.process.execute(('sbox', ))
        self.process.results('Suggestion Box')
        self.process.execute(('cancel', ))  # local clean up

    @unittest.skipUnless(debug is 'create_notice' or debug is 'all',
                         "testing {}".format(debug,))
    def test_create_notification(self):
        ui.log.debug('>>> Inside function test_create_notification()')

    @unittest.skipUnless(debug is 'directory' or debug is 'all',
                         "testing {}".format(debug,))
    def test_employee_directory(self):
        ui.log.debug('>>> Inside function test_employee_directory()')

    @unittest.skipUnless(debug is 'notify' or debug is 'all',
                         "testing {}".format(debug,))
    def test_notify(self):
        ui.log.debug('>>> Inside function test_notify()')

    @unittest.skipUnless(debug is 'home' or debug is 'all',
                         "testing {}".format(debug,))
    def test_home(self):
        ui.log.debug('>>> Inside function test_home()')

    @unittest.skipUnless(debug is 'wiki' or debug is 'all',
                         "testing {}".format(debug,))
    def test_wiki(self):
        ui.log.debug('>>> Inside function test_wiki()')

    @unittest.skipUnless(debug is 'comments' or debug is 'all',
                         "testing {}".format(debug,))
    def test_comments(self):
        ui.log.debug('>>> Inside function test_comments()')

    @unittest.skipUnless(debug is 'license' or debug is 'all',
                         "testing {}".format(debug,))
    def test_license(self):
        ui.log.debug('>>> Inside function test_license()')

    @unittest.skipUnless(debug is 'reports' or debug is 'all',
                         "testing {}".format(debug,))
    def test_license_reports(self):
        ui.log.debug('>>> Inside function test_license_reports()')

    @unittest.skipUnless(debug is 'expire' or debug is 'all',
                         "testing {}".format(debug,))
    def test_license_expire(self):
        ui.log.debug('>>> Inside function test_license_expire()')

    @unittest.skipUnless(debug is 'requirements' or debug is 'all',
                         "testing {}".format(debug,))
    def test_license_requirements(self):
        ui.log.debug('>>> Inside function test_license_requirements()')

    @unittest.skipUnless(debug is 'sales_report' or debug is 'all',
                         "testing {}".format(debug,))
    def test_sales_commission_report(self):
        ui.log.debug('>>> Inside function test_sales_commission_report()')

    @unittest.skipUnless(debug is 'goals' or debug is 'all',
                         "testing {}".format(debug,))
    def test_sales_corporate_goals(self):
        ui.log.debug('>>> Inside function test_sales_corporate_goals()')

    @unittest.skipUnless(debug is 'rates' or debug is 'all',
                         "testing {}".format(debug,))
    def test_sales_commission_rates(self):
        ui.log.debug('>>> Inside function test_sales_commission_rates()')

    @unittest.skipUnless(debug is 'base' or debug is 'all',
                         "testing {}".format(debug,))
    def test_sales_base(self):
        ui.log.debug('>>> Inside function test_sales_base()')

    @unittest.skipUnless(debug is 'file' or debug is 'all',
                         "testing {}".format(debug,))
    def test_file(self):
        ui.log.debug('>>> Inside function test_file()')

    @unittest.skipUnless(debug is 'watch' or debug is 'all',
                         "testing {}".format(debug,))
    def test_watch(self):
        ui.log.debug('>>> Inside function test_watch()')

    @unittest.skipUnless(debug is 'manage' or debug is 'all',
                         "testing {}".format(debug,))
    def test_watch_manage(self):
        ui.log.debug('>>> Inside function test_watch_manage()')

    @unittest.skipUnless(debug is 'user' or debug is 'all',
                         "testing {}".format(debug,))
    def test_user_config(self):
        ui.log.debug('>>> Inside function test_user_config()')

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
