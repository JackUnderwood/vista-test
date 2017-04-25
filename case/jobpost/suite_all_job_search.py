import unittest

import ui
from ui import UI
from ui.low.job_posts import JobPosts

__author__ = 'John Underwood'

MSG_SUCCESS = 'the result-target has results'
MSG_FAILED  = 'the result-target is empty'


class AllJobSearch(unittest.TestCase):
    """
    Test inside the Manage Job Posts page each of its search filter individually.
    """
    ui.log.info(">> Inside AllJobSearch class")
    process = UI()
    debug = 'all'

    def setUp(self):
        self.process.wait()

    def tearDown(self):
        self.process.update({
            'reset': (
                'Click', '//*[@id="job-search-wrap"]/div[2]/div[3]/button'),
            'away': ('Click', '//*[@id="content"]/h1'),  # click away
        })
        self.process.execute(('away', 'reset', ))

    @classmethod
    def setUpClass(cls):
        JobPosts()

    @classmethod
    def tearDownClass(cls):
        cls.process.wait(3)
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*

    @unittest.skipUnless(
        debug is 'division' or debug is 'all', "testing {}".format(debug,))
    def test_division(self):
        ui.log.info('>>> Inside function test_ard_group()')
        self.process.update({
            'division': ('Click', 'css=.ui-multiselect.ui-widget.'
                                  'ui-state-default.ui-corner-all.'
                                  'multi_s.multi_s_division'),
            'domesticLT': ('Click', '#ui-multiselect-s_division-option-3'),
            'hcp': ('Click', '#ui-multiselect-s_division-option-4'),
        })
        self.process.execute(('division', 'domesticLT', 'hcp', 'division', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'ard' or debug is 'all', "testing {}".format(debug,))
    def test_ard_group(self):
        ui.log.info('>>> Inside function test_division()')
        self.process.update({
            'ard': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                             'ui-corner-all.multi_s.multi_s_ard_group'),
            'emergency': ('Click', '#ui-multiselect-s_ard_group-option-3'),
            'hospitalist': ('Click', '#ui-multiselect-s_ard_group-option-5'),
        })
        self.process.execute(('ard', 'emergency', 'hospitalist', 'ard'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'job_status' or debug is 'all', "testing {}".format(debug,))
    def test_job_status(self):
        ui.log.info('>>> Inside function test_job_status()')
        self.process.update({
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'active': ('Click', '#ui-multiselect-s_job_status-option-1'),
            'hot': ('Click', '#ui-multiselect-s_job_status-option-4')
        })
        self.process.execute(('jobStatus', 'active', 'hot',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'job_type' or debug is 'all', "testing {}".format(debug,))
    def test_job_type(self):
        ui.log.info('>>> Inside function test_job_type()')
        self.process.update({
            'jobType': ('Click',
                        'css=.ui-multiselect.ui-widget.ui-state-default.'
                        'ui-corner-all.multi_s.multi_s_job_type'),
            'general': ('Click', '#ui-multiselect-s_job_type-option-5'),
            'locums': ('Click', '#ui-multiselect-s_job_type-option-8'),
            'tempToPerm': ('Click', '#ui-multiselect-s_job_type-option-16'),
            'whitaker': ('Click', '#ui-multiselect-s_job_type-option-17'),
        })
        self.process.execute(('jobType', 'general', 'locums',
                              'tempToPerm', 'whitaker', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'board_status' or debug is 'all', "testing {}".format(debug,))
    def test_job_board_status(self):
        ui.log.info('>>> Inside function test_job_board_status()')
        self.process.update({
            'boardStatus': ('Click',
                            'css=.ui-multiselect.ui-widget.ui-state-default.'
                            'ui-corner-all.multi_s.multi_s_job_board_status'),
            'ready': ('Click', '#ui-multiselect-s_job_board_status-option-2'),
            'rejected': ('Click', '#ui-multiselect-s_job_board_status-option-5'),
        })
        self.process.execute(('boardStatus', 'ready', 'rejected', 'boardStatus'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'specialty' or debug is 'all', "testing {}".format(debug,))
    def test_specialty(self):
        ui.log.info('>>> Inside function test_specialty()')
        self.process.update({
            'boardStatus': ('Click',
                            'css=.ui-multiselect.ui-widget.ui-state-default.'
                            'ui-corner-all.multi_s.multi_s_specialty'),
            'ambulance': ('Click', '#ui-multiselect-s_specialty-option-4'),
            'cardiology': ('Click', '#ui-multiselect-s_specialty-option-8'),
            'oncology': ('Click', '#ui-multiselect-s_specialty-option-95'),
            'pathology': ('Click', '#ui-multiselect-s_specialty-option-102'),
            'trauma': ('Click', '#ui-multiselect-s_specialty-option-156'),
        })
        self.process.execute(('boardStatus', 'ambulance', 'cardiology',
                              'oncology', 'pathology', 'trauma', 'boardStatus',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'tm' or debug is 'all', "testing {}".format(debug,))
    def test_territory_manager(self):
        ui.log.info('>>> Inside function test_territory_manager()')
        self.process.update({
            'tm': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                            'ui-corner-all.multi_s.multi_s_tm'),
            'first': ('Click', '#ui-multiselect-s_territory_manager-option-3'),
            'second': ('Click', '#ui-multiselect-s_territory_manager-option-18'),
            'third': ('Click', '#ui-multiselect-s_territory_manager-option-21'),
        })
        self.process.execute(('tm', 'first', 'second', 'third', 'tm',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'state' or debug is 'all', "testing {}".format(debug,))
    def test_state(self):
        ui.log.info('>>> Inside function test_state()')
        self.process.update({
            'state': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                               'ui-corner-all.multi_s.multi_s_state'),
            'ca': ('Click', '#ui-multiselect-s_state-option-9'),
            'fl': ('Click', '#ui-multiselect-s_state-option-14'),
            'ny': ('Click', '#ui-multiselect-s_state-option-42'),
        })
        self.process.execute(('state', 'ca', 'fl', 'ny', 'state'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)

    @unittest.skipUnless(
        debug is 'scheduler' or debug is 'all', "testing {}".format(debug,))
    def test_scheduler(self):
        ui.log.info('>>> Inside function test_scheduler()')
        self.process.update({
            'scheduler': (
                'Click',
                'css=.ui-multiselect.ui-widget.ui-state-default.ui-corner-all.'
                'multi_s.multi_s_user'),
            'first': ('Click', '#ui-multiselect-s_user-option-1'),
            'second': ('Click', '#ui-multiselect-s_user-option-8'),
            'third': ('Click', '#ui-multiselect-s_user-option-16'),
        })
        self.process.execute(('scheduler', 'first', 'second', 'third',
                              'scheduler', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED)
        self.process.compare(html != '', True, message=compare_message)
