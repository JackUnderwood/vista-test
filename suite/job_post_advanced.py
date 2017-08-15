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
        self.process.wait()
        pass
