import unittest

import ui
from ui import UI
from tool.helpers import find_rows, get_color, get_row_numbers

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
    debug = 'no_post_to_ready_to_post'  # 'all'

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
        """
        Prerequisites:
        + Approved status: Approved
        + Ready to post: Yes
        + Reason not to post: No

        1 Find a set of approved jobs,
        2 Select the top-most job
        3 Expand the row
        4 Click the job's edit button
        5 Click Reject check box to select
        6 Select the reason for rejection
        7 Click Confirm
        8 Click Save
        Expected: Saves successfully and row's color is #FFCCFF - pastel violet
        """
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
        """
        Prerequisites:
        + Approved status: Not Approved
        + Ready to post: No
        + Reason not to post: No

        1 Find a set of rejected jobs,
        2 Select the top-most job
        3 Expand the row
        4 Click the Approved checkbox
        5 Cancel the alert
        Expected: Alert stating, "You are about to approve a job that has not
                  been set to 'Ready to Post'."

        6 Click the job's edit button
        7 Click Ready to Post check box to select
        8 Check for required fields alert box
        9 Fill in the required fields, i.e. subtitle, and internal/ext descriptions
        10 Click Ready to Post check box to select
        11 Click Rejected check box to deselect
        12 Click Save
        Expected: Saves successfully and row's color turns to blue
        """
        ui.log.info(">>> Inside function test_rejected_to_approved()")
        runtime = {
            'jobBoardStatus': ('Click', 'css=.ui-multiselect.ui-widget.'
                                        'ui-state-default.ui-corner-all.multi_s.'
                                        'multi_s_job_board_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_board_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobBoardStatusReject': (
                'Click', '#ui-multiselect-s_job_board_status-option-5')
        }
        self.process.update(runtime)
        order = ('jobBoardStatus', 'wait', 'jobBoardStatusReject', )
        self.process.execute(order)
        self.process.wait()

        rows = find_rows(
            self.process,
            'expandable-row',
            './td/div/div[3]/div[2]/div[3]/div/div/div/div[2]/strong',
            'innerHTML'
        )
        not_approved_row_ids = [r[0] for r in rows if 'Not Approved' in r]
        if not check_valid(self.process, not_approved_row_ids):
            self.assertTrue(False, msg='no "Not Approved" rows available')
        not_approved_row_ids.sort(reverse=True)
        # Strip out the text, i.e. "expandable_"
        ids = [r[r.find('_') + 1:] for r in not_approved_row_ids]
        job_id = ids[0]
        all_row_numbers = get_row_numbers(self.process)
        index = all_row_numbers.index(job_id) + 1

        self.process.update({  # //*[@id="expandable_97848"]
            'expand': (
                'Click',
                '//*[@id="result-target"]/tbody/tr[{}]'.format(index, )),
            'approved': (
                'Click',
                '//*[@id="expandable_{}"]/td/div/div[3]/label[1]'.format(job_id, )),
        })
        self.process.execute(('expand', 'approved'))
        self.process.wait()
        expected = ("You are about to approve a Job that has not been set "
                    "to \'Ready to Post\'. Are you sure? Press OK to continue.")
        actual = self.process.dismiss_alert()
        self.process.compare(expected, actual, message="dismiss alert")
        self.process.wait()

        self.process.update({
            'edit': ('Click', '#edit_{}'.format(job_id, )),
            'template': ('Select',
                         '#JobDescriptionTemplates__job_description_template_id',
                         'Allergy'),
            'ready': ('Click',
                      '//*[@for="job_board_post_status__is_ready_to_post"]'),
            'reject': ('Click',
                       '//*[@for="job_board_rejection_history__is_rejected"]'),
            'save': ('Click', '#edit-save'),
            'reset': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[3]/button'),
            'entry': ('Type', '#s_job_number', job_id),
            'refresh': ('Click',
                        '//*[@id="job-search-wrap"]/div[2]/div[2]/button')
        })
        self.process.execute(('edit', 'template', 'ready', 'reject', 'save', ))
        self.process.wait()
        expected = "Job Saved"
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

        # Check for the background color.
        self.process.execute(('reset', 'entry', 'refresh'))
        self.process.wait()

        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            '#cceeee', actual_color, message="blue background expected")
        self.assertTrue(result, msg='color blue expected')

    @unittest.skipUnless(debug is 'none_to_ready_to_post' or debug is 'all',
                         "testing {}".format(debug,))
    def test_none_to_ready_to_post(self):
        """
        + Approved OFF
        + Rejected OFF
        + Ready to post NO
        + Reason not to post NO

        1 Find a set of jobs that have no status
        2 Select the top-most job
        3 Click on the job's edit button
        4 Fill in the required fields
        5 Select Ready to Post check box
        6 Save the job

        Expected: job saves successfully and changes to blue - #CCEEEE
        """
        ui.log.info(">>> Inside function test_none_to_ready_to_post()")
        runtime = {
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': ('Click', '#ui-multiselect-s_job_status-option-4'),
        }
        self.process.update(runtime)
        self.process.execute(('jobStatus', 'wait', 'jobStatusActive',
                              'jobStatusHot'))
        self.process.wait()
        # Get the white background elements and expand the first item
        rows = self.process.find_elements(
            '//*[@id="result-target"]/tbody/tr[@class=" " or @class="odd "]')
        row_ids = [row.find_element_by_xpath('./td[1]').text for row in rows]
        job_number = row_ids.pop(0)
        self.process.update({
            'edit': ('Click', '#edit_' + job_number,),
            'ready': ('Click',
                      '//*[@for="job_board_post_status__is_ready_to_post"]')
        })
        self.process.execute(('edit',))
        self.process.wait()
        self.process.execute(('ready',))
        # Click Ready to Post may display a popup dialog.
        dialog = self.process.spy('//*[@for="used_by_modal"]', 'innerHTML')
        ui.log.info("DIALOG Alert Text: {}".format(dialog, ))
        # 'You need to fill out required subtitle and/or description'
        if dialog:
            self.process.compare(True, False, message='needs required fields')
            self.process.update({
                'okay': ('Click', '//*[@button="dismiss"]'),
                'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle'),
                'template': (
                    'Select',
                    '#JobDescriptionTemplates__job_description_template_id',
                    'Allergy'
                ),
            })
            # Click Template may display an alert dialog.
            self.process.execute(('okay', 'subtitle', 'template', ))
            self.process.accept_alert()
            self.process.wait()
            self.process.execute(('ready', ))

        self.process.wait()
        self.process.update({
            'save': ('Click', '#edit-save'),
        })
        expected = 'Job Saved'
        self.process.execute(('save', ))
        self.process.results(expected)
        self.process.wait()

        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            '#cceeee', actual_color, message="blue background expected")
        self.assertTrue(result, msg='color blue expected')

    @unittest.skipUnless(debug is 'none_to_approved' or debug is 'all',
                         "testing {}".format(debug,))
    def test_none_to_approved(self):
        """
        Prerequisite: requires jobs that have no status (white)
        + Approved OFF
        + Rejected OFF
        + Ready to post NO
        + Reason not to post NO
        + Job has subtitle NO
            OR Job has description NO

        1 Find a set of jobs that have no status
        2 Select the top-most job
        3 Click on the job's edit button
        4 Click on Approved
        Expected: 'fill out required subtitle and/or description' alert
        5 Dismiss alert and fill in the required fields
        6 Select Approved check box
        Expected: Check for alert "You are about to approve a Job that has not
                  been set to 'Ready to Post'."
        7 Dismiss the alert and save the job
        Expected: job saves successfully and changes to blue
        """
        ui.log.info(">>> Inside function test_none_to_approved()")
        runtime = {
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': ('Click', '#ui-multiselect-s_job_status-option-4'),
            'expandAll': ('Click',
                          '//*[@id="result-target"]/thead/tr[1]/td[3]/i[1]'),
        }
        self.process.update(runtime)
        self.process.execute(('jobStatus', 'wait', 'jobStatusActive',
                              'jobStatusHot', ))
        self.process.wait()
        # Get the white background elements that have no subtitle OR description
        subtitle_locator = ('./td/div/div[3]/div[3]/div[6]/div/div/div/'
                            'div[2]/strong')
        no_subtitle_rows = find_rows(self.process, 'expandable-row',
                                     subtitle_locator, 'innerHTML')
        valid_rows = [r[0][r[0].find('_')+1:]
                      for r in no_subtitle_rows if 'No' in r]
        if len(valid_rows) < 1:
            # If all subtitles are available, then look for no descriptions
            description_locator = ('./td/div/div[3]/div[3]/div[7]/div/div/div/'
                                   'div[2]/strong')
            no_desc_rows = find_rows(self.process, 'expandable-row',
                                     description_locator, 'innerHTML')
            valid_rows = [r[0][r[0].find('_')+1:]
                          for r in no_desc_rows if 'No' in r]
            if len(valid_rows) < 1:
                self.process.compare(True, False,
                                     message="no valid rows available")
                self.process.teardown()
        job_number = valid_rows.pop(0)
        self.process.update({
            'edit': ('Click', '#edit_' + job_number,),
            'approve': ('Click', '//*[@for="jobs__show_on_job_board"]')
        })
        expected = ('You need to fill out required subtitle and/or '
                    'description fields.')
        self.process.execute(('edit',))
        self.process.wait()
        self.process.execute(('approve',))
        self.process.wait()  # //*[@id="displayContent_1497542939805"]/div/p
        dialog = self.process.find_element('//*[@for="used_by_modal"]')
        if not dialog:
            self.assertTrue(False,
                            msg='"fill out required" dialog did not appear')
        dialog_text = dialog.find_element_by_xpath('./div/p').text
        self.process.compare(expected, dialog_text)
        self.process.update({
            'okay': ('Click', '//*[@button="dismiss"]'),
            'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle'),
            'template': (
                'Select',
                '#JobDescriptionTemplates__job_description_template_id',
                'Allergy'
            ),
        })
        expected = ('You are about to approve a Job that has not been set to '
                    '\'Ready to Post\'. Are you sure? Press OK to continue.')
        self.process.execute(('okay', 'subtitle', 'template', ))
        self.process.accept_alert()
        self.process.wait()
        self.process.execute(('approve', ))
        self.process.wait()
        actual = self.process.accept_alert()
        self.process.compare(expected, actual)
        self.process.update({
            'save': ('Click', '#edit-save'),
        })
        expected = 'Job Saved'
        self.process.execute(('save', ))
        self.process.results(expected)
        self.process.wait(2)

        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            '#ffddbb', actual_color, message="violet background expected")
        self.assertTrue(result, msg='row color violet expected')

    @unittest.skipUnless(debug is 'none_to_reason_not_to_post' or debug is 'all',
                         "testing {}".format(debug,))
    def test_none_to_reason_not_to_post(self):
        """
        Prerequisite: requires jobs that have no status (white)
        + Approved OFF
        + Rejected OFF
        + Ready to post NO
        + Reason not to post NO

        1 Find a set of jobs that have no status
        2 Select the top-most job
        3 Click on the job's edit button
        4 Select the Reason Not to Post option "Job is a duplicate"
        5 Save the job
        Expected: job saves successfully and changes to rust
         class=" nopost"
         background #fdb
        """
        ui.log.info(">>> Inside function test_none_to_reason_not_to_post()")
        runtime = {
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': ('Click', '#ui-multiselect-s_job_status-option-4'),
        }
        self.process.update(runtime)
        self.process.execute(('jobStatus', 'wait', 'jobStatusActive',
                              'jobStatusHot', ))
        self.process.wait()
        # Get the white background elements
        rows = self.process.find_elements(
            '//*[@id="result-target"]/tbody/tr[@class=" " or @class="odd "]')
        if not rows:
            self.process.compare(True, False,
                                 message="no white jobs rows available")
            self.assertTrue(False, msg='no white rows')

        row_ids = [row.find_element_by_xpath('./td[1]').text for row in rows]
        job_number = row_ids.pop(0)
        self.process.update({
            'edit': ('Click', '#edit_' + job_number,),
            'reason': (
                'Select',
                '#job_board_post_status__job_board_post_status_reasons_id',
                'Job is a duplicate'),
            'save': ('Click', '#edit-save'),
            'reset': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[3]'),
            'job': ('Type', '#s_job_number', job_number),
            'search': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[2]')
        })
        expected = 'Job Saved'
        self.process.execute(('edit', 'reason', ))
        self.process.wait()
        self.process.execute(('save',))
        self.process.wait()
        self.process.results(expected, locator='toast-container')

        self.process.execute(('reset', 'job', 'search', ))
        expected = '#ffddbb'
        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            expected, actual_color, message="violet background expected")
        self.assertTrue(result, msg='row color violet expected')

    @unittest.skipUnless(debug is 'none_to_reason_not_to_post_other'
                         or debug is 'all',
                         "testing {}".format(debug,))
    def test_none_to_reason_not_to_post_other(self):
        """
        Prerequisite: requires jobs that have no status (white)
        1 Find a set of jobs that have no status
        2 Select the top-most job
        3 Click on the job's edit button
        4 Select the Reason Not to Post option "Other"
        5 Save the job
        Expected: Check for alert "You need to fill out an explanation for the
                  reason not to post."
        6 Fill out the explanation not to post
        7 Save the job
        Expected: job saves successfully and changes to rust
         class=" nopost"
         background #fdb
        """
        ui.log.info(">>> Inside function test_none_to_reason_not_to_post()")
        runtime = {
            'jobStatus': ('Click',
                          'css=.ui-multiselect.ui-widget.ui-state-default.'
                          'ui-corner-all.multi_s.multi_s_job_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_status-option-1',
                     {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobStatusActive': (
                'Click', '#ui-multiselect-s_job_status-option-1'),
            'jobStatusHot': ('Click', '#ui-multiselect-s_job_status-option-4'),
        }
        self.process.update(runtime)
        self.process.execute(('jobStatus', 'wait', 'jobStatusActive',
                              'jobStatusHot', ))
        self.process.wait()
        # Get the white background elements
        rows = self.process.find_elements(
            '//*[@id="result-target"]/tbody/tr[@class=" " or @class="odd "]')
        if not rows:
            self.process.compare(True, False,
                                 message="no white jobs rows available")
            self.assertTrue(False, msg='no white rows')

        row_ids = [row.find_element_by_xpath('./td[1]').text for row in rows]
        job_number = row_ids.pop(0)
        self.process.update({
            'edit': ('Click', '#edit_' + job_number,),
            'reason': (
                'Select',
                '#job_board_post_status__job_board_post_status_reasons_id',
                'Other'),
            'other': (
                'Type',
                '#job_board_post_status__job_board_status_explanation',
                'QA reason not to post'),
            'save': ('Click', '#edit-save'),
            'reset': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[3]'),
            'job': ('Type', '#s_job_number', job_number),
            'search': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[2]')
        })
        expected = 'Job Saved'
        self.process.execute(('edit', 'reason', 'other', ))
        self.process.wait()
        self.process.execute(('save',))
        self.process.wait()
        self.process.results(expected, locator='toast-container')

        self.process.execute(('reset', 'job', 'search', ))
        expected = '#ffddbb'
        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            expected, actual_color, message="violet background expected")
        self.assertTrue(result, msg='row color violet expected')

    @unittest.skipUnless(debug is 'no_post_to_ready_to_post' or debug is 'all',
                         "testing {}".format(debug,))
    def test_reason_not_to_post_to_ready_to_post(self):
        """
        Prerequisite: requires jobs that have reason not to post (rust)
        + Approved OFF
        + Rejected OFF
        + Ready to post NO
        + Reason not to post YES

        1 Find a set of jobs that have reason not to post - use Job Board Status
          option Don't Post
        2 Select the top-most job
        3 Click on the job's edit button
        4 Select the Ready to Post check box
        If subtitle/descriptions are empty then expect dialog:
            "You need to fill out required subtitle and/or description fields."
        Expected: Reason Not to Post clears out
        5 Click Save button
        Expected: job saves successfully and changes to blue
         class=" ready"
         background #cee
        """
        ui.log.info(">>> Inside function test_reason_not_to_post_to_"
                    "ready_to_post()")
        runtime = {
            'jobBoardStatus': ('Click', 'css=.ui-multiselect.ui-widget.'
                                        'ui-state-default.ui-corner-all.multi_s.'
                                        'multi_s_job_board_status'),
            'wait': ('Wait', '#ui-multiselect-s_job_board_status-option-1',
                      {'condition': 'element_to_be_clickable', 'wait_time': '2'}),
            'jobBoardStatusNoPost': (
                'Click', '#ui-multiselect-s_job_board_status-option-3'),
        }
        self.process.update(runtime)
        order = ('jobBoardStatus', 'wait', 'jobBoardStatusNoPost', )
        self.process.execute(order)
        self.process.wait()

        job_number = self.process.spy(
            '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        self.process.update({
            'edit': ('Click', '#edit_{}'.format(job_number, )),
            'ready': (
                'Click', '//*[@for="job_board_post_status__is_ready_to_post"]'),
            'subtitle': ('Type', '#jobs__job_board_subtitle', 'QA Subtitle'),
            'ok': ('Click', '//*[@button="dismiss"]'),
            'template': (
                'Select',
                '#JobDescriptionTemplates__job_description_template_id',
                'Allergy'),
            'save': ('Click', '#edit-save'),
            'reset': ('Click', '//*[@id="job-search-wrap"]/div[2]/div[3]/button'),
            'entry': ('Type', '#s_job_number', job_number),
            'refresh': ('Click',
                        '//*[@id="job-search-wrap"]/div[2]/div[2]/button')
        })
        self.process.execute(('edit', 'ready'))
        self.process.wait()
        dialog = self.process.spy('//*[@for="used_by_modal"]', 'innerHTML')
        ui.log.info("DIALOG Alert Text: {}".format(dialog, ))
        if dialog:
            self.process.execute(('ok', 'subtitle', 'template', ))
            self.process.wait()
            self.process.accept_alert()
        # Actual will be a number if not cleared
        actual = self.process.get_selected_option(
            '#job_board_post_status__job_board_post_status_reasons_id')
        self.process.compare('', actual, message='')

        self.process.execute(('save',))
        self.process.wait()

        self.process.execute(('reset', 'entry', 'refresh',))
        expected = '#cceeee'
        rgb = self.process.get_css_property(
            '//*[@id="result-target"]/tbody/tr[1]', 'background-color')
        actual_color = get_color(rgb)
        ui.log.info('COLOR: {}'.format(actual_color, ))
        result = self.process.compare(
            expected, actual_color, message="blue background expected")
        self.assertTrue(result, msg='row color blue expected')
