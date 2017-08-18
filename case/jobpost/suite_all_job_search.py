import unittest

import ui
from ui import UI
from ui.low.job_posts import JobPosts
from ui.high.job_active_hot import JobActiveHot

__author__ = 'John Underwood'

MSG_SUCCESS = 'target has results for '
MSG_FAILED = 'target is empty for '


class AllJobSearch(unittest.TestCase):
    """
    Test inside the Manage Job Posts page each of its search filter individually.
    """
    ui.log.info(">> Inside AllJobSearch class")
    process = UI()
    debug = 'all'
    test = None

    def setUp(self):
        """
        Feedback message returns name of related test case
        unittest.TestCase.id(self) returns a string, i.e.
        'case.jobpost.suite_all_job_search.AllJobSearch.test_ard_group'
        :return: void
        """
        self.process.wait()
        self.test = unittest.TestCase.id(self).split('.')[-1:][0]

    def tearDown(self):
        self.process.update({
            'reset': (
                'Click', '//*[@id="job-search-wrap"]/div[3]/div[3]/button'),
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
        ui.log.info('>>> Inside function test_division()')
        self.process.update({
            'division': ('Click', 'css=.ui-multiselect.ui-widget.'
                                  'ui-state-default.ui-corner-all.'
                                  'multi_s.multi_s_division'),
            'domesticLT': ('Click', '#ui-multiselect-s_division-option-3'),
            'hcp': ('Click', '#ui-multiselect-s_division-option-4'),
        })
        expected = 'Division'
        self.process.execute(('division', 'domesticLT', 'hcp', 'division', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'ard' or debug is 'all', "testing {}".format(debug,))
    def test_ard_group(self):
        ui.log.info('>>> Inside function test_ard_group()')
        self.process.update({
            'ard': ('Click', 'css=.ui-multiselect.ui-widget.ui-state-default.'
                             'ui-corner-all.multi_s.multi_s_ard_group'),
            'emergency': ('Click', '#ui-multiselect-s_ard_group-option-3'),
            'hospitalist': ('Click', '#ui-multiselect-s_ard_group-option-5'),
        })
        expected = 'Ard Group'
        self.process.execute(('ard', 'emergency', 'hospitalist', 'ard'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'job_status' or debug is 'all', "testing {}".format(debug,))
    def test_job_status(self):
        ui.log.info('>>> Inside function test_job_status()')
        JobActiveHot()
        expected = 'Job Status'
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

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
        expected = 'Job Type'
        self.process.execute(('jobType', 'general', 'locums',
                              'tempToPerm', 'whitaker', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

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
        expected = 'Job Board Status'
        self.process.execute(('boardStatus', 'ready', 'rejected', 'boardStatus'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'specialty' or debug is 'all', "testing {}".format(debug,))
    def test_specialty(self):
        ui.log.info('>>> Inside function test_specialty()')
        self.process.update({
            'specialty': ('Click',
                            'css=.ui-multiselect.ui-widget.ui-state-default.'
                            'ui-corner-all.multi_s.multi_s_specialty'),
            'ambulance': ('Click', '#ui-multiselect-s_specialty-option-4'),
            'cardiology': ('Click', '#ui-multiselect-s_specialty-option-8'),
            'oncology': ('Click', '#ui-multiselect-s_specialty-option-95'),
            'pathology': ('Click', '#ui-multiselect-s_specialty-option-102'),
            'trauma': ('Click', '#ui-multiselect-s_specialty-option-156'),
        })
        expected = 'Specialty'
        self.process.execute(('specialty', 'ambulance', 'cardiology',
                              'oncology', 'pathology', 'trauma', 'specialty',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

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
        expected = 'Territory Manager'
        self.process.execute(('tm', 'first', 'second', 'third', 'tm',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

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
        expected = 'State'
        self.process.execute(('state', 'ca', 'fl', 'ny', 'state'))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

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
        expected = 'Scheduler'
        self.process.execute(('scheduler', 'first', 'second', 'third',
                              'scheduler', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'city' or debug is 'all', "testing {}".format(debug,))
    def test_city(self):
        ui.log.info('>>> Inside function test_city()')
        self.process.update({
            'city': ('TypeAndTab', '#s_city', 'manhattan'),
        })
        expected = 'City'
        self.process.execute(('city', ))
        self.process.wait(3)
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'number' or debug is 'all', "testing {}".format(debug,))
    def test_job_number(self):
        ui.log.info('>>> Inside function test_job_number()')
        self.process.update({
            'number': ('TypeAndTab', '#s_job_number', '92000-5000')
        })
        expected = 'Job Number(s)'
        self.process.execute(('number',))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'created' or debug is 'all', "testing {}".format(debug,))
    def test_created_date(self):
        ui.log.info('>>> Inside function test_created_date()')
        self.process.update({
            'created': ('Click', '#drp_autogen0'),
            'previousMonth': ('Click', '//*[@id="ui-id-7"]/a'),
        })
        expected = 'Created Date'
        self.process.execute(('created', 'previousMonth', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'modified' or debug is 'all', "testing {}".format(debug,))
    def test_last_modified_date(self):
        ui.log.info('>>> Inside function test_last_modified_date()')
        self.process.update({
            'modified': ('Click', '#drp_autogen1'),
            'last30Days': ('Click', '//*[@id="ui-id-14"]/a'),
        })
        expected = 'Last Modified Date'
        self.process.execute(('modified', 'last30Days', ))
        self.process.wait()
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(
        debug is 'keywords' or debug is 'all', "testing {}".format(debug,))
    def test_keywords(self):
        ui.log.info('>>> Inside function test_keywords()')
        self.process.update({
            'keyword': ('TypeAndTab', '#s_keywords', 'Daily'),
        })
        expected = 'Keywords'
        self.process.execute(('keyword', ))
        self.process.wait_for_element(
            '//*[@id="result-target"]/tbody/tr[1]', wait_time=45)
        html = self.process.spy('//*[@id="result-target"]/tbody', 'innerHTML')
        compare_message = (MSG_SUCCESS if html != '' else MSG_FAILED) + self.test
        result = self.process.compare(html != '', True, message=compare_message)
        self.assertTrue(result, msg=expected)
