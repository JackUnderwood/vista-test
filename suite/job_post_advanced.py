import unittest

import ui
from ui import UI
from ui.high.job_post_advanced import JobAdvanced

__author__ = 'John Underwood'


class TestSuiteJobPostAdvanced(unittest.TestCase):
    """
    This suite uses the Advanced search feature.
    """
    ui.log.info(">> Inside TestSuiteJobPostAdvanced class")
    process = UI()
    debug = 'all'

    def setUp(self):
        self.process.get("jobs/search")
        self.process.wait()
        JobAdvanced()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.process.wait()
        cls.process.teardown()

    # *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES *^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'basic_single_positive' or debug is 'all',
                         "testing {}".format(debug,))
    def test_basic_single_positive(self):
        """
        Find "EMR Types is Cerner"
        :return: void
        """
        ui.log.info(">>> Inside function test_basic_single_positive()")
        runtime = {
            'group': (
                'Select',
                '//*[@id="adv-seach-prime"]/div/div[2]/select',
                'EMR Types'),
            'option': ('Select', '//*[@id="adv-seach-prime"]/div/div[4]/select',
                       'Cerner'),
            'search': ('Click',
                       '//*[@id="job-search-wrap"]/div[3]/div[2]/button'),
            'expand': ('Click',
                       '//*[@id="result-target"]/thead/tr[1]/td[3]/i[1]'),
        }
        self.process.update(runtime)
        self.process.execute(('group', 'option', 'search', ))
        self.process.wait()
        self.process.execute(('expand', ))
        expected = 'EMR: Cerner'
        job_number = self.process.spy(
            '//*[@id="result-target"]/tbody/tr[1]/td[1]', 'innerHTML')
        result = self.process.spy(
            '//*[@id="expandable_{}"]/td/div/div[2]/div/div'.format(job_number),
            'innerHTML')
        self.process.compare(True, expected in result)
        self.process.wait()
        self.assertTrue(result, msg=expected)
