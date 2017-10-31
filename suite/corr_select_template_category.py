"""
Start inside Select a Template drawer.
Test various template categories.
"""
import unittest

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'


class TestSuiteCorrSelectTemplateCategory(unittest.TestCase):
    """
    Start at the 'Select a Template' drawer, and select every possible option,
    i.e. Client Sales, Provider Recruitment, Provider Licensing, etc.
    """
    ui.log.info(">> Inside TestSuiteCorrSelectTemplateCategory class")
    process = UI()
    debug = 'all'
    no_templates = 'No templates are available.'

    @classmethod
    def setUpClass(cls):
        ui.log.info(">>> Setup the class")
        License()
        Checklist()
        runtime = {
            'template': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[1]'),
            'option': 'Provider Licensing',
            'category': ('Select', '#category', '&option;')
        }
        cls.process.update(runtime)
        cls.process.wait()
        cls.process.execute(('template',))

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'client sales' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_client_sales(self):
        ui.log.info(">>> Inside test_corr_template_category_client_sales()")
        option = 'client sales'
        expected = self.no_templates
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy('//*[@id="correspondenceChooser_form"]/p[2]',
                                 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'provider recruitment' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_provider_recruitment(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_provider_recruitment()")
        option = 'provider recruitment'
        expected = self.no_templates
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy('//*[@id="correspondenceChooser_form"]/p[2]',
                                 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'provider credentialing' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_provider_credentialing(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_provider_credentialing()")
        option = 'provider credentialing'
        expected = 'Templates'  # the Templates label; templates are available
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy(
            '//*[@id="correspondenceChooser_form"]/p[2]/label', 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'provider licensing' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_provider_licensing(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_provider_licensing()")
        option = 'provider licensing'
        expected = 'Templates'  # the Templates label; templates are available
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy(
            '//*[@id="correspondenceChooser_form"]/p[2]/label', 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'assignment correspondence' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_assignment_correspondence(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_assignment_correspondence()")
        option = 'assignment correspondence'
        expected = self.no_templates
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy('//*[@id="correspondenceChooser_form"]/p[2]',
                                 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'converted correspondence' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_converted_correspondence(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_converted_correspondence()")
        option = 'converted correspondence'
        expected = self.no_templates
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy('//*[@id="correspondenceChooser_form"]/p[2]',
                                 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)

    @unittest.skipUnless(debug is 'provider privileging' or debug is 'all',
                         "testing {}".format(debug,))
    def test_corr_template_category_provider_privileging(self):
        ui.log.info(
            ">>> Inside test_corr_template_category_provider_privileging()")
        option = 'provider privileging'
        expected = self.no_templates
        self.process.update({'option': option.title()})
        self.process.execute(('category',))
        inner = self.process.spy('//*[@id="correspondenceChooser_form"]/p[2]',
                                 'innerHTML')
        res = expected in inner
        result = self.process.compare(True, res, message=option)
        self.assertTrue(result, msg=option)
