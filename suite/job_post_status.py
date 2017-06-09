import unittest

import ui
from ui import UI
from case.jobpost._helpers import find_rows

__author__ = 'John Underwood'


def check_valid(process, rows_list):
    result = True
    if len(rows_list) < 1:
        process.compare(True, False, message="no valid rows available")
        result = False
    return result


class TestSuiteJobPostStatus(unittest.TestCase):
    """
    Create a set of various starting statuses to ending statuses.
    For example: job is Ready to Post and Approved and you want to move it
    to Rejected.
    """
    ui.log.info(">> Inside TestSuiteJobPostStatus class")
    process = UI()
    debug = 'all'

    def setUp(self):
        self.process.get("jobs/search")
        self.process.wait()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.process.wait()
        cls.process.teardown()

    # *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'ready_approved_to_rejected' or debug is 'all',
                         "testing {}".format(debug,))
    def test_ready_approved_to_rejected(self):
        ui.log.info(">>> Inside function test_ready_approved_to_rejected()")
        runtime = {
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'wait1': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': ('Click', '#ui-multiselect-s_job_status-option-4'),
            'clickAway': ('Click', '//*[@id="content"]/h1'),
            'jobBoardStatus': ('Click', 'css=.ui-multiselect.ui-widget.'
                                        'ui-state-default.ui-corner-all.multi_s.'
                                        'multi_s_job_board_status'),
            'wait2': ('Wait', '#ui-multiselect-s_job_board_status-option-1',
                      {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobBoardStatusApprove': (
                'Click', '#ui-multiselect-s_job_board_status-option-1')
        }
        self.process.update(runtime)
        order = ('jobStatus', 'wait1', 'jobStatusActive', 'jobStatusHot',
                 'clickAway', 'jobBoardStatus', 'wait2', 'jobBoardStatusApprove')
        self.process.execute(order)
        
        approved_locator = './td/div/div[3]/div[2]/div[3]/div/div/div/div[2]/strong'
        rows = find_rows(self.process, 'expandable-row',
                         approved_locator, 'innerHTML')
        valid_approved_rows_id = [r[0] for r in rows if 'Approved' in r]
        if not check_valid(self.process, valid_approved_rows_id):
            self.assertTrue(False, msg='no valid "Approved" rows available')

        ready_to_post_locator = './td/div/div[3]/div[2]/div[4]/div/div/div[2]/strong'
        rows = find_rows(self.process, 'expandable-row',
                         ready_to_post_locator, 'innerHTML')
        valid_ready_to_post_rows_id = [r[0] for r in rows if 'Yes' in r]
        if not check_valid(self.process, valid_ready_to_post_rows_id):
            self.assertTrue(False, msg='no valid "Ready to Post" rows available')
        # Get the intersection of the two results.
        approved_and_ready_to_post = (set(valid_approved_rows_id) &
                                      set(valid_ready_to_post_rows_id))
        if not check_valid(self.process, approved_and_ready_to_post):
            self.assertTrue(False, msg='no valid rows available')
        ids = [r[r.find('_')+1:] for r in approved_and_ready_to_post]
        ids.sort(reverse=True)
        edit_button_id = "#edit_{}".format(ids[0], )
        self.process.update({
            'edit': ('Click', edit_button_id),
            'reject': (
                'Click',
                '//label[@for="job_board_rejection_history__is_rejected"]'),
            'reason': ('Select',
                       '#job_board_rejection_history__rejection_reason_id',
                       'Incomplete description/add detail'),
            'confirm': ('Click', '#confirm-reject'),
            'save': ('Click', '#edit-save'),
        })
        expected = 'Job Saved'
        self.process.execute(('edit', 'reject', 'reason', 'confirm', 'save', ))
        row_class = self.process.spy(
            '//*[@id="result-target"]/tbody/tr[1]', 'class')

        self.process.compare(True, 'rejected' in row_class,
                             message='class set to "rejected"')

        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'rejected_to_approved' or debug is 'all',
                         "testing {}".format(debug,))
    def test_rejected_to_approved(self):
        ui.log.info(">>> Inside function test_rejected_to_approved()")
        pass
