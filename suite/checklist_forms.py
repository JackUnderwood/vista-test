import unittest

import ui
from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

__author__ = 'John Underwood'
NOTES = """In computer programming, a placeholder is a character, word, or 
string of characters that may be used to take up space until such a time that 
the space is needed. For example, a programmer may know that she needs a certain 
number of values or variables, but doesn't yet know what to input. She can use 
a placeholder as a temporary solution until a proper value or variable can be 
assigned. For example, the designer of an online newsletter may have a template 
that they fill with dummy text so they can get an idea of how to layout a page 
looks. One of the most common filler texts is lorem ipsum."""


class TestSuiteChecklistForms(unittest.TestCase):
    ui.log.info(">> Inside TestSuiteChecklistForms class")
    process = UI()
    debug = 'all'  # use 'all'; or test individual case methods below

    def setUp(self):
        License()
        self.process.wait()
        Checklist()
        self.process.wait(3)  # delay so ribbon has time to display

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.process.wait(1)
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'carrier' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_carrier(self):
        ui.log.info(">>> Inside function test_add_carrier()")
        runtime = {
            'malpractice': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/li[5]/a'
            ),
            'addCarrier': (
                'Click', '//*[@id="malpracticeGrid_form_inline"]/a[2]'),
            'findInsuranceProvider': (
                'Type', '#insurance_provider_id_desc', 'ame'),
            'selectInsuranceProvider': ('Click', '#167224'),  # Neurology
            'startDate': ('Type', '#start_date', '01072015'),
            'endDate': ('Type', '#end_date', '05182015'),
            'occurrenceAmount': ('Type', '#per_occurrence_amount', '2000000'),
            'aggregateAmount': ('Type', '#aggregate_amount', '2000000'),
            'policyNumber': ('Type', '#policy_number', 'WWF42BAR69'),
            'save': ('Click', '//*[@button="save"]'),
        }
        expected = "Carrier saved"
        self.process.update(runtime)
        order = ('malpractice', 'addCarrier', 'findInsuranceProvider',
                 'selectInsuranceProvider', 'startDate', 'endDate',
                 'occurrenceAmount', 'aggregateAmount', 'policyNumber', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'claim' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_claim(self):
        ui.log.info(">>> Inside function test_add_claim()")
        runtime = {
            'malpractice': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/li[5]/a'
            ),
            'addClaim': ('Click', '//*[@id="malpracticeGrid_form_inline"]/a[1]'),
            'findInsuranceProvider': (
                'Type',
                '#insurance_provider_id_desc',
                'ame'
            ),  # Orthopaedic Surgeons
            'selectInsuranceProvider': ('Click', '#62963'),
            'status': ('Select', '#claim_status_id', 'Open'),
            'startDate': ('Type', '#start_date', '01062015'),
            'endDate': ('Type', '#end_date', '05172015'),
            'description': ('Type', '#description', 'Needle in a haystack'),
            'settleAmount': ('Type', '#settlement_amount', '550000'),
            'claimNumber': ('Type', '#claim_number', 'WTF42FOO69'),
            'note': ('Type', '#note', NOTES),
            'save': ('Click', '//*[@button="save"]'),
        }
        expected = "Claim saved"
        self.process.update(runtime)
        order = ('malpractice', 'addClaim', 'findInsuranceProvider',
                 'selectInsuranceProvider', 'status', 'startDate', 'endDate',
                 'description', 'settleAmount', 'claimNumber', 'note', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'education' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_education(self):
        ui.log.info(">>> Inside function test_add_education()")
        runtime = {
            'education': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/li[3]/a'
            ),
            'addEducation': (
                'Click', '//*[@id="educationGrid_form_inline"]/a[1]'),
            'findEducation': ('Type', '#education_entity_id_desc', 'utah'),
            'sEducation': ('Click', '#user_name'),
            'sDegree': ('Select', '#education_degree_id', 'Doctor of Medicine'),
            'sType': ('Select', '#education_type_id', 'Medical School'),
            'startDate': ('Type', '#start_date', '01042015'),
            'endDate': ('Type', '#end_date', '05172015'),
            'director': ('Type', '#director', 'Dr. James Kildeare'),
            'honor': ('Type', '#honor', 'Summa cum Laude'),
            'checkCv': ('Click', '//*[@for="use_on_cv"]'),
            'save': ('Click', '//*[@button="save"]')
        }
        expected = "Education saved"
        self.process.update(runtime)
        order = ('education', 'addEducation', 'findEducation', 'sEducation',
                 'sDegree', 'sType', 'startDate', 'endDate', 'director', 'honor',
                 'checkCv', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'examination' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_an_examination(self):
        ui.log.info(">>> Inside function test_add_examination()")
        runtime = {          #
            'exam': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/li[4]/a'),
            'addExam': ('Click', '//*[@id="examinationGrid_form_inline"]/a[1]'),
            'checkPassed': (
                'Click',
                '//*[@id="examinationEdit_form"]/div[1]/div/label', ),
            'sExamination': (
                'Select',
                '#examination_id',
                'COMAT'
            ),
            'sState': ('Select', '#state_code_id', 'Colorado'),
            'examDate': ('Type', '#exam_date', '01052015'),
            'score': ('Type', '#score', '94'),
            'save': ('Click', '//*[@button="save"]')
        }
        expected = "Examination saved"
        self.process.update(runtime)
        order = ('exam', 'addExam', 'checkPassed', 'sExamination', 'sState',
                 'examDate', 'score', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'experience' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_experience(self):
        ui.log.info(">>> Inside function test_add_experience()")
        runtime = {
            'experience': (
                'Click',
                'css=#content>div.row>div.col.s3>ul>li:nth-child(2)>a'),
            'addExperience': (
                'Click', 'css=#experienceGrid_form_inline>a.leaf.btn'),
            'findClient': ('Type', '#client_id_number_desc', 'acute family'),
            'selectClient': ('Click', '//*[@item_id="315711"]'),  # Acute Family
            # #user_name
            'check': (
                'Click',
                '//*[@id="ExperienceEdit_form"]/div[5]/div[2]/label'),
            'description': ('Type', 'name=description', 'Genetics research'),
            'startDate': ('Type', '#start_date', '01042015'),
            'endDate': ('Type', '#end_date', '05172015'),
            'department': ('Type', '#department', 'Urology'),
            'departmentChair': ('Type', '#department_chair', 'Jack Shoop'),
            'capacity': ('Type', '#capacity', 'Rare Genetic Diseases'),
            'notes': ('Type', '#notes', 'Notes on rare genetic diseases'),
            'save': ('Click', '//*[@button="save"]')
        }
        expected = "Experienced saved"
        self.process.update(runtime)
        order = ('experience', 'addExperience', 'findClient', 'selectClient',
                 'description', 'check', 'startDate', 'endDate', 'department',
                 'departmentChair', 'capacity', 'notes', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, locator='toast-container')
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'email' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_email(self):
        ui.log.info(">>> Inside function test_add_email()")
        from tool.generators.generator import gen_email

        runtime = {
            'expand': ('Click', '//*[@id="ribbon_form"]/ul/li/div[1]'),
            'email': (
                'Click',
                '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[3]'),
        }
        expected = "Email saved"

        self.process.update(runtime)
        order = ('email', )
        self.process.execute(order)
        # Spy for the name in the drawers
        name = self.process.spy('/html/body/main/div[2]/div[1]/h3', 'innerHTML')
        name = name[name.find('(')+1:name.find(')')]
        ui.log.debug('EXTRACTED NAME {}'.format(name,))
        email = gen_email(name)
        ui.log.debug('EMAIL ADDRESS {}'.format(email,))

        runtime = {
            'addEmail': ('Click', '//*[@id="emailGrid_form"]/a'),
            'emailAddress': ('Type', '#email_address', email),
            'emailType': (
                'Select', '#email_correspondence_method_type_id', 'Work'),
            'save': ('Click', '//*[@id="editEmail_form"]/div[9]/a[1]')
        }
        self.process.update(runtime)
        order = ('addEmail', 'emailAddress', 'emailType', 'save')
        self.process.execute(order)
        self.process.wait()
        result = self.process.results(expected)
        self.assertTrue(result, msg=expected)
