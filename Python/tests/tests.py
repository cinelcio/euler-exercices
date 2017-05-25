import unittest
import problem_001 as p1

class TestProblem001(unittest.TestCase):
    def test_counter(self):
        self.assertTrue(p1.SumOfMultiples.counter == 0)

    # def test_increment(self):
    #     with SumOfMultiples(number1 = 3, limit = 10) as AfterTen:
    #         self.assertEqual(counter, 10, 'After 10 interations, the counter is 10.')
    #
    # def test_result(self):
    #     self.assertEqual(expected, actual, 'message')


if __name__ == '__main__':
    unittest.main()
