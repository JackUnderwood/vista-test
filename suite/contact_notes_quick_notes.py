"""
Start inside Contact Notes drawer
Test various Follow Up's Quick Notes
"""
import unittest

import ui
from ui import UI

__author__ = 'John Underwood'


class TestSuiteContactNotesQuickNotes(unittest.TestCase):
    ui.log.info(">> Inside TestSuiteContactNotesQuickNotes class")
    process = UI()
    result = []
    debug = 'disconnected'
    data = {
        'provider': 'Amy Nayi',
        'providerId': '652981'
    }

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
        pass

    def tearDown(self):
        pass

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
        expected = {
            'feedback': 'Call Logged',
            'note': 'Called and left a voicemail.',
        }
        self.process.execute(('contact',))
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(expected['feedback'])
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected['note'] in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        self.process.execute(('cancel',))
        # All results must be true to pass.
        message = 'Feedback: {} & Note: {}'.format(expected['feedback'],
                                                   expected['note'])
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'disconnected' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_disconnected(self):
        ui.log.info(">>> Inside test_quick_note_disconnected()")
        runtime = {
            'quick': ('Select', '//*[@class="cQuickNotes"]', 'Disconnected'),
        }
        expected = {
            'feedback': 'Call Logged',
            'note': 'Call was disconnected.',
        }
        self.process.execute(('contact',))
        self.process.update(runtime)
        self.process.execute(('quick', 'save'))
        res = self.process.results(expected['feedback'])
        self.result.append(res)
        self.process.execute(('contact', 'comments',))
        self.process.wait()
        inner = self.process.spy('//*[@id="lastFive"]/div/div[1]/div/div',
                                 'innerHTML')
        res = expected['note'] in inner
        self.process.compare(True, res, message='match the note')
        self.result.append(res)
        self.process.execute(('cancel',))
        # All results must be true to pass.
        message = 'Feedback: {} & Note: {}'.format(expected['feedback'],
                                                   expected['note'])
        self.assertTrue(all(self.result), msg=message)

    @unittest.skipUnless(debug is 'not interested' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_not_interested(self):
        ui.log.info(">>> Inside test_quick_note_not_interested()")

    @unittest.skipUnless(debug is 'follow up' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_follow_up(self):
        ui.log.info(">>> Inside test_quick_note_follow_up()")

    @unittest.skipUnless(debug is 'no answer' or debug is 'all',
                         "testing {}".format(debug, ))
    def test_quick_note_no_answer(self):
        ui.log.info(">>> Inside test_quick_note_no_answer()")
