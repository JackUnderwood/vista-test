"""
Start inside Contact Notes drawer
Test various Follow Up's Quick Notes
"""
import unittest

import ui
from ui import UI

__author__ = 'John Underwood'


class TestSuiteContactNotesQuickNotes(unittest.TestCase):
    """
    Prerequisite: This test suite requires a provider that already has a phone
    number listed.
    """
    # TODO: 'prerequisite' func that adds a new phone number for the provider
    ui.log.info(">> Inside TestSuiteContactNotesQuickNotes class")
    process = UI()
    result = []
    debug = 'all'
    data = {
        'provider': 'n:ramirez p:779 652-5821',  # 'Amy Nayi',
        'providerId': '833235'                   # '652981'
    }
    feedback = 'Call Logged'

    @classmethod
    def setUpClass(cls):
        ui.log.info(">>> Setup the class")
        runtime = {
            'find': ('Type', '#main_desc', cls.data['provider']),
            'select': ('Click', '//*[@item_id="{}"]'.
                       format(cls.data['providerId'], )),
            'phone': ('Click',
                      '//*[@id="ribbon_form"]/ul/li/div[3]/div[4]/div[1]/a[4]'),
            'contact': ('Click',
                        '//*[@id="phoneGrid_grid"]/tbody/tr[1]/td[4]/a/span'),
            'comments': ('Click', '#viewLastFive'),
            'save': ('Click', '//*[@button="save"]'),
            'cancel': ('Click',
                       '//a[@button="close" and contains(text(), "Cancel")]'),
        }
        cls.process.update(runtime)
        order = ('find', 'select', 'phone',)
        cls.process.execute(order)
        cls.process.wait()

    def setUp(self):
        self.process.execute(('contact',))

    def tearDown(self):
        self.process.execute(('cancel',))
        self.result.clear()

    @classmethod
    def tearDownClass(cls):
        cls.process.teardown()

    # ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^* TEST CASES ^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*
    @unittest.skipUnless(debug is 'voicemail' or debug is 'all',
                         "testing {}".format(debug,))
    def test_quick_note_voicemail(self):
        ui.log.info(">>> Inside test_quick_note_voicemail()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'Voicemail'),
        }
        expected = 'Called and left a voicemail.'
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(self.feedback)
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        # All results must be true to pass.
        message = 'Feedback: {} & Note: {}'.format(self.feedback, expected, )
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'disconnected' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_disconnected(self):
        ui.log.info(">>> Inside test_quick_note_disconnected()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'Disconnected'),
        }
        expected = 'Call was disconnected.'
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(self.feedback)
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        message = 'Feedback: {} & Note: {}'.format(self.feedback, expected,)
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'not interested' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_not_interested(self):
        ui.log.info(">>> Inside test_quick_note_not_interested()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'Not Interested'),
        }
        expected = 'Entity was not interested in talking to VISTA Staffing.'
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(self.feedback)
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        message = 'Feedback: {} & Note: {}'.format(self.feedback, expected)
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'follow up' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_follow_up(self):
        ui.log.info(">>> Inside test_quick_note_follow_up()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'Follow Up'),
        }
        expected = 'Follow up maintenance call.'
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(self.feedback)
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        message = 'Feedback: {} & Note: {}'.format(self.feedback, expected)
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'no answer' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_no_answer(self):
        ui.log.info(">>> Inside test_quick_note_no_answer()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'No Answer'),
        }
        expected = 'No answer, and no voicemail was available.'
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(self.feedback)
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        message = 'Feedback: {} & Note: {}'.format(self.feedback, expected)
        self.assertTrue(all(self.result), msg=message)
