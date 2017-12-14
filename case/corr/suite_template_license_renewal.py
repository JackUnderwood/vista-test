import unittest

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist
from ui.high.checklist_select_template import ChecklistSelectTemplate

__author__ = 'John Underwood'


class TemplateLicenseRenewal(unittest.TestCase):
    ui.log.info(">> Inside AllJobSearch class")
    process = UI()
    checklist = None
    debug = 'all'
    test = None

    @classmethod
    def setUpClass(cls):
        License()
        cls.checklist = Checklist()
        ChecklistSelectTemplate()

    @classmethod
    def tearDownClass(cls):
        cls.process.wait(3)
        cls.process.teardown()

    def tearDown(self):
        # Get the current window, close it, and return to the checklist page.
        self.process.check_for_new_window()
        self.process.driver.close()
        self.process.check_for_new_window()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(
        debug is 'american' or debug is 'all', "testing {}".format(debug,))
    def test_american(self):
        ui.log.info('>>> Inside function test_american()')
        expected = {
            'template': 'American Boards Verification',
            'entity': self.checklist.entity
        }
        self.process.update({
            'american': ('Click',
                         '//*[@id="correspondenceChooser_form"]/p[2]/p[1]/a'),
        })
        self.process.execute(('american',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'authorization' or debug is 'all', "testing {}".format(debug,))
    def test_authorization(self):
        ui.log.info('>>> Inside function test_authorization()')
        expected = {
            'template': 'Authorization/Release Statement',
            'entity': self.checklist.entity
        }
        self.process.update({
            'authorization': ('Click',
                              '//*[@id="correspondenceChooser_form"]'
                              '/p[2]/p[2]/a'),
        })
        self.process.execute(('authorization',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'claims' or debug is 'all', "testing {}".format(debug,))
    def test_claims(self):
        ui.log.info('>>> Inside function test_claims()')
        expected = {
            'template': 'Claims History Request',
            'entity': self.checklist.entity
        }
        self.process.update({
            'claims': ('Click',
                       '//*[@id="correspondenceChooser_form"]/p[2]/p[3]/a'),
        })
        self.process.execute(('claims',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'cover' or debug is 'all', "testing {}".format(debug,))
    def test_cover(self):
        ui.log.info('>>> Inside function test_cover()')
        expected = {
            'template': 'Cover letter - Introduction',
            'entity': self.checklist.entity
        }
        self.process.update({
            'cover': ('Click',
                      '//*[@id="correspondenceChooser_form"]/p[2]/p[4]/a'),
        })
        self.process.execute(('cover',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'ecfmg' or debug is 'all', "testing {}".format(debug,))
    def test_ecfmg(self):
        ui.log.info('>>> Inside function test_ecfmg()')
        expected = {
            'template': 'ECFMG request',
            'entity': self.checklist.entity
        }
        self.process.update({
            'ecfmg': ('Click',
                      '//*[@id="correspondenceChooser_form"]/p[2]/p[5]/a'),
        })
        self.process.execute(('ecfmg',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'federation' or debug is 'all', "testing {}".format(debug,))
    def test_federation(self):
        ui.log.info('>>> Inside function test_federation()')
        expected = {
            'template': 'Federation clearance request (FSMB)',
            'entity': self.checklist.entity
        }
        self.process.update({
            'federation': ('Click',
                           '//*[@id="correspondenceChooser_form"]/p[2]/p[6]/a'),
        })
        self.process.execute(('federation',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'hosp' or debug is 'all', "testing {}".format(debug,))
    def test_hosp(self):
        ui.log.info('>>> Inside function test_hosp()')
        expected = {
            'template': 'Hosp. Privs. Verif.',
            'entity': self.checklist.entity
        }
        self.process.update({
            'hosp': ('Click',
                     '//*[@id="correspondenceChooser_form"]/p[2]/p[7]/a'),
        })
        self.process.execute(('hosp',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'license_app' or debug is 'all', "testing {}".format(debug,))
    def test_license_app(self):
        ui.log.info('>>> Inside function test_license_app()')
        expected = {
            'template': 'License Application Transmittal',
            'entity': self.checklist.entity
        }
        self.process.update({
            'licenseApp': ('Click',
                           '//*[@id="correspondenceChooser_form"]/p[2]/p[8]/a'),
        })
        self.process.execute(('licenseApp',))
        self.process.check_for_new_window()
        selected = self. process.get_selected_option('//*[@id="template_id" and '
                                                     '@class="browser-default"]',
                                                     attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'license_notice' or debug is 'all', "testing {}".format(debug,))
    def test_license_notice(self):
        ui.log.info('>>> Inside function test_license_notice()')
        expected = {
            'template': 'License notice of non-renewal',
            'entity': self.checklist.entity
        }
        self.process.update({
            'licenseNotice': ('Click',
                            '//*[@id="correspondenceChooser_form"]/p[2]/p[9]/a'),
        })
        self.process.execute(('licenseNotice',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'license_renewal' or debug is 'all', "testing {}".format(debug,))
    def test_license_renewal(self):
        ui.log.info('>>> Inside function test_license_renewal()')
        expected = {
            'template': 'License Renewal',
            'entity': self.checklist.entity
        }
        self.process.update({
            'licenseRenewal': (
                'Click',
                '//*[@id="correspondenceChooser_form"]/p[2]/p[10]/a'),
        })
        self.process.execute(('licenseRenewal',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'license_verify' or debug is 'all', "testing {}".format(debug,))
    def test_license_verify(self):
        ui.log.info('>>> Inside function test_license_verify()')
        expected = {
            'template': 'License Verification',
            'entity': self.checklist.entity
        }
        self.process.update({
            'licenseVerify': (
                'Click',
                '//*[@id="correspondenceChooser_form"]/p[2]/p[11]/a'),
        })
        self.process.execute(('licenseVerify',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'license_verify_form' or debug is 'all', "testing {}".format(debug,))
    def test_license_verify_form(self):
        ui.log.info('>>> Inside function test_license_verify_form()')
        expected = {
            'template': 'License Verification + Form',
            'entity': self.checklist.entity
        }
        self.process.update({
            'licenseVerifyForm': (
                'Click',
                '//*[@id="correspondenceChooser_form"]/p[2]/p[12]/a'),
        })
        self.process.execute(('licenseVerifyForm',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'malpractice' or debug is 'all', "testing {}".format(debug,))
    def test_malpractice(self):
        ui.log.info('>>> Inside function test_malpractice()')
        expected = {
            'template': 'Malpractice Insurance Verification',
            'entity': self.checklist.entity
        }
        self.process.update({
            'malpractice': ('Click',
                            '//*[@id="correspondenceChooser_form"]/p[2]/p[13]/a'),
        })
        self.process.execute(('malpractice',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'medical' or debug is 'all', "testing {}".format(debug,))
    def test_medical(self):
        ui.log.info('>>> Inside function test_medical()')
        expected = {
            'template': 'Medical Education Verification',
            'entity': self.checklist.entity
        }
        self.process.update({
            'medical': ('Click',
                        '//*[@id="correspondenceChooser_form"]/p[2]/p[14]/a'),
        })
        self.process.execute(('medical',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'post' or debug is 'all', "testing {}".format(debug,))
    def test_post(self):
        ui.log.info('>>> Inside function test_post()')
        expected = {
            'template': 'Post-Grad Training Verification',
            'entity': self.checklist.entity
        }
        self.process.update({
            'post': ('Click',
                     '//*[@id="correspondenceChooser_form"]/p[2]/p[15]/a'),
        })
        self.process.execute(('post',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'reference' or debug is 'all', "testing {}".format(debug,))
    def test_reference(self):
        ui.log.info('>>> Inside function test_reference()')
        expected = {
            'template': 'Reference Recommendation',
            'entity': self.checklist.entity
        }
        self.process.update({
            'reference': ('Click',
                          '//*[@id="correspondenceChooser_form"]/p[2]/p[16]/a'),
        })
        self.process.execute(('reference',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
        provider = self.process.spy('#desc_provider_id', 'value')
        self.assertEqual(expected['entity'], provider, msg=expected['entity'])

    @unittest.skipUnless(
        debug is 'release' or debug is 'all', "testing {}".format(debug,))
    def test_release(self):
        ui.log.info('>>> Inside function test_release()')
        expected = {
            'template': 'Release and Authorization',
            'entity': self.checklist.entity
        }
        self.process.update({
            'release': ('Click',
                        '//*[@id="correspondenceChooser_form"]/p[2]/p[17]/a'),
        })
        self.process.execute(('release',))
        self.process.check_for_new_window()
        selected = self.process.get_selected_option('//*[@id="template_id" and '
                                                    '@class="browser-default"]',
                                                    attribute_name='text')
        self.assertEqual(expected['template'], selected,
                         msg=expected['template'])
