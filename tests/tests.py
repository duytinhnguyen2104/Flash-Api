from pyunitreport import HTMLTestRunner
import unittest
import pytest

class My_Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(123456, 654321)

class MoreTests(unittest.TestCase):
    def test_1(self):
        print("This is different to test.MoreTests.test_1")
        self.assertEqual("minh thong", 123456)


if __name__ == '__main__':
    tests = unittest.TestLoader().loadTestsFromTestCase(My_Tests)
    more_tests = unittest.TestLoader().loadTestsFromTestCase(MoreTests)
    suite = unittest.TestSuite([tests, more_tests])
    outfile = file('./reports/coverage/index.html', 'w')
    HTMLTestRunner(stream=outfile,verbosity=2).run(suite)