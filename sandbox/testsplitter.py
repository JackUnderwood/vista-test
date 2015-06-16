__author__ = 'John Underwood'
import unittest

import sandbox.splitter as splitter

# Unit Test
class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        """Executes after every test"""
        pass

    def tearDown(self):
        """Executes after every test"""
        pass

    def test_simple_string(self):
        r = splitter.split('GOOG 100 490.90')
        self.assertEqual(r, ['GOOG', '100', '490.90'])

    def test_type_convert(self):
        r = splitter.split('GOOG 100 490.90', [str, int, float])
        self.assertEqual(r, ['GOOG', 100, 490.9])

    def test_delimiter(self):
        r = splitter.split('GOOG,100,490.90', delimiter=',')
        self.assertEqual(r, ['GOOG', '100', '490.90'])

    def test_delimiter_with_spaces(self):
        r = splitter.split('GOOG, 100,  490.90', delimiter=',')
        self.assertEqual(r, ['GOOG', '100', '490.90'])

    def test_all_parameters(self):
        r = splitter.split('GOOG, 100,  490.90',
                           types=[str, int, float],
                           delimiter=',')
        self.assertEqual(r, ['GOOG', 100, 490.9])

if __name__ is '__main__':
    unittest.main()
