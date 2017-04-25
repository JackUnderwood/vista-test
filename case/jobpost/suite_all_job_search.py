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
    debug = 'job_type'

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
