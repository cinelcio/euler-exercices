import unittest
from tools import fibonacci


class TestFibonacciCounter(unittest.TestCase):
    def test_arguments_are_not_int_CountFibonacci(self):
        f = fibonacci.FiboCounter()
        self.assertFalse(f.CountFibonacciSequence("ab"), 'This parameter should return False')
        self.assertFalse(f.CountFibonacciSequence([1,2,3]), 'This parameter should return False')

    def test_return_result(self):
        f = fibonacci.FiboCounter()
        self.assertEqual(f.CountFibonacciSequence(20), 6765)

    def test_return_list(self):
        f = fibonacci.FiboCounter()
        self.assertEqual(str(f.CountFibonacciSequence(20, showlist = True)), '[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]')

    def test_ResultByProximate_returns_None(self):
        f = fibonacci.FiboCounter()
        self.assertIs(None, f.GetResultByNearValue(2), 'Change this test if the method is now working.')

    @unittest.skip('Method not read yet')
    def test_arguments_are_not_int_ResultByPosition(self):
        f = fibonacci.FiboCounter()
        self.assertFalse(f.GetResultByPosition("ab"), 'This parameter should return False')
        self.assertFalse(f.GetResultByPosition([1,2,3]), 'This parameter should return False')


if __name__ == '__main__':
    unittest.main()
