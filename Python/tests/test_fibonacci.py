import unittest
from tools import fibonacci as f


class TestFibonacciCounter(unittest.TestCase):
    def test_arguments_are_not_int_CountFibonacci(self):
        self.assertFalse(f.FiboCounter.CountFibonacciSequence("ab"), 'This parameter should return False')
        self.assertFalse(f.FiboCounter.CountFibonacciSequence([1,2,3]), 'This parameter should return False')

    def test_return_result(self):
        self.assertEqual(f.FiboCounter.CountFibonacciSequence(20), 6765)

    def test_return_list(self):
        self.assertEqual(f.FiboCounter.CountFibonacciSequence(20, showresults = True), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765])

    def test_arguments_are_not_int_ResultByProximate(self):
        self.assertFalse(f.FiboCounter.GetResultByProximate("ab"), 'This parameter should return False')
        self.assertFalse(f.FiboCounter.GetResultByProximate([1,2,3]), 'This parameter should return False')

    def test_ResultByProximate_returns_None(self):
        self.assertIs(None, f.FiboCounter.GetResultByProximate(2), 'Change this test if the method is now working.')

    def test_arguments_are_not_int_ResultByPosition(self):
        self.assertFalse(f.FiboCounter.GetResultByPosition("ab"), 'This parameter should return False')
        self.assertFalse(f.FiboCounter.GetResultByPosition([1,2,3]), 'This parameter should return False')


if __name__ == '__main__':
    unittest.main()
