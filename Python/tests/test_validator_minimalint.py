import unittest
from tools import validator


class TestValidatorOfPositiveInt(unittest.TestCase):

    def test_validation_of_None(self):
        v = validator.Validator()
        self.assertEqual(v.validatePositiveInt(None), None)

    def test_if_all_arguments_are_not_int(self):
        v = validator.Validator()
        self.assertFalse(v.validatePositiveInt("ab"), 'This parameter should return False')
        self.assertFalse(v.validatePositiveInt([1,2,3]), 'This parameter should return False')
        self.assertFalse(v.validatePositiveInt((1,2,3)), 'This parameter should return False')
        self.assertFalse(v.validatePositiveInt({1,2,3}), 'This parameter should return False')

    def test_return_string_not_int(self):
        v = validator.Validator()
        v.validatePositiveInt("ab")
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: ab.")
        v.validatePositiveInt([1,2,3])
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: [1, 2, 3].")
        v.validatePositiveInt((1,2,3))
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: (1, 2, 3).")
        v.validatePositiveInt({1,2,3})
        self.assertMultiLineEqual(v.warning, "The following argument is not an integer: {1, 2, 3}.")

    def test_not_negative_numbers(self):
        v = validator.Validator()
        self.assertFalse(v.validatePositiveInt(-1))
        self.assertFalse(v.validatePositiveInt(-1,7))

    def test_return_string_negative_numbers(self):
        v = validator.Validator()
        v.validatePositiveInt(-1)
        self.assertMultiLineEqual(v.warning, "Only positive integers are allowed. -1 is negative.")
        v.validatePositiveInt(-1,2)
        self.assertMultiLineEqual(v.warning, "Only positive integers are allowed. -1 is negative.")

    def test_zero(self):
        v = validator.Validator()
        self.assertEqual(None, v.validatePositiveInt(0), 'This now should return None due to value zero')

    def test_return_string_zero(self):
        v = validator.Validator()
        v.validatePositiveInt(0)
        self.assertMultiLineEqual(v.warning, "The argument value is 0 (zero).")

    def test_correct_input(self):
        v = validator.Validator()
        self.assertTrue(v.validatePositiveInt(3), 'This should return True.')

    def test_return_string_correct_input(self):
        v = validator.Validator()
        v.validatePositiveInt(3)
        self.assertMultiLineEqual(v.warning, "The data is a positive integer higher than 0 (zero).")

    def test_TypeError_when_no_value_is_input(self):
        v = validator.Validator()
        with self.assertRaises(TypeError):
            v.validatePositiveInt()

if __name__ == '__main__':
    unittest.main()
