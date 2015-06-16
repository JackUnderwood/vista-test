# __author__ = 'John Underwood'
""" Start at the very beginning."""
import unittest


class TestIndySandbox(unittest.TestCase):
    def setUp(self):
        print("Hello, there setUp()!!!")

    def tearDown(self):
        print("Goodbye, there tearDown()!!!")

    def test_add_experience(self):
        print("Run test add_experience!!!")

if __name__ is '__main__':
    unittest.main()
