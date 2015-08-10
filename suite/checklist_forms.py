__author__ = 'John Underwood'
import unittest

from ui import UI
from ui.low.license import License
from ui.high.checklist import Checklist

NOTES = """Id vix minimum philosophia, pri clita lobortis inimicus ex. Qui
decore nusquam id. Eum modo electram deseruisse no, eos at clita menandri.
Vel alii cetero saperet in, mea te erant causae labitur, liber partiendo
est et.  Et vix malis intellegat consectetuer, mel regione democritum id, cum
delicata iracundia ea. Pro cu saepe eligendi dissentias, detraxit evertitur in
eos. Nonumes suscipit scaevola duo te, eam quot facer constituto cu, ex causae
utamur inimicus mei."""


class TestSuiteChecklistForms(unittest.TestCase):
    print(">> Inside TestSuiteChecklistForms class")
    process = UI()
    debug = 'all'  # use this to test individual test case methods below

    def setUp(self):
        License()
        Checklist({'rowNum': '5'})
        self.process.wait(5)  # delay so ribbon has time to display

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        UI().wait(3)
        UI().teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'carrier' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_carrier(self):
        print(">>> Inside function test_add_carrier()")
        runtime = {
            'malpractice': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/div/a[4]'
            ),
            'addCarrier': ('Click', '//*[@id="malpracticeGrid_form"]/a[2]'),
            'findInsuranceProvider': ('Type', '#insurance_provider_id_desc', 'ame'),
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
        result = self.process.results(expected, 'toast-container', 8)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'claim' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_claim(self):
        print(">>> Inside function test_add_claim()")
        runtime = {
            'malpractice': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/div/a[4]'
            ),
            'addClaim': ('Click', '//*[@id="malpracticeGrid_form"]/a[1]'),
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
        result = self.process.results(expected, 'toast-container', 8)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'education' or debug is 'never',
                         "testing {}".format(debug,))
    def test_add_education(self):
        print(">>> Inside function test_add_education()")
        runtime = {
            'education': (
                'Click',
                '//*[@id="content"]/div[2]/div[1]/ul/div/a[2]'
            ),
            'addEducation': ('Click', '//*[@id="educationGrid_form"]/a[1]'),
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
                 'sDegree', 'sType', 'startDate', 'endDate','director', 'honor',
                 'checkCv', 'save', )
        self.process.execute(order)
        result = self.process.results(expected, 'toast-container', 8)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'examination' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_examination(self):
        print(">>> Inside function test_add_examination()")
        runtime = {          #
            'exam': ('Click', '//*[@id="content"]/div[2]/div[1]/ul/div/a[3]'),
            'addExam': ('Click', '//*[@id="examinationGrid_form"]/a[1]'),
            'checkPassed': (
                'Click',
                '//*[@id="examinationEdit_form"]/div[1]/div/div[1]/div/label',),
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
        result = self.process.results(expected, 'toast-container', 8)
        self.assertTrue(result, msg=expected)

    @unittest.skipUnless(debug is 'experience' or debug is 'all',
                         "testing {}".format(debug,))
    def test_add_experience(self):
        print(">>> Inside function test_add_experience()")
        pass
